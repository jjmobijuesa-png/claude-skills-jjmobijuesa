---
name: estratega-ventas-inmobiliario-vista-al-rio
description: |
  Estratega comercial inmobiliario para el proyecto Edificio Vista al Río
  de **INMOBILIARIA JUEZ & JUEZ** (Quevedo, Los Ríos, Ecuador). 30
  departamentos, 10 pisos, 6 ya vendidos, 24 por colocar. Convierte la
  base calificada "Base Entregable Experto Datos de Contacto.xlsx" en
  olas segmentadas de prospección por email desde jjmobijuesa@gmail.com,
  bajo régimen de **invitación reservada con destinatarios en CCO**.

  La skill destila tres capas:
  1. Segmentación por capacidad de pago (regla del 30% sobre ingreso
     mensual frente a la cuota de construcción de USD 2.000/mes).
  2. Mensaje sugerente listo para envío (variantes 2 dorm / 3 dorm /
     inversionista).
  3. Plan de envío en olas con la skill `gmail-send-playwright` o, en
     fallback, draft manual.

  Casos de uso:
  - Lanzar primera ola comercial a TIER PREMIUM (≥USD 6.000/mes).
  - Lanzar segunda ola a TIER ALTO (USD 4.500–5.999) con plan de codeudor.
  - Lanzar campaña de nutrición a TIER MEDIO-ALTO (USD 3.500–4.499).
  - Recalcular embudo: 200 contactos → 40 interesados → 24 ventas.
---

# Estratega de ventas inmobiliario — Edificio Vista al Río

## 0. Promotora y régimen de comunicación

- **Promotora**: INMOBILIARIA JUEZ & JUEZ.
- **Remitente operativo**: `jjmobijuesa@gmail.com`.
- **Carácter del envío**: **invitación reservada**. La oferta es
  privada, no abierta al público general.
- **Destinatarios**: siempre en **CCO (BCC)**. En el campo `Para` va
  únicamente el remitente. Ningún invitado debe ver la lista del resto.
- **Ubicación oficial**: 🗺️ https://maps.app.goo.gl/iGZ22Kng1o5qND9V6

## 1. Ficha técnica del producto

| Variable | Valor |
|---|---|
| Promotora | INMOBILIARIA JUEZ & JUEZ |
| Ubicación | Quevedo, provincia de Los Ríos, Ecuador |
| Google Maps | https://maps.app.goo.gl/iGZ22Kng1o5qND9V6 |
| Pisos | 10 |
| Departamentos totales | 30 |
| Vendidos | 6 |
| **Por colocar** | **24** |
| Tipologías | 2 dorm (120 m²) y 3 dorm (150 m²) |
| Precio referencia 2 dorm | USD 200.000 |
| Precio referencia 3 dorm | USD 250.000 (estimado, 150 m² × 1.666) |
| Costo construcción | USD 1.300/m² |
| Precio promedio venta | USD 1.666/m² |
| Plazo construcción | 30 meses |
| Margen objetivo | 21–25 % |
| **Prioridad A** | **Confort y seguridad al máximo** |
| **Reserva inicial** | **USD 1.000** (separa la unidad y abre acceso al expediente completo) |

## 2. Estructura financiera de venta

| Etapa | % | Monto (2 dorm) | Observación |
|---|---|---|---|
| Entrada | 20 % | USD 40.000 | Al firmar la promesa de compraventa |
| Cuotas durante obra | 30 % | USD 60.000 | 30 cuotas de USD 2.000/mes |
| Crédito hipotecario | 50 % | USD 100.000 | A escritura, con banco aliado |

## 3. Calificación de prospectos — regla del 30 %

La cuota mensual de USD 2.000 no debe pasar del 30 % del ingreso del
cliente. Mínimo ingreso técnico: **USD 6.667/mes** (ideal). Se aceptan
con codeudor desde USD 4.500/mes.

| Tier | Ingreso mensual | Producto sugerido |
|---|---|---|
| **PREMIUM** | ≥ USD 6.000 | 2 dorm directo / 3 dorm si ≥ USD 7.000 |
| **ALTO** | USD 4.500 – 5.999 | 2 dorm con codeudor o cónyuge |
| **MEDIO-ALTO** | USD 3.500 – 4.499 | Nutrición + plan extendido |
| NO CALIFICA | < USD 3.500 | Descartar |

