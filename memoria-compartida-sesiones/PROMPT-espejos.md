# Instrucción para los chats espejo (una sola vez)

Los espejos creados desde `main` después del 26-sep ya reciben los avisos solos: el hook
`UserPromptSubmit` les muestra `[relevo]` y `[avisos]` antes de cada respuesta.
Pega esto **solo** en un espejo que no muestre la línea `[avisos]` (arrancó antes de este hook):

---
Actualízate con la skill `memoria-compartida-sesiones` y aplícala desde ahora sin que te dé comandos:
1. `git fetch origin main && git merge --no-edit origin/main`.
2. Lee `memoria-compartida-sesiones/AVISOS.md` (sección Vigentes), `RELEVO.md` y el `ESTADO.md` de tu hilo, y aplica los avisos en tu hilo.
3. En cada mensaje mío, antes de responder, ejecuta `bash memoria-compartida-sesiones/scripts/sincronizar-relevo.sh`, lee su salida `[relevo]` y `[avisos]`, y sigue la rutina del aviso A3.
4. Después de cada paso significativo, si no ves que se publique solo, ejecuta `bash memoria-compartida-sesiones/scripts/checkpoint-relevo.sh`.
5. Trabaja solo tu hilo.
---
