---
name: correo-relay-adjuntos
description: |
  Flujo end-to-end de reenvío de correos con adjuntos vía Gmail. Recibe
  un thread_id origen, descarga TODOS sus adjuntos en un ZIP, los
  extrae, filtra (regex opcional), redacta un nuevo correo con el
  cuerpo y destinatarios que le indiques, adjunta los archivos
  extraídos + extras del disco, y envía verificando en Sent. Un solo
  comando encadena `gmail-attachments/download_all_zip.py` +
  `gmail-send-playwright/send.py`.
trigger_phrases:
  - "reenvía los adjuntos del correo X al destinatario Y"
  - "descarga los archivos de este thread y mándalos a"
  - "relay adjuntos Gmail"
  - "extrae los archivos del correo y envíalos a"
  - "haz zip y reenvía"
idioma_de_salida: español
nivel: aplicada
dominio: operación / correo
metadata:
  version: 1.0
  fecha: 2026-07-05
  origen: pedido del usuario (2026-07-05); consolidación de gmail-attachments + gmail-send-playwright
  relacionada: gmail-attachments, gmail-send-playwright, triage-inbox-rapido-jjmobijuesa, comite-cuarto-guerra-qvp
---

# Skill `correo-relay-adjuntos`

## Doctrina

Un flujo cotidiano del usuario: **le llega un correo con anexos, y
tiene que reenviarlos a un tercero** (contable, banquero, socio,
comisión). Los pasos manuales son tediosos:

