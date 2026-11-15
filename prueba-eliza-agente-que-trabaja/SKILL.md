---
name: prueba-eliza-agente-que-trabaja
description: >-
  Distinguir un agente que TRABAJA de uno que solo resulta convincente. Tres preguntas que
  separan «lo hizo» de «dijo que lo hizo», y la variante cara del efecto ELIZA: la
  automatización silenciosa que informa éxito mientras no produce nada. Invocar ante «el
  agente dice que lo hizo», «la tarea corre bien pero no veo resultados», al aceptar la
  demostración de un proveedor, antes de dar por bueno cualquier tablero, y siempre que una
  salida sea agradable de leer.
trigger_phrases:
  - "el agente dice que lo hizo"
  - "corre bien pero no veo resultados"
  - "¿esto está funcionando de verdad?"
  - "efecto ELIZA"
  - "la demostración del proveedor"
  - "me parece que funciona"
idioma_de_salida: español
nivel: aplicada
dominio: verificación / honradez operativa
metadata:
  version: 1.0
  fecha: 2026-11-08
  origen: clase magistral 28 del Aula. Concepto de Joseph Weizenbaum («ELIZA», Communications of the ACM, 1966; «Computer Power and Human Reason», 1976), traído por un post de Laboratorio del Futuro en LinkedIn el 8-nov-2026. La variante de telemetría salió de una avería real hallada ese mismo día en esta instalación.
  fuente: G:\Mi unidad\5 Clases-Magistrales-HTML\04-ia-y-sistemas\28-construir-un-agente-y-prueba-eliza.html
  relacionada: disenar-agente-cinco-compuertas, bucle-verificacion-garantia-vs-sugerencia, auditoria-evidencia-cuatro-niveles, prediccion-con-reloj, segundo-cerebro-anclaje-verificable, regla-del-primer-tropiezo, observador-escalera-tres-afirmaciones
---

# Skill `prueba-eliza-agente-que-trabaja`

## Acerca de mí (cargar al arrancar)
Leer `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md` y
`MEMORY.md`. Es la **compuerta 4** de [[disenar-agente-cinco-compuertas]], extraída aparte
porque se usa sola y muchísimo más a menudo que el diseño completo.

## Doctrina central

**Efecto ELIZA: atribuir comprensión a un sistema que solo imita.** Joseph Weizenbaum lo
describió en 1966 con su propio programa y pasó el resto de su vida advirtiéndolo. El caso
que lo fundó no fue un ingenuo engañado: fue **su propia secretaria**, que lo había visto
programar ELIZA durante meses y sabía que era solo código, pidiéndole salir de la
habitación para hablar a solas con la máquina.

🚦 **Saber cómo funciona no inmuniza. La prueba no es para ingenuos: es para usted.**

### La variante cara, que casi nadie nombra

El efecto se ilustra siempre con conversaciones porque ahí es vistoso. **Su forma más cara
es muda:** una automatización que imita con precisión la forma de la señal de éxito que
usted buscaba.

> Un código de salida cero se ve exactamente igual cosechando cuatrocientos registros o
> ninguno.

Y a diferencia del chatbot, **nunca produce la sensación de estar hablando con alguien, así
que nunca despierta sospecha.** Un tablero en verde es un ELIZA perfecto.

### Las tres preguntas

Ninguna pregunta por el modelo, por el proveedor ni por la tecnología.

| | Pregunta | Qué caza |
|---|---|---|
| **a** | ¿Sería la salida **igual de convincente si fuera falsa**? | La fluidez que no informa. Si sí, el tono no le está diciendo nada |
| **b** | ¿Puedo separar **«lo hizo» de «dijo que lo hizo»**, con un rastro que no venga del propio agente? | La autocertificación |
| **c** | Si **borro el adorno** —el resumen amable, el tono, el emoji, el código de salida—, ¿queda algo medible debajo? | El decorado |

**La prueba del borrado (c) es la más barata y la que más rinde.** Hermana de la «cifra de
contrabando» de [[prediccion-con-reloj]]: si al quitar el elemento la frase no pierde
sentido, no informaba, decoraba.

### La jerarquía del rastro

De peor a mejor. **Suba todo lo que pueda; el escalón 1 no es evidencia.**

