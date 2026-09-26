---
name: cierre-verificado-integridad
description: >
  Disciplina de cierre que se aplica SIEMPRE al terminar una respuesta que tocó
  un modelo, libro o entregable: (1) verificar la integridad de lo actualizado
  (controles en 0, totales, escenario de prueba, sin procesos huérfanos), (2)
  crear o actualizar la skill pertinente, (3) integrarla a la memoria compartida.
  Un cierre sin estos tres pasos está incompleto.
metadata:
  type: feedback
---

# Cierre verificado (integridad · skill · memoria)

Instrucción permanente de Francisco Duque: **ninguna respuesta que modifique un
modelo o entregable se da por terminada sin cerrar estos tres pasos.** El cierre
mismo es la skill.

**Por qué:** un cambio sin verificar puede romper controles en silencio; un
hallazgo que no deja skill se repite; una skill que no entra a la memoria no se
recuerda en la próxima sesión.

## Cómo aplicarla

1. **Integridad de lo actualizado.**
   - Reabrir el libro con `CalculateFull()` y leer los **controles que deben dar 0**
     (ingresos vs. consolidador, obra vs. presupuesto, intereses vs. costo
     financiero, capital vs. monto) y los **totales** clave (ventas, utilidad).
   - **Escenario de prueba:** cambiar una variable independiente, comprobar que lo
     dependiente se recalcula, y **revertir** (ver [[modelo-excel-sistema-vivo]]).
   - Confirmar que no quedaron **procesos huérfanos** (`EXCEL.EXE`) y que hubo
     **respaldo previo** de cada escritura.
   - Reportar los números y las banderas (🚦) al usuario, sin adornos.
2. **Skill pertinente.** Codificar el hallazgo nuevo como skill en
   `~/.claude/skills/<nombre>/SKILL.md` o actualizar la existente
   ([[llave-maestra-autoaprendizaje-ia]]): buscar por MECANISMO, no por síntoma.
3. **Memoria compartida.** Registrar en `…/memory/` (proyecto o feedback) y añadir
   la línea de una sola frase en `MEMORY.md` y, si es skill nueva, en
   `skills_index.md`. Convertir fechas relativas a absolutas.

## Firma del incumplimiento

Entregar un libro «ya está» sin haber leído sus controles; cerrar sin escenario de
prueba; dejar un `EXCEL.EXE` colgado; o resolver algo nuevo y no dejar ni skill ni
memoria. Enlaza con [[regla-del-primer-tropiezo]] y [[eficiencia-generacion-respuestas]].