1. Abrir el correo, descargar cada adjunto (o el ZIP de "Descargar
   todos"), extraerlo, mover a una carpeta.
2. Abrir compose nuevo, escribir destinatario, asunto, cuerpo.
3. Adjuntar cada archivo desde la carpeta.
4. Enviar y verificar en Sent.

Esta skill lo hace en un solo comando con validación por dry-run y
filtros regex (por si algún adjunto NO debe reenviarse — por
ejemplo, información sensible interna).

## Qué NO hacer / compuertas 🚦

- 🚦 **Autorización explícita del usuario** antes del envío real.
  Siempre correr primero `--dry-run` para mostrar la lista de
  adjuntos filtrados; el usuario aprueba antes de mandar en vivo.
- 🚦 **Nunca reenviar adjuntos que contengan secretos** (contraseñas,
  cookies, tokens). Usar `--exclude-filter "credentials|token|password"`
  como defensa.
- 🚦 **Nunca reenviar a listas de correo desconocidas.** El
  destinatario debe estar validado en la conversación.
- 🚦 **No pisar la carpeta del usuario.** Todo va a work-dir temporal
  (`%TEMP%\gmail-relay-<uuid>`) que se borra al final.
- **Curar antes de reenviar**: si el usuario dice "reenvía TODOS",
  igual mostrar la lista y esperar OK. Un adjunto malo puede tener
  consecuencias jurídicas o comerciales.

## Protocolo paso a paso

> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

### Paso 0 · Pre-requisitos
- Edge corriendo con `--remote-debugging-port=9222` (no necesario si
  usamos perfil dedicado, pero conveniente).
- Perfil Edge persistente `~/.notebooklm/browser_profile_<tag>`
  logueado a la cuenta origen/destino. Los tags actuales:
  - **`jjm`** → jjmobijuesa@gmail.com (dedicado).
  - `edge` → perfil general del usuario.
- Body del correo en un archivo `body.txt` (texto plano; el script
  respeta saltos de línea).

### Paso 1 · Identificar el thread origen

Usar el Gmail MCP `search_threads`:

```
search_threads("from:X subject:Y", pageSize=10)
```

Capturar el `id` del hilo (el `thread_id`).

### Paso 2 · DRY-RUN (obligatorio antes del envío real)

```bash
"C:\Users\datos\.notebooklm-venv\Scripts\python.exe" \
  "C:\Users\datos\.claude\skills\correo-relay-adjuntos\scripts\relay.py" \
  --profile jjm \
  --source-thread <THREAD_ID> \
  --to "destino@dominio.com" \
  --subject "Reenvío adjuntos" \
  --body-file body.txt \
  --attach-filter "\.(pdf|xlsx|docx)$" \
  --exclude-filter "borrador|draft" \
  --dry-run
```

El script descarga+extrae los adjuntos, aplica filtros, y **muestra
la lista** que se enviaría. NO envía nada. El usuario revisa.

### Paso 3 · Enviar en vivo

Cuando el usuario confirma la lista del dry-run, correr el mismo
comando **sin** `--dry-run`. Si quieres inspeccionar los archivos
descargados después, añadir `--keep-work-dir`.

### Paso 4 · Verificar

El script imprime `ENVIADO CONFIRMADO` si el asunto aparece en
`in:sent newer_than:1h`. Si no, revisar manualmente en Gmail o con
el MCP `search_threads`.

## Ejemplos completos

### Ejemplo 1 · Reenviar los Excel del comité SEM 24 al contador

```bash
python relay.py \
  --profile jjm \
  --source-thread 19ecdd85755653c2 \
  --to "contador@empresa.com" \
  --subject "Reenvío — Excels comité SEM 24 para revisión" \
  --body-file body.txt \
  --attach-filter "\.xlsx?$"
```

### Ejemplo 2 · Reenviar solo los PDFs y añadir uno del disco

```bash
python relay.py \
  --profile jjm \
  --source-thread 19ecdd85755653c2 \
  --to "socio@empresa.com,secretaria@empresa.com" \
  --subject "Anexos para reunión" \
  --body-file body.txt \
  --attach-filter "\.pdf$" \
  --extra-attach "E:\vars\var 5\Quevepalma\actas\SEM-24-acta.pdf"
```

### Ejemplo 3 · DRY-RUN para auditar qué se enviaría

```bash
python relay.py --profile jjm --source-thread <ID> \
  --to test@example.com --subject "Test" --body-file body.txt \
  --dry-run --keep-work-dir
```

## Cómo depurar si falla

- **`descarga (exit 2)`** → thread_id inválido o Gmail no cargó a
  tiempo. Verificar el thread_id con `search_threads`. Reintentar.
- **`envío (exit 4)`** → Gmail cambió selectores o el upload
  colgó. Revisar `stderr` del subproceso. Comprobar tamaño total
  <25 MB.
- **`no hay adjuntos que reenviar tras filtros`** → los filtros
  matchearon todo o nada. Reintentar sin filtros o ajustar.
- **`AVISO: no se confirmó Sent`** → el correo puede estar en cola
  o en enviados. Verificar manualmente.
- **Perfil no logueado** → el script sale con instrucciones para
  correr `login.py` de `gmail-attachments`.

## Autodepuraciones aplicadas 2026-07-05

- **`send.py`**: espera de upload cambiada de fijo 22 s a adaptativa
  según tamaño total de adjuntos (15 s mínimo, tope 3 min).
- **`download_all_zip.py`**: esperas fijas de 4 s y 7 s cambiadas a
  esperas por selectores del DOM Gmail; fallback al timeout fijo si
  el selector no aparece a tiempo.

## Portabilidad (revisar el 20% al reusar)

Cuenta/perfil de Edge, ruta del venv Python, selectores DOM Gmail
(cambian ocasionalmente), tope 25 MB de Gmail. Todo lo demás es
estable.

## Relacionado

- [[gmail-attachments]] — script de descarga (`download_all_zip.py`).
- [[gmail-send-playwright]] — script de envío (`send.py`).
- [[triage-inbox-rapido-jjmobijuesa]] — cómo encontrar threads.
- [[comite-cuarto-guerra-qvp]] — caso típico (reenviar Excels del comité).
- [[cierre-jornada-apagado]] — envío diario del resumen (relacionado).
