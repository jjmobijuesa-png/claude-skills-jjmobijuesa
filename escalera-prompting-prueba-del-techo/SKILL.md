---
name: escalera-prompting-prueba-del-techo
description: |
  Diagnostica en qué escalón de prompting se está trabajando y, sobre todo,
  CUÁNDO hay que subir. Los cuatro niveles —directo, estructurado, de
  razonamiento y agéntico— son conocidos; lo que casi nunca se escribe es la
  señal de fallo que avisa de que el escalón actual se quedó pequeño. Esta skill
  aporta esa pieza: una PRUEBA DEL TECHO por escalón, formulable en una línea,
  falsable y observable en el trabajo real. Incluye la compuerta que impide
  subir por moda y la corona de la escalera, que no es una técnica sino declarar
  el límite.

  Casos de invocación: «la IA me da respuestas genéricas», «¿necesito un agente
  para esto?», «¿por qué me contesta distinto cada vez?», «el razonamiento está
  bien pero los datos no existen», «¿vale la pena montar RAG?».

trigger_phrases:
  - "niveles de prompting"
  - "prueba del techo"
  - "¿necesito un agente?"
  - "respuestas genéricas"
  - "me contesta distinto cada vez"
  - "¿subo a agéntico?"
idioma_de_salida: español neutro técnico-instruccional
nivel_madurez: maestra
fuente: clase magistral 32 del Aula (14-nov-2026)
---

# La escalera de prompting y la prueba del techo

## Acerca de mí (cargar al arrancar)
Leer `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md`.
Clase que la originó:
`G:\Mi unidad\5 Clases-Magistrales-HTML\04-ia-y-sistemas\32-tres-escalones-y-el-limite-declarado.html`.

## Doctrina central

> **Un cuadro de niveles que solo dice «cuándo usar cada uno» no es un
> instrumento: es una lámina.** Un instrumento es aquello que puede marcar que
> algo va mal. Sin una señal de fallo, cada quien se queda en el escalón que le
> resulta cómodo y cree que es el adecuado.

La tabla de cuatro niveles circula desde hace años y es correcta. El problema no
es su contenido, es su uso: **se lee para situarse, no para detectar**. Esta skill
le añade la lectura que falla.

**Regla dura:** no se sube de escalón por ambición, por moda ni por curiosidad.
**Se sube cuando la prueba del techo falla.** Subir antes es gasto; subir después
se paga en un entregable que hubo que rehacer.

## Los cuatro escalones y su prueba del techo

| # | Escalón | Está aquí si… | **PRUEBA DEL TECHO** (la señal de subir) | Qué cambia al subir |
|---|---|---|---|---|
| 1 | **Directo** | Escribe la pregunta y acepta la primera respuesta. Zero-shot | **La misma pregunta dos veces da dos respuestas incompatibles.** La variación no viene del modelo: viene de que usted no fijó papel ni formato | Fijar rol, contexto, restricciones y formato de salida |
| 2 | **Estructurado** | Da rol, contexto, formato y ejemplos. Few-shot | **La respuesta tiene la forma pedida y el contenido equivocado.** El molde se cumple, el razonamiento no aparece | Exigir pasos intermedios, alternativas y verificación de consistencia |
| 3 | **Razonamiento** | Pide descomponer, razonar, evaluar y responder. CoT, ToT, autoconsistencia | **El razonamiento es impecable y los datos están inventados.** Ya no es cuestión de pensar mejor: faltan hechos del mundo | Dar herramientas, fuentes de datos y memoria. Se entra en lo agéntico |
| 4 | **Agéntico** | Orquesta herramientas, datos, memoria y acciones. ReAct, RAG | **Hace lo que usted pidió y nadie sabe decir con qué garantía lo hizo.** Funciona y no es defendible ante un tercero | Declarar el límite: compuertas, modos y evidencia con su cobertura |

🚦 **La prueba del escalón 3 es la más engañosa de las cuatro**, porque la calidad
visible del razonamiento inspira confianza en los hechos que hay debajo. Es la que
produce los errores más caros y los más difíciles de ver en revisión.

## La corona: lo que no es un quinto escalón

Al llegar arriba aparece un problema que no se resuelve con más técnica: el sistema
funciona y nadie puede decir con qué garantía. Lo que corona la escalera **no es una
capa más, es una forma de responder**:

1. **Declarar qué se rehúsa hacer.** Una herramienta que dice qué no hace se puede
   auditar; una que promete todo solo se puede creer. Ver
   [[sala-limpia-reimplementacion-licita]] para la versión fuerte de esta idea.
2. **Entregar evidencia con su confianza, su cobertura y sus limitaciones.** Una
   cifra sin cobertura declarada no es evidencia: es una impresión con formato de
   dato. Ver [[auditoria-evidencia-cuatro-niveles]].