1. El agente informa que lo hizo. *(No es evidencia. Es una afirmación del interesado.)*
2. El sistema que lo lanza informa que terminó sin error. *(Tampoco: mide el proceso, no el trabajo.)*
3. **Cambió un artefacto comprobable**: fecha de modificación, recuento de filas, tamaño, asiento.
4. **Un tercero acusa recibo**: un acuse, un registro ajeno, una respuesta de otra parte.
5. **Un humano usó el resultado** y le sirvió.

## Qué NO hacer / compuertas 🚦

- 🚦 **Nunca aceptar la señal que emite el propio agente como prueba de su trabajo.** Es la
  más barata de falsificar, y no hace falta mala fe: basta un fallo silencioso aguas arriba.
- 🚦 **Una explicación plausible no es una comprobación.** Caso que lo enseñó (8-nov-2026):
  se anotó en memoria que un perfil de navegador «necesitaba relogueo». Encajaba con la
  experiencia previa, explicaba el síntoma y **era falso: ese perfil no existía en el
  disco**. La comprobación costaba un comando; la explicación costó semanas.
- 🚦 **No mirar solo la última corrida.** La avería se ve en la **serie**: ciento treinta y
  dos días con el recuento plano y el código de salida en cero. Una corrida buena no prueba
  nada; una serie plana sí prueba algo.
- 🚦 **Un aviso sin lector equivale al silencio.** Caso del 8-nov-2026: el guion **sí**
  escribía `ADVERTENCIA: 0 capturados`, dentro de un registro de 364 KB que nadie abría.
  Sale peor que no avisar, porque permite creer que el sistema avisaría. **La comprobación
  no es «¿emite aviso?», es «¿quién lo lee, y qué se detiene si nadie lo lee?»** Un aviso
  solo cuenta cuando llega a una persona o frena algo.
- 🚦🚦 **Una colección vacía no puede significar dos cosas.** El defecto más común en los propios arneses: un ayudante que devuelve `[]` tanto si no hay nada como si **no pudo mirar**. Caso del 8-nov-2026, cómico y caro: un guion de esta casa, escrito *para* esta clase, listaba fuentes y devolvía lista vacía al fallar el comando; la comprobación de más abajo lo leyó como «la fuente nueva no existe» estando en `ready`. **Regla: el error se propaga o se grita; nunca se convierte en dato.** Si una función puede devolver «vacío» y «no sé», tiene que devolver cosas distintas.
- 🚦🚦 **Un veredicto enmascarado es peor que un registro perdido.** Hermana de la anterior,
  pero por el otro lado: no es que el fallo se vuelva dato, es que **un fallo preciso se
  degrada a fallo genérico y se pierde la causa**. Caso del 8-nov-2026, en el vigía de X: la
  envoltura `.bat` redirigía su salida con `>> watcher.log`, que en Windows deja el archivo
  tomado, y el `log()` del guion abría *ese mismo* archivo en modo añadir. `PermissionError`
  al escribir una línea de bitácora, la excepción subió hasta `__main__`, y **el código de
  salida pasó de 3 —«la sesión de X caducó», que dice exactamente qué hacer— a 1, «algo
  falló»**. El diagnóstico sobrevivió por casualidad: estaba en el texto del rastreo.
  **Regla: la ruta de registro nunca puede derribar la ruta de resultado.** Toda escritura de
  bitácora va envuelta, y la envoltura y el guion escriben en archivos distintos.
- 🚦 **No confundir «no falló» con «funcionó».** Son medidas de cosas distintas y el verde
  del tablero mide la primera.
- 🚦 **Cuidado con la salida bonita.** Si el entregable es agradable de leer, **mire el
  número de debajo antes de darlo por bueno.** La fluidez es un estímulo, no una prueba.
- 🚦 **En demostraciones de proveedor:** pida ejecutar un caso **suyo, elegido por usted en
  el momento**, y pida ver el rastro de nivel 3 o superior. Una demostración sobre casos del
  proveedor no es una demostración, es un anuncio.

## Protocolo de uso

1. **Nombrar el artefacto comprobable** que debería cambiar si el agente trabajó: un
   archivo, una fila, un contador, un acuse. Si no existe ninguno, **ese es el hallazgo** y
   el trabajo es crearlo.
