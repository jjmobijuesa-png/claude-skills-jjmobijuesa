---
name: agente-trading-arquitectura-y-frenos
description: >-
  Arquitectura mínima de un agente que toca mercados y, sobre todo, LOS FRENOS QUE NO SON
  NEGOCIABLES: ningún agente ejecuta una orden real solo, ninguna credencial vive en un
  prompt o un repositorio, y papel primero por un periodo declarado de antemano. Cubre los
  cinco componentes legítimos (régimen, freno por caída, backtest con costos, revisión,
  papel) y los SEIS RIESGOS que los discursos de venta omiten, incluido el riesgo de ruina.
  Un freno escrito en el prompt NO es un freno. Invocar ante cualquier automatización que
  mueva dinero o decida sobre él.
trigger_phrases:
  - "agente de trading"
  - "bot que opere solo"
  - "automatizar mis inversiones"
  - "backtest de esta estrategia"
  - "freno por drawdown"
  - "agente que ejecute órdenes"
  - "prompt para operar mercados"
idioma_de_salida: español
nivel_de_madurez: aplicada
dominio: agentes-ia / mercados y gobierno del riesgo
fuente:
  - "Post de @ZenithcoreAi en X, 27-oct-2026 — https://x.com/ZenithcoreAi/status/2115022865691271428 (leído y auditado el 29-oct-2026; el post ANUNCIA un prompt que no contiene)"
  - "Material de estudio de la casa: G:\\Mi unidad\\5 Clases-Magistrales-HTML\\04-ia-y-sistemas\\22-agente-trading-anatomia-promesa.html"
relacionada: doctrina-thorp-matematica-vs-multitud, simons-ventaja-estadistica-validada, gobernanza-datos-financieros-ia, mcp-conexion-ambitos-y-frontera, arnes-agentico-bucle-y-contexto, rigor-matematico-filtro-pseudociencia
---

## Acerca de mí (cargar al arrancar)
Leer `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md` y
`MEMORY.md`. **No es asesoría de inversión** y no la sustituye: es una skill de
**arquitectura y frenos**. Su autoridad empieza y acaba en cómo se construye el sistema,
nunca en qué comprar.

## Doctrina central

**Los cinco componentes que sí son legítimos** —están en la fuente y resisten la
auditoría—:

| # | Componente | Para qué |
|---|---|---|
| 1 | **Detección de régimen** | Saber en qué estado está el mercado antes de aplicar una regla |
| 2 | **Freno por caída acumulada** | Detener la operación al cruzar un umbral declarado de antemano |
| 3 | **Backtest con costos** | Probar contra el pasado **con comisiones, deslizamiento e impuestos** |
| 4 | **Revisión periódica** | Un repaso fijo de lo ocurrido, no una mirada cuando algo duele |
| 5 | **Papel primero** | Operar sin dinero real durante un periodo **declarado antes de empezar** |

**Los tres frenos de la casa, que no se negocian:**

1. **Ningún agente ejecuta una orden real por su cuenta.** El agente propone; una persona
   ejecuta. Y la aprobación va **en el mecanismo**, no en una frase: aprobación obligatoria
   por herramienta o un *hook* ([[mcp-conexion-ambitos-y-frontera]]).
2. **Ninguna credencial vive en un prompt, un repositorio o un archivo de configuración
   compartido.** Expansión de variables o un ayudante que las imprima en el momento.
3. **Papel primero, por un periodo declarado antes de empezar.** Declararlo después es
   elegir el plazo que convenga al resultado.

**Los seis riesgos que los discursos de venta omiten** —y que esta skill añade—:
**sobreajuste** (la estrategia aprendió el pasado, no el mercado) · **costo total**
(comisiones, deslizamiento, impuestos, datos, infraestructura) · **latencia y calidad de
datos** · **riesgo de ruina** (una secuencia de pérdidas que deja fuera de juego antes de
que la ventaja se manifieste) · **responsabilidad** (quién responde por una orden que el
agente mandó) · **modo degradado** (qué hace el sistema cuando se cae la conexión, el
proveedor de datos o el modelo).

## Qué NO hacer / compuertas 🚦

