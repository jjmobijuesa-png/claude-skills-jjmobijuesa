---
name: arquitectura-consejo-multiagente
description: >-
  Patrón de referencia para construir un CONSEJO de agentes con una sola voz:
  orquestador + registro desacoplado + despacho paralelo + Committee adversarial
  + RAG + memoria en 3 capas + caché de prompts. Invocar al diseñar sistemas
  multiagente (Pilar IV del Alfa Lab), o antes de adoptar un framework de terceros.
trigger_phrases:
  - "arquitectura multiagente"
  - "varios agentes que se coordinan"
  - "consejo de agentes / comité de IA"
  - "cómo orquesto especialistas"
  - "OpenExecutive"
  - "por qué me sale tan caro el agente"
idioma_de_salida: español
nivel_de_madurez: especializada
dominio: agentes-ia / arquitectura
fuente:
  - 'OpenExecutive (SenteLabsAI), Apache 2.0 verificada en el archivo LICENSE. ~2.975 estrellas, 279 forks, creado jun-2026, activo (commits de ago-2026). https://github.com/SenteLabsAI/OpenExecutive'
  - 'Documentación técnica leída vía deepwiki.com/SenteLabsAI/OpenExecutive y el CLAUDE.md del repo'
  - 'Post de midudev en LinkedIn (activity-7499104783518175232) + 9 de sus 78 comentarios, que aportan la crítica'
---

## Acerca de mí (cargar al arrancar)
Leer `...\memory\user_role.md` + `MEMORY.md`. Aplica al **Pilar IV** (agentes
AlphaLab) y **Pilar V** (IA local soberana) de [[project_alfalab_uteq]].
Hermana de [[agentic-ai-hitchhiker-guide]] (stack agentic),
[[graph-engineering-memoria-agentes]] (memoria) y —clave—
[[kleper-cerebro-operador-contra]] (la capa que DISCUTE).

## De dónde sale (y por qué importa el origen)
Un CEO despidió programadores para reemplazarlos con IA; los desarrolladores
respondieron publicando un **«CEO open source»**: 8 agentes de Claude que cubren
estrategia, finanzas, legal, RR. HH., operaciones, marketing, producto y
directorio. Nació como sátira y quedó como **implementación de referencia
funcionando**, con licencia permisiva.

**Doctrina de uso: se cosecha como ARQUITECTURA, no se adopta como producto.**
Adoptarlo tal cual es *eficacia operativa* — cualquiera lo clona hoy
([[porter-estrategia-unico-no-mejor]]). Lo defendible es el patrón + tu corpus.

## El patrón, en seis piezas
1. **Orquestador con voz única.** Un agente recibe, decide a quién consultar y
   **sintetiza una sola respuesta**. Regla del repo: *nunca exponer al usuario la
   arquitectura interna de agentes*. El usuario habla con **uno**, no con ocho.
2. **Registro desacoplado (`SPECIALIST_REGISTRY`).** Un diccionario mapea dominio
   → clase de agente (finanzas→CFO, legal→GC…). El orquestador **no conoce** las
   implementaciones: añadir un especialista es registrar una entrada, no tocar el
   núcleo.
3. **Despacho paralelo.** Si varios dominios son relevantes, se lanzan a la vez
   (`asyncio.gather`). Todas las llamadas de análisis son **asíncronas**.
4. **⭐ Committee — revisión adversarial.** Antes de que la salida llegue al
   usuario, **los agentes se critican entre sí**. Es validación cruzada, no
   consenso automático. *Esta es la pieza más valiosa del diseño.*
5. **RAG en dos capas de conocimiento.** Base curada (Markdown versionado en git)
   + documentos propios de la empresa (indexados en ChromaDB). Los datos de la
   empresa van **gitignored**: «nunca subir datos de la compañía al repositorio».
6. **Memoria en 3 capas.** *Episódica* (SQLite; un pase en segundo plano con un
   modelo barato extrae decisiones e iniciativas) · *Conocimiento* (ChromaDB) ·
   *Peer memory* (fichas por persona, opcional). Más un **scheduler** que empuja
   seguimientos proactivos, con reclamo de tarea de instancia única.

## ⭐ Las reglas de caché (lo más transferible de todo)
El repo advierte que romperlas **multiplica el costo por 10**:

| Regla | Detalle |
|---|---|
| **Nunca contenido dinámico en bloques cacheados** | Si el bloque `cache_control` cambia en cada llamada, la caché no sirve para nada. |
| **Orden fijo de construcción** | ① definiciones de herramientas *ordenadas por nombre* → ② persona del ejecutivo (**nunca** interpolada con f-string) → ③ perfil de la empresa → ④ índice del conocimiento. |
| **El contexto RAG va en el turno del usuario** | **No** en el prompt de sistema. Es la regla de oro: el recuperado cambia siempre, el sistema no. |

Estas tres reglas valen para **cualquier** sistema propio con Claude, no solo
para este repo. Enlazan con [[eficiencia-generacion-respuestas]].

## Qué NO hacer / compuertas 🚦
- 🚦 **No instalarlo sin auditar.** Es código de terceros con acceso a tu API key
  → pasa por [[auditar-skills-antes-de-instalar]] (Doctrina 10): cuarentena,
  revisión, y solo entonces mover.
