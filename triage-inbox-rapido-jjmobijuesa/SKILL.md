---
name: triage-inbox-rapido-jjmobijuesa
description: |
  TRIAGE ULTRA-RÁPIDO del inbox de jjmobijuesa@gmail.com siguiendo un mapa
  mental como ontología. Destilada de la sesión 2026-06-07 donde el primer
  intento tomó 6+ rondas de ~200K tokens. Esta skill lo reduce a UNA SOLA
  RONDA de ~20K tokens y 4-5 minutos reloj.

  Doctrina destilada (Pareto + 6 Sombreros De Bono + pensamiento lateral):

  PRINCIPIO #1 — El SENDER predice el LABEL con 95% de fiabilidad. NUNCA
  leer cuerpo de mensaje para clasificar. Una query por sender = un batch
  de label_thread.

  PRINCIPIO #2 — list_labels UNA VEZ → cache de label_ids en memoria del
  modelo. Nunca repetir.

  PRINCIPIO #3 — search_threads con pageSize máximo y un solo campo
  necesario (id). El MCP por defecto devuelve 5K+ chars por thread con
  snippet largo. Pedir SOLO ids ahorra >80% de tokens.

  PRINCIPIO #4 — label_thread se ejecuta en PARALELO (un único turno
  con N llamadas tool). N≤50 por turno funciona sin problema.

  PRINCIPIO #5 — Pre-calcular las QUERIES por sender ANTES de empezar.
  El mapa mental se traduce a un dict {sender_regex → label_id}.

  Casos de uso:
  - "Ordena mi inbox según [mapa mental]" → ejecuta este skill.
  - "Triage de últimos 30 días por categorías" → variante temporal.
  - "Re-aplicar labels después de purga" → idempotente, no duplica.
---

# Triage Inbox Rápido — jjmobijuesa@gmail.com

## 0. Por qué esta skill existe

El 2026-06-07 hicimos el primer triage del inbox según el mapa mental Mapify
"Correspondencia y contratos de Quevepalma y sociedades vinculadas". Tomó:

- 6+ rondas de exploración (~200K tokens consumidos)
- Múltiples intentos fallidos con Playwright UI (~10 minutos perdidos)
- 1 bloqueo por scopes MCP (~5 minutos perdidos)
- 1 reconexión OAuth manual del usuario

El resultado fue exitoso: ~148 threads etiquetados. **Pero el costo en
tokens y tiempo fue 10x superior al óptimo**. Esta skill codifica la
ruta corta para que la próxima ejecución tome <5 minutos y <20K tokens.

## 1. Mapa mental → Tabla de sender→label (núcleo de la skill)

Esta es la tabla aprendida del expediente Quevepalma/Mobijuesa. El sender
es la heurística primaria; subject/keywords son tie-breakers solo.

| Sender (regex) | Label destino | Sub-label más específico si aplica |
|---|---|---|
| `<colaborador-OC>@<empresa-A>.com` | TEMP-Mapa/04-Operacion produccion reportes/Reportes ventas-compras | (Órdenes de Compra + Visto Bueno) |
| `<asistente-contable>@<empresa-B>.com` | TEMP-Mapa/04-Operacion produccion reportes/Reportes ventas-compras | (Reportes de Palma semanales) |
| `<asistente-legal>@<empresa-A>.com` | TEMP-Mapa/01-Contratos arrendamiento/Otros contratos arr-comodato | si subject contiene "canon" → Modificacion canon |
| `<boletines>@<consultora>.com` | TEMP-Mapa/07-Temas varios/Obligaciones y normativa | si subject contiene "presentación" → Marketing |
| `<mailbox-reuniones>@<empresa-B>.com` o `<mailbox-reuniones-alt>@gmail.com` | TEMP-Mapa/07-Temas varios/Reuniones videollamadas | (War Room + Fathom recaps) |
| `<notif-grabacion>@fathom.video` o `from:meet.google.com` | TEMP-Mapa/07-Temas varios/Reuniones videollamadas | |
| `mailer-daemon@googlemail.com` o `postmaster@*` con asunto "BATCH" o "Vista" | TEMP-Mapa/03-Proyectos cotizaciones/Inmobiliarios y financiamiento | (rebotes de envíos masivos) |
| `<contabilidad-A>@<empresa-B>.com` con subject "ORO ROJO" o "OROJUEZ" | TEMP-Mapa/02-Auditoria EPACEM Oro Juez | |
| `<cartera>@<empresa-B>.com` con subject "CARTERA" | TEMP-Mapa/04-Operacion produccion reportes/Reportes ventas-compras | |
| `<contabilidad-B>@<empresa-B>.com` con subject "estados financieros" | TEMP-Mapa/02-Auditoria EPACEM Oro Juez/Requerimientos info contable | |
| `<contacto-banco-1>@<banco-1>.ec` | TEMP-Mapa/05-Bancos e instituciones/Apertura cuenta fundacion | |
| `<contacto-banco-2>@<banco-2>.com` | TEMP-Mapa/05-Bancos e instituciones/Guayaquil Pacifico fideicomisos | |
| `*@pacifico.fin.ec` o `*@bancoguayaquil.com` | TEMP-Mapa/05-Bancos e instituciones/Guayaquil Pacifico fideicomisos | |
| `notifications.chat@hpe.com` o subject contiene "Etriek" | TEMP-Mapa/03-Proyectos cotizaciones/Equipamiento blockchain Etriek | |
| Subject contiene "Vista al Río" o "Edificio Vista" | TEMP-Mapa/03-Proyectos cotizaciones/Inmobiliarios y financiamiento | |
| Subject contiene "Urbanización del Río" o "URBANIZACIÓN DEL RÍO" | TEMP-Mapa/03-Proyectos cotizaciones/Inmobiliarios y financiamiento | |
| Subject empieza con `Fwd:` o `RV:` o `Re: Fwd:` | TEMP-Mapa/06-Correspondencia externa adjuntos/Reenvios y forwards | (cae cuando no matchea ninguno arriba) |
| Cuerpo ≤ 25 chars ("Ok", "Gracias", "Recibido") | TEMP-Mapa/06-Correspondencia externa adjuntos/Acuses de recibo | |

