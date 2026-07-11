---
name: agentic-ai-hitchhiker-guide
description: |
  Doctrina técnica para construir agentes IA reales — destilada del paper
  «The Hitchhiker's Guide to Agentic AI: From Foundations to Systems»
  de Haggai Roitman (junio 2026, arXiv:2606.24937). Cubre las 5 capas
  del stack agentic: Foundation (Transformers + GPU + SFT/LoRA/MoE),
  Alignment & Reasoning (RLHF/PPO/DPO/GRPO + reward modeling + chain-of-
  thought + test-time scaling), Agentic Systems (RAG + Agentic RAG +
  memory systems + agent harness + design patterns), Multi-Agent (MCP +
  Agent skills + A2A protocol + topologías) y Deployment & Evaluation.

  Premisa central del autor: "construir grandes sistemas agentic
  requiere entender CADA capa del pipeline, no solo una". Esta skill
  es la doctrina que cualquier conversación nueva sobre construir
  agentes IA en este computador debe leer primero.

trigger_phrases:
  - "construir agente IA"
  - "diseñar sistema agentic"
  - "qué dice el hitchhiker guide"
  - "stack agentic completo"
  - "memory systems para agentes"
  - "agent harness"
  - "multi-agent coordination"

idioma_de_salida: español neutro técnico
nivel_madurez: especializada
fuente: paper arXiv:2606.24937 (Roitman, 2026-06-22) + paperswithcode.co/paper/2606.24937
---

# Hitchhiker's Guide to Agentic AI — Doctrina destilada

> "Building great agentic systems requires understanding every layer of
> the pipeline, not just one." — Haggai Roitman, 2026

## Las 5 capas del stack agentic

### 1. Foundation Layer — el sustrato LLM

- **Arquitectura Transformer** — atención multi-cabeza, encoder/decoder, paper «Attention Is All You Need» (arXiv:1706.03762, 181k citas).
- **GPU systems** — clústeres tipo XTX (25.000 GPUs) o universitarios; latencia y throughput de inferencia son cuellos reales.
- **Training**: **SFT** (Supervised Fine-Tuning) + **LoRA** (Low-Rank Adaptation, fine-tune barato) + **MoE** (Mixture of Experts, escalado eficiente).
- **Compression + inference optimization** — cuantización, distillation, pruning, KV-cache, batching dinámico.

### 2. Alignment & Reasoning Layer

- **RLHF** (Reinforcement Learning from Human Feedback) — el método clásico de InstructGPT/ChatGPT.
- **PPO** (Proximal Policy Optimization) — algoritmo RL estable.
- **DPO** (Direct Preference Optimization) — alternativa más simple que PPO sin reward model explícito.
- **GRPO** (Generative Reward Process Optimization) — variante reciente con foco en razonamiento.
- **Reward modeling** — qué se está optimizando importa más que el algoritmo.
- **RL for Large Reasoning Models** — entrenar reasoning específicamente (estilo o1/r1).
- **Chain-of-thought** — el modelo razona en pasos explícitos.
- **Test-time scaling** — gastar más cómputo en inferencia (best-of-N, beam search, tree search, self-consistency) para subir calidad.

### 3. Agentic Systems Layer

- **Agentic training + trajectory-based RL** — RL sobre trayectorias multi-step de uso de tools.
- **RAG** (Retrieval-Augmented Generation) — pegar contexto relevante antes de generar.
- **Agentic RAG** — el agente decide qué retrievar, cuándo y cómo.
- **Memory systems** — cuatro tipos no excluyentes:
  - *In-context*: dentro del prompt actual.
  - *External*: vector store, archivo, base de datos.
  - *Episodic*: recuerdo de eventos específicos (qué pasó, cuándo).
  - *Semantic*: conocimiento general organizado.
- **Agent harness** — la infraestructura que orquesta loops, tools, memoria.
- **Context management** — qué entra y qué sale del contexto activo (compactación, eviction, prioridades).
- **Agent design pattern taxonomy** — taxonomía de patrones recurrentes (ReAct, Plan-and-Execute, Reflexion, Tree-of-Thoughts, etc).

### 4. Multi-Agent Coordination

- **MCP** (Model Context Protocol) — protocolo de Anthropic para conectar agentes con tools y datos. Es lo que usan los `mcp__*` de este computador.
- **Agent skills + tool use** — skills como las que usamos aquí (function calling estructurado).
- **A2A** (Agent-to-Agent) communication protocol — agentes que se hablan entre sí.
- **Topologías**:
  - *Centralizada*: un orquestador que delega.
  - *Descentralizada*: agentes pares que negocian.
  - *Jerárquica*: árbol de mando con sub-agentes especializados.

### 5. Deployment & Evaluation

- **Development frameworks** — LangChain, LlamaIndex, AutoGen, CrewAI, Anthropic SDK, etc.
- **UI design** — chat, sidebar, embedded, API-first.
- **Evaluation methodology** — benchmarks, golden sets, A/B testing, traces, telemetría.
- **Production deployment** — observability, rate limiting, fallbacks, costos.

