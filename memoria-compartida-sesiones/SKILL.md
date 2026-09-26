---
name: memoria-compartida-sesiones
description: |
  Memoria compartida entre TODAS las sesiones de Claude del usuario:
  agente local en la PC (con o sin Remote Control), sesiones en la nube
  (claude.ai/code), teléfono y tablet. La fuente única de verdad es este
  repo de GitHub: `MEMORIA.md` (estado vivo) + `bitacora/` (una entrada
  por sesión). Al iniciar: sincronizar y leer. Al cerrar: escribir
  entrada, actualizar MEMORIA.md, commit y push.

  Usar SIEMPRE al empezar o terminar una sesión de trabajo, al cambiar
  de dispositivo, o cuando el usuario pida continuar algo "que hablamos
  en la nube / en la PC / en otro chat".

trigger_phrases:
  - "memoria compartida"
  - "guarda la sesión"
  - "sube el resumen"
  - "continúa lo de la nube"
  - "continúa lo de la PC"
  - "qué hablamos en el otro chat"
  - "cierra sesión"
  - "sincroniza memoria"
  - "pasa la posta"
  - "toma la posta"
  - "retoma la posta"
  - "agente espejo"
  - "crea espejo para"
  - "qué hilos esperan"

idioma_de_salida: español neutro
nivel_madurez: aplicada
fuente: sesión en la nube 2026-09-26 (ver bitacora/2026-09-26-nube-ver-sesiones-remote-control.md)
---

# Memoria compartida entre sesiones

## Doctrina

Las sesiones de Claude NO comparten memoria entre sí: el chat de la nube
no ve la PC y el agente de la PC no ve el chat de la nube. Lo único que
todas ven es **GitHub**. Por eso la memoria compartida vive aquí, en
texto plano, versionada.

- Nube → lee y escribe el repo directamente (se clona al iniciar).
- PC → el repo vive en `~/.claude/skills/`; se sincroniza con `git pull` / `git push`.
- Teléfono/tablet → controlan sesiones de nube o de PC (Remote Control); no guardan nada propio.

Todas las sesiones consumen la misma cuenta y los mismos límites de uso.

## Estructura

```
memoria-compartida-sesiones/
├── SKILL.md              # esta doctrina
├── MEMORIA.md            # estado vivo: proyectos, archivo principal, pendientes
├── bitacora/             # AAAA-MM-DD-<origen>-<tema>.md, una por sesión
├── RELEVO.md             # protocolo de posta PC ⇄ nube (agente espejo)
├── PROMPT-agente-local.md # prompt para activar el relevo en la PC
├── relevos/_plantilla/   # plantilla para hilos nuevos (ESTADO, HISTORIAL, PROMPT-pc)
├── relevos/<hilo>/       # ESTADO.md (TURNO), archivos/, HISTORIAL.md, PROMPT-pc.md
└── scripts/              # cargar-memoria.sh (SessionStart), checkpoint-relevo.sh (Stop)
```

## Protocolo de INICIO (automático o manual)

1. `git pull` del repo (en la PC: `cd ~/.claude/skills && git pull`).
2. Leer `MEMORIA.md` y las 3 entradas más recientes de `bitacora/`.
3. Decir al usuario en 2–3 líneas dónde quedó el trabajo y qué sigue.

## Protocolo de CIERRE (al terminar o cuando el usuario lo pida)

1. Crear `bitacora/AAAA-MM-DD-<pc|nube>-<tema-corto>.md` con:
   - Qué se pidió · qué se hizo · archivos tocados (ruta en el repo) · decisiones · pendientes.
   - Máx. ~40 líneas. Sin secretos, contraseñas, tokens ni datos bancarios completos.
2. Actualizar `MEMORIA.md` (sección "Estado actual" y "Pendientes"); borrar lo resuelto.
3. `git add memoria-compartida-sesiones && git commit -m "memoria: <tema>" && git push`.
   - Si `push` falla por cambios remotos: `git pull --rebase` y reintentar.
4. Confirmar al usuario que quedó subido.

## Reglas

- Trabajar el mismo archivo en un solo dispositivo a la vez; push antes de cambiar.
- Los entregables (documentos, Excel, productos) van al repo, no solo a la PC,
  si deben estar disponibles en la nube.
- Nunca subir credenciales, cookies ni `.env`.

## Activación automática

**Nube:** el repo trae `.claude/settings.json` con un hook `SessionStart`
que ejecuta `scripts/cargar-memoria.sh` (requiere que esté en la rama `main`).

**PC (Windows, una vez):** agregar a `C:\Users\<usuario>\.claude\settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      { "hooks": [ { "type": "command",
        "command": "bash ~/.claude/skills/memoria-compartida-sesiones/scripts/cargar-memoria.sh" } ] }
    ]
  }
}
```

(Usa el `bash` de Git for Windows. Si ya hay otros hooks, añadir este dentro de la lista existente.)

El cierre no es automático: pedir "guarda la sesión" o "cierra sesión" al final.

## Relevo automático con agente espejo

Para hilos largos que no deben cortarse por límites de uso, ver `RELEVO.md`:
un agente principal (PC) y un espejo (nube) se pasan la posta a través de
`relevos/<hilo>/ESTADO.md` (campo TURNO). El hook `Stop` ejecuta
`scripts/checkpoint-relevo.sh` y sube cada avance en caliente.
**Un hilo = un agente de la PC = una carpeta = un chat espejo.** Un chat coordinador
lleva la tabla de hilos en `MEMORIA.md` y crea espejos con "crea espejo para <agente>"
(ver `RELEVO.md` › Coordinador).
