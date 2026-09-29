# AVISOS para todos los agentes (PC y espejos)

El hook `UserPromptSubmit` (`scripts/sincronizar-relevo.sh`) imprime la sección
**Vigentes** antes de cada respuesta, en todas las sesiones que tienen los hooks.
Cada agente la aplica **sin que el usuario dé comandos**. Lo escribe el coordinador;
un aviso se mueve a «Archivados» cuando ya no hace falta.

## Vigentes

- **A1 (2026-09-28) Excepción de datos.** Solo el hilo `flujo-caja-proyeccion-mobijuesa` puede
  guardar el Excel real de flujo de caja de Mobijuesa en su `archivos/`. No borrarlo ni ponerle
  candado. En los demás hilos rige la regla general: solo `.md` con resúmenes y punteros.
  Detalle: `MEMORIA.md` › Regla de datos y excepciones.
- **A2 (2026-09-28) Red de skills.** `mapear_red_skills.py` ya conserva `_` en los nombres y
  `memoria-compartida-sesiones` está enlazada (159 skills, 607 aristas, 0 huérfanas). Al citar
  notas de memoria, usar la grafía con guion bajo. **PC:** regenerar `memory/skills_network.md`.
- **A3 (2026-09-28) Rutina de cada respuesta**, para cada agente en su propio hilo:
  1. Leer la línea `[relevo]` de tu hilo y estos avisos.
  2. Si el TURNO es del otro lado, tomar la posta (TURNO = tu lado, fila en `HISTORIAL.md`)
     y empezar por la sección «Para … al volver» del `ESTADO.md`, si existe.
  3. Checkpoint en caliente en cada paso (el hook lo publica en `main`).
  4. Trabajar solo tu hilo; no editar carpetas de otros hilos.
- **A4 (2026-09-28) Espejos duplicados.** Si hay dos chats espejo del mismo hilo, trabaja solo
  el que recibió el último mensaje del usuario. Si el `HISTORIAL.md` muestra un checkpoint de
  otro espejo en los últimos 10 minutos, no escribas: avisa al usuario.

## Archivados

_(vacío)_
