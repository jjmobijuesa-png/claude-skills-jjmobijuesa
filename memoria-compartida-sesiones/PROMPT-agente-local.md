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
3. **Instala estos hooks** en `~/.claude/settings.json`, sin borrar los que ya existen. Muéstrame el JSON final antes de guardarlo:
   ```json
   "SessionStart":     [{"hooks":[{"type":"command","command":"bash ~/.claude/skills/memoria-compartida-sesiones/scripts/cargar-memoria.sh"}]}],
   "UserPromptSubmit": [{"hooks":[{"type":"command","command":"bash ~/.claude/skills/memoria-compartida-sesiones/scripts/sincronizar-relevo.sh"}]}],
   "PostToolUse":      [{"matcher":"Write|Edit","hooks":[{"type":"command","command":"bash ~/.claude/skills/memoria-compartida-sesiones/scripts/checkpoint-relevo.sh"}]}],
   "Stop":             [{"hooks":[{"type":"command","command":"bash ~/.claude/skills/memoria-compartida-sesiones/scripts/checkpoint-relevo.sh"}]}]
   ```
   Usa el bash de Git for Windows.
4. **Primer volcado** en `relevos/agente-ia-local-autoreflexivo/`:
   - Copia a `archivos/` los documentos y archivos centrales en los que trabajamos en esta sesión y marca el **archivo principal**. No subas credenciales, cookies ni `.env`.
   - Completa `ESTADO.md` para un lector que no vio esta conversación: tema, **razonamiento en curso**, decisiones, siguiente paso exacto y pendientes. TURNO = PC.
   - Actualiza `MEMORIA.md` con el archivo principal y agrega una fila a `HISTORIAL.md`. Commit y push a `main`.
5. **Checkpoint en caliente, siempre y sin que te lo pida.** Hoy la nube tiene más saldo que la PC, así que tu hilo se cortará y el espejo debe continuar sin comandos. Mientras elaboras CADA respuesta, después de cada paso significativo (conclusión, cálculo, tabla, sección, archivo guardado), actualiza `archivos/` y `ESTADO.md` (lo recién hecho, el siguiente paso exacto y la hora). El hook PostToolUse lo publica en `main` al instante. No esperes al final: el corte puede llegar en medio de una respuesta.
6. **Al inicio de cada respuesta**, lee `ESTADO.md`. Si TURNO = NUBE, el espejo avanzó mientras estabas detenido: lee su resumen y sus cambios en `archivos/`, cópialos a tu ubicación de trabajo, pon TURNO = PC, agrega una fila a HISTORIAL y continúa. No hace falta que te lo diga.

Al terminar, confírmame: qué archivos subiste, cuál es el archivo principal, cuál es el siguiente paso registrado y si los cuatro hooks quedaron instalados.
---

## Funcionamiento sin comandos
| Dónde escribe el usuario | Qué pasa automáticamente |
|---|---|
| PC (cada respuesta) | Sincroniza; si el espejo avanzó, recupera la posta; checkpoint en caliente en cada paso |
| Chat espejo (cualquier mensaje) | Sincroniza; toma la posta (TURNO = NUBE) y continúa desde el siguiente paso |
| Cualquiera: "guarda la sesión" | Entrada en `bitacora/` + MEMORIA + push |