- 🚦 **No crear un segundo cerebro.** Trae su propia memoria (ChromaDB+SQLite) que
  **no se habla con la memoria compartida** de este computador. Si se usa, debe
  **alimentarse de `...\memory\`**, no fundar un almacén paralelo. Dos memorias
  que no se conocen es peor que una sola.
- 🚦 **Ocho agentes del mismo modelo NO son ocho opiniones.** Crítica de Alejandro
  Téllez: *«la diversidad funcional puede ser solo aparente… pueden compartir
  errores de origen»*. La tensión entre funciones es un **mecanismo de control**,
  y hay que **diseñarla**: independencia, contradicción deliberada y trazabilidad
  de quién valida qué. → Implementar con [[kleper-cerebro-operador-contra]].
- 🚦 **El análisis no es la decisión.** Crítica de Julián Mac Loughlin: *«ocho
  agentes te devuelven ocho análisis bien fundados, y el trabajo real empieza
  justo después, cuando dos se contradicen y hay que elegir con información
  incompleta»*. **Un directivo rara vez falla por falta de análisis.** No prometer
  que el consejo decide.
- 🚦 **Costo:** cada consulta dispara varios agentes en paralelo → múltiplo de
  tokens. Estimar costo por consulta **antes** de desplegar.
- 🚦 **Modelos desactualizados en el repo:** usa `claude-sonnet-4-6`,
  `claude-opus-4-7` y Haiku 3.5. Los vigentes son **Opus 5, Sonnet 5, Haiku 4.5**
  → actualizar IDs antes de correr nada ([[selector-modelo-claude-optimo]]).
- 🚦 **Licencia:** Apache 2.0 **estándar verificada en el archivo `LICENSE`** (la
  API de GitHub reporta «Other», el README acierta). Uso comercial libre **con
  atribución**.

## Lecciones de mantenimiento (aplicables a nuestras skills)
- **El modo de fallo más común**: añadir comportamiento nuevo bajo un tema ya
  documentado **sin actualizar la documentación**. Ellos lo resuelven exigiendo
  que todo cambio material actualice también su ficha de arquitectura. → Para
  nosotros: **toda skill que cambie debe actualizar su línea en `MEMORY.md`**.
- **Nada de stubs**: solo código que funciona.
- **Datos de la empresa jamás en el repositorio.**

## Protocolo para construir un consejo propio
> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**
1. **Define los dominios** (no los agentes): ¿qué preguntas distintas hay que
   responder? Un dominio sin pregunta propia no merece agente.
2. **Registro desacoplado**: dominio → agente. Añadir uno no debe tocar el núcleo.
3. **Despacho paralelo** solo cuando varios dominios son relevantes de verdad.
4. **Committee obligatorio**: un pase adversarial antes de entregar. Sin él, el
   consejo solo multiplica confianza, no calidad.
5. **RAG**: base curada versionada + documentos propios. El recuperado va en el
   **turno del usuario**.
6. **Caché**: respetar el orden fijo y no meter nada dinámico en los bloques.
7. **Trazabilidad**: registrar **quién dijo qué y quién validó**. En el Alfa Lab
   eso es anclaje criptográfico en la IBPP (Pilar V).
8. **Cierre humano**: el consejo entrega análisis; **la elección y su consecuencia
   son del humano**. Escribirlo en el propio sistema.

## Aplicación a los expedientes
| Frente | Qué se cosecha |
|---|---|
| **Alfa Lab · Pilar IV** | Implementación de referencia del patrón Explorer/Builder/Critic/Tester. El **Committee** es literalmente el «Critic sin contexto compartido» del prompt DIRA-Alfa, ya funcionando. Sirve como evidencia ante CAF/UTEQ de que el patrón es viable. |
| **Alfa Lab · Pilar V** | Corre sobre **Ollama / LM Studio / vLLM** → Llama 3, DeepSeek o Mistral **on-premise** en la UTEQ, con ChromaDB y SQLite locales = soberanía de datos real. |
| **Cooperativa B5★ y PYMEs** | Su caso de uso declarado es «dirección senior para empresas sin C-suite» — describe a la cooperativa naciente y a Mobijuesa. |
| **War Room QVP** | 🚦 **No sustituir** lo existente: [[control-financiero-semanal-qvp]] y [[cfo-mensual-con-claude]] están afinados a cifras reales; un CFO genérico sería peor. |

## Cómo depurar si falla
- **Costo disparado** → casi siempre es la caché rota: buscar contenido dinámico
  dentro de un bloque con `cache_control`, o una persona interpolada.
- **Respuestas que se contradicen sin resolverse** → falta el pase del Committee.
- **El sistema «olvida»** → la memoria episódica no se está escribiendo o no se
  relee al arrancar.

## Portabilidad (revisar el 20% al reusar)
El patrón es agnóstico del framework. Cambian: los dominios, el almacén vectorial
y los IDs de modelo. Las reglas de caché y el Committee son lo estable.

## Reuso (no empezar de cero)
[[kleper-cerebro-operador-contra]] (la capa CONTRA = Committee) ·
[[graph-engineering-memoria-agentes]] (memoria persistente) ·
[[agentic-ai-hitchhiker-guide]] (las 5 capas del stack) ·
[[llm-como-funcionan-stanford-cs229]] (datos+evaluación+sistemas) ·
[[auditar-skills-antes-de-instalar]] · [[porter-estrategia-unico-no-mejor]].

## Ejemplos de invocación
- «Diseña el consejo de agentes del Alfa Lab con este patrón.»
- «¿Por qué se disparó el costo de mi agente?»
- «¿Adoptamos OpenExecutive o solo su arquitectura?»
