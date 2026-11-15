---
name: disenar-agente-cinco-compuertas
description: >-
  La puerta de entrada para construir un agente. Decide PRIMERO si la tarea merece un
  agente o si es una regla, una plantilla o un guion de tres líneas, y solo entonces lo
  diseña. Cinco compuertas que se responden por escrito antes de abrir nada: número,
  serie de verificación, arnés, prueba ELIZA y responsable. Invocar ante «quiero
  automatizar esto», «hazme un agente que…», «¿me conviene un agente para…?», o al
  evaluar el agente que ya tiene alguien montado.
trigger_phrases:
  - "quiero armar un agente"
  - "hazme un agente que"
  - "¿me conviene un agente para esto?"
  - "automatizar esta tarea"
  - "diseñar un agente desde cero"
  - "cinco compuertas"
idioma_de_salida: español
nivel: aplicada
dominio: diseño de agentes / decisión
metadata:
  version: 1.0
  fecha: 2026-11-08
  origen: clase magistral 28 del Aula. Tres fuentes del 7 y 8-nov-2026 (guía de 7 pasos de Msc. Luis Caiza Soria en LinkedIn; hilo de @bottegamd en X y el artículo «Harness, Loop and Graph» de @0xwhrrari; efecto ELIZA de Laboratorio del Futuro) más la avería del puerto de depuración hallada ese mismo día en esta instalación.
  fuente: G:\Mi unidad\5 Clases-Magistrales-HTML\04-ia-y-sistemas\28-construir-un-agente-y-prueba-eliza.html
  relacionada: prueba-eliza-agente-que-trabaja, cartera-agentes-producto-y-servicio, arnes-agentico-bucle-y-contexto, cuantificar-antes-de-pedir, prediccion-con-reloj, skills-empaquetar-procedimiento, bucle-verificacion-garantia-vs-sugerencia, arquitectura-consejo-multiagente
---

# Skill `disenar-agente-cinco-compuertas`

## Acerca de mí (cargar al arrancar)
Leer `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md` y
`MEMORY.md`. Voz de la casa: Francisco Duque, *usted*, cortés-formal. Esta skill es la
**puerta de entrada** de la serie de agentes; para verificar uno ya construido se pasa a
[[prueba-eliza-agente-que-trabaja]], y para venderlo a
[[cartera-agentes-producto-y-servicio]].

## Doctrina central

**La pregunta que casi nadie hace es la primera: ¿esta tarea merece un agente?** Las guías
al uso empiezan en «defina el objetivo», que ya da por supuesto que sí. La mayor parte del
dinero que se pierde en agentes se pierde antes de la primera línea, al automatizar algo
que era una regla.

Un agente cuesta diez veces más que una regla: hay que construirlo, vigilarlo, y se
degrada solo cuando cambia cualquier cosa a su alrededor. **Solo se justifica cuando el
trabajo tiene volumen, tiene verificación posible y tiene dueño.**

### Las cinco compuertas

Se responden **por escrito, en una hoja, antes de abrir nada.**

| # | Compuerta | Lo que hay que poder escribir |
|---|---|---|
| 1 | **¿Tiene número?** | Volumen y frecuencia medidos. «Resumir correos» es una queja; «40 correos al día, 15 minutos cada mañana, 5 días a la semana» es una tarea y ya dice el premio |
| 2 | **¿Quién verifica, y en qué serie?** | El registro concreto donde se leerá si funcionó, **nombrado antes de encender** |
| 3 | **¿Qué ve exactamente?** | El arnés: qué archivos, qué fragmento, qué herramientas, qué permisos, qué pasa al llenarse el contexto |
| 4 | **Prueba ELIZA** | ¿Distingo «lo hizo» de «dijo que lo hizo», con un rastro ajeno al propio agente? |
| 5 | **¿Quién responde si falla?** | Una persona con nombre, y el punto exacto en que pasa a humano |

**La decisión es binaria y se escribe:**
- **Cinco** → se construye.
- **Cuatro** → se construye, con la que falta anotada como riesgo aceptado y **fecha de revisión**.
- **Menos de cuatro** → **no es un agente.** Es una regla en el archivo de instrucciones, una
  plantilla o un guion. Se anota el «no» **con su motivo**: ese documento es el que evita
  volver a plantear lo mismo dentro de seis meses.

### Criterio contra acceso — la columna que ordena el diseño

Al repasar un diseño ajeno o propio, clasifique cada pieza:

| Pieza | Qué es |
|---|---|
| Objetivo, rol, pasos, **lo que no debe hacer** | **Criterio.** No se delega ni se compra |
| Conocimiento propio cargado (guías, plantillas, ejemplos buenos) | **Criterio.** Es lo que separa su respuesta de una genérica |
| Elegir qué capacidades se activan | **Criterio** |
| Tener esas capacidades disponibles | Acceso |
| Conectores a correo, almacenamiento, mensajería | **Solo acceso.** No añade un gramo de juicio; añade superficie de riesgo |

🚦 **Si al terminar el reparto casi todo cayó en «acceso», no está construyendo un agente:
está repartiendo llaves.**

## Qué NO hacer / compuertas 🚦

- 🚦 **No empezar por la herramienta.** «Vamos a usar tal framework» antes de la compuerta 1
  es la forma más cara de descubrir que bastaba una regla.
- 🚦 **No saltar la compuerta 2 «porque ya se verá».** La serie elegida *después* es siempre
  la que da la razón. Si al nombrarla se descubre que no existe, **el primer entregable
  cambia**: es crear el registro, no el agente. Hermana de [[prediccion-con-reloj]].
