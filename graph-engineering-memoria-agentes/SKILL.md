---
name: graph-engineering-memoria-agentes
description: >-
  Doctrina para dar MEMORIA PERMANENTE a sistemas multiagente mediante un
  knowledge graph que reemplaza la ventana de contexto. Invocar al diseñar
  agentes que deben recordar entre ejecuciones (AlphaLab del Alfa Lab, DIRA-Alfa,
  cualquier orquestación multiagente).
trigger_phrases:
  - "graph engineering"
  - "memoria de agentes"
  - "knowledge graph para agentes"
  - "memoria compartida multiagente"
  - "la memoria del agente muere con el contexto"
idioma_de_salida: español
nivel_de_madurez: especializada
dominio: blockchain-fintech / agentes-ia
fuente:
  - "X @beamnxw status 2081324327899746541 (2026-07): graph engineering = OS del stack de agentes"
  - "X @nicos_ai status 2081066452694556956 (2026-07): pipeline de 5 fases, PDF 12 págs de ingeniero senior de Anthropic"
---

## Acerca de mí (cargar al arrancar)
Leer `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md`
y `MEMORY.md`. Hermana de [[agentic-ai-hitchhiker-guide]] (capa *memory systems*
del stack agentic) y de [[era-pc-agentico-doctrina]]. Se aplica sobre el **Pilar IV
del Alfa Lab** (agentes AlfaLab Explorer/Builder/Critic/Tester/Strategist/
Workers/Supervisor) y sobre la orquestación de [[project_alfalab_uteq]].

## Doctrina central
> «La memoria de tus agentes muere con su ventana de contexto. Un knowledge
> graph la hace permanente.» — @nicos_ai

La mayoría de los frameworks apilan texto no estructurado dentro de prompts
planos. La **ingeniería de grafos** sustituye la ventana de contexto cruda por
un **grafo relacional estructurado** que es a la vez memoria y sistema operativo
del stack de agentes: la topología explícita del grafo controla los DAG de
planificación, la ejecución de herramientas, la memoria y la coordinación
multiagente. Los **nodos** ejecutan modelos especializados, las **funciones de
arista** enrutan decisiones, y la **memoria de grafo** preserva el estado a
través de bucles de ejecución largos. El grafo **no se reconstruye: crece**.

## El pipeline de 5 fases (núcleo replicable)
1. **Extraer** — un modelo barato (Haiku) saca de cada documento entidades y
   triples *sujeto–predicado–objeto*. Una llamada por documento. **El esquema
   Pydantic es el único "training data".**
2. **Resolver** — un modelo fuerte (Sonnet) fusiona entidades duplicadas
   («Edwin Aldrin» = «Buzz Aldrin») usando las *descripciones* como contexto,
   sin depender del solape de texto.
3. **Ensamblar** — nodos canónicos + aristas tipadas + *provenance* en cada
   triple → un único grafo conectado.
4. **Consultar** — se serializa un *subgrafo*, el modelo razona sobre los
   triples y **cada respuesta cita una arista concreta** (trazabilidad).
5. **Repetir** — cada documento nuevo vuelve a entrar por el mismo pipeline y
   se fusiona con los nodos existentes. El grafo crece de forma incremental.

## Las 3 capas de memoria de un consejo (cosechado de OpenExecutive)
Un sistema multiagente en producción no tiene «una» memoria, sino **tres**, y
conviene separarlas al diseñar:

| Capa | Qué guarda | Dónde | Cómo se llena |
|---|---|---|---|
| **Episódica** | decisiones e iniciativas pasadas | SQLite | un pase en **segundo plano con un modelo barato** extrae lo decidido tras cada respuesta |
| **Conocimiento** | base curada + documentos propios | vector store (ChromaDB) | indexación; se consulta por recuperación |
| **De interlocutor** | ficha por persona, entre canales | almacén aparte | se acumula por conversación |

Más un **scheduler** que empuja seguimientos proactivos, con **reclamo de tarea
de instancia única** para que dos procesos no ejecuten lo mismo.

