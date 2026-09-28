# RELEVO — Agente IA Local autoreflexivo

| Campo | Valor |
|---|---|
| **TURNO** | NUBE |
| Principal | Sesión local «Agente IA Local autoreflexivo» (PC, Remote Control activo) |
| Espejo | Sesión nube «Agente IA Local autoreflexivo - en la nube» (también coordinador de hilos) |
| Último checkpoint | 2026-09-28 10:34 (Guayaquil) — espejo: estado real de PR #1 + hipótesis de guiones verificada |
| Motivo del último relevo | toma automática: el usuario escribió en el espejo. La PC recupera la posta al volver (ver «Para la PC al volver»). |

## ▶ Para la PC al volver (leer primero)
PR #1 avanzó el 27-sep y **ya cerró por decisión de Francisco 4 de las 5 cuestiones**.
Lo único que queda antes de fusionarlo **solo lo puede hacer la PC**:
1. Ejecutar los dos comandos PowerShell **de solo lectura** de `AUDITORIA_RED.md` (rama
   `claude/awesome-einstein-6h3af4`, secciones 7 y 8):
   - Sección 8 → enlaces a memoria sin archivo en `memory\`. Esperado: vacío o solo
     `anthropic-skills:notebooklmskill`. Cualquier otro nombre = nota con otra grafía: avisar antes de tocar.
   - Sección 7 → skills del disco que no están en `skills_index.md`. Esperado: ~4 nombres.
2. Registrar aquí los resultados (solo nombres de notas/skills; nada sensible).
3. Si la sección 8 sale limpia → Francisco fusiona PR #1. Si no → corregir la grafía y repetir.
4. Decisión pendiente de Francisco: enlazar la huérfana `memoria-compartida-sesiones` (ver abajo).

## 🚦 Regla de datos que rige este canal — leer antes de escribir aquí

`archivos/` transporta **resúmenes y punteros en Markdown, nunca el documento
fuente**. Hay un `.gitignore` que bloquea todo lo que no sea `.md`, verificado
en vivo el 26-sep (un `.xlsx` y un `.pdf` de prueba quedaron ignorados).

**Por qué:** el hook `PostToolUse` publica esta carpeta en `main` de forma
automática, silenciosa y sin revisión. Lo que entra sale del computador al
instante y queda en el historial de GitHub, de donde no se retira limpio.

**Qué NO sale de la PC, bajo ninguna forma:** cédulas, nombres de personas
naturales, escrituras y certificados del expediente COAC, cifras de deuda
personal, DSCR, cierres mensuales, y los modelos financieros de Belén y San
Sebastián. Rige `gobernanza-datos-financieros-ia`.

**Cómo se pasa un documento al espejo:** se deja su **ruta local** y un resumen
de lo concluido. El espejo no ve `G:` ni `E:`, así que el archivo no le serviría
de nada; el resumen sí.

## Tema / objetivo del hilo

✅ **Confirmado por la PC, y corrige la hipótesis del espejo.**

El espejo supuso, por el título de la sesión, que el hilo trataba del bucle
autoreflexivo de bookmarks (`agente-local-autoreflexivo-bookmarks`). **No es
así.** Ese fue el origen de la sesión hace meses, pero el hilo vivo es otro:

**Operación diaria del PC de Francisco Duque** — diagnóstico y reparación de la
máquina, expedientes, impresión, y gobierno del corpus de skills. Los tramos
recientes: cámara bloqueada en Meet (era la cámara virtual de EShare),
activación de las sesiones en la nube y Remote Control, y la auditoría de la red
de skills que produjo PR #1.

## Razonamiento en curso

**Hilo abierto: las 5 cuestiones que PR #1 dejó a criterio de Francisco.**
El espejo hizo bien la auditoría del repositorio, pero **no pudo cerrarlas
porque viven fuera de su alcance**: la mitad de la red son notas de memoria en
`~/.claude/projects/C--Users-datos-Downloads/memory/`, que la nube no ve y la PC
sí. Esa es exactamente la división de trabajo de este relevo, y es la razón de
ser del mecanismo.

| # | Cuestión de PR #1 | Quién puede cerrarla |
|---|---|---|
| 1 | 13 notas de memoria escritas con guion: ¿pasar a guion bajo? | **PC** — hay que leer los nombres reales en disco |
| 2 | `[[skill-anterior]]` y `[[wikilink]]`: ¿marcadores de plantilla? | PC o nube |
| 3 | `[[arquitectura-financiera-escalonada]]`: ¿nota sin prefijo? | **PC** — se comprueba en `memory/` |
| 4 | Dos rutas relativas de scripts que apuntan a otra skill | PC o nube |
| 5 | Qué cifra de skills es la oficial (154 vs 158) | **PC** — `skills_index.md` vive en `memory/` |

**Hipótesis del espejo sobre el origen de las grafías con guion — ✅ mecanismo verificado
en el código (28-sep).** En `regla-del-primer-tropiezo/mapear_red_skills.py`,
`slug()` es `re.sub(r"[^a-z0-9\-]", "-", …)`: convierte **todo `_` en `-`**. Cada
`[[nota_con_guion_bajo]]` de memoria se registra como destino inexistente y la sección
«Enlaces rotos» de `memory/skills_network.md` lo imprime como `[[nota-con-guion]]`.
Copiar desde esa lista produce exactamente las variantes que PR #1 corrigió.
Que se haya copiado de ahí sigue siendo inferencia, pero el mecanismo existe.

**Consecuencia:** el script seguirá listando como «rotos» todos los enlaces a memoria
(con la grafía equivocada) y puede reintroducir el error. **Propuesta para Francisco**
(no aplicada): que `slug()` conserve `_` (`[^a-z0-9_\-]`) y que la sección se llame
«Destinos fuera del repo (memoria o rotos)». Es un cambio de 1 línea en la skill
`regla-del-primer-tropiezo`.

### Estado real de las 5 cuestiones de PR #1 (leído del PR el 28-sep)
| # | Cuestión | Estado |
|---|---|---|
| 1 | 13 notas con guion → guion bajo | ✅ Hecho en la ronda 2, aprobada por Francisco. **Falta verificar en disco** (comando §8) |
| 2 | `[[skill-anterior]]`, `[[wikilink]]` | ✅ Eran marcadores de plantilla; eliminados |
| 3 | `[[arquitectura-financiera-escalonada]]` | ✅ Tratada como nota de memoria sin prefijo. **Falta verificar que el archivo existe** (comando §8) |
| 4 | Rutas de scripts a otra skill | ✅ `compra-fruta-semanal-qvp` usa la ruta completa a `gmail-attachments\scripts\download_all_zip.py` |
| 5 | 154 vs 158 | ✅ Cifra oficial = la del repo: **159** (158 + `memoria-compartida-sesiones`). Los nombres no registrados en el índice salen con el comando §7 |

Grafo actual: 159 nodos, 606 aristas; **huérfana: `memoria-compartida-sesiones`**
(nadie la enlaza). Candidatas naturales para enlazarla: `skills-versionado-git-github`
y `llave-maestra-autoaprendizaje-ia`. Decisión de Francisco.

## Lo que construyó el espejo en este hilo (26-sep)

- La skill `memoria-compartida-sesiones`: MEMORIA, bitácora, relevo en caliente,
  hooks, plantilla de hilos y rol de coordinador.
- Los hilos `flujo-caja-proyeccion-mobijuesa` y `financial-report-mobijuesa`,
  cada uno con su propio espejo. No se razonan aquí.
- La auditoría de la red de skills → PR #1.

## Archivos centrales

Punteros, no copias (ver la regla de datos de arriba):

| Qué | Ruta local | Estado |
|---|---|---|
| **PRINCIPAL** — corpus de skills | `~/.claude/skills/` (= este repo) | 158 `SKILL.md`, sincronizado |
| Índice de skills | `…/memory/skills_index.md` | fuera del repo; dice 154 |
| Mapa de la red | `…/memory/skills_network.md` | fuera del repo; dice 592 aristas, hoy son 606 |
| Memoria compartida del proyecto | `…/memory/` | **no sale de la PC** |
| PR de la auditoría | `jjmobijuesa-png/claude-skills-jjmobijuesa#1` | abierto, sin fusionar |

