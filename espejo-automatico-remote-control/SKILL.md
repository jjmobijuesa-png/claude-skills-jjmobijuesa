---
name: espejo-automatico-remote-control
description: |
  Crea automáticamente un chat espejo en la nube por cada sesión de la PC abierta con
  `claude remote-control`, con el nombre «Espejo — <título de la sesión>», su carpeta de
  relevo en `memoria-compartida-sesiones/relevos/<hilo>/` y su fila en el registro
  `ESPEJOS.md`. La ejecuta el COORDINADOR (sesión de la nube con las herramientas de
  sesiones remotas): la PC no puede crear sesiones en la nube, pero el coordinador sí ve
  las sesiones de Remote Control y las empareja.

  Usar cuando el usuario diga «crea espejo para <agente>», «revisa si hay sesiones sin
  espejo», o en cada mensaje al coordinador (paso 0 de su rutina), y en cada disparo de
  la rutina programada «Espejos automáticos».

trigger_phrases:
  - "crea espejo para"
  - "espejo automático"
  - "sesiones sin espejo"
  - "abrí claude remote-control"
  - "nuevo agente en la PC"

idioma_de_salida: español
nivel_madurez: aplicada
fuente: sesión nube coordinadora, 2026-09-29
relacionada: memoria-compartida-sesiones
---

# Espejo automático para cada `claude remote-control`

Complemento de [[memoria-compartida-sesiones]]: esa skill define el relevo en caliente
entre la PC y un espejo; esta crea el espejo sin que el usuario lo pida.

## Límite real (leer antes de prometer)
- `claude remote-control` corre en la PC y **no puede crear sesiones en la nube**. Tampoco
  existe un evento que avise a la nube en el instante en que se abre.
- Lo que sí existe: las sesiones de Remote Control aparecen en la lista de sesiones de la
  cuenta (origen `claude_code_cli`, etiqueta `remote-control-sdk`, tipo `bridge`), y el
  coordinador puede listarlas y crear sesiones nuevas.
- Por eso el espejo se crea **en el siguiente ciclo del coordinador**: cuando el usuario le
  escribe, o cuando dispara la rutina programada (si está activa). No es instantáneo.

## Procedimiento del coordinador (paso 0 de cada mensaje o disparo)
1. `list_sessions` (primeras 20). Candidatas: `tags` contiene `remote-control-sdk`,
   `session_status` ≠ `ARCHIVED`, y título que no esté en «Excluidas» de `ESPEJOS.md`.
2. Descartar las que ya están en `ESPEJOS.md` (por **id** de la sesión de la PC).
3. Para cada candidata nueva:
   - **Si el usuario ya confirmó** («crea espejo para …», o la regla de abajo está activa):
     a. `hilo` = título en minúsculas, sin acentos, espacios → `-`.
     b. Copiar `memoria-compartida-sesiones/relevos/_plantilla/` a `relevos/<hilo>/`
        (con su `archivos/.gitignore`), completar ESTADO (nombre, id de la sesión PC,
        TURNO = PC), HISTORIAL y PROMPT-pc.
     c. Agregar la fila en la tabla de hilos de `MEMORIA.md` y en `ESPEJOS.md`.
     d. Publicar en `main` (el hook lo hace al editar; si no, `checkpoint-relevo.sh`).
     e. `create_session` con título **«Espejo — <título exacto de la sesión PC>»**, repo
        `jjmobijuesa-png/claude-skills-jjmobijuesa`, rama `main`, y el prompt de
        «Prompt del espejo» (abajo) con el nombre del hilo.
     f. Anotar el id del espejo en `ESPEJOS.md`.
   - **Si no hay confirmación:** registrarla en «Sesiones de la PC sin espejo» de
     `ESPEJOS.md` y avisar al usuario en una línea.
4. Informar al usuario: espejos creados (nombre) y candidatas pendientes.

**Regla de confirmación:** por defecto se crea el espejo sin preguntar para toda sesión
nueva de Remote Control, salvo las «Excluidas». Si el usuario prefiere confirmar cada una,
anotarlo en `MEMORIA.md` y seguir la rama «sin confirmación».

## Prompt del espejo (plantilla)
> Eres el agente espejo en la nube del hilo `memoria-compartida-sesiones/relevos/<hilo>/`
> («<título>»). El principal corre en la PC con `claude remote-control` (sesión `<id>`).
> Lee `memoria-compartida-sesiones/SKILL.md`, `RELEVO.md`, `AVISOS.md` (Vigentes),
> `MEMORIA.md` y tu carpeta. Canal único: `main`. Un hilo = un espejo: trabaja solo el tuyo.
> Relevo en caliente sin comandos: los hooks muestran `[relevo]`/`[avisos]` y publican
> cada edición; cualquier mensaje del usuario aquí = la PC se detuvo → toma la posta (A3).
> Regla de datos: `archivos/` solo resúmenes y punteros `.md`. Primer mensaje: toma la
> posta, informa el estado en 3–4 líneas y prepara un marco en `archivos/` sin inventar el
> tema (lo confirma la PC). Responde en español.

## Lado PC
Nada extra: con los 4 hooks de `memoria-compartida-sesiones` instalados, la sesión nueva
recibe los avisos (A5 le dice cómo identificar su hilo) y vuelca en caliente a `relevos/<hilo>/`.
Si la sesión PC arranca antes de que exista su carpeta, A5 le indica crearla desde la
plantilla; el coordinador la reconoce luego por el id y solo crea el espejo.

## Rutina programada (opcional)
Para que no dependa de escribirle al coordinador: una rutina «Espejos automáticos» que
dispare cada hora una sesión nueva en este entorno con la instrucción «aplica la skill
`espejo-automatico-remote-control`». Cada disparo consume uso de la cuenta; activarla
solo con autorización del usuario.