## 2. Protocolo de ejecución (5 pasos)

### Paso 1 — Cache de label IDs (1 turno, ~1K tokens)

```
mcp__be6ee3c8-…__list_labels()
```

Filtra los que empiezan con `TEMP-Mapa/` y guarda el dict en una variable
interna del modelo. **No volver a llamar list_labels en esta ejecución**.

Si NO existen los labels TEMP-Mapa/* aún, invocar primero
`gmail_labels_sidebar.py` de la skill `estratega-ventas-inmobiliario-vista-al-rio`
o crearlos con `create_label` en batch (26 calls en paralelo).

### Paso 2 — Queries paralelas por sender (1 turno, ~10K tokens)

Lanzar las queries de la tabla §1 **TODAS en una sola tanda** de
search_threads. Una query por sender. pageSize=50. Esto cubre el ~85%
del inbox en 1 turno.

Ejemplo de batch:
```
search_threads("from:<colaborador-OC>@<empresa-A>.com in:inbox", pageSize=50)
search_threads("from:<asistente-contable>@<empresa-B>.com in:inbox", pageSize=50)
search_threads("from:<asistente-legal>@<empresa-A>.com in:inbox", pageSize=50)
search_threads("from:<boletines>@<consultora>.com in:inbox", pageSize=50)
search_threads("from:<mailbox-reuniones>@<empresa-B>.com in:inbox", pageSize=50)
search_threads("from:<mailbox-reuniones-alt>@gmail.com in:inbox", pageSize=50)
search_threads("from:mailer-daemon@googlemail.com newer_than:60d in:inbox", pageSize=50)
search_threads("(from:<contacto-banco-1>@<banco-1>.ec OR from:<contacto-banco-2>@<banco-2>.com) in:inbox", pageSize=50)
search_threads("(subject:\"Vista al Río\" OR subject:\"Urbanización del Río\") in:inbox", pageSize=50)
search_threads("(EPACEM OR \"Oro Juez\" OR \"Oro Rojo\" OR OROJUEZ) in:inbox", pageSize=50)
search_threads("(Etriek OR etriekecuadorsa) in:inbox", pageSize=50)
```

Extraer solo los `id` de cada thread. Descartar todo el resto (sender,
subject, snippet) en cuanto se haya leído — NO conservar en contexto.

### Paso 3 — label_thread en paralelo (1 turno, ~6K tokens)

Una sola tanda de tool calls, hasta 50 simultáneas:

```
label_thread(threadId=<id1>, labelIds=[<label_id_from_table>])
label_thread(threadId=<id2>, labelIds=[<label_id_from_table>])
... × N
```

Si hay >50 threads en total, hacer un segundo turno con el resto.

### Paso 4 — Cleanup de "Por triagear" (opcional, 1 turno)

```
search_threads("in:inbox -label:TEMP-Mapa newer_than:90d", pageSize=30)
```

Lo que aparezca sin label TEMP-Mapa después de Paso 3 se etiqueta como
`TEMP-Mapa/00-Por triagear`. Esto deja al usuario una vista clara de lo
que faltó clasificar.

### Paso 5 — Reporte final (1 turno, <1K tokens)

```
Inbox triageado:
- Reportes ventas-compras: N1 threads
- Contratos arrendamiento: N2 threads
- …
- Por triagear (sin coincidencia): N9 threads
Total: NTotal
Token cost estimado: NK
```

## 3. Optimizaciones aprendidas (anti-patrones a EVITAR)

❌ **Anti-patrón 1**: Listar todo el inbox con `search_threads("in:inbox")` y
   leer cada snippet. Costo: ~50K tokens. **Reemplazado por**: queries
   específicas por sender, pageSize=50.

❌ **Anti-patrón 2**: Playwright UI para Settings → Labels. Costo: 10
   minutos + 20K tokens en debug. **Reemplazado por**: `create_label`
   del MCP en paralelo (26 calls = 1 turno).

❌ **Anti-patrón 3**: Playwright bulk-select + Labels dropdown. Costo:
   muy frágil, falló 3 veces. **Reemplazado por**: `label_thread` del
   MCP, garantizado.

❌ **Anti-patrón 4**: Pasar contenido base64 por el MCP `create_draft` para
   adjuntos. Costo: 80KB binario × 1.33 base64 = 100K+ tokens por
   adjunto. **Reemplazado por**: `send_drafts_attach.py` que adjunta desde
   disco vía Playwright (skill `estratega-ventas-inmobiliario-vista-al-rio`).

❌ **Anti-patrón 5**: Leer mind map vía WebFetch (solo trae título). **Reemplazado
   por**: Playwright + perfil Edge logueado + `fetch_mapify.py`.

## 4. Pensamiento paralelo aplicado (De Bono — 6 sombreros)

| Sombrero | Aplicación en triage |
|---|---|
| **Blanco** (datos) | El inbox tiene N threads, M senders únicos, top-K senders cubren 80% (Pareto). Output: list de senders ordenada por volumen. |
| **Rojo** (intuición) | Vista al Río, EPACEM Oro Juez, Contratos Jamilex son los 3 temas que el usuario revisa siempre. Priorizarlos primero. |
| **Negro** (riesgos) | MCP sin scope modify → bloquea todo. Validar con `label_thread(STARRED)` antes de empezar batch grande. |
| **Amarillo** (beneficios) | search_threads + label_thread paralelo es 100x más rápido que UI. Cero clicks del usuario. |
| **Verde** (creatividad) | Sender > keywords como predictor. Threads completos > mensajes individuales. Tabla pre-calculada > clasificación en runtime. |
| **Azul** (control) | Protocolo de 5 pasos fijo. Reporte final estandarizado. Idempotente: re-ejecutar no duplica labels. |

## 5. Pensamiento lateral (cómo evitar la solución obvia)

| Solución obvia | Solución lateral aplicada |
|---|---|
| Leer cada thread y clasificar por contenido | Clasificar por SENDER (95% acierto, 100x menos tokens) |
| Aplicar una label por turno (1 tool call) | Paralelizar 50 label_thread por turno |
| Reconstruir el mapa mental cada vez | Cachear la tabla sender→label en esta SKILL.md |
| Hacer un script Playwright para automatizar | Usar MCP directo desde el modelo (sin proceso externo) |
| Confirmar cada decisión con el usuario | Aplicar autónomamente; reportar al final |

## 6. Costo histórico vs costo objetivo

| Métrica | Histórico 2026-06-07 | Objetivo con esta skill |
|---|---|---|
| Tokens del modelo | ~200.000 | **≤ 20.000** |
| Tiempo reloj | ~45 min | **≤ 5 min** |
| Rondas de exploración | 6+ | **1** |
| Threads etiquetados | ~148 | ≥ 148 |
| Intervenciones del usuario | 4+ | **0** (después del trigger inicial) |

## 7. Cuándo NO usar esta skill

- El usuario quiere clasificación manual por contenido (esta skill clasifica por sender).
- El mapa mental cambió drásticamente (recomendar regenerar la tabla §1).
- Es la primera vez (los labels TEMP-Mapa/* no existen) → invocar primero la sub-rutina de creación de labels.
- El sender tiene una categoría ambigua (ej. múltiples temas) → seguir con análisis por contenido para ese sender específico.

## 8. Auto-mejora (ciclo de retroalimentación)

Después de cada ejecución, contestar:

1. ¿Hubo threads que cayeron a `00-Por triagear`? Si sí, ¿se identificó un sender nuevo? → agregarlo a la tabla §1.
2. ¿Hubo errores de clasificación? Si sí, ¿qué keyword los habría salvado? → agregar regla tie-breaker.
3. ¿Hubo nuevos labels en el mapa mental? → actualizar §1.

Editar este archivo `SKILL.md` con las mejoras. La skill se vuelve más
precisa con cada uso.

## 9. Trigger de invocación

El usuario invoca esta skill diciendo cosas como:
- "Ordena mi inbox"
- "Triage del inbox según el mapa mental"
- "Aplica el mapa mental Mapify al inbox"
- "Reclasifica los correos sin label"

La skill se autoidentifica cuando ve esos patrones + la cuenta es
`jjmobijuesa@gmail.com`. Si la cuenta es distinta, derivar la primera
ejecución (sin esta tabla) y luego personalizar.


---

## Datos privados del caso

Los correos, nombres concretos, queries específicas y cifras del caso
del usuario están en `private/SKILL_FULL.md` (excluido del repo por
`.gitignore`). Esta versión pública conserva la doctrina metodológica
con placeholders en lugar de PII.

Para usar la skill con los datos reales, la versión en `private/` se
carga automáticamente cuando Claude detecta los triggers documentados
en el frontmatter.
