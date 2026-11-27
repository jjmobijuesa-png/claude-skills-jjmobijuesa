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
  `memoria-compartida-sesiones` está enlazada. Al citar
  notas de memoria, usar la grafía con guion bajo.
  **Medido el 27-nov-2026 regenerando el mapa: 210 skills, 1.079 aristas, 1 racimo, 0 huérfanas.** Las cifras de la tarde (199 / 897) eran previas a las tres skills de la clase 32.
  Mapa regenerado ese día; el pendiente de regenerarlo queda CERRADO. Las cifras
  se generan con `mapear_red_skills.py`, no se copian a mano.
- **A3 (2026-09-28) Rutina de cada respuesta**, para cada agente en su propio hilo:
  1. Leer la línea `[relevo]` de tu hilo y estos avisos.
  2. Si el TURNO es del otro lado, tomar la posta (TURNO = tu lado, fila en `HISTORIAL.md`)
     y empezar por la sección «Para … al volver» del `ESTADO.md`, si existe.
  3. Checkpoint en caliente en cada paso (el hook lo publica en `main`).
  4. Trabajar solo tu hilo; no editar carpetas de otros hilos.
- **A4 (2026-09-28) Espejos duplicados.** Si hay dos chats espejo del mismo hilo, trabaja solo
  el que recibió el último mensaje del usuario. Si el `HISTORIAL.md` muestra un checkpoint de
  otro espejo en los últimos 10 minutos, no escribas: avisa al usuario.

- **A5 (2026-09-29) Sesión nueva (p. ej. abierta con `claude remote-control`).** Si tu
  conversación no dice todavía a qué hilo perteneces:
  1. Compara el título de tu sesión y el primer mensaje del usuario con la tabla de hilos de
     `MEMORIA.md`. Si coincide claramente con uno, ese es tu hilo: dilo en una línea y sigue A3.
  2. Si no coincide, pregunta al usuario en una línea: «¿Continúo un hilo existente
     (lista) o abro uno nuevo?». Para uno nuevo, copia `relevos/_plantilla/` y agrega la fila
     en `MEMORIA.md`.
  3. Desde ese momento, escribe en `ESTADO.md` de tu hilo en caliente (A3.3): los hooks solo
     publican lo que tú escribes; si no actualizas `ESTADO.md`, el espejo no recibe nada.

- **A6 (2026-09-29) Espejo automático.** Toda sesión de la PC abierta con `claude remote-control`
  recibe un espejo «Espejo — <título>» creado por el coordinador (skill
  `espejo-automatico-remote-control`; registro en `ESPEJOS.md`). **PC:** si tu hilo no existe
  aún, créalo desde la plantilla (A5); el espejo aparecerá en el siguiente ciclo del coordinador.
  **Espejos:** no crees otros espejos; eso lo hace solo el coordinador.

- **A7 (2026-11-20) Verticalidad de la cadena: skill de carga obligada en los hilos de
  blockchain.** Los hilos `ibpp-ecualedger-soberana` y
  `junta-politica-financiera-blockchain-soberana` cargan
  `del-miedo-al-requisito-verificable` **antes** de evaluar una arquitectura, un
  proveedor, un borrador normativo o un material de origen dudoso. Aporta dos cosas que
  no estaban en la red: el **cuestionario de diez capas** de verticalidad —jurisdicción,
  infraestructura física, red, consenso, llaves, reglas, identidad, datos, aplicación y
  **salida**— y la conversión **miedo → requisito → verificación**, que vuelve utilizable
  un material impresentable sin citarlo.
  🚦 **Compuerta dura: ese género de fuente NUNCA se cita en un documento
  institucional** — ni a BID, ni a CAF, ni ante la JRPFM, ni en material de la Fundación.
  Una sola cita de esa procedencia destruye la credibilidad del documento entero, y el
  argumento se sostiene sin ella. **El requisito entra al expediente; la fuente no.**
  🚦 **La fila de «salida» es la prueba de fuego:** un sistema del que no se puede salir
  no es soberano por mucho que lo diga su documentación.
  Este aviso informa a esos hilos; **no autoriza a nadie a editar la carpeta de otro
  hilo** (sigue rigiendo A3.4).

## Archivados

_(vacío)_