En esta casa la corona **ya existe y tenía otro nombre**: las compuertas 🚦 de
`~/.claude/CLAUDE.md` son, literalmente, la lista de lo que esta operación rehúsa.

## Qué NO hacer / compuertas 🚦

- 🚦 **No subir de escalón sin escribir la señal que obligó a subir.** Si no se puede
  escribir en una línea, no es un techo: son ganas de probar herramienta nueva.
- 🚦 **No confundir «respuesta distinta» con «respuesta incompatible».** Dos redacciones
  del mismo contenido no son la prueba del escalón 1. La prueba exige contradicción
  de fondo.
- 🚦 **No tratar el escalón 4 como meta.** En esta casa es el suelo, no la cima: la red
  de skills ya es un sistema agéntico. Lo que falta arriba no es potencia, es
  declaración.
- 🚦 **No responder al techo del escalón 3 con más razonamiento.** Es el reflejo
  equivocado y el más común: si los datos no existen, pensar mejor los inventa mejor.
- 🚦 **El escalón no es una propiedad de la persona, es de la tarea.** El mismo día se
  trabaja en el 1 para un resumen y en el 4 para una conciliación. Diagnosticar por
  tarea, nunca por usuario.

## Protocolo de uso

1. **Nombrar la tarea**, no la herramienta. «Resumir un acta» y «conciliar cinco
   cuentas» no están en el mismo escalón aunque se usen el mismo día.
2. **Buscar cuál de las cuatro señales se vio esta semana** en esa tarea. No se lee la
   tabla de arriba abajo para situarse: se lee buscando el fallo observado.
3. **Si ninguna señal apareció, quedarse donde está.** Es un resultado válido y es el
   más frecuente.
4. **Si apareció una, subir un solo escalón** y volver a medir. Nunca dos de golpe:
   saltar del 1 al 4 impide saber qué resolvió el problema.
5. **Al llegar al 4, pasar a la corona:** escribir qué rehúsa el montaje y con qué
   cobertura entrega sus cifras.

## Cómo depurar si falla

- **«Estoy en el 4 y sigue fallando»:** casi siempre el techo real era del 3 y se
  tapó con herramientas. Quitar herramientas y comprobar si los hechos estaban.
- **«No sé en qué escalón estoy»:** es señal de escalón 1 o 2. Quien trabaja en el 3
  o el 4 lo sabe, porque tuvo que montarlo.
- **«Subí y no mejoró»:** la señal que lo hizo subir no estaba escrita. Volver al paso
  1 del protocolo y escribirla antes de tocar nada.
- **«Todas las señales me parecen aplicables»:** no se nombró la tarea, se nombró la
  herramienta. Partir la tarea en dos y repetir.
- **«Funciona y no sé por qué»:** eso es exactamente la prueba del techo del 4. La
  salida no es técnica: es declarar el límite.

## Portabilidad (revisar el 20 % al reusar)
El mecanismo no es de prompting: **es el de cualquier escalera de capacidades que se
enseña sin su señal de fallo.** Vale igual para herramientas de oficina, para procesos
de obra y para niveles de delegación en un equipo. Lo que cambia al reusar es cuál es
la señal observable en ese dominio; lo que no cambia es que sin señal de fallo el
cuadro no diagnostica.

## Reuso (no empezar de cero)
Para elegir el modelo adecuado a la dificultad real, [[selector-modelo-claude-optimo]].
Para decidir si una tarea merece agente o es una regla de tres líneas,
[[disenar-agente-cinco-compuertas]]. Para el arnés que rodea al prompt,
[[arnes-agentico-bucle-y-contexto]]. Para exigir número antes de pedir,
[[cuantificar-antes-de-pedir]]. Para separar lo que una herramienta garantiza de lo
que sugiere, [[bucle-verificacion-garantia-vs-sugerencia]].

## Ejemplos de invocación
- «La IA me da respuestas muy genéricas, ¿qué hago?»
- «¿Esto necesita un agente o lo resuelvo con un prompt?»
- «Me contesta distinto cada vez que le pregunto lo mismo.»
- «El razonamiento está bien pero las cifras no existen.»
- «¿Vale la pena montar RAG para esto?»

## Vecindad en la red
Prompting y modelos: [[prompting-opus-5-doctrina]], [[selector-modelo-claude-optimo]].
Agentes: [[disenar-agente-cinco-compuertas]], [[arnes-agentico-bucle-y-contexto]],
[[prueba-eliza-agente-que-trabaja]].
Verificación: [[bucle-verificacion-garantia-vs-sugerencia]],
[[auditoria-evidencia-cuatro-niveles]], [[prediccion-con-reloj]].
Hermanas de la clase 32: [[sala-limpia-reimplementacion-licita]],
[[metadatos-que-ocultan-el-dato-decisivo]].
