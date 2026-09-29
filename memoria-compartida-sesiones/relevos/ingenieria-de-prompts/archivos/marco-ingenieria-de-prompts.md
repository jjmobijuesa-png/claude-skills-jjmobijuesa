# Marco provisional — hilo «Ingienería de prompts»

_Autor: espejo en la nube, 2026-09-28 22:01 (Guayaquil). **Provisional:** la PC aún no ha volcado
nada. El tema real lo confirma la PC; este marco solo ordena las hipótesis._

## 0. Punto de partida: las 4 skills candidatas (según `ESTADO.md`, sin confirmar)

| Skill | Qué aporta a la ingeniería de prompts | Pregunta que responde |
|---|---|---|
| `prompting-opus-5-doctrina` | Doctrina del **QUITAR** (sin «verifica/doble-chequea», sin «no pienses»), control de longitud, cadencia, alcance y delegación; bloques de prompt canónicos; `references/system_prompt_base_opus5.md` | **¿Cómo** se le escribe al modelo? |
| `selector-modelo-claude-optimo` | Emparejar dificultad real ↔ modelo (Haiku / Sonnet / Opus / Fable) + palanca de esfuerzo; regla: el agente recomienda, el usuario decide | **¿A qué** modelo y con qué esfuerzo? |
| `eficiencia-generacion-respuestas` | Entregar el DELTA, reutilizar, no releer archivos grandes, verificar por muestreo | **¿Cuánto** debe producir la respuesta? |
| `llave-maestra-autoaprendizaje-ia` | Protocolo de 6 pasos para destilar una fuente y codificarla como skill; 7 principios de autoría | **¿Cómo se archiva** lo aprendido? |

Relación: las cuatro ya se enlazan entre sí (la doctrina Opus 5 cita a las otras tres). Juntas
forman una cadena: **elegir modelo → escribir el prompt → acotar la salida → archivar el aprendizaje**.
Adyacente: `metodo-mit-notebooklm-riguroso/PROMPTS_LITERALES.md` (prompts de uso, no de doctrina).

## 1. Posible alcance (hipótesis, elegir una o combinar)

| Opción | Qué sería el hilo | Entregable probable |
|---|---|---|
| **A. Skill maestra de prompting** | Unificar las 4 en una doctrina de ingeniería de prompts (con enlaces, sin duplicar contenido) | Skill nueva o índice-orquestador + actualización de enlaces en la red |
| **B. Biblioteca de prompts** | Plantillas reutilizables por tipo de tarea (informe financiero, análisis Excel, código, estudio) aplicando la doctrina | Carpeta de plantillas `.md` + guía de uso |
| **C. Auditoría de prompts existentes** | Revisar `PROMPT-pc.md`, `PROMPT-espejos.md`, `PROMPT-agente-local.md` y system prompts propios con la doctrina del QUITAR | Informe de hallazgos + versiones corregidas |
| **D. Migración a Opus 5 / modelo 5.x** | Pasar prompts escritos para 4.x al comportamiento nuevo (concisión, alcance, sin sobre-verificación) | Tabla antes/después por prompt |
| **E. Actualización de las skills** | Refrescar precios/IDs/modelos (la doctrina pide verificar en `claude-api`, no de memoria) y cerrar brechas | Commits sobre las 4 skills |

Fuera de alcance por defecto: datos financieros reales (rige `gobernanza-datos-financieros-ia`);
temas de otros hilos (flujo de caja, financial report, estudios generales).

## 2. Qué debe volcar la PC (primer volcado en caliente)

En `ESTADO.md`, para un lector que no vio la conversación:
1. **Tema confirmado** en una línea y cuál de las opciones A–E (u otra) es.
2. **Archivo principal**: ruta local + resumen de qué contiene y qué se concluyó (sin copiar el fuente si es sensible).
3. **Razonamiento en curso**: decisiones tomadas, hipótesis descartadas, qué skills se tocan.
4. **Prompts en trabajo**: si son no sensibles, pueden ir completos como `.md` en `archivos/`;
   si contienen datos de clientes/empresa, solo ruta + resumen.
5. **Fuentes** usadas (guía oficial, Perplexity, NotebookLM, etc.) con enlace o ruta.
6. **Siguiente paso exacto** y la hora del checkpoint; fila en `HISTORIAL.md`.

## 3. Preguntas abiertas para Francisco

1. ¿Cuál es el objetivo del hilo: una skill (A), una biblioteca de plantillas (B), auditar prompts (C), migrar (D), actualizar skills (E) u otro?
2. ¿Para qué modelos y superficies son los prompts: Claude Code (PC/nube), claude.ai, API, NotebookLM, Perplexity?
3. ¿Los prompts son para uso personal, para Mobijuesa/Quevepalma o para enseñar/compartir? (define tono, idioma y si pueden publicarse).
4. ¿Hay un archivo principal ya iniciado en la PC? ¿Dónde está?
5. ¿El resultado se integra en las skills existentes o nace una skill nueva (y con qué nombre)?
6. ¿Se corrige la grafía del hilo («Ingienería» → «Ingeniería») en títulos y registros? La carpeta ya usa `ingenieria-de-prompts`.

## 4. Siguiente paso del espejo (si el usuario sigue aquí sin volcado de la PC)
Esperar la respuesta a §3.1. Con esa respuesta, el espejo puede avanzar sin la PC en C, D o E
(todo el material está en el repo); en A o B conviene el volcado de la PC para no duplicar trabajo.
