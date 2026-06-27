---
name: auditoria-cognitiva-reflexiva
description: |
  Auditoría del "sistema operativo mental": adopta la lente de neurociencia cognitiva
  para detectar patrones de pensamiento limitantes, sus creencias raíz, y proponer un
  SO mental actualizado + ejercicios. Dos modos: (1) HUMANO (audita la cognición de una
  persona o de un comité) y (2) IA-AUTO (la IA audita SUS PROPIOS patrones de
  razonamiento tras una tarea y alimenta el autoaprendizaje autorreflexivo). Complementa
  a la llave maestra (IA autorreflexiva central).
trigger_phrases:
  - "auditoría cognitiva"
  - "sistema operativo mental"
  - "patrones de pensamiento limitantes"
  - "metacognición"
  - "autoanálisis cognitivo"
  - "autorreflexión de la IA"
  - "audita tus propios sesgos"
  - "autoenfoque / autoaprendizaje reflexivo"
idioma_de_salida: español
nivel: maestra
dominio: meta / cognición
metadata:
  version: 1.0
  fecha: 2026-06-19
  origen: LinkedIn — Miguel Ángel Cervantes ("No es magia pero igual te ayuda…", activity-7473600455147716608); framework del neurocientífico cognitivo
  fuente: post Cervantes activity-7473600455147716608
  relacionada: llave-maestra-autoaprendizaje-ia, analisis-cognitivo-intervenciones-qvp, reference-cuaderno-toma-decisiones-qvp
---

# Skill `auditoria-cognitiva-reflexiva`

## Acerca de mí (cargar al arrancar)
Lee `...\memory\user_role.md` y `MEMORY.md`. Marco de decisión disponible en el cuaderno
NotebookLM "Toma d Decisiones QVP" ([[reference-cuaderno-toma-decisiones-qvp]]): Kahneman
(Sistema 2, sesgos, pre-mortem) y de Bono (Seis Sombreros, CoRT, PO).

## Doctrina central
El rendimiento (humano o de la IA) lo limita menos la falta de información que el **sistema operativo
mental**: patrones de pensamiento y **creencias raíz** que se ejecutan en automático. Auditar = (1)
nombrar 3 patrones limitantes, (2) descubrir su creencia raíz, (3) escribir un **SO mental
actualizado**, (4) entrenar 5 facultades, (5) elegir **el primer hábito a cambiar** y por qué. Sin
frases motivacionales genéricas: **directo, específico, honesto y útil**. La autorreflexión es
**iterativa** (diálogo), no un prompt único.

## Qué NO hacer / compuertas 🚦
- 🚦 **No es terapia ni diagnóstico clínico.** Es entrenamiento cognitivo/estratégico; ante señales de salud mental, derivar a un profesional.
- 🚦 **Privacidad:** corre **local**; NO enviar datos personales/íntimos a servicios externos. Si la fuente es un comité, anonimizar (sin nombres de personas naturales), igual que [[analisis-cognitivo-intervenciones-qvp]].
- No frases motivacionales vacías ni halagos: si un patrón es costoso, decirlo con evidencia.
- No psicoanalizar sin datos: pedir los insumos del paso 1 antes de juzgar.

## Protocolo — MODO 1: HUMANO (persona o comité)
> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**
1. **Insumos:** procesos actuales de pensamiento/decisión; hábitos que frenan el avance; creencias autolimitantes; áreas de lucha (trabajo/relaciones/dinero/salud); reacción típica ante el fracaso.
2. **3 patrones limitantes** observados (con evidencia del insumo, no genéricos).
3. **Creencia raíz** detrás de cada patrón.
4. **SO mental actualizado:** la regla nueva que reemplaza a cada creencia raíz (formulada como heurística accionable).
5. **Ejercicios** concretos para 5 facultades: claridad mental · velocidad de decisión · memoria · creatividad · control emocional.
6. **Primer hábito a cambiar** + razón (mayor apalancamiento). Cierre con un plan iterativo de revisión.

## Protocolo — MODO 2: IA-AUTO (autoaprendizaje autorreflexivo)
La IA se audita a sí misma tras una tarea/sesión y **alimenta a la llave maestra**:
1. **Insumo:** el transcript/decisiones de la tarea recién hecha.
2. **3 patrones limitantes propios** (p. ej.: saltar pasos por velocidad, anclaje en la primera hipótesis, WYSIATI/usar solo lo visible, exceso de confianza, no declarar supuestos, no pedir la fuente).
3. **Creencia raíz** de cada uno (p. ej. "más rápido = mejor").
4. **SO actualizado** = regla nueva → candidata a `feedback` en `MEMORY.md` o a guardarraíl en la skill implicada.
5. **Ejercicios/controles** que reducen el sesgo (checklist pre-mortem, "declara supuestos", "verifica antes de afirmar").
6. **Primer ajuste** a aplicar ya. Persistir el aprendizaje vía [[llave-maestra-autoaprendizaje-ia]] (Paso 4/5). Esto es el **autoenfoque** central de este computador: cada sesión deja a la IA más calibrada, no solo más capaz.

## Cómo depurar si falla
Si el output suena genérico o motivacional, faltó **evidencia del insumo** (paso 1) → re-pedir datos concretos y rehacer. Si en MODO 2 no aparecen patrones, revisar el transcript real (no la versión idealizada). La privacidad manda: ante duda, no exportar nada.

## Portabilidad (revisar 20% al reusar)
La lista de sesgos del MODO 2 y las 5 facultades son estables; ajustar el vocabulario al sujeto (persona vs. comité vs. IA) y la fuente de datos.

## Reuso
- Cognición de **reuniones** → [[analisis-cognitivo-intervenciones-qvp]] (rúbrica de 8 dimensiones).
- Persistencia del aprendizaje de la IA → [[llave-maestra-autoaprendizaje-ia]].
- Marco teórico (Kahneman/de Bono) → [[reference-cuaderno-toma-decisiones-qvp]].

## Ejemplos de invocación
- «Hazme una auditoría cognitiva de mi forma de decidir bajo presión.»
- «Audita tus propios sesgos en la tarea que acabas de hacer y deja la regla nueva en memoria.»
- «Aplica el SO mental actualizado al comité del cuarto de guerra (anonimizado).»