- 🚦 **Un freno escrito en el prompt NO es un freno.** Una instrucción es **contexto**: el
  modelo la lee y puede no seguirla ([[arnes-agentico-bucle-y-contexto]]). El freno por
  caída tiene que estar en código que el agente no pueda saltar.
- 🚦 **Un backtest sin costos no es un backtest.** Es una curva. Y una curva sin costos
  siempre sube más que la realidad.
- 🚦 **Desconfiar de «casi sin código» junto a «usted supervisa el riesgo».** Son
  incompatibles: no se audita una capa de riesgo que no se entiende. Si la promesa incluye
  las dos cosas, una de las dos es falsa.
- 🚦 **Todo umbral numérico sin derivación es arbitrario.** Un «freno al 15 %» que nadie
  justificó no es una decisión de riesgo: es un número redondo. Derivarlo del capital, del
  horizonte y de la tolerancia real ([[cuantificar-antes-de-pedir]]).
- 🚦 **Antes de seguir una receta de redes, comprobar que la receta existe.** El caso que
  originó esta skill: el post dice que el prompt está abajo y **no hay prompt**; la
  respuesta más votada lo señala. La promesa circuló 69.000 veces sin su contenido.
- 🚦 **No convertir esto en consejo de inversión.** Si la pregunta es *qué* comprar o
  vender, la respuesta correcta es que no corresponde: no hay licencia ni mandato.

## Protocolo de uso

1. **Separar las dos preguntas:** si la estrategia tiene ventaja, y si el sistema que la
   ejecuta es seguro. Son auditorías distintas y la segunda es la que gobierna esta skill.
2. **Antes de escribir una línea**, declarar por escrito: capital en riesgo, umbral de
   freno **con su derivación**, duración del papel y quién aprueba cada orden.
3. **Montar el freno y la aprobación como mecanismo** —hook o aprobación obligatoria— y
   probar que funcionan **provocando el caso**, no leyendo el código.
4. **Backtest con los cuatro costos.** Si alguno no se puede estimar, declararlo como
   supuesto visible, no omitirlo.
5. **Papel durante el periodo declarado**, con la bitácora que se usará después.
6. **Revisión en fecha fija**, no cuando duele.

## Cómo depurar si falla

- **En papel iba bien y en real no:** mirar primero costos y deslizamiento; después,
  sobreajuste. Casi nunca es el modelo.
- **El agente operó algo que nadie aprobó:** la aprobación estaba en el prompt, no en el
  mecanismo. Es el fallo de diseño más común y el más caro.
- **El freno no se activó:** comprobar que el umbral se evalúa en el código y con qué dato;
  un freno que depende de un precio que llegó tarde no frena.
- **Se cayó el proveedor de datos y el sistema siguió operando:** falta el modo degradado.
  Por omisión, el modo degradado debe ser **detenerse**.

## Portabilidad (revisar el 20% al reusar)
Los cinco componentes son del dominio de mercados. **Los tres frenos, la distinción entre
instrucción y mecanismo y los seis riesgos valen para cualquier agente que mueva dinero o
active algo irreversible** — cobros, pagos, despachos, firmas.

## Reuso (no empezar de cero)
Para la doctrina de ventaja estadística validada,
[[simons-ventaja-estadistica-validada]] y [[doctrina-thorp-matematica-vs-multitud]]. Para
qué datos pueden salir de la casa, [[gobernanza-datos-financieros-ia]]. Para la aprobación
obligatoria y la frontera dato-frente-a-orden, [[mcp-conexion-ambitos-y-frontera]]. Para
distinguir contexto de garantía, [[arnes-agentico-bucle-y-contexto]].

## Ejemplos de invocación
- «Quiero montar un agente que opere por mí, ¿por dónde empiezo?»
- «Este hilo promete un prompt de trading, ¿sirve?»
- «¿Dónde pongo el freno por caída para que de verdad frene?»

## Vecindad en la red
Mercados y rigor: [[simons-ventaja-estadistica-validada]],
[[doctrina-thorp-matematica-vs-multitud]], [[rigor-matematico-filtro-pseudociencia]].
Gobierno del agente: [[arnes-agentico-bucle-y-contexto]],
[[mcp-conexion-ambitos-y-frontera]], [[gobernanza-datos-financieros-ia]].
Cuantificación previa: [[cuantificar-antes-de-pedir]].
