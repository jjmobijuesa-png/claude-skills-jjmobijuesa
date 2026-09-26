---
name: construccion-hilos-wa-don-omar
description: |
  Construye RESPUESTAS y HILOS de WhatsApp para Francisco Duque con un registro
  "concreto y a la vez explicativo", emulando los códigos de comunicación de
  Don Omar Juez Zambrano (+593 99 322 2777) y el registro entre-iguales observado
  en el intercambio Gemini Pro ↔ Claude Pro. Redacta borradores listos para enviar;
  NO envía sola (el envío lo confirma Francisco). Para leer el chat real usa
  [[whatsapp-web-cdp-lectura-envio]].
trigger_phrases:
  - "arma el hilo de whatsapp"
  - "redáctame la respuesta para whatsapp"
  - "responde como le hablo a don omar"
  - "constrúyeme el mensaje de wa"
  - "estilo don omar"
idioma_de_salida: español (Ecuador), trato de usted
nivel: aplicada
dominio: comunicación / redacción táctica
metadata:
  version: 1.0
  fecha: 2026-08-25
  relacionada: redaccion-entre-iguales-no-peticion, voz-y-tono-usuario, percibir-y-hablarle-al-humano, whatsapp-web-cdp-lectura-envio, humanizacion-texto-sin-firma-ia
---

# Skill `construccion-hilos-wa-don-omar`

## Para qué sirve
Producir mensajes de WhatsApp de Francisco que sean **concretos pero explicativos**: van al
punto, pero dan el *porqué* en una línea. El molde es doble: (1) los **códigos de Don Omar Juez**
(interlocutor real de Francisco) y (2) el **registro entre iguales** del hilo «Gemini Pro vs. Claude
Pro» que el usuario identificó como muy semejante — protocolar, respetuoso, sin súplica ni relleno.

## Los códigos del registro (cómo suena)
1. **Trato de "usted", cordial-formal ecuatoriano.** Respeto sin distancia fría. (Ver [[voz-y-tono-usuario]].)
2. **Entre iguales, no petición.** Se propone y se decide de igual a igual; nunca se ruega ni se sube el tono. (Ver [[redaccion-entre-iguales-no-peticion]].)
3. **Concreto: una idea por mensaje.** Si hay tres asuntos, tres mensajes cortos (hilo), no un párrafo largo.
4. **Explicativo en una línea.** No solo el "qué": también el "por qué", breve. Ej.: *"Le propongo mover la reunión al jueves; así llego con las cifras ya cerradas."*
5. **Cierre accionable.** Cada mensaje termina en un **siguiente paso** o una **pregunta cerrada** (sí/no, fecha, monto), no en aire.
6. **Economía y firmeza.** Sin floreo, sin disculpas innecesarias, sin emojis de relleno. Respeto + claridad = autoridad tranquila.
7. **Sin huella de IA.** Nada de `≈`, `~`, ni fraseo robótico ([[humanizacion-texto-sin-firma-ia]]).

## Método para construir un hilo
1. **Objetivo en una frase:** ¿qué decisión/acción busco de la otra parte?
2. **Descomponer en mensajes cortos** (2–5), uno por idea, en orden: contexto → punto/propuesta → razón breve → siguiente paso.
3. **Anclar a lo concreto:** fecha, monto, lugar, entregable. Nada ambiguo.
4. **Revisar el tono:** ¿suena de igual a igual, cordial y firme? ¿sobra alguna palabra?
5. **Entregar como borrador** para que Francisco lo revise y envíe.

## Plantillas
- **Apertura / retomar:** *"Estimado Don Omar, buenos días. Retomo el tema de [X]."*
- **Propuesta con razón:** *"Le propongo [acción concreta]. Lo veo así porque [razón breve]."*
- **Seguimiento firme:** *"Quedo pendiente de [entregable] para el [fecha]. Con eso avanzamos a [siguiente paso]."*
- **Cierre con pregunta cerrada:** *"¿Le parece bien el [día] a las [hora]? Confírmeme y lo dejo agendado."*

## Qué NO hacer
- No mandar párrafos largos ni "muros de texto": romper en hilo.
- No rogar, no sobre-disculparse, no rellenar con cortesías vacías.
- No inventar compromisos ni cifras; si falta un dato, preguntarlo de forma cerrada.
- 🚦 **No enviar sin confirmación de Francisco.** Esta skill **redacta**; el envío es de él o requiere su OK explícito para ese mensaje concreto (ver [[whatsapp-web-cdp-lectura-envio]] §8).

## Calibración con el corpus real — PENDIENTE (2026-08-25)
Este registro está definido por principios + el molde Gemini↔Claude. **Falta afinarlo con los mensajes
reales de Don Omar** (cadencia, muletillas, longitud típica, saludos). Intento de lectura del chat
(+593 99 322 2777) el 2026-08-25 **bloqueado**: WhatsApp Web quedó "descargando tus mensajes" y no
abrió el panel (teléfono offline / sesión a medio sincronizar). **Método correcto para el histórico:**
exportar el chat desde el teléfono (menú del chat → Exportar chat, sin archivos) y volcarlo, o
reintentar la lectura con el teléfono en línea vía [[whatsapp-web-cdp-lectura-envio]]. Al obtener el
corpus: extraer 8–10 rasgos concretos y actualizar la sección "códigos" arriba (subir a v2).

## Relacionadas
- [[redaccion-entre-iguales-no-peticion]] · [[voz-y-tono-usuario]] · [[percibir-y-hablarle-al-humano]] · [[whatsapp-web-cdp-lectura-envio]] · [[humanizacion-texto-sin-firma-ia]]
