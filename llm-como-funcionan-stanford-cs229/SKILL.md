---
name: llm-como-funcionan-stanford-cs229
description: >-
  Cómo funcionan realmente los LLM (Stanford CS229, Yann Dubois): lo decisivo no
  es la arquitectura sino DATOS + EVALUACIÓN + SISTEMAS; pre vs post-entrenamiento;
  leyes de escala empíricas; y por qué la alucinación puede nacer en el SFT.
  Invocar al diseñar IA local soberana, evaluar modelos o explicar LLM a terceros.
trigger_phrases:
  - "cómo funciona realmente ChatGPT"
  - "pre-entrenamiento vs post-entrenamiento"
  - "leyes de escala"
  - "por qué alucinan los modelos"
  - "RLHF / SFT"
  - "IA local soberana del Alfa Lab"
idioma_de_salida: español
nivel_de_madurez: especializada
dominio: agentes-ia / fundamentos
fuente:
  - "Stanford CS229 Machine Learning — clase invitada «Building Large Language Models», Yann Dubois (2024). YouTube I58zjMMG2pA; transcripción íntegra (19.512 palabras) en E:\\vars\\var 5\\YouTube-jjmobijuesa\\transcripciones\\_manuales\\I58zjMMG2pA__I58zjMMG2pA.md"
  - "Bookmark @fdc_ec (❤27.686, el más votado del corpus): https://x.com/AnatoliKopadze/status/2057105488165163198"
  - "Material de estudio: E:\\vars\\var 5\\Clases-Magistrales-HTML\\08-stanford-como-funcionan-los-llm.html"
---

## Acerca de mí (cargar al arrancar)
Leer `...\memory\user_role.md` + `MEMORY.md`. Complementa a
[[winston-representacion-restricciones-ia]] (qué **es** la IA) y a
[[agentic-ai-hitchhiker-guide]] (el stack agentic completo). Aplica al **Pilar V**
de [[project_alfalab_uteq]] (IA local soberana anclada criptográficamente).

## Doctrina central
Un **LLM = modelo de la distribución de probabilidad sobre secuencias de tokens**.
Es **autorregresivo**: predice el siguiente token, se condiciona a él y repite.
El ejemplo de la clase: «el ratón se comió el queso» (probable) · «el el ratón
comió queso» (falla sintáctica) · «el queso se comió al ratón» (falla semántica).

**Los 5 componentes al entrenar:** arquitectura · pérdida y algoritmo · **datos**
· **evaluación** · **sistemas**.
> «La academia se concentra en arquitectura y algoritmos… pero **en la práctica lo
> que importa son los otros tres: datos, evaluación y sistemas**.»

**Dos mitades:** *pre-entrenamiento* (modelar todo internet → GPT-2/GPT-3) y
*post-entrenamiento* (convertirlo en asistente → SFT + RLHF → ChatGPT).

**Leyes de escala:** más datos + modelo más grande = mejor, y **cuánto mejor es
predecible** (lineal en escala log). Aquí **no aparece el sobreajuste**.

## Qué NO hacer / compuertas 🚦
- 🚦 **No presentar las leyes de escala como teoría.** Son **empíricas**: «no hay
  nada teórico en ello». Sin evidencia de meseta próxima, pero probablemente
  llegará y **no se sabe cuándo**. Nunca proyectar capacidades futuras como hecho.
- 🚦 **No proponer entrenar un LLM desde cero** para el Alfa Lab: sin datos ni
  cómputo a esa escala es una fantasía cara. El terreno real es el
  **post-entrenamiento** sobre modelos abiertos.
- 🚦 **No prometer «IA sin alucinaciones».** La hipótesis de la clase es que la
  alucinación puede ser **estructural del SFT** → el control real es verificación
  formal + trazabilidad, no una promesa de exactitud.
- 🚦 **No optimizar contra el modelo de recompensa** sin vigilar la
  **sobreoptimización** (aprender a agradar al juez en vez de acertar).
- 🚦 No copiar la broma del profesor fuera de contexto: el sobreajuste **sí existe**
  en aprendizaje automático clásico.

## El hallazgo que más importa: origen de la alucinación
En el **SFT** se entrena con pocas respuestas ideales y **el modelo no aprende
nada nuevo**. Si el humano escribe una respuesta que contiene algo que el modelo
**nunca vio en el pre-entrenamiento** (p. ej. una referencia bibliográfica real),
desde la perspectiva del modelo se le está enseñando a **producir algo que suene
plausible sin saber si es cierto**. → Aprende el hábito de inventar con confianza,
**aunque todos los datos de entrenamiento sean correctos**.

**Consecuencia operativa para EcuaLedger:** la compuerta contra alucinación en
smart contracts deja de ser un temor genérico y pasa a tener mecanismo: por eso
son obligatorias la **verificación formal** antes de desplegar y el **anclaje
criptográfico** de cada inferencia (modelo + pesos + prompt + salida) en la IBPP.

## Protocolo de uso
> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**
1. Ante una decisión de IA, clasifica: ¿es problema de **datos**, de **evaluación**
   o de **sistemas**? (Rara vez es de arquitectura.)
2. Si se busca capacidad soberana: trabajar en **post-entrenamiento** sobre modelo
   abierto con corpus propio (notarial, agrícola, jurídico ecuatoriano).
3. Construir **evaluación propia** antes que modelo propio: el benchmark es el
   activo diferenciador ([[seelig-activo-invisible-reencuadre]]).
4. Toda inferencia que produzca efecto jurídico → **trazabilidad on-chain**.

## Cómo depurar si falla
Si el modelo ajustado inventa datos, revisa el conjunto de SFT: probablemente
contiene afirmaciones que el modelo base no podía conocer.

## Portabilidad (revisar el 20% al reusar)
Doctrina técnica estable; cambian los nombres de modelos y las cifras de escala.
Lo local: la ruta de la transcripción.

## Reuso (no empezar de cero)
[[agentic-ai-hitchhiker-guide]] · [[graph-engineering-memoria-agentes]] ·
[[winston-representacion-restricciones-ia]] · [[selector-modelo-claude-optimo]] ·
[[era-pc-agentico-doctrina]].

## Ejemplos de invocación
- «Explícame para el comité cómo funciona realmente ChatGPT.»
- «¿Entrenamos un modelo propio en el Alfa Lab o hacemos post-entrenamiento?»
- «¿De dónde salen las alucinaciones y cómo las controlamos?»
