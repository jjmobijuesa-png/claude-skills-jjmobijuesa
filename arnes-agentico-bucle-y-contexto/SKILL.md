---
name: arnes-agentico-bucle-y-contexto
description: >-
  Cómo opera por dentro un agente de programación: el bucle de reunir-actuar-verificar,
  el ARNÉS que decide qué ve el modelo, y qué se pierde exactamente cuando el contexto
  se llena. Incluye los dos agujeros de las redes de seguridad (lo remoto y los enlaces
  simbólicos) y por qué un permiso NO es una barrera. Invocar al diagnosticar «el agente
  dejó de hacerme caso», al decidir dónde escribir una regla, o al diseñar cualquier
  agente propio.
trigger_phrases:
  - "el agente dejó de seguir mis instrucciones"
  - "se me llenó el contexto"
  - "por qué olvida lo que le dije al principio"
  - "cómo funciona el bucle agéntico"
  - "deshacer lo que hizo el agente"
  - "modos de permiso"
  - "arnés agéntico"
idioma_de_salida: español
nivel_de_madurez: aplicada
dominio: agentes-ia / fundamentos operativos
fuente:
  - "Documentación oficial de Anthropic, «How Claude Code works» — https://code.claude.com/docs/en/how-claude-code-works (leída íntegra y verificada por HTTP el 12-oct-2026)"
  - "Material de estudio de la casa: G:\\Mi unidad\\5 Clases-Magistrales-HTML\\04-ia-y-sistemas\\17-arquitectura-claude-code.html"
relacionada: memoria-agente-claude-md-reglas, mcp-conexion-ambitos-y-frontera, skills-empaquetar-procedimiento, regla-del-primer-tropiezo
---

## Acerca de mí (cargar al arrancar)
Leer `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md` y
`MEMORY.md`. Es la **primera** de las cuatro skills destiladas de los documentos núcleo:
explica el marco dentro del cual operan [[memoria-agente-claude-md-reglas]],
[[mcp-conexion-ambitos-y-frontera]] y [[skills-empaquetar-procedimiento]]. Complementa
[[llm-como-funcionan-stanford-cs229]] (qué es el modelo) con **qué lo rodea**.

## Doctrina central

**El agente no ejecuta un plan: recorre un bucle.** Tres fases que *se entremezclan* —
reunir contexto, actuar, verificar— y en las que cada paso se decide con lo aprendido en
el anterior. De ahí la consecuencia práctica más rentable: **delegar, no dictar**.
Enumerar los pasos pelea contra el mecanismo.

> «El bucle lo mueven dos componentes: los modelos que razonan y las herramientas que
> actúan. Claude Code es la capa alrededor del modelo que provee las herramientas y
> administra el contexto que el modelo ve. A esa capa envolvente es a lo que el término
> *arnés agéntico* se refiere.»

**El modelo razona; el arnés decide qué le llega.** Memoria, MCP y skills son tres
maneras de gobernar ese arnés — no tres funciones sueltas.

**Qué ve el agente:** su proyecto, su terminal, su estado de git, sus `CLAUDE.md`, la
memoria automática y las extensiones configuradas. Por eso trabaja *a través* del
proyecto y no dentro de un archivo.

**Cuando el contexto se llena, el orden importa:** primero se descartan **las salidas de
herramientas más viejas**, después se resume la conversación. Sobreviven las peticiones y
los fragmentos de código clave. **Lo que se pierde son las instrucciones detalladas del
principio.**

## Qué NO hacer / compuertas 🚦

- 🚦 **No diagnosticar «desobediencia» sin descartar compactación.** Si el agente dejó de
  seguir algo dicho veinte mensajes atrás, lo más probable es que **ya no esté en el
  contexto**. El remedio no es repetirlo más fuerte: es moverlo a un archivo.
- 🚦 **Un modo de permisos no bloquea nada.** Permisos e instrucciones son **contexto**,
  no configuración que se impone. Para que algo se bloquee con independencia de lo que el
  modelo decida, hace falta un **hook de tipo PreToolUse**. Esta distinción es la que
  convierte una regla en garantía.
- 🚦 **Los puntos de control NO cubren lo remoto.** Bases de datos, interfaces de
  programación, despliegues y envíos quedan fuera; y la restauración **omite enlaces
  simbólicos y duros**. Para lo irreversible solo existen el modo de permisos, las reglas
  escritas y la costumbre de confirmar.
- 🚦 **No confundir interrumpir con corregir.** `Esc` cancela la llamada en curso;
  escribir y pulsar `Enter` **encola** y se lee al terminar las llamadas en curso, dentro
  del mismo turno. Usar lo primero cuando el rumbo es malo; lo segundo cuando falta matiz.

## Protocolo de uso

1. **Ante «no me hace caso»:** ¿la instrucción está en un archivo que se carga en cada
   sesión, o solo se dijo en el chat? Si es lo segundo, el diagnóstico está hecho.
2. **Ante una tarea larga:** declarar el encuadre completo al principio y confiar el
   detalle al agente. Reservar `/context` para ver qué ocupa espacio.
3. **Ante algo irreversible:** comprobar que existe un hook, no solo una frase en una
   skill. Si no lo hay, pedir confirmación explícita.
4. **Ante trabajo que llenaría la ventana de lectura:** delegarlo a un subagente, que
   trabaja en su propia ventana y devuelve un resumen.

## Cómo depurar si falla

- **«Siguió una regla que yo no escribí»:** viene del contexto que el propio arnés añade
  — los `CLAUDE.md`, el estilo de salida, los avisos de archivos cambiados en disco y las
  líneas de atribución. Todo ello es configurable.
- **La compactación entra en bucle y aparece un error:** hay un archivo o una salida tan
  grande que el contexto se vuelve a llenar tras cada resumen. El arnés deja de compactar
  a propósito en vez de iterar.
- **Dos sesiones «no se acuerdan» entre sí:** es el diseño. Cada sesión arranca con la
  ventana limpia; lo único que cruza son los `CLAUDE.md` y la memoria automática
  ([[memoria-agente-claude-md-reglas]]).

## Portabilidad (revisar el 20% al reusar)
Los nombres de los modos de permiso y los atajos son propios del producto; **el bucle, la
distinción contexto-frente-a-garantía y el orden de descarte al compactar son generales** y
valen para cualquier arnés agéntico, incluido uno propio.

## Reuso (no empezar de cero)
Para el modelo por dentro, [[llm-como-funcionan-stanford-cs229]]. Para el panorama de la
industria, [[agentic-ai-hitchhiker-guide]] y [[era-pc-agentico-doctrina]]. Para no gastar
ventana de más, [[ahorro-de-tokens]] y [[eficiencia-generacion-respuestas]].

## Ejemplos de invocación
- «El agente dejó de respetar una regla a media sesión, ¿por qué?»
- «¿Dónde escribo esto para que valga siempre?»
- «¿Puedo deshacer lo que acaba de hacer?»

## Vecindad en la red
Hermanas de la serie: [[memoria-agente-claude-md-reglas]],
[[mcp-conexion-ambitos-y-frontera]], [[skills-empaquetar-procedimiento]].
Marco de origen: [[programa-estudio-profundo-mit]] (Aula) y
[[regla-del-primer-tropiezo]] (método de diagnóstico).
