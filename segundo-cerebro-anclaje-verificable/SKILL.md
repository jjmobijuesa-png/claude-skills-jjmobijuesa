---
name: segundo-cerebro-anclaje-verificable
description: >-
  Cómo montar un archivo de conocimiento del que se pueda RESPONDER CON CITA, y por qué la
  mayoría de los «segundos cerebros» no llega ahí. Trae la JERARQUÍA DE CUATRO NIVELES DEL
  ANCLAJE —frase en el prompt, regla permanente, hook, respuesta citada— donde solo el
  cuarto cierra el problema, y la estructura raw/wiki/output como regla de integridad y no
  de orden. Nombra el fallo silencioso: sin anclaje el modelo rellena los huecos y devuelve
  la mezcla sin marca. Invocar al montar, auditar o consultar cualquier base de conocimiento.
trigger_phrases:
  - "montar un segundo cerebro"
  - "bóveda de Obsidian con IA"
  - "cómo sé que la respuesta viene de mis fuentes"
  - "el modelo se inventó parte de la respuesta"
  - "anclaje de respuestas"
  - "organizar mis notas para consultarlas con IA"
  - "raw wiki output"
idioma_de_salida: español
nivel_de_madurez: aplicada
dominio: agentes-ia / conocimiento y verificabilidad
fuente:
  - "Post de @danikkk_wqs en X, 27-oct-2026 — https://x.com/danikkk_wqs/status/2115177570824081911 (leído y auditado el 29-oct-2026). Remite a un artículo de @imryven con el montaje completo, no auditado"
  - "Material de estudio de la casa: G:\\Mi unidad\\5 Clases-Magistrales-HTML\\04-ia-y-sistemas\\23-segundo-cerebro-claude-obsidian.html"
relacionada: memoria-agente-claude-md-reglas, auditor-integral-notebooklm, arnes-agentico-bucle-y-contexto, metodo-mit-notebooklm-riguroso, auditoria-evidencia-cuatro-niveles, graph-engineering-memoria-agentes
---

## Acerca de mí (cargar al arrancar)
Leer `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md` y
`MEMORY.md`. Esta casa **ya opera** un sistema de este tipo —memoria por archivos, red de
skills, el Aula y cuadernos con cita—, así que la skill sirve para **auditarlo y no bajar
de nivel**, más que para montarlo de cero.

## Doctrina central

**El problema, en una línea:** un archivo de conocimiento sin anclaje verificable no es un
registro de lo que usted sabe, **es un generador de texto plausible con sus notas al lado**.

**La jerarquía de cuatro niveles del anclaje.** Es el aporte central y no está en la fuente:

| Nivel | Mecanismo | Qué garantiza |
|---|---|---|
| 1 | Frase en cada pregunta («usando solo mis fuentes») | **Nada.** Depende de escribirla cada vez y de que el modelo la respete |
| 2 | Regla en el archivo de instrucciones permanentes | Mejor: no hay que repetirla. Pero sigue siendo contexto, y **se pierde al compactar** |
| 3 | Un *hook* que lo imponga | Se ejecuta siempre. **Primera garantía real** |
| 4 | **Respuesta con cita verificable** | Devuelve la afirmación **y el fragmento de la fuente**. **El único nivel que cierra el problema** |

Los dos primeros son **contexto**; el tercero es **garantía**; el cuarto permite
**comprobar sin creerle a nadie**. La distinción contexto-frente-a-garantía viene de
[[arnes-agentico-bucle-y-contexto]] y es la que hace falsa la tranquilidad del nivel 1.

**La estructura de tres carpetas es una regla de integridad, no de orden:**

- **`raw/`** — la fuente tal como llegó. **No se edita nunca.** Es la evidencia a la que
  volver. Sin ella, revisar un hallazgo obliga a fiarse del resumen.
- **`wiki/`** — lo destilado y enlazado. **Es lo único que se cita.**
- **`output/`** — lo que usted produce, aislado, para que lo propio no se confunda con lo
  leído.

**El fallo es silencioso.** Cuando el anclaje falla, el texto sigue saliendo fluido y sin
marca que distinga la fuente de la suposición. Por eso no se detecta por lectura: se
detecta por diseño.

## Qué NO hacer / compuertas 🚦