## 6. Capa de adopción práctica (lote LinkedIn fedphd, 2026-06-27)
Complemento aplicado a las 5 capas académicas, destilado de los guardados de LinkedIn de fedphd
([[reference-linkedin-ia-cognicion-lote-fedphd]]):
- **Mindset power-user (Tipo 1 vs Tipo 2)** — Kike Sanchis: el que usa la IA "como herramienta eléctrica"
  (atajos, config, features ocultas) construye ventaja; el que abre Claude y cierra la pestaña no.
  `activity:7476311006504329217`.
- **Validar antes de construir** — Javi Consuegra: gastar en web/logo/plan antes de validar la demanda es
  el error caro; construir el agente/producto **después** de probar que alguien paga. `activity:7467824949806792704`.
  (Su doctrina de autoría de skills ya vive en [[llave-maestra-autoaprendizaje-ia]].)
- **De IA general a agentes verticales/especializados** — Rafael Sansores: el valor migra del modelo
  genérico a versiones de dominio. `activity:7468407901540397056`.
- **El PC agéntico (hardware)** — Ivan Aradillas: "tu próximo portátil ejecutará agentes, no apps"
  (NVIDIA RTX Spark, 128 GB de memoria unificada) → evidencia práctica de [[era-pc-agentico-doctrina]].
  `activity:7467486493629005824`.
- **Gobernanza de IA en LATAM** — Angélica Castillo: marco peruano de IA; ancla el enfoque regulatorio
  para el expediente EcuaLedger. `activity:7460184880434360322`.

## Ejemplo de referencia real: Palantir (ontología + AIP + Apollo + FDE)
Del cuaderno NotebookLM «Palantir» ([[reference-cuaderno-palantir]]): materializa varias capas del
stack en producción — **Ontología** (gemelo digital = memoria *semantic* de la capa 3), **AIP**
(orquestación de LLMs/agentes anclados en hechos deterministas, anti-alucinación = capa 4), **Apollo**
(despliegue autónomo air-gapped por «tirón declarativo» = capa 5) y **Forward-Deployed Engineers**
(iteración en el frente = "retropropagación humana"). Lecciones de diseño: **GIGO** (la IA vale lo que
su ontología), **lock-in** de ontología (favorecer ontologías abiertas) y **data poisoning**
(mitigación criptográfica con hashes en blockchain). Plantilla operativa del [[reference_cuaderno_darpa|Alfa Lab]].

## Cómo se aplica a este computador

| Capa del paper | Implementación local | Ejemplo concreto |
|---|---|---|
| Foundation (LLM) | Claude Opus + Sonnet via Claude Code | El modelo que está leyendo este texto |
| Alignment | Skills + compuertas 🚦 | `llave-maestra-autoaprendizaje-ia` impone Pareto+persistencia |
| Agentic Systems | Skills + MEMORY.md + `analizar_query.py` | El bucle X.com bookmarks → autoreflex → skills `intereses-*` |
| Multi-Agent | MCP servers conectados + skills hijas | `mcp__Claude_in_Chrome__*`, `mcp__be6ee3c8...gmail__*` |
| Deployment | venv `~/.notebooklm-venv` + scheduled tasks | Watcher autostart, fetch_share.py via Edge debug |

## Compuertas 🚦

1. **No usar test-time scaling ciegamente** — gasta tokens; reservar para problemas donde la calidad importa más que la latencia.
2. **No mezclar memory types sin etiquetar** — confusión clásica: meter conversación reciente como "semantic" cuando es "episodic".
3. **No abusar de Agentic RAG cuando RAG simple basta** — el agente decidiendo "cuándo retrievar" añade un loop más; medir si la ganancia justifica el costo.
4. **MCP es la lingua franca** — diseñar nuevas integraciones como servidores MCP siempre que sea posible, no como adapters ad-hoc.
5. **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

## Cómo depurar si la doctrina falla

- Si un agente pierde el hilo: revisar context management (capa 3).
- Si las respuestas son alucinaciones: revisar reward model + alignment (capa 2).
- Si el agente no usa la tool correcta: revisar tool registration + skills (capa 4).
- Si no escala en producción: revisar deployment + observability (capa 5).

## Citas y artículos relacionados

- **Attention Is All You Need** — arXiv:1706.03762 (181k citas)
- **Language Models are Few-Shot Learners** — arXiv:2005.14165 (59k citas, GPT-3)
- **RoBERTa** — arXiv:1907.11692 (30k citas)
- **Communication-Efficient Learning of Deep Networks from Decentralized Data** — arXiv:1602.05629 (24k citas, Federated Learning)

## Relacionado

- [[llave-maestra-autoaprendizaje-ia]] — esta es su capa teórica.
- [[agente-local-autoreflexivo-bookmarks]] — instancia local del bucle agentic.
- [[entrenador-experto-notebooklm-ecualedger]] — suite de orquestación.
