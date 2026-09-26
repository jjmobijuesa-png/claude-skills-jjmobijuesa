# RELEVO — Agente IA Local autoreflexivo

| Campo | Valor |
|---|---|
<<<<<<< HEAD
| **TURNO** | PC |
| Principal | Sesión local «Agente IA Local autoreflexivo» (PC, Remote Control activo) |
| Espejo | Sesión nube «Ver otras sesiones de Claude Code» (claude.ai/code) |
| Último checkpoint | 2026-09-26 — primer volcado de la PC |
| Motivo del último relevo | — (aún no ha habido relevo real) |

## 🚦 Regla de datos que rige este canal — leer antes de escribir aquí

`archivos/` transporta **resúmenes y punteros en Markdown, nunca el documento
fuente**. Hay un `.gitignore` que bloquea todo lo que no sea `.md`.

**Por qué:** el hook `PostToolUse` publica esta carpeta en `main` de forma
automática, silenciosa y sin revisión. Lo que entra sale del computador al
instante y queda en el historial de GitHub, de donde no se retira limpio.

**Qué NO sale de la PC, bajo ninguna forma:** cédulas, nombres de personas
naturales, escrituras y certificados del expediente COAC, cifras de deuda
personal, DSCR, cierres mensuales, y los modelos financieros de Belén y San
Sebastián. Rige `gobernanza-datos-financieros-ia`.

**Cómo se pasa un documento al espejo:** se deja su **ruta local** y un resumen
de lo concluido. El espejo no puede abrirlo —no ve `G:` ni `E:`— así que el
archivo no le serviría de nada; el resumen sí.

## Tema / objetivo del hilo

Sesión de operación diaria del PC de Francisco Duque: diagnóstico y reparación
de la máquina, expedientes, impresión, y gobierno del corpus de 158 skills.
Últimos tramos: cámara de Meet, activación de sesiones en la nube y auditoría
de la red de skills.

## Razonamiento en curso

**Hilo abierto: las 5 cuestiones que PR #1 dejó a criterio de Francisco.**
El espejo hizo bien la auditoría del repositorio, pero **no pudo cerrarlas
porque viven fuera de su alcance**: la mitad de la red son notas de memoria en
`~/.claude/projects/C--Users-datos-Downloads/memory/`, que la nube no ve y la PC
sí. Esa es exactamente la división de trabajo de este relevo.

| # | Cuestión de PR #1 | Quién puede cerrarla |
|---|---|---|
| 1 | 13 notas de memoria escritas con guion: ¿pasar a guion bajo? | **PC** — hay que leer los nombres reales en disco |
| 2 | `[[skill-anterior]]` y `[[wikilink]]`: ¿son marcadores de plantilla? | PC o nube |
| 3 | `[[arquitectura-financiera-escalonada]]`: ¿nota de memoria sin prefijo? | **PC** — se comprueba en `memory/` |
| 4 | Dos rutas relativas de scripts que apuntan a otra skill | PC o nube |
| 5 | Qué cifra de skills es la oficial (154 vs 158) | **PC** — `skills_index.md` vive en `memory/` |

**Hipótesis del espejo sobre el origen de las grafías con guion**, que conviene
verificar: `mapear_red_skills.py` convierte guion bajo en guion al listar
enlaces rotos; si esa lista se usó para escribir enlaces nuevos, explicaría las
variantes. **Sin verificar.**

## Archivos centrales

Punteros, no copias (ver la regla de datos de arriba):

| Qué | Ruta local | Estado |
|---|---|---|
| **PRINCIPAL** — corpus de skills | `~/.claude/skills/` (= este repo) | 158 `SKILL.md`, sincronizado |
| Índice de skills | `…/memory/skills_index.md` | fuera del repo; dice 154 |
| Mapa de la red | `…/memory/skills_network.md` | fuera del repo; dice 592 aristas, hoy son 606 |
| Memoria compartida del proyecto | `…/memory/` | **no sale de la PC** |
| PR de la auditoría | `jjmobijuesa-png/claude-skills-jjmobijuesa#1` | abierto, sin fusionar |

