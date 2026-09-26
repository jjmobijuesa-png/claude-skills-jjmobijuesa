# Prompt para la sesión local "Flujo de caja y proyección Mobijuesa"

Copia lo que está entre las líneas y pégalo en esa sesión de la PC.

---
Este hilo tiene un **agente espejo en la nube** que continúa automáticamente cuando tú te detienes (fin del intervalo de 5 h, cupo o crédito). Hoy la nube tiene más saldo que la PC. Solo se comunican por GitHub: mi repo privado `jjmobijuesa-png/claude-skills-jjmobijuesa`, clonado en `~/.claude/skills`, rama `main`. Apruebo expresamente todo lo que sigue.

1. **Sincroniza**: `cd ~/.claude/skills && git pull origin main`. Lee `memoria-compartida-sesiones/SKILL.md` y `memoria-compartida-sesiones/RELEVO.md` (sobre todo "Regla para el agente de la PC") y aplícalos desde ahora.
2. **Instala estos hooks** en `~/.claude/settings.json`, sin borrar los que ya existen. Muéstrame el JSON final antes de guardarlo:
   ```json
   "SessionStart":     [{"hooks":[{"type":"command","command":"bash ~/.claude/skills/memoria-compartida-sesiones/scripts/cargar-memoria.sh"}]}],
   "UserPromptSubmit": [{"hooks":[{"type":"command","command":"bash ~/.claude/skills/memoria-compartida-sesiones/scripts/sincronizar-relevo.sh"}]}],
   "PostToolUse":      [{"matcher":"Write|Edit","hooks":[{"type":"command","command":"bash ~/.claude/skills/memoria-compartida-sesiones/scripts/checkpoint-relevo.sh"}]}],
   "Stop":             [{"hooks":[{"type":"command","command":"bash ~/.claude/skills/memoria-compartida-sesiones/scripts/checkpoint-relevo.sh"}]}]
   ```
   Usa el bash de Git for Windows.
3. **Primer volcado** en `~/.claude/skills/memoria-compartida-sesiones/relevos/flujo-caja-proyeccion-mobijuesa/`: copia a `archivos/` los archivos centrales (marca el principal; sin credenciales) y completa `ESTADO.md` para un lector que no vio esta conversación: tema, razonamiento en curso, decisiones, siguiente paso exacto y pendientes. TURNO = PC. Agrega una fila a `HISTORIAL.md`.
4. **Checkpoint en caliente, siempre y sin que te lo pida**: mientras elaboras CADA respuesta, después de cada paso significativo (conclusión, cálculo, tabla, sección, archivo guardado), actualiza `archivos/` y `ESTADO.md` (lo recién hecho, el siguiente paso exacto y la hora). El hook PostToolUse lo publica en `main` al instante. No esperes al final de la respuesta: el corte puede llegar en medio y el espejo debe tener la información del momento.
5. **Al inicio de cada respuesta**, lee `ESTADO.md`. Si TURNO = NUBE, el espejo avanzó mientras estabas detenido: lee su resumen y sus cambios en `archivos/`, cópialos a tu ubicación de trabajo, pon TURNO = PC, agrega una fila a HISTORIAL y continúa desde su siguiente paso. No hace falta que te lo diga.

6. **Siguiente paso de este hilo (requiere Edge, solo la PC puede hacerlo)**: abre en mi sesión de LinkedIn (fedphd@gmail.com) la publicación https://www.linkedin.com/feed/update/urn:li:activity:7508480383286452224/ (skill `linkedin-guardados-fedphd`, solo lectura). Extrae autor, fecha, texto completo, descripción de imágenes o carrusel y enlaces, y guárdalo YA en `archivos/linkedin-post-7508480383286452224.md` para que el espejo lo tenga. Después busca, crea y aplica su directriz al flujo de caja y la proyección, con checkpoint en caliente en cada paso.

Confírmame qué archivos subiste, cuál es el principal, el siguiente paso registrado y que los cuatro hooks quedaron instalados.
---