⭐ **Regla de oro heredada:** el **contexto recuperado (RAG) va en el turno del
usuario, NUNCA en el prompt de sistema cacheado** — meter ahí lo que cambia en
cada llamada rompe la caché y multiplica el costo. El grafo de esta skill cumple
el papel de la capa de **conocimiento**; la episódica es complementaria, no la
sustituye. Patrón completo en [[arquitectura-consejo-multiagente]].

## Qué NO hacer / compuertas 🚦
- 🚦 **No** meter datos sensibles del usuario en el grafo sin decidir antes qué
  va *on-graph* (hashes, entidades) y qué queda *off-graph* (PII) — coherente
  con la mitigación de datos personales de [[project_alfalab_uteq]] (SSI + hash).
- 🚦 **No** reconstruir el grafo desde cero en cada corrida: se fusiona, no se
  regenera (rompe *provenance* y desperdicia tokens — viola
  [[eficiencia-generacion-respuestas]]).
- 🚦 **No** usar un modelo caro para la fase Extraer (es trabajo de Haiku) ni uno
  barato para Resolver/Consultar (requiere razonamiento) — ver
  [[selector-modelo-claude-optimo]].
- 🚦 **No** guardar respuestas sin la arista que las sustenta: sin *provenance*,
  el grafo pierde su ventaja auditable (clave para EcuaLedger/IBPP).
- No inventar el contenido del PDF fuente más allá de lo destilado aquí; si se
  necesita el detalle completo, leer el paper (la fuente es un hilo de X, no el
  PDF: skill parcialmente **huérfana** hasta conseguir el PDF).

## Protocolo paso a paso
> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**
1. Definir el **esquema Pydantic** de entidades y relaciones del dominio (ej.:
   para el Alfa Lab: `Cooperativa`, `Socio`, `Cosecha`, `Token`, `Nodo`,
   `Contrato`, `Ley`; relaciones `tokeniza`, `valida`, `ancla_en`).
2. Fase Extraer con Haiku sobre cada fuente (memos, actas, leyes, transcripciones).
3. Fase Resolver con Sonnet para deduplicar entidades.
4. Ensamblar el grafo con *provenance* (de qué documento salió cada triple).
5. Conectar el grafo como **memoria compartida** de la orquestación multiagente:
   los *Workers* escriben, los *Critic/Tester* contrastan contra él, y los bucles
   siguen vivos de un día para otro.
6. Persistir el grafo fuera de la conversación (archivo/DB) para que sobreviva a
   la compactación de contexto.

## Cómo depurar si falla
- Si el grafo «no recuerda» entre sesiones: verificar que se persiste a disco/DB
  y que la fase Repetir fusiona en vez de recrear.
- Si hay entidades duplicadas: reforzar las *descripciones* que usa la fase
  Resolver, no el texto literal.
- Si las respuestas no son auditables: exigir cita de arista en la fase Consultar.

## Portabilidad (revisar el 20% al reusar)
Cambian: el esquema Pydantic del dominio, los modelos asignados a cada fase
(Haiku/Sonnet vía [[selector-modelo-claude-optimo]]) y el store de persistencia.
El pipeline de 5 fases es estable y portable al Claude remoto (Doctrina 8).

## Reuso (no empezar de cero)
Componer con [[agentic-ai-hitchhiker-guide]] (memoria de agentes),
[[llave-maestra-autoaprendizaje-ia]] (destilar fuentes al grafo) y el Pilar IV de
[[project_alfalab_uteq]]. Enlaza conceptualmente con
[[winston-representacion-restricciones-ia]]: el grafo es la *representación* que
expone las restricciones del problema.

## Ejemplos de invocación
- «Dale memoria persistente a los agentes del Alfa Lab con un knowledge graph.»
- «Arma el pipeline de graph engineering para el expediente EcuaLedger.»
- «¿Cómo evito que la memoria de mis agentes muera con el contexto?»