2. **Mirarlo, no preguntarlo.** Fecha de modificación, recuento, tamaño. Treinta segundos.
3. **Mirar la serie, no la última vez.** ¿Lleva plano desde cuándo?
4. **Aplicar las tres preguntas** y escribir las respuestas. Si la (b) no se puede
   responder, el agente está autocertificándose.
5. **Subir el rastro un escalón** en la jerarquía, aunque sea uno solo. Es la mejora de
   mayor rendimiento que existe en un agente.
6. **Dejar la comprobación automatizada, con umbral y con destinatario**: no «corrió», sino
   «el recuento subió al menos N desde la última vez», y **que falle con ruido donde
   alguien lo vea**. Un verde que no puede ponerse rojo no es un verde, y un rojo que nadie
   lee no es un rojo.

## Cómo depurar si falla

- **«Todo está en verde y nada avanza»:** está midiendo el proceso y no el producto. Salte
  al escalón 3 de la jerarquía y mire el artefacto.
- **«El indicador está puesto y la función no existe»:** el caso canónico del 8-nov-2026. Un
  navegador se lanzaba con el indicador del puerto de depuración **presente en la línea de
  órdenes** y el puerto no estaba a la escucha, porque desde Chromium 136 ese indicador se
  ignora en silencio sobre el perfil por defecto. **Que el indicador aparezca no prueba
  nada; solo prueba el puerto a la escucha.** Detalle en
  [[feedback_cdp_9222_ignorado_perfil_defecto]].
- **«Me convence y no sé por qué»:** aplique el borrado (c). Quite tono, resumen y formato.
  Lo que quede es lo que había.
- **«El proveedor enseñó algo impresionante»:** pida su propio caso, en vivo, y el rastro.
  Si solo hay nivel 1 o 2, no ha visto el producto: ha visto la interfaz.
- **«Sospecho pero no puedo probarlo»:** no hace falta probar el engaño. Basta constatar que
  **no se puede distinguir** el trabajo hecho del narrado. Esa imposibilidad ya es el
  veredicto, y se informa así.
- **«El agente es mío y me da pudor desconfiar»:** el caso fundacional es precisamente el de
  alguien que conocía el código por dentro. El pudor es parte del efecto.

## Portabilidad (revisar el 20% al reusar)
Sirve para agentes, para tareas programadas, para tableros, para demostraciones de
proveedor, para informes de un equipo y para su propia automatización doméstica, **porque
el mecanismo no es de inteligencia artificial: es que la señal de éxito más barata de
emitir es la que emite el interesado.** Lo que cambia al reusar es cuál es el artefacto
comprobable de ese dominio.

## Reuso (no empezar de cero)
Para los grados de garantía de un montaje, [[bucle-verificacion-garantia-vs-sugerencia]].
Para clasificar evidencia ya existente, [[auditoria-evidencia-cuatro-niveles]]. Para
afirmaciones sobre el futuro, [[prediccion-con-reloj]]. Para la jerarquía de anclaje,
[[segundo-cerebro-anclaje-verificable]]. Para separar lo que alguien afirma de lo que
sostiene, [[observador-escalera-tres-afirmaciones]]. Ante el primer fallo,
[[regla-del-primer-tropiezo]].

## Ejemplos de invocación
- «La tarea corre todos los días, ¿cómo sé que está haciendo algo?»
- «Me enseñaron una demostración de un agente de ventas, ¿qué le pido?»
- «Este informe del agente me parece demasiado bueno.»
- «¿Está funcionando el autorespondedor?»

## Vecindad en la red
Serie de agentes: [[disenar-agente-cinco-compuertas]],
[[cartera-agentes-producto-y-servicio]].
Verificación: [[bucle-verificacion-garantia-vs-sugerencia]],
[[auditoria-evidencia-cuatro-niveles]], [[prediccion-con-reloj]],
[[segundo-cerebro-anclaje-verificable]], [[observador-escalera-tres-afirmaciones]],
[[historiografia-cinco-filtros-fuentes]].
Operación: [[arnes-agentico-bucle-y-contexto]], [[regla-del-primer-tropiezo]],
[[cierre-verificado-integridad]].