- 🚦 **No construir el agente de todo.** Una sola tarea repetida; cuando funcione, se copia
  la estructura para la siguiente. Es el consejo que el autor de la fuente original puso en
  su primer comentario y no en el post, y es el mejor de los tres.
- 🚦 **Un permiso no es una barrera.** Conceder acceso a una herramienta no limita al agente
  a usarla bien. Ver [[arnes-agentico-bucle-y-contexto]].
- 🚦 **No prometer autonomía donde hay sugerencia.** Si la salida requiere que un humano la
  revise antes de surtir efecto, el agente **propone**, no ejecuta, y así se le describe al
  cliente. Compuerta de [[bucle-verificacion-garantia-vs-sugerencia]].
- 🚦 **El «no» también es entregable.** Un diagnóstico que concluye «esto no merece agente»
  vale dinero y ahorra más. No se esconde.

## Protocolo de uso

> **Tómese su tiempo. La hoja de compuertas se escribe entera antes de tocar nada.**

1. **Enunciar la tarea en una frase que contenga un número.** Si no sale el número, se para
   aquí y se mide primero ([[cuantificar-antes-de-pedir]]).
2. **Rellenar las cinco compuertas por escrito**, en ese orden. Ninguna se deja «pendiente».
3. **Contar.** Aplicar la decisión binaria de arriba. Si es «menos de cuatro», redactar el
   «no» con su motivo y proponer la regla, plantilla o guion que sí resuelve, y terminar.
4. **Si se construye:** repartir cada pieza en criterio o acceso, y diseñar el arnés antes
   que el prompt — qué entra en contexto y qué se hace cuando se llene.
5. **Prueba con casos reales**, no inventados, y revisión de cada resultado contra la serie
   de la compuerta 2.
6. **Fijar la fecha de revisión en el mismo acto de ponerlo en marcha.** Un agente anotado y
   no revisado es peor que ninguno.
7. **Dejar el hallazgo como capacidad** ([[llave-maestra-autoaprendizaje-ia]]) y registrar
   en `MEMORY.md`.

## Cómo depurar si falla

- **«El agente pasó todas las pruebas y el problema sigue abierto»:** no es el modelo ni el
  prompt. Es el **arnés** — lo que el agente ve. Volver a la compuerta 3 y escribir, literal,
  qué archivos y qué fragmentos entran en contexto. Ver [[arnes-agentico-bucle-y-contexto]].
- **«Funciona en la demostración y no en producción»:** la demostración usó casos elegidos.
  Compuerta 6 del protocolo: casos reales, tomados al azar del montón.
- **«No sé si está funcionando»:** falta la compuerta 2. No se diagnostica mirando salidas;
  se diagnostica mirando la serie. Si no hay serie, ese es el fallo, no el agente.
- **«Informa éxito y no produce nada»:** compuerta 4, y es el fallo más caro de todos. Pasar
  entero a [[prueba-eliza-agente-que-trabaja]].
- **«Se construyó y nadie lo usa»:** faltó la compuerta 5. Sin una persona con nombre, un
  agente es de nadie y muere sin que se note.
- **«Cada vez hace algo distinto con la misma entrada»:** el contexto se está llenando y lo
  que se descarta cambia entre corridas. Es arnés, no temperatura.

## Portabilidad (revisar el 20% al reusar)
Las cinco compuertas valen para un agente de software, para un procedimiento de oficina y
para contratar a una persona, **porque el mecanismo no es técnico: es que un trabajo sin
volumen, sin verificación y sin dueño no se sostiene lo haga quien lo haga.** Lo que cambia
al reusar es qué cuenta como «serie» en ese dominio y quién puede ser el responsable.

## Reuso (no empezar de cero)
Para el interior del agente, [[arnes-agentico-bucle-y-contexto]]. Para varios agentes
coordinados, [[arquitectura-consejo-multiagente]]. Para memoria entre ejecuciones,
[[graph-engineering-memoria-agentes]]. Para decidir entre regla, skill y guion,
[[skills-empaquetar-procedimiento]]. Para exigir número antes de pedir,
[[cuantificar-antes-de-pedir]]. Para la fecha de revisión, [[prediccion-con-reloj]]. Para
auditar una herramienta antes de meterla, [[auditar-skills-antes-de-instalar]] y
[[cosechar-repositorios-de-agentes]].

## Ejemplos de invocación
- «Quiero un agente que me ordene la bandeja de entrada cada mañana.»
- «¿Vale la pena automatizar el informe semanal o lo dejo como plantilla?»
- «Diséñame el agente de cobranzas.»
- «Revisa este agente que ya tengo montado y dime qué le falta.»

## Vecindad en la red
Serie de agentes: [[prueba-eliza-agente-que-trabaja]],
[[cartera-agentes-producto-y-servicio]].
Interior: [[arnes-agentico-bucle-y-contexto]], [[arquitectura-consejo-multiagente]],
[[graph-engineering-memoria-agentes]], [[agentic-ai-hitchhiker-guide]],
[[mcp-conexion-ambitos-y-frontera]].
Decisión y medida: [[cuantificar-antes-de-pedir]], [[prediccion-con-reloj]],
[[skills-empaquetar-procedimiento]], [[control-versiones-entregables]].
Doctrina: [[era-pc-agentico-doctrina]], [[llave-maestra-autoaprendizaje-ia]].
Antes de montar nada: [[escalera-prompting-prueba-del-techo]] — no se sube a agéntico
por ambición, sino cuando la prueba del techo del escalón anterior falla.
