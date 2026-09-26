---
name: orquestacion-multimodelo-mobijuesa360
description: |
  Doctrina y mecánica COMPARTIDA (memoria común, todas las sesiones y todos
  los agentes) para orquestar tres coprocesadores de IA — Gemini Pro,
  DeepSeek y Perplexity — todos bajo la misma identidad Google
  mobijuesa360@gmail.com activa en Edge. Claude sigue siendo el cerebro
  orquestador local; cada motor se usa por su fortaleza específica, con
  verificación obligatoria de todo lo que devuelva, registro persistente de
  cada intercambio, y la opción de traer la ventana al frente cuando el
  usuario quiera verlo en vivo.

  Unifica y referencia (no duplica) los mecanismos ya existentes:
  `gemini-active-use`, `deepseek-active-use`, `perplexity-active-use`
  (acceso técnico por motor) y `multi-agente-gemini-coprocesador`
  (protocolo específico de Gemini como coprocesador de proyecto). Esta
  skill es la capa de doctrina que decide CUÁNDO usar CUÁL motor y CÓMO
  verificarlo — no reemplaza los scripts de acceso de cada una.

  Trigger: cualquier tarea que se beneficie de investigación web pesada,
  razonamiento largo delegado, o una "segunda opinión" de otro modelo —
  en cualquier proyecto, no solo inmobiliario.
---

# Orquestación multi-modelo — mobijuesa360@gmail.com

## 0. Por qué existe esta skill (memoria común)

Nace de la sesión de trabajo en el Proyecto San Sebastián (29-ago-2026), donde se usó a Gemini Pro
como coprocesador real y se documentaron, con evidencia concreta, dos alucinaciones que solo se
detectaron por verificar contra fuente primaria (ver [[reference_gemini_handshake_multiagente]] y
[[entrenador-experto-notebooklm-gerente-inmobiliario]]). El usuario pidió elevar ese aprendizaje a
una capacidad **compartida por todos los agentes, en todas las sesiones** — no algo que haya que
redescubrir cada vez. Esta skill vive en `~/.claude/skills/` (global, no atada a ningún proyecto).

## 1. Los tres motores y para qué sirve cada uno

| Motor | Fortaleza | Cuándo delegarle |
|---|---|---|
| **Gemini Pro** | Contexto masivo (2M tokens), Google Workspace/Drive/Gmail nativo de mobijuesa360, Deep Research, Python interno, visión | Analizar archivos/carpetas grandes de Drive, investigación web larga (modo Deep Research), tareas que requieran leer Gmail/Sheets de mobijuesa360 sin scraping |
| **DeepSeek** | Razonamiento largo y barato (modo DeepThink/R1) | Cadenas de razonamiento profundo o análisis extenso donde no hace falta buscar en la web — ahorra tokens locales |
| **Perplexity** | Búsqueda con citación en tiempo real | Preguntas que necesitan fuentes web actuales y verificables con URL — el "fact-check rápido" antes de confiar en lo que otro motor dijo |

Los tres son **coprocesadores**, nunca la fuente de verdad. Claude decide qué delegar, y siempre
verifica antes de usar el resultado en un entregable real.

## 2. Estado actual de las cuentas por motor (verificado 29-ago-2026 — no asumir, confirmar)

| Motor | Perfil de Edge usado hoy | Cuenta confirmada | Estado |
|---|---|---|---|
| Gemini Pro | `C:\Users\datos\.notebooklm\browser_profile_edge` | **mobijuesa360@gmail.com** (confirmado en pantalla por el script) | ✅ Funcional |
| DeepSeek | Documentado como `browser_profile_jjm` / Edge debug 9222 (jjmobijuesa) | jjmobijuesa@gmail.com | 🚦 NO se detectó sesión de mobijuesa360 al probar `browser_profile_edge` (sondeo headless, 29-ago-2026: 0 cuentas detectadas en chat.deepseek.com) |
| Perplexity | Documentado como `browser_profile_jjm` / Edge debug 9222 (jjmobijuesa) | jjmobijuesa@gmail.com | 🚦 NO se detectó sesión de mobijuesa360 al probar `browser_profile_edge` (sondeo headless, 29-ago-2026: 0 cuentas detectadas, además se topó con un reto de Cloudflare) |

**Antes de la primera vez que se necesite DeepSeek o Perplexity bajo mobijuesa360**, hay que hacer
login una vez en `browser_profile_edge` con esa cuenta — mismo patrón que resolvió NotebookLM/Gemini
esta sesión:
1. Intentar primero el refresco automático (headless, sin molestar al usuario) si ya hubo login
   antes y solo caducó la sesión — ver [[notebooklm-login-reauth]] §2 como plantilla del método.