- 🚦 **No dar por anclada una respuesta porque se pidió en el prompt.** Es el nivel 1.
  Basta olvidar la fórmula una vez, o que la instrucción quede atrás al compactarse una
  conversación larga, para que el modelo vuelva a rellenar.
- 🚦 **Cuando la respuesta vaya a sostener una decisión, no bajar del nivel 4.** Preguntar
  al cuaderno con citas, no a una conversación suelta ([[auditor-integral-notebooklm]],
  [[metodo-mit-notebooklm-riguroso]]).
- 🚦 **No autogenerar el archivo de instrucciones permanentes.** Una entrevista produce un
  archivo largo que **hereda supuestos que nadie revisó**, y los archivos largos
  **reducen la adherencia** ([[memoria-agente-claude-md-reglas]]). Escribirlo a mano y
  corto.
- 🚦 **Un grafo denso no es conocimiento verificado.** Que dos notas estén enlazadas no
  dice nada sobre si el enlace es correcto. La verificación contra `raw/` es lo que
  convierte el grafo en conocimiento ([[graph-engineering-memoria-agentes]]).
- 🚦 **Distinguir el tiempo de montaje del tiempo de valor.** «Veinte minutos» mide el
  andamiaje; el valor aparece semanas después. Las dos cifras suelen convivir en el mismo
  discurso de venta y se recuerda la primera.
- 🚦 **No confundir esta jerarquía con los cuatro niveles de evidencia** de
  [[auditoria-evidencia-cuatro-niveles]]: aquella clasifica **de qué calidad es una
  prueba**; esta, **si la respuesta procede de verdad del corpus**. Son ortogonales y se
  usan juntas.

## Protocolo de uso

1. **Conservar `raw/` siempre.** Toda fuente que entre al archivo guarda su original sin
   editar, con su ruta anotada en la nota destilada.
2. **Declarar el nivel de anclaje de cada consulta** antes de hacerla. Si la respuesta va a
   sostener una decisión, nivel 4 o no se hace.
3. **Si hace falta imponer la restricción**, ponerla en un *hook*, no en el prompt.
4. **Al destilar, dejar el puntero a la fuente en la nota**, para que el nivel 4 siga siendo
   posible meses después.
5. **Auditar periódicamente una muestra**: tomar tres afirmaciones del `wiki/` y
   comprobarlas contra `raw/`. Lo que no se pueda comprobar, se marca.

## Cómo depurar si falla

- **La respuesta mezcla mis fuentes con cosas que no están:** está operando en nivel 1 o 2.
  Subir de nivel, no reforzar la frase.
- **La regla estaba escrita y dejó de cumplirse a media sesión:** compactación. El remedio
  no es repetirla más fuerte, es moverla a un mecanismo.
- **No puedo comprobar una nota:** falta el `raw/` o falta el puntero. Es deuda de
  integridad: marcar la nota como no verificable antes de volver a usarla.
- **El cuaderno responde pero sin citas:** la consulta no se hizo sobre el corpus cerrado.
  Trampas concretas en [[auditor-integral-notebooklm]].

## Portabilidad (revisar el 20% al reusar)
Las herramientas concretas son sustituibles. **La jerarquía de cuatro niveles, la
separación raw/wiki/output y el carácter silencioso del fallo** valen para cualquier
sistema donde un modelo responda sobre un corpus propio.

## Reuso (no empezar de cero)
Para las instrucciones permanentes y sus techos, [[memoria-agente-claude-md-reglas]]. Para
el nivel 4 en la práctica, [[auditor-integral-notebooklm]] y
[[metodo-mit-notebooklm-riguroso]]. Para la calidad de la prueba,
[[auditoria-evidencia-cuatro-niveles]]. Para la memoria entre sesiones,
[[memoria-compartida-sesiones]].

## Ejemplos de invocación
- «¿Cómo sé que esta respuesta salió de mis documentos?»
- «Quiero montar una bóveda de notas que la IA consulte.»
- «El resumen trae una afirmación que no recuerdo haber leído.»

## Vecindad en la red
Instrucciones y memoria: [[memoria-agente-claude-md-reglas]],
[[memoria-compartida-sesiones]], [[graph-engineering-memoria-agentes]].
Anclaje en la práctica: [[auditor-integral-notebooklm]],
[[metodo-mit-notebooklm-riguroso]]. Marco: [[arnes-agentico-bucle-y-contexto]].
Rigor de la prueba: [[auditoria-evidencia-cuatro-niveles]].
