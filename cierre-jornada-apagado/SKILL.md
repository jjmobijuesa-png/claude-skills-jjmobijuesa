---
name: cierre-jornada-apagado
description: |
  Rutina de CIERRE DE JORNADA: finaliza los entregables abiertos, envía una
  confirmación al usuario (correo a jjmobijuesa@gmail.com con el/los archivo(s)
  adjunto(s), o mensaje de WhatsApp a su propio número si WhatsApp Web está
  logueado), cierra los programas y APAGA el computador con un temporizador de
  gracia abortable.

  Casos de uso:
  - "cierra todo y apaga el computador"
  - "termina, envíame el archivo y apaga"
  - "cierre de jornada"

  Orden obligatorio (no alterar):
  1. Guardar/finalizar todos los archivos en curso.
  2. Enviar la confirmación con el adjunto ANTES de cerrar nada (necesita Edge).
  3. Verificar que el envío salió (search_threads in:sent).
  4. Commit + push del repo de skills (sólo si hay cambios — ver Paso 4).
  5. Apagar con `shutdown /s /t 90` (cierra programas y apaga; abortable con
     `shutdown /a`). Nunca usar /f sin avisar — respeta trabajo sin guardar.

  Reglas de seguridad heredadas:
  - El envío de mensajes/correo en nombre del usuario requiere su autorización;
    aquí se ejecuta solo bajo instrucción explícita de cierre.
  - El apagado se hace con temporizador de gracia (90 s) para permitir abortar
    y para que las apps con cambios sin guardar pregunten al usuario.
---

# Cierre de jornada y apagado

## Paso 1 — Finalizar
Guardar cualquier Excel/PDF/Word en proceso. Confirmar que los archivos
existen en disco con su ruta.

## Paso 2 — Confirmación al usuario (elegir la vía más fiable)
**Vía A (preferida): correo con adjunto** — más confiable.
```
python C:/Users/datos/.claude/skills/gmail-send-playwright/scripts/send.py \
  --profile jjm --to "jjmobijuesa@gmail.com" \
  --subject "Confirmacion - cierre de jornada" \
  --body-file <body.txt> --attach "<ruta del archivo>"
```
**Vía B (alterna): WhatsApp al propio número** — solo si WhatsApp Web está
logueado en el perfil Edge. Usar enlace `wa.me/<numero>?text=<msg>` o Playwright.

## Paso 3 — Verificar
`search_threads` con `in:sent newer_than:1h subject:"cierre"` para confirmar
que el correo salió. Si no, reintentar antes de apagar.

## Paso 4 — Versionar las skills del día (Git → GitHub)

Sincronizar el repo `claude-skills-jjmobijuesa` antes del apagado.
Doctrina 9 de [[llave-maestra-autoaprendizaje-ia]]: una skill nueva no
existe hasta estar commiteada.

```bash
cd "C:/Users/datos/.claude/skills"

# 1. Detectar si hay cambios reales (sin ruido pyc)
if git status --porcelain | grep -v "^??.*__pycache__" | grep -q .; then
    # 2. Stage selectivo (el .gitignore filtra secretos y skills sensibles)
    git add -A

    # 3. Mostrar al usuario un resumen del diff
    n_files=$(git diff --cached --name-only | wc -l)
    echo "Archivos a commitear: $n_files"
    git diff --cached --stat | tail -5

    # 4. Commit con fecha y mensaje del agente
    FECHA=$(date "+%Y-%m-%d %H:%M")
    git commit -m "EOD ${FECHA}: <breve descripción de los cambios del día>" \
               -m "Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"

    # 5. Push — si Credential Manager está configurado, no pide interacción
    git push origin main 2>&1 || echo "ADVERTENCIA: push falló, revisar credenciales antes del apagado"
else
    echo "Sin cambios en skills/ — no commit"
fi
```

Compuertas 🚦 del versionado:
- Si el push falla con error de auth → **avisar al usuario, no apagar**
  hasta que él autorice (puede haber trabajo intelectual en riesgo si
  el disco fallara antes del próximo arranque).
- Si aparece un archivo nuevo no contemplado en `.gitignore` que pueda
  contener secretos (cookies, tokens) → abortar el commit y avisar.
- Si el `.gitignore` no existe o fue borrado → abortar y avisar.

## Paso 5 — Apagar
```
shutdown /s /t 90 /c "Apagado solicitado por el usuario. Aborte con: shutdown /a"
```
Informar al usuario el temporizador y el comando de aborto.

## Notas
- Las tareas programadas (crons de vigilancia, OLA 2) corren en el próximo
  arranque; el apagado no las pierde.
- Si un Excel del usuario está abierto con cambios sin guardar (lock `~$`),
  el apagado sin `/f` le permitirá guardar.
- El paso 4 (git push) se introdujo el 2026-06-27 al subir el repo a
  GitHub. Antes de esa fecha el paso 4 era el apagado directo.