## Siguiente paso concreto

Cerrar las cinco cuestiones de PR #1 con los datos locales: leer los nombres
reales de las notas en `memory/`, resolver el descuadre 154 vs 158 nombrando las
skills no registradas, y decidir sobre los marcadores de plantilla. Después,
fusionar PR #1.

## Pendientes / preguntas abiertas

- **PR #1 sin fusionar** — pendiente de cerrar las cinco cuestiones.
- **PR #2** (`claude/quirky-pascal-4epmn1`) — ya está en `main`; comprobar si
  procede cerrarlo.
- **Notas de Gemini de la reunión del 22-sep** — nunca se recogieron; deberían
  estar en `G:\Mi unidad\Meet Recordings` como
  `Meeting started … - Notes by Gemini`.
- **`REPARAR_EXPLORADOR.bat`** en Descargas — creado, nunca ejecutado.
- **Excel `MsoAria.dll`** — sin comprobar si reincide tras el saneamiento.
- **10 planos de lotes** del expediente COAC — sin revisar ni imprimir.
=======
| **TURNO** | NUBE |
| Principal | Sesión local "Agente IA Local autoreflexivo" (PC, Remote Control) |
| Espejo | Sesión nube "Agente IA Local autoreflexivo - en la nube" (también coordinador de hilos) |
| Último checkpoint | 2026-09-26 00:18 (Guayaquil) — espejo nube: toma de posta |
| Motivo del último relevo | toma automática: PC detenida (tope de gasto mensual; sin volcado previo de la PC) |

## Tema / objetivo del hilo
_Pendiente de confirmar por la PC._ **Hipótesis del espejo:** el hilo trabaja sobre el
bucle autoreflexivo de aprendizaje de la skill `agente-local-autoreflexivo-bookmarks`
(bookmarks de X @fdc_ec → clasificación por tema → aumentar o crear skills `intereses-*`),
posiblemente extendido a LinkedIn (`linkedin-guardados-fedphd`) y a la memoria compartida.
La sesión de la PC acumuló ~400k tokens de contexto antes de detenerse.

## Razonamiento en curso
_No hay volcado de la PC:_ la sesión se detuvo antes de que existiera el protocolo de relevo,
así que su razonamiento solo está en esa conversación.

Lo que sí construyó el espejo en este hilo (sesión nube, 2026-09-26):
- La skill `memoria-compartida-sesiones` (MEMORIA, bitácora, RELEVO en caliente, hooks,
  plantilla de hilos, rol de coordinador). Nació como herramienta para este hilo.
- Los hilos `flujo-caja-proyeccion-mobijuesa` y `financial-report-mobijuesa`, cada uno con su
  propio espejo (no se razonan aquí).

## Archivos centrales
- _Ninguno todavía en `archivos/`._ La PC debe copiar el archivo principal y marcarlo.
- Contexto relacionado en el repo: `agente-local-autoreflexivo-bookmarks/SKILL.md`,
  `memoria-compartida-sesiones/PROMPT-agente-local.md` (prompt con toda la historia).

## Siguiente paso concreto
1. **PC** (cuando se libere el límite): pegar `memoria-compartida-sesiones/PROMPT-agente-local.md`.
   Instala los 4 hooks y hace el primer volcado: tema real, razonamiento en curso, archivo
   principal a `archivos/`, siguiente paso. Al ver TURNO = NUBE, lee este ESTADO y recupera la posta.
2. **Espejo**: con el volcado, continuar desde el siguiente paso que registre la PC.

## Bloqueantes
- 🔴 Sin volcado de la PC: el espejo no conoce el razonamiento ni el archivo principal del hilo.

## Pendientes / preguntas abiertas
- ¿Cuál es el archivo principal del hilo y en qué ruta está?
- ¿Confirma la PC que el tema es el bucle autoreflexivo de bookmarks, u otro?
- Usuario: el espejo viejo de flujo de caja y el "(en caliente)" siguen activos; elegir uno.
>>>>>>> 6422e4cf06b37cacdca1f79272e2337a83daca0d
