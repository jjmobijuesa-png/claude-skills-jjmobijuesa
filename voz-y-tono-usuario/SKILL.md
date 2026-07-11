---
name: voz-y-tono-usuario
description: |
  Construye y mantiene la GUÍA DE VOZ Y TONO del usuario a partir de sus correos
  REALES (Gmail enviados), para que el agente redacte emails, informes, propuestas y
  presupuestos en su propio estilo. Cierra el único hueco del "cerebro operativo" que
  al agente local le faltaba (ya tiene CLAUDE.md + MEMORY.md + user_role.md + skills).
trigger_phrases:
  - "voz y tono"
  - "escribe con mi estilo"
  - "redacta como yo"
  - "guía de estilo del usuario"
  - "extrae mi tono de escritura"
  - "que el correo suene a mí"
idioma_de_salida: español
nivel: aplicada
dominio: comunicación / contexto-del-usuario
metadata:
  version: 1.0
  fecha: 2026-06-27
  origen: YouTube playlist IA jjmobijuesa, video QGFXRzYwQlU ("Configura Claude Cowork… Cerebro Operativo") — doctrina del "cerebro operativo" de Claridad Artificial
  fuente: https://www.youtube.com/watch?v=QGFXRzYwQlU
  relacionada: redaccion-humana-legislativa, triage-inbox-rapido-jjmobijuesa, llave-maestra-autoaprendizaje-ia
---

# Skill `voz-y-tono-usuario`

## Acerca de mí (cargar al arrancar)
Lee `...\memory\user_role.md` y `MEMORY.md`. Esta skill PRODUCE/actualiza un archivo de **voz y
tono** que pasa a ser parte de la memoria compartida (el "Acerca de mí" estilístico), complementando
a `user_role.md` (quién es) con **cómo escribe**.

## Doctrina (cerebro operativo — el hueco que faltaba)
El "cerebro operativo" de Claude se sostiene en 4 cimientos: **CLAUDE.md** (constitución), **mi-contexto /
user_role** (quién soy), **MEMORY.md** (memoria viva que crece sola) y **voz-y-tono** (cómo escribo).
Este computador ya tiene los tres primeros; **faltaba la voz**. Sin ella, los correos/informes que
redacta el agente suenan a IA genérica, no al usuario. Esta skill destila el estilo del **corpus real**
de correos enviados y lo deja como guía aplicable.

## Qué NO hacer / compuertas 🚦
- 🚦 **Gmail = solo lectura** para construir la guía; **enviar** sigue requiriendo OK por tanda
  (usar `gmail-send-playwright`/draft). No publicar la guía fuera del computador.
- No inventar el estilo: si hay pocos correos, dilo y marca la guía como "provisional".
- No usar la voz para suplantar al usuario ante terceros sin su autorización explícita.
- No mezclar cuentas: por defecto **jjmobijuesa@gmail.com** (confirmar si se pide otra).

## Protocolo paso a paso
> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**
1. **Reunir corpus:** con el **Gmail MCP** busca correos **enviados** representativos
   (`search_threads "in:sent"`, variando destinatario formal/informal). Lee 15–40 respuestas reales.
2. **Destilar el estilo** en dimensiones: registro (formal↔cercano), saludo/despedida típicos, longitud
   de frase, conectores y muletillas propias, uso de listas/negritas, nivel de tecnicismo, emojis (sí/no),
   tratamiento (tú/usted), firmas, y "tics" reconocibles. Distingue **por contexto** (Directorio QVP vs.
   cliente vs. institucional EcuaLedger vs. personal).
3. **Escribir la guía** en `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\reference_voz_y_tono_jjmobijuesa.md`
   (con 2–3 ejemplos antes/después), e indexarla en `MEMORY.md`.
4. **Aplicar:** al redactar cualquier email/informe/propuesta, cargar la guía y escribir en esa voz;
   verificar con [[redaccion-humana-legislativa]] que no suene a IA (estilo humano).
5. **Mantener:** actualizar la guía cuando el usuario corrija un borrador ("así no hablo yo") — el ajuste
   se persiste vía [[llave-maestra-autoaprendizaje-ia]].

## Cómo depurar si falla
Si el texto sigue sonando ajeno, casi siempre faltó **segmentar por contexto** (paso 2) o se tomó muestra
de correos reenviados/automáticos. Pide al usuario 3 correos que "suenen a él" y recalibra.

## Portabilidad / Reuso
Cuenta de correo y rutas son el 20% variable. Reusa el Gmail MCP y, para el QC anti-IA,
[[redaccion-humana-legislativa]]; para vaciar/clasificar el inbox, [[triage-inbox-rapido-jjmobijuesa]].

## Ejemplos de invocación
- «Extrae mi voz y tono de mis correos y guárdala.»
- «Redacta este correo al Directorio con mi estilo.»
- «Actualiza mi guía de voz: en lo institucional soy más formal.»