🚦 **Este hilo no tiene un «archivo principal» único** en el sentido de un
documento que se edita. Su objeto es el **corpus de skills completo**. Por eso
`archivos/` está vacío y debe seguir estándolo: no hay nada que copiar, solo
estado que registrar.

## Siguiente paso concreto

**PC:** ejecutar los comandos §7 y §8 de `AUDITORIA_RED.md` y anotar aquí el resultado
(ver «Para la PC al volver»). Con la §8 limpia, Francisco fusiona PR #1.
_(Actualizado por el espejo el 28-sep: las decisiones de las 5 cuestiones ya están tomadas;
solo falta la verificación en disco.)_

## Respuestas a las preguntas que dejó el espejo

1. **¿Archivo principal y ruta?** → No hay uno solo: el objeto es
   `~/.claude/skills/` entero. Ver el aviso de arriba.
2. **¿El tema es el bucle de bookmarks?** → **No.** Corregido arriba.
3. **¿Espejo viejo de flujo de caja y el «(en caliente)»?** → Decisión de
   Francisco, sigue abierta.

## Pendientes / preguntas abiertas

- **PR #1 sin fusionar** — pendiente de cerrar las cinco cuestiones.
- **PR #2** (`claude/quirky-pascal-4epmn1`) — ya está en `main`; comprobar si
  procede cerrarlo.
- **Dos espejos activos** para flujo de caja; Francisco debe elegir uno.
- **Notas de Gemini de la reunión del 22-sep** — nunca se recogieron; deberían
  estar en `G:\Mi unidad\Meet Recordings` como
  `Meeting started … - Notes by Gemini`.
- **`REPARAR_EXPLORADOR.bat`** en Descargas — creado, nunca ejecutado.
- **Excel `MsoAria.dll`** — sin comprobar si reincide tras el saneamiento.
- **10 planos de lotes** del expediente COAC — sin revisar ni imprimir.
