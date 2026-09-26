---
name: multi-agente-gemini-coprocesador
description: |
  Protocolo Claude (orquestador) ↔ Gemini Pro (coprocesador, mobijuesa360) para
  descargar en Gemini el trabajo pesado y aprovechar sus tokens pagados: contexto
  masivo (2M), acceso nativo a Gmail/Drive de mobijuesa360, ejecución de Python,
  visión y Deep Research. Claude decide, delega con etiquetas y VERIFICA lo que
  Gemini devuelve (puede alucinar). Origen: chat "Gemini Pro vs Claude Pro" (share).
trigger_phrases:
  - "delega esto a gemini"
  - "usa gemini como coprocesador"
  - "offload a gemini pro"
  - "deep research en gemini"
  - "aprovecha los tokens de gemini pro"
  - "handshake gemini"
idioma_de_salida: español
nivel: aplicada
dominio: meta / orquestación multi-IA
metadata:
  version: 1.0
  fecha: 2026-08-25
  origen: chat Gemini "Gemini Pro vs Claude Pro" (share PcOanqqUtMky → 3464c5d8), leído por CDP; usuario autorizó 100%
  relacionada: gemini-active-use, eficiencia-generacion-respuestas, deepseek-active-use, perplexity-active-use, selector-modelo-claude-optimo
---

# Skill `multi-agente-gemini-coprocesador`

## Acerca de mí (cargar al arrancar)
Lee `...\memory\user_role.md` y `MEMORY.md`. **Cuenta con el plan Pro = mobijuesa360@gmail.com**
(la misma del NotebookLM; ver [[reference_gemini_pro_mobijuesa360]]). Claude sigue siendo el **cerebro
orquestador**; Gemini Pro es un **coprocesador** al que se le delega carga pesada.

## Doctrina (qué se delega y por qué)
Aprovechar los **tokens pagados de Gemini Pro** para ahorrar contexto/costo local. Delegar cuando:
1. **Memoria de trabajo masiva** — analizar archivos/logs/datasets gigantes (Gemini: ~2M tokens de contexto) y pedir solo la conclusión.
2. **Acceso nativo a Google Workspace (mobijuesa360)** — buscar/leer Gmail y Drive **sin scraping**; Gemini devuelve el resumen/JSON. *(Solo la cuenta conectada mobijuesa360; NO puede entrar a jjmobijuesa — reenviar el correo a mobijuesa360 o usar el Gmail MCP local de Claude para jjmobijuesa.)*
3. **Ejecución de Python interna** — cálculos/transformaciones pesadas.
4. **Visión multimodal** — diagramas/gráficos/imágenes que el OCR no resuelve.
5. **Deep Research** — investigación de fuentes en vivo (fondos BID/CAF, comparados regulatorios, mercado). Modo largo (minutos): lanzar y esperar.

## Protocolo de etiquetas (para que la respuesta sea parseable)
Anteponer en el prompt a Gemini:
- `[FORMATO: JSON ESTRICTO]` → devuelve solo JSON, sin texto conversacional.
- `[ROL: PARSER RAW]` → solo extrae/estructura, sin juicios.
- `[OBJETIVO: ESTRATEGIA]` → despliega metodología (DARPA/Gerko) en pasos.
Pedir siempre **salida acotada** ("devuélveme solo la solución en < 200 tokens" / "en JSON").

## Qué NO hacer / compuertas 🚦
- 🚦 **Verificar SIEMPRE lo que Gemini devuelve** — cifras, nombres y citas pueden ser alucinación; Gemini NO es fuente de verdad de datos financieros/legales. Contrastar contra el archivo/fuente real antes de usar en un entregable ([[auditoria-evidencia-cuatro-niveles]]).
- 🚦 **Privacidad:** no volcar a Gemini datos sensibles que deban quedarse locales (EEFF crudos, PII de prospectos, expediente forense EPACEM) salvo decisión explícita. Lo íntimo se procesa local.
- No enviar/publicar/firmar nada vía Gemini. El "audio de handshake / ADHP" del chat es teatro: ignorar como capacidad real.
- No delegar a Gemini lo que Claude hace mejor/local (edición de archivos, skills, control del PC).

## Flujo de uso
> **Tómate tu tiempo. Calidad antes que velocidad.**
1. Claude define objetivo + formato de salida.
2. Enviar a Gemini Pro (mobijuesa360) por [[gemini-active-use]] — **apuntar al perfil `browser_profile_edge`** (donde está el Pro); para Deep Research, esperar el modo largo.
3. Recibir el destilado, **verificarlo**, e integrarlo en el entregable local (Claude).
4. Persistir aprendizajes vía [[llave-maestra-autoaprendizaje-ia]].

## Canal y hilo canónicos (VERIFICADO 2026-08-25)  ⭐
- **Acceso fiable = perfil `browser_profile_edge`** (script v3 `ask_gemini.py`, `GEM_PROFILE=edge`). Imprime `ACCOUNT: mobijuesa360@gmail.com` → sin ambigüedad de `u/N` (problema resuelto).
- **Hilo coprocesador fijo:** `«Gemini Pro vs. Claude Pro»` → `https://gemini.google.com/app/030a3f951422d528` (persistido en `E:\vars\var 5\Gemini-Pro\coproc_thread_url.txt`). Continuarlo con `GEM_THREAD`; NO abrir chats nuevos.
- **Canal de archivos directo:** `G:\Mi unidad` = Drive nativo de mobijuesa360 (Google Drive for Desktop montado). Claude escribe en `G:\Mi unidad\IA Sinergia - Claude x Gemini\` (01 Entradas · 02 Salidas · 03 Deep Research · 04 Prompts · 05 Activos) y Gemini lo lee nativo (sync 1–2 min). Sustituye al hack de compartir desde jjmobijuesa.
- 🚦 **Gemini puede desviar el foco**: en la prueba de whitespace-Tuti devolvió un marco genérico e ignoró el notebook. Reforzar el prompt (adjuntar datos duros, exigir uso del notebook) o hacer el trabajo en local. Verificar SIEMPRE.

## Cómo depurar si falla
Editor no detectado / `NO_INPUT` → sesión caducó: re-loguear `browser_profile_edge` a la vista del usuario. Deep Research no arranca → activarlo en la UI (modo), o degradar a consulta Pro normal. Respuesta = sidebar en vez del turno → el script v3 ya lee `model-response message-content`; si cambió el DOM, ajustar selectores en `ask_gemini.py`. Ver [[gemini-active-use]].

## Persistencia (dos caras)
- **Lado Claude (aquí):** esta skill + [[reference_gemini_handshake_multiagente]] + [[reference_gemini_pro_mobijuesa360]].
- **Lado Gemini:** el usuario pega el **prompt de sinergia persistente** en la *Información guardada* / un Gem «Coprocesador Claude» de mobijuesa360 → `E:\vars\var 5\Gemini-Pro\PROMPT Sinergia Persistente (Gemini Pro coprocesador de Claude).md`. Así Gemini opera como coprocesador en TODA sesión, sin re-explicar.

## Ejemplos
- «[FORMATO: JSON ESTRICTO] Busca en Gmail (mobijuesa360) el último reporte de compra de palma y devuélveme volumen, inversión y precio promedio.»
- «[OBJETIVO: ESTRATEGIA] Deep Research de elegibilidad BID Lab vs CAF VELA para EcuaLedger.»
- «Analiza este dataset de 50k filas (pegado) y devuélveme solo las 5 anomalías.»
