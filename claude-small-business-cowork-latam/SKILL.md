---
name: claude-small-business-cowork-latam
description: >-
  Instala y ADAPTA el plugin «Claude for Small Business» de Cowork al mercado
  español/latinoamericano usando un "cerebro operativo" (contexto .md). Invocar
  para automatizar tareas de PYME (CRM, facturas/impagos, briefing semanal,
  contratos, cierres de mes) en Quevepalma, Mobijuesa, Vista al Río o Belén.
trigger_phrases:
  - "Claude for Small Business"
  - "plugin de negocios de Cowork"
  - "cerebro operativo Cowork"
  - "automatizar mi PYME con Claude"
  - "adaptar el plugin al mercado español / latinoamericano"
idioma_de_salida: español
nivel_de_madurez: aplicada
dominio: productividad / PYME
fuente:
  - "YouTube G7iyOM1pUtQ (2026-07, canal en español): instalar y personalizar Claude for Small Business en Cowork"
  - "Complementa [[reference_youtube_ia_cowork_jjmobijuesa]] (doctrina cerebro operativo)"
---

## Acerca de mí (cargar al arrancar)
Leer `...\memory\user_role.md` + `MEMORY.md`. El usuario opera varias PYMEs
(Quevepalma, Mobijuesa, Vista al Río / INMOBILIARIA JUEZ & JUEZ, Proyecto Belén):
esos son los negocios reales donde este plugin rinde. Mercado objetivo = **Ecuador
(LATAM)**, no EE. UU.

## Distinción clave: skill vs. plugin
- **Skill** = especialista en UNA tarea, basada en instrucciones (ej.: «redactar
  facturas»). Es *la herramienta*.
- **Plugin** = *departamento integral* = un conjunto de skills + integraciones.
  Es *la caja de herramientas* (ej.: el «departamento financiero» completo).
- «Claude for Small Business» es un **plugin** de Anthropic con **15 flujos**:
  CRM cleanup, Monday brief, caza-facturas/impagos, revisor de contratos,
  creación de contenido, cierres de mes, facturación, etc. Cada flujo se dispara
  con un comando `/nombre` desde el chat.

## Doctrina central
El plugin **sin tu contexto no sirve**: viene pensado para una *small business*
estadounidense (QuickBooks, DocuSign, dólar, retail). La magia está en
**personalizarlo con tu "cerebro operativo"** — un archivo `.md` con la estructura
de tu empresa, tu stack de herramientas y tu mercado. Con eso, Claude **detecta**
que tu realidad es distinta (sociedad ecuatoriana/española, euro o dólar
según país, servicios en vez de retail, aplicativos locales como Holded) y
sustituye los flujos que no encajan por los tuyos, redactando además **en tu tono**.

## Qué NO hacer / compuertas 🚦
- 🚦 **No** ejecutar el plugin sin cargar antes el cerebro operativo: sin contexto,
  Claude no sabe tus herramientas ni tu jurisdicción y el resultado es inservible.
- 🚦 **No** confundir skill con plugin (una tarea vs. un departamento) al explicarlo.
- 🚦 **Envío de correos/acciones externas = autorización explícita del usuario.**
  El flujo de impagos genera **borradores** en Gmail; NO enviar sin OK (coherente
  con [[correo-relay-adjuntos]] y las compuertas de la casa).
- 🚦 **Permisos heredados:** Cowork hereda los permisos de las carpetas
  compartidas (Drive). Una carpeta sin acceso para un miembro tampoco lo tendrá
  vía Cowork. No asumir acceso total.
- 🚦 **El plugin NO gestiona el negocio solo** — hay mucho *hype*; es una
  herramienta que ahorra tiempo, el humano sigue siendo necesario (Doctrina de la
  casa: la IA decide/apoya, el humano firma).
- 🚦 Cloud **no entrena con tus datos** (declarado por Anthropic) → privacidad OK,
  pero igual segregar datos sensibles.

## Protocolo paso a paso
> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**
1. **Instalar Cowork desktop**: `claude.com/download` (Windows) → instalar.
2. **Añadir el plugin**: arriba-izquierda → *Cowork → Customize* → *Añadir plugin*
   (+) → *Explorar plugins* → buscar «Small Business» → instalar (+).
3. **Construir el cerebro operativo** (obligatorio): pegar el prompt de contexto,
   responder los **12 puntos** (estructura de empresa, stack, mercado, tono);
   Claude devuelve un `.md`. Guardarlo. (Si ya existe de un vídeo previo, solo
   verificar/completar.)
4. **Personalizar el plugin**: *Customize → Small Business → Personalizar*, e
   instruir: «Personaliza el plugin Small Business para mi caso específico según
   la estructura de mi empresa y mi stack; mi mercado es **Ecuador (LATAM)**;
   analiza mi archivo de contexto e identifica qué datos adicionales necesitas.»
   Adjuntar el `.md` de contexto. Responder las preguntas que haga.
5. **Guardar el plugin**. Si sale `plugin validation failed`, decírselo a Claude
   («sale este error: …») y aplicar la versión corregida que devuelva.
6. **Usar** los flujos por comando: `/CRM cleanup revisa HubSpot`, `/Monday brief`,
   caza-facturas → «busca impagos en la carpeta X y deja borradores en Gmail».
7. **Programar** los recurrentes: «programa este briefing todos los lunes a las
   7:30» → queda automatizado (ver también [[claude-routines-apis-skills-github]]).

## Cómo depurar si falla
- `plugin validation failed` al guardar → pegar el error a Claude; corrige el YAML/JSON.
- El plugin sugiere apps de EE. UU. → reforzar en el contexto el mercado y los
  aplicativos locales (Holded, gestor externo + Drive compartido, etc.).
- Redacta con tono ajeno → enriquecer el cerebro operativo con muestras de tu voz
  (ver [[voz-y-tono-usuario]]).

## Portabilidad (revisar el 20% al reusar)
Cambia por empresa: el cerebro operativo (`.md`), el stack de herramientas y el
país/moneda. El procedimiento de instalación/personalización es estable.

## Reuso (no empezar de cero)
Apóyate en [[reference_youtube_ia_cowork_jjmobijuesa]] (doctrina cerebro
operativo), [[voz-y-tono-usuario]] (tono en los correos), [[correo-relay-adjuntos]]
(envíos) y [[triage-inbox-rapido-jjmobijuesa]] (Gmail).

## Ejemplos de invocación
- «Instálame Claude for Small Business para Mobijuesa y adáptalo a Ecuador.»
- «Arma el cerebro operativo de Quevepalma para el plugin de negocios.»
- «Programa el Monday brief automático de Vista al Río.»
