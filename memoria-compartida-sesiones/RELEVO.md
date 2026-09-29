# Protocolo de RELEVO EN CALIENTE PC ⇄ nube

Objetivo: que el razonamiento de un hilo **no se rompa** cuando la sesión de la PC
se corta (fin del intervalo de 5 h, cupo o crédito agotado, PC apagada).
La nube tiene hoy el mayor saldo: el **espejo** debe tener **en todo momento** la
información caliente para continuar **sin que nadie dé un comando**.
**Un solo agente trabaja a la vez.**

## Estrategia
1. **La PC escribe en caliente, constantemente.** Mientras elabora cada respuesta,
   después de cada paso significativo, vuelca razonamiento y archivos a
   `relevos/<hilo>/` y lo publica en `main`. No espera al final: el corte puede
   llegar en medio de una respuesta y en ese momento ya no puede escribir nada.
2. **El espejo toma la posta solo.** Cualquier mensaje del usuario en el chat espejo
   significa "la PC se detuvo". El espejo sincroniza, asume el TURNO y continúa
   desde el siguiente paso, sin pedir comandos.
3. **La PC recupera la posta sola.** Cualquier mensaje del usuario en la PC
   significa "vuelve la PC". La PC sincroniza, lee lo que avanzó el espejo,
   asume el TURNO y continúa.

## Canal
`memoria-compartida-sesiones/relevos/<hilo>/` en la rama **`main`** del repo privado
`jjmobijuesa-png/claude-skills-jjmobijuesa`.
- `ESTADO.md` — estado vivo; **TURNO** (`PC` | `NUBE`) = quién trabajó por última vez.
- `archivos/` — copia actual de los documentos y entregables centrales (incluido el principal).
- `HISTORIAL.md` — una fila por cada cambio de TURNO.

## Automatización (hooks)
| Hook | Script | Qué hace |
|---|---|---|
| `SessionStart` | `cargar-memoria.sh` | Al abrir la sesión: pull + muestra MEMORIA y bitácora |
| `UserPromptSubmit` | `sincronizar-relevo.sh` | **Antes de cada respuesta**: trae lo último de `main`, muestra el TURNO de cada hilo y los **avisos vigentes** de `AVISOS.md` |
| `PostToolUse` (Write/Edit) | `checkpoint-relevo.sh` | **Después de cada edición**: si cambió el relevo, commit + push a `main` |
| `Stop` | `checkpoint-relevo.sh` | Al terminar la respuesta: último checkpoint |

El agente también puede ejecutar `bash <skills>/memoria-compartida-sesiones/scripts/checkpoint-relevo.sh`
en medio de una respuesta cuando lo crea necesario.

## Regla para el agente de la PC (principal)
- **En cada respuesta, antes de razonar**: lee el `ESTADO.md` de tu hilo (el hook ya sincronizó).
  Si TURNO = NUBE, el espejo avanzó: lee su resumen y sus cambios en `archivos/`, copia
  esos cambios a tu ubicación de trabajo, pon TURNO = PC, agrega una fila a HISTORIAL y continúa.
- **Durante la respuesta**, después de cada paso significativo (una conclusión, una tabla,
  una sección, un cálculo, un archivo guardado):
  1. Copia a `archivos/` la versión actual de los archivos centrales que cambiaron.
  2. Actualiza `ESTADO.md`: razonamiento en curso, lo recién hecho, **siguiente paso exacto**
     y la hora del checkpoint.
  El hook PostToolUse lo publica al instante.
- Escribe `ESTADO.md` para un lector que **no vio la conversación**: el espejo solo tiene eso.
- No necesitas detectar tu saldo: como el checkpoint es constante, el corte encuentra
  el estado ya publicado.

## Regla para el agente espejo (nube)
- **En cada mensaje del usuario, sin esperar comandos**:
  1. El hook ya sincronizó `main`. Lee `ESTADO.md`, `HISTORIAL.md` y `archivos/` de tu hilo.
  2. Si TURNO = PC: toma la posta automáticamente (TURNO = NUBE, motivo "toma automática:
     PC detenida", fila en HISTORIAL) y resume en 2–3 líneas dónde quedó.
  3. Continúa desde el **siguiente paso**, con el mismo checkpoint en caliente que la PC.
- Si falta un insumo que solo la PC puede obtener (p. ej. LinkedIn en Edge), regístralo
  en ESTADO como bloqueante, avanza en todo lo demás y díselo al usuario.
- Trabaja **solo tu hilo**.

## Reglas comunes
- Gana el TURNO quien recibió el último mensaje del usuario; el otro solo lee.
- Conflicto en push → el script integra `origin/main`; si choca el mismo archivo,
  prevalece la versión de quien tiene el TURNO.
- Nada de credenciales, cookies ni `.env` en `archivos/`.
- El espejo usa la cuenta y el crédito del propio usuario.
- Frases opcionales (no necesarias): "pasa la posta", "toma la posta", "devuelve la posta", "retoma la posta".

## Un espejo por hilo
Cada agente de la PC tiene **su propia carpeta** en `relevos/` y **su propio chat espejo**.
Un chat nunca razona dos hilos. La continuidad vive en `ESTADO.md`: si un espejo se archiva,
cualquier sesión nueva del repo continúa el hilo igual.

## Avisos (actualizaciones sin comandos)
Cuando cambia una regla o una decisión que afecta a varios hilos, el coordinador la escribe en
`AVISOS.md` › Vigentes. El hook la muestra antes de cada respuesta en **todas** las sesiones con
hooks (PC y espejos), y cada agente la aplica en su hilo sin que el usuario la pegue.

## Coordinador
Un chat de la nube (hoy: "Ver otras sesiones de Claude Code") que **no razona los temas**:
lleva la tabla de hilos de `MEMORIA.md`, publica avisos en `AVISOS.md`, informa qué hilos esperan, y crea hilos y
espejos cuando el usuario dice **"crea espejo para <agente>"**.

## Crear un hilo nuevo ("crea espejo para <agente>")
1. Copiar `relevos/_plantilla/` a `relevos/<hilo-en-kebab-case>/` y completar `ESTADO.md`.
2. Generar `relevos/<hilo>/PROMPT-pc.md` desde la plantilla y agregar la fila en `MEMORIA.md`.
3. Commit + push a `main`.
4. Crear la sesión espejo (título "Espejo — <nombre>", repo `claude-skills-jjmobijuesa`) con la
   instrucción de aplicar la "Regla para el agente espejo" de este archivo, solo para ese hilo.
5. Dar al usuario el `PROMPT-pc.md` para pegarlo en el agente de la PC.
