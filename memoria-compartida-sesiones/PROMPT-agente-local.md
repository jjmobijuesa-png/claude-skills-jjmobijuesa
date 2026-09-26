# Prompt para pegar en la sesión "Agente IA Local autoreflexivo"

Copia lo que está entre las líneas y pégalo en esa sesión (en la PC o desde la app vía Remote Control).

---
Te pongo al día de lo que hice en una sesión de Claude Code en la nube (claude.ai/code, sesión "Ver otras sesiones de Claude Code") mientras tú estabas detenido por el tope de gasto mensual. Esa sesión es ahora tu **agente espejo**: tú eres el **agente principal** y nos comunicamos únicamente a través de GitHub. Lo apruebo todo expresamente.

## La historia, en orden
1. Aprendí a ver todas mis sesiones en la app y en claude.ai/code. Las sesiones locales aparecen cuando se inician con `claude remote-control` (o `/remote-control`); eso ya funciona contigo.
2. Te detuviste con "You've hit your monthly spend limit". No me faltaba saldo: el bloqueo es el tope de gasto mensual (claude.ai/settings/usage). La nube y la PC comparten la misma cuenta y los mismos límites. Ya sé usar mi saldo promocional en la nube.
3. Decidimos que **GitHub es la fuente única de verdad**: mi repo privado `jjmobijuesa-png/claude-skills-jjmobijuesa`, que en esta PC está clonado en `~/.claude/skills`.
4. El espejo creó la skill **`memoria-compartida-sesiones`** para que todas mis sesiones compartan memoria.
5. Elegí el **relevo automático**: cuando tú te detengas (cupo, intervalo de 5 h, crédito, PC apagada), el espejo en la nube toma la posta, sigue razonando sobre el mismo archivo y te la devuelve. Trabaja un solo agente a la vez, según el campo TURNO.
6. Todo está en el PR https://github.com/jjmobijuesa-png/claude-skills-jjmobijuesa/pull/2 (rama `claude/quirky-pascal-4epmn1`), hacia `main`.

## Qué creó el espejo (dentro de `~/.claude/skills/`)
- `memoria-compartida-sesiones/SKILL.md`: doctrina y protocolos de inicio y cierre.
- `memoria-compartida-sesiones/MEMORIA.md`: estado vivo (proyectos, archivo principal, pendientes, hilos con relevo).
- `memoria-compartida-sesiones/RELEVO.md`: protocolo de posta PC ⇄ nube.
- `memoria-compartida-sesiones/bitacora/`: un resumen por sesión (lee las dos entradas del 2026-09-26).
- `memoria-compartida-sesiones/relevos/agente-ia-local-autoreflexivo/`: el canal de ESTE hilo, con `ESTADO.md` (TURNO = PC, vacío hasta tu primer checkpoint), `HISTORIAL.md` y `archivos/`.
- `memoria-compartida-sesiones/scripts/cargar-memoria.sh` (para SessionStart) y `checkpoint-relevo.sh` (para Stop: commit y push automáticos de la skill).
- `.claude/settings.json` del repo: esos mismos hooks para las sesiones de la nube.

## Lo que tienes que hacer ahora
1. **Trae lo creado.** `cd ~/.claude/skills && git pull origin main`. Si no aparece la carpeta `memoria-compartida-sesiones/` (porque el PR aún no está fusionado), ejecuta `git fetch origin claude/quirky-pascal-4epmn1 && git merge --no-edit origin/claude/quirky-pascal-4epmn1 && git push origin HEAD:main`. Muéstrame el resultado antes del push.
2. **Lee** `SKILL.md`, `RELEVO.md`, `MEMORIA.md` y las entradas de `bitacora/`, y aplica la skill desde ahora.
3. **Instala los hooks** en `~/.claude/settings.json`, sin borrar los que ya existen:
   - `SessionStart` → `bash ~/.claude/skills/memoria-compartida-sesiones/scripts/cargar-memoria.sh`
   - `Stop` → `bash ~/.claude/skills/memoria-compartida-sesiones/scripts/checkpoint-relevo.sh`
   Usa el bash de Git for Windows y muéstrame el JSON final antes de guardarlo.
4. **Haz el primer checkpoint** en `relevos/agente-ia-local-autoreflexivo/`:
   - Copia a `archivos/` los documentos y archivos centrales en los que trabajamos en esta sesión y marca cuál es el **archivo principal**. No subas credenciales, cookies ni `.env`.
   - Completa `ESTADO.md`: tema, **razonamiento en curso** (lo suficiente para que el espejo continúe sin leer esta conversación), archivos centrales, siguiente paso concreto y pendientes. Deja TURNO = PC.
   - Actualiza `MEMORIA.md` con el archivo principal y agrega una fila a `HISTORIAL.md`.
   - Commit y push a `main`.
5. **Desde ahora**, actualiza `ESTADO.md` y `archivos/` después de cada avance significativo (el hook Stop se encarga de subirlos). Si ves un aviso de límite de uso, de cupo o crédito por agotarse, o te digo "pasa la posta", entrega la posta: TURNO = NUBE, motivo, fila en HISTORIAL, push, y avísame para que abra el espejo.
6. Cuando te diga **"retoma la posta"**: `git pull origin main`, lee `ESTADO.md`, `HISTORIAL.md` y lo que el espejo cambió en `archivos/`, copia esos cambios a tu ubicación de trabajo y continúa desde el siguiente paso registrado.

Al terminar, confírmame: qué archivos subiste, cuál es el archivo principal, cuál es el siguiente paso registrado y si los dos hooks quedaron instalados.
---

## Frases de control (en cualquier dispositivo)
| Dónde | Frase | Efecto |
|---|---|---|
| PC | "pasa la posta" | Checkpoint + TURNO = NUBE |
| Nube (espejo) | "toma la posta" | Pull de `main`, lee ESTADO y continúa |
| Nube (espejo) | "devuelve la posta" | Checkpoint + TURNO = PC + push a `main` |
| PC | "retoma la posta" | Pull, lee cambios del espejo y continúa |
| Cualquiera | "guarda la sesión" | Entrada en `bitacora/` + MEMORIA + push |
