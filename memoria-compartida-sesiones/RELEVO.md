# Protocolo de RELEVO (posta) PC ⇄ nube

Objetivo: que el razonamiento de un hilo **no se rompa** cuando la sesión
principal se detiene (fin de cupo, intervalo de 5 h, crédito agotado,
PC apagada). Un agente **espejo** en la nube toma la posta, sigue razonando
sobre el mismo archivo y la devuelve. **Un solo agente trabaja a la vez.**

## Canal
`memoria-compartida-sesiones/relevos/<hilo>/`
- `ESTADO.md` — estado vivo del hilo; el campo **TURNO** (`PC` | `NUBE`) decide quién trabaja.
- `archivos/` — copia de los documentos/entregables centrales (incluido el archivo principal).
- `HISTORIAL.md` — una fila por cada relevo.

Rama: **`main`** del repo `jjmobijuesa-png/claude-skills-jjmobijuesa` (privado).

## 1. Checkpoint en caliente (agente con el TURNO)
Después de **cada avance significativo**, no solo al final:
1. Copiar a `archivos/` la versión actual de los archivos centrales.
2. Reescribir `ESTADO.md` (razonamiento, siguiente paso, pendientes, hora).
3. El hook `Stop` (`scripts/checkpoint-relevo.sh`) hace commit + push al terminar la respuesta.

Si el corte llega sin aviso, el espejo pierde como máximo un paso.
El agente no ve su saldo con precisión: por eso el checkpoint es continuo.

**Entregar la posta de inmediato ante:** aviso de límite de uso, cupo o
crédito casi agotado, el usuario dice "pasa la posta", o la PC se va a apagar.

## 2. Entregar la posta (PC → NUBE)
1. Checkpoint completo.
2. `ESTADO.md`: **TURNO = NUBE**, "Motivo del último relevo".
3. Fila nueva en `HISTORIAL.md`. Push.
4. Avisar: *"Posta entregada. Abre la sesión espejo y di: toma la posta de <hilo>."*

## 3. Tomar la posta (espejo en la nube)
1. `git pull origin main`.
2. Leer `ESTADO.md`, `HISTORIAL.md` y `archivos/`. Verificar **TURNO = NUBE**.
3. Resumir al usuario en 3 líneas dónde quedó y continuar el **siguiente paso**.
4. Trabajar sobre `archivos/` con checkpoints en caliente; push a `main`.

## 4. Devolver la posta (NUBE → PC)
1. Checkpoint completo + resumen de lo razonado en la nube en `ESTADO.md`.
2. **TURNO = PC**, fila en `HISTORIAL.md`. Push a `main`.
3. En la PC, el agente principal ("retoma la posta"): `git pull`, lee `ESTADO.md`,
   copia de `archivos/` a su ubicación de trabajo lo que cambió, y continúa.

## Reglas
- Si el TURNO no es tuyo: **solo leer**, no editar `archivos/`.
- Conflicto en push → `git pull --rebase`; si choca el mismo archivo, gana quien tiene el TURNO.
- Nada de credenciales, cookies ni `.env` en `archivos/`.
- El espejo usa la cuenta y el crédito del propio usuario.

## Un espejo por hilo (regla)
Cada agente de la PC tiene **su propia carpeta** en `relevos/` y **su propio chat espejo**
en la nube. Un chat nunca razona dos hilos: así no se mezclan ideas ni contenidos.
La continuidad vive en `ESTADO.md`, no en el chat: si un espejo se archiva, cualquier
sesión nueva que diga "toma la posta de <hilo>" continúa igual.

## Coordinador
Un chat de la nube (hoy: "Ver otras sesiones de Claude Code") que **no razona los temas**:
- Lee la tabla de hilos de `MEMORIA.md` y el TURNO de cada `ESTADO.md`; informa qué hilo espera en la nube.
- Crea hilos y espejos cuando el usuario dice **"crea espejo para <agente>"**.
- Mantiene actualizada la tabla de hilos.

## Crear un hilo nuevo ("crea espejo para <agente>")
1. Copiar `relevos/_plantilla/` a `relevos/<hilo-en-kebab-case>/` y completar `ESTADO.md`
   (nombre, principal, espejo, tema, siguiente paso conocido).
2. Generar `relevos/<hilo>/PROMPT-pc.md` desde la plantilla y agregar la fila en la tabla de `MEMORIA.md`.
3. Commit + push.
4. Crear la sesión espejo en la nube (título "Espejo — <nombre>", repo `claude-skills-jjmobijuesa`)
   con la instrucción: leer `SKILL.md`, `RELEVO.md` y `relevos/<hilo>/`, trabajar SOLO ese hilo,
   y si TURNO = PC, esperar a "toma la posta".
5. Dar al usuario el `PROMPT-pc.md` para pegarlo en el agente de la PC.