2. Si no hay sesión previa en absoluto, el login inicial requiere navegador headed (visible) — no se
   puede hacer desde el sandbox del agente. Entregarle al usuario el comando o pedirle que abra
   DeepSeek/Perplexity una vez en su Edge normal con mobijuesa360 activo, y luego replicar esa
   sesión al `browser_profile_edge` si hace falta aislarla.

## 3. Cómo se ve la interacción (transparencia, no misterio)

- Cada motor corre en una ventana de Edge automatizada por Playwright, **posicionada fuera del área
  visible del escritorio** por defecto (no roba el foco). Esto NO es ocultar nada: es una decisión
  de no interrumpir al usuario.
- **Si el usuario quiere verlo en vivo**, quitar el argumento de posición fuera de pantalla
  (`--window-position=2200,2200`) o pasar `headless=False` sin ese offset, y decírselo antes de
  lanzar la consulta.
- El hilo de Gemini es persistente y real — el usuario puede abrirlo él mismo en su propio
  navegador con la cuenta mobijuesa360 y ver todo el historial. Dar siempre la URL del hilo activo
  cuando se le informe del resultado.
- El "protocolo de audio/handshake algorítmico" que en algún momento se exploró como canal
  eficiente entre modelos **no funciona** — es teatro (herramienta de audio de Gemini falla). No
  reintentarlo; usar texto plano, que es lo que de verdad se puede verificar y registrar.

## 4. Registro persistente (obligatorio, no opcional)

Cada motor ya persiste su propio historial — mantener esta convención en cualquier sesión futura:

- Gemini: `E:\vars\var 5\Gemini-consultas\YYYY-MM-DD_HHMMSS_<slug>.md`
- DeepSeek: `E:\vars\var 5\DeepSeek-consultas\YYYY-MM-DD_<slug>.md`
- Perplexity: `E:\vars\var 5\Perplexity-consultas\YYYY-MM-DD_<slug>.md`

Cada archivo debe incluir: fecha, pregunta/prompt completo, respuesta completa, URL del hilo (si
aplica), y motor+perfil usado. Esto es lo que permite que la siguiente sesión (u otro agente) audite
qué se le preguntó a quién y qué contestó, sin tener que volver a preguntar.

## 5. Disciplina de verificación (la parte que no es negociable)

Dos incidentes reales documentados en la sesión de origen — tratarlos como el estándar de cuánto se
puede confiar en un motor delegado sin chequear:

1. **Gemini inventó un ID de carpeta de Google Drive** con formato plausible
   (`drive.google.com/drive/folders/InformeFinancieroUrbSanSebastian` — los IDs reales son hashes,
   nunca el nombre del archivo). Se resolvió consultando la base local de Google Drive for Desktop
   (`mirror_metadata_sqlite.db`), no confiando en la respuesta del modelo.
2. **Gemini citó una cifra de presupuesto ($337,947.56) atribuida a un documento real**, que resultó
   no estar en ese documento al verificarlo — el número real era $505,839.51. Y en una segunda
   ronda, citó seis cifras de una supuesta "fuente oficial" que resultó ser un PDF sin texto legible
   (solo imágenes) — la cita era inventada, aunque una de las seis cifras (por otra vía) resultó
   correcta.

**Regla operativa:** cuando un motor delegado cite "un documento" o "una fuente", pedir el
identificador exacto (source_id, URL, nombre de archivo) y leer esa fuente directamente
(`source fulltext` en NotebookLM, `WebFetch`/navegación real para una URL, apertura directa del
archivo) antes de usar la cifra en cualquier entregable que el usuario vaya a mostrar a un tercero
(banco, socio, autoridad). Un dato "que suena preciso" no es lo mismo que un dato verificado.

## 6. Flujo de uso recomendado

1. Definir el objetivo y el formato de salida esperado ANTES de escribir el prompt al motor.
2. Elegir el motor según la tabla de la sección 1.
3. Ejecutar vía la skill de acceso correspondiente (`gemini-active-use`, `deepseek-active-use`,
   `perplexity-active-use`) — esta skill no reimplementa esos scripts.
4. Guardar el intercambio (si el script no lo hace ya automáticamente).
5. Verificar cualquier cifra o cita específica antes de usarla (sección 5).
6. Si el hallazgo es significativo, dejar registro en la memoria del proyecto correspondiente
   (`~/.claude/projects/.../memory/`), no solo en el archivo de consulta suelto.

## Relacionado
- [[multi-agente-gemini-coprocesador]] — protocolo específico y detallado de Gemini como
  coprocesador (canal de archivos vía Drive, hilo canónico, etiquetas de formato).
- [[gemini-active-use]] · [[deepseek-active-use]] · [[perplexity-active-use]] — mecánica de acceso
  por motor.
- [[reference_gemini_handshake_multiagente]] — bitácora de hallazgos y alucinaciones confirmadas.
- [[notebooklm-login-reauth]] — plantilla del método de refresco/login que aplica igual a
  DeepSeek/Perplexity si hace falta autenticar mobijuesa360 por primera vez.