## 4. Pool actual (al 2026-06-07)

Fuente: `E:\vars\var 7\3 Marketing\DBM\Base calificada\Base Entregable Experto Datos de Contacto.xlsx`,
hoja `Base Contactos`, 1.023 registros.

| Tier | Cantidad con email válido |
|---|---|
| PREMIUM | 17 |
| ALTO | 35 |
| MEDIO-ALTO | 132 |
| **Total viable** | **184** |

Archivos generados (todos en `E:\vars\var 8\2 Edif Vista al Rio\0 Estrategia Comercial\`):

| Archivo | Contenido |
|---|---|
| `OLA_1_LISTA_ENVIO.xlsx` | **Principal**. Hojas: Criterios financieros · Resumen por tier · Embudo · Lista de envío Ola 1 · Detalle Ola 1 |
| `OLA_1_PRIORITARIOS.xlsx` | 52 contactos PREMIUM + ALTO ordenados por ingreso |
| `OLA_2_MEDIO_ALTO.xlsx` | 132 contactos MEDIO-ALTO con criterios y resumen |
| `OLA_1_LISTA_ENVIO.csv` | Espejo CSV de la hoja de envío Ola 1 |
| `OLA_1_PRIORITARIOS.csv` | Espejo CSV |
| `OLA_2_MEDIO_ALTO.csv` | Espejo CSV |

## 5. Embudo objetivo

```
184 emails enviados (olas 1 y 2)
  → 30 % apertura      ≈ 55 abrieron
  → 25 % CTR           ≈ 14 click a brochure / agenda
  → 50 % visita        ≈  7 visitan sala de ventas
  → 70 % conversión    ≈  5 reservan

Para colocar 24 unidades en 6 meses → repetir el ciclo 5 veces
o ampliar fuente con referidos y publicidad pagada.
```

## 6. Plan de olas

1. **OLA 1 — semana 1** : 52 PREMIUM+ALTO con email "tipo gerente".
2. **OLA 2 — semana 3** : 132 MEDIO-ALTO con email "tipo familia
   inversionista" y plan extendido.
3. **OLA 3 — semana 6** : reenvío a no-abridores con asunto distinto.
4. **OLA 4 — semana 9** : invitación a evento de pre-venta en sala
   modelo (los renders están en
   `E:\vars\var 8\2 Edif Vista al Rio\1 Planos Edf VISTA AL RIO\9 Renders`).

## 7. Activos de marketing disponibles

- Renders: `9 Renders\Edificio Vista al Rio*.png` y `departamento Vista al Rio*.png`.
- Planos arquitectónicos PDF: `2 Arquitectonico\Arquitect.Quevedo Edi #1-LAMINA 1..8-8.pdf`.
- Memorias técnicas: `7 Memorias Técnicas`.
- Permisos y licencias: `10 Permisos y Licencias`.

## 8. Modelo de mensaje (resumen)

Ver `templates/email_vista_al_rio.md` para el cuerpo completo con
asunto, preview, gancho, oferta, garantía, CTA y firma.

Variantes:

- `email_2dorm_gerente.md` — para Tier PREMIUM gerente / piloto.
- `email_3dorm_familia.md` — para PREMIUM con holgura ≥ USD 7.000.
- `email_inversionista.md` — para perfil con plusvalía / renta como gancho.

## 9. Mecánica de envío con CCO (BCC)

1. Abrir Gmail logueado en `jjmobijuesa@gmail.com` (perfil Edge).
2. Invocar la skill `gmail-send-playwright` con:
   - `to`: `jjmobijuesa@gmail.com` (a sí mismo).
   - **`bcc`**: lista de prospectos del lote (hasta 50 por envío para
     evitar marcado como spam por Gmail).
   - `subject`: el asunto de la plantilla, neutro y singular.
   - `body`: cuerpo en tono "Estimado(a) profesional invitado(a)" — no
     personalizar nombre cuando el envío es masivo por CCO.
   - `attachments`: render principal + brochure PDF si existe.
3. Registrar envío en `bitacora_envios.csv` con fecha, lote, asunto.

### Regla del depósito de USD 1.000

Cada email debe dejar claro que **una vez aceptada la visita o la
videoconferencia, un depósito de USD 1.000 da acceso completo** a:

- Planos, memorias técnicas, permisos.
- Renders en alta resolución.
- Cronograma y curva financiera.
- Selección preferente de piso y unidad.

El depósito **se acredita al 100 % al monto de la entrada** cuando el
invitado firma la promesa de compraventa.

## 10. Regla apologética de venta

Vista al Río **NO** es un departamento; es **patrimonio frente al río
con confort y seguridad al máximo, dentro de una comunidad curada por
invitación**. Toda comunicación enmarca el producto en cuatro anclajes:

1. **Confort al máximo** — terminados premium, áreas amplias,
   ventilación natural, balcón frontal al río en cada unidad, áreas
   comunes de uso exclusivamente residente.
2. **Seguridad al máximo** — biométrico por piso, videovigilancia
   perimetral 24/7, doble filtro de acceso y comunidad curada.
3. **Ubicación irrepetible** — frente fluvial en Quevedo, eje
   productivo del país.
4. **Plan financiero amable** — 50 % en obra con cuotas de USD 2.000;
   50 % final con crédito hipotecario tradicional. Reserva con USD
   1.000.

## 11. Reglas no negociables

- **Siempre** enviar con **destinatarios en CCO (BCC)**. Ningún
  invitado puede ver la lista de los demás.
- **Siempre** firmar como **INMOBILIARIA JUEZ & JUEZ**, nunca
  abreviado.
- **Siempre** incluir el link de Google Maps:
  https://maps.app.goo.gl/iGZ22Kng1o5qND9V6
- **Siempre** mencionar la reserva de **USD 1.000** como la llave que
  abre el acceso al expediente completo y separa la unidad.
- **Siempre** ofrecer agenda de visita o videoconferencia antes que
  cierre por email.
- **Nunca** prometer rentabilidad garantizada por escrito (incumple
  norma SEPS / Superintendencia de Compañías).
- **Nunca** enviar email sin que el campo "INGRESO ≥ 3.500" esté
  validado en la base.
- **Nunca** usar la palabra "blockchain" ni "cripto" en este contexto
  (es un proyecto inmobiliario tradicional).
- **Nunca** reenviar el email del prospecto a un tercero. Régimen de
  estricta confidencialidad.

## 12. Estado del proyecto (snapshot 2026-06-07 19:30 UTC)

- 6/30 vendidos (20 % colocados).
- 24/30 disponibles (80 %).
- **OLA 1 ejecutada**: 52 invitaciones en 3 batches CCO. Entregadas 49 (94,2 %). Rebotes 3.
- **OLA 2 ejecutada**: 132 invitaciones en 4 batches CCO de 33 cada uno. Entregadas ≈122 (92,4 %). Rebotes 10.
- **Reenvío typos**: 2 emails con `.co` corregidos a `.com` y reenviados ese mismo día.
- **Reporte al CEO** <CEO de la empresa hermana> enviado a <CEO>@<empresa-A>.com con 3 Excels adjuntos.
- **Vigilancia activa**: cron `vista-rio-vigilancia-inbox` cada 6 horas durante 72h.
- **Cron OLA 2 14 días desactivado** (la ola se adelantó por decisión del CEO).

## 13. Doctrina anti-spam y tamaños de batch (LECCIÓN APRENDIDA v3)

**Regla del límite diario de Gmail gratis**: 500 destinatarios externos por
día por cuenta. Para evitar marcado como spam ANTES del límite:

| Volumen total a enviar | Batches recomendados | Destinatarios por batch | Comentario |
|---|---|---|---|
| ≤ 50 | 1 batch | hasta 50 | sin riesgo |
| 50–100 | 2 batches | 25–50 | seguro |
| 100–200 | 3–4 batches | 33–50 | **óptimo** (lo que usamos en OLA 2) |
| > 200 | 5+ batches | 30–40 | dividir en días |

**Regla del delay**: el script `send_drafts_attach.py` mete ~10s entre
batches naturalmente (carga de drafts + Send). Para envíos de > 100
recipientes en el mismo día, considerar pausa de 5-10 min entre batches.

**Regla de oro**: TODOS los destinatarios en CCO (BCC). Nunca en TO ni CC.
El campo TO debe llevar SIEMPRE al propio remitente (`jjmobijuesa@gmail.com`).

## 14. Pipeline de recuperación de rebotes (LECCIÓN APRENDIDA v3)

Cuando un email rebota, NO se descarta al contacto. Se ejecuta un pipeline
de recuperación con cinco fuentes en orden de costo creciente:

### Paso 1 — Auto-corrección de TYPOs (gratis, instantáneo)

Patrones recurrentes a corregir automáticamente:
- `.co` al final cuando claramente debió ser `.com` (ej. `outlook.co` → `outlook.com`)
- `gmial.com` → `gmail.com`
- `hotnail.com` → `hotmail.com`
- `yahoo.es` con `.es` siendo en realidad `.com`
- Espacios o caracteres unicode raros

→ Re-enviar inmediatamente con `create_draft` + `send_drafts_attach.py`.

### Paso 2 — WebSearch del nombre + empresa (gratis, ~30s)

```
WebSearch("<NOMBRE> <EMPRESA> LinkedIn email")
WebSearch("<NOMBRE> <Quevedo|Los Ríos|Ecuador> contacto")
```

ZoomInfo, LinkedIn público, directorios oficiales suelen confirmar:
- Si el contacto sigue en la empresa.
- Su LinkedIn URL pública.
- Formato de email institucional.

### Paso 3 — Variantes de email institucional

Si el dominio es institucional (`@uteq.edu.ec`, `@empresa.com`),
probar variantes:
- inicialnombre + apellido
- nombre.apellido
- inicial + apellido + segundo apellido

Re-enviar a una variante por vez (NO masivamente para evitar penalty
del MTA receptor).

### Paso 4 — Perplexity Pro y LinkedIn DM (manual)

Si los pasos 1-3 no dan resultado:
- Buscar en Perplexity Pro (cuenta del usuario: hilo `e21b0957-a5fe-4880-aad3-bedf29205bb1`).
- Si hay LinkedIn URL del contacto: DM personal con copia del pitch.
- X.com (Twitter) y Facebook: solo si hay perfil verificado del contacto.

### Paso 5 — Canal telefónico (fallback definitivo)

Todos los contactos en la base original tienen celular. Si los pasos 1-4
fallan, llamar al celular registrado y solicitar email actual o coordinar
visita directamente.

### Soft bounces (mailbox full)

NO son rebotes definitivos. Reintentar el mismo email en 24-48 horas.
Si rebota dos veces más, escalar al pipeline web.

## 15. Lecciones aprendidas (autoaprendizaje codificado v3)

1. **El script Playwright debe esperar `div[gh="cm"]` con retries**
   (3 intentos × 60s). En la primera apertura de Gmail aparece un splash
   de Google Workspace que confunde la detección de UI.
2. **El campo BCC se abre con `Ctrl+Shift+B`** independiente del idioma
   de Gmail. Su input se localiza vía JS evaluando los `combobox`
   visibles del diálogo de compose.
3. **El subject "BATCH" es ambiguo**. Usar prefijo explícito (`OLA 1 BATCH`,
   `OLA 2 BATCH`, `REENVÍO`) para que `--subject-contains` filtre sin colisiones.
4. **El MCP `create_draft` es preferible al Playwright para crear**.
   Permite BCC nativo y validación inmediata vía `list_drafts`.
   El Playwright queda solo para adjuntar + enviar.
5. **Los adjuntos vía MCP base64 inflan contexto**. NUNCA pasar > 100 KB
   binario por MCP. Usar el script Playwright que adjunta desde disco.
6. **La verificación post-envío es vía `search_threads in:sent newer_than:Xm`**
   y simultáneamente `from:mailer-daemon newer_than:Xm` para capturar rebotes
   inmediatos.
7. **Tasa de rebote esperable**: 5-8 % en bases con 2-3 años. Si supera
   12 %, la base está desactualizada y requiere refresh antes de seguir.


---

## Datos privados del caso

Los correos, nombres concretos, queries específicas y cifras del caso
del usuario están en `private/SKILL_FULL.md` (excluido del repo por
`.gitignore`). Esta versión pública conserva la doctrina metodológica
con placeholders en lugar de PII.

Para usar la skill con los datos reales, la versión en `private/` se
carga automáticamente cuando Claude detecta los triggers documentados
en el frontmatter.
