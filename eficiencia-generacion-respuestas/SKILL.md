---
name: eficiencia-generacion-respuestas
description: |
  Doctrina de EFICIENCIA en la generación de respuestas: resolver cada prompt por el camino que
  consume menos tokens y menos pasos sin sacrificar calidad. Regla central: producir solo el DELTA que
  el usuario necesita (la sección/cuadro/archivo que cambia), no regenerar documentos completos;
  reutilizar artefactos ya creados; evitar releer archivos grandes; y entregar piezas integrables en
  vez de rehacer todo. Útil en cualquier tarea larga o iterativa con archivos pesados.
  Triggers: "solo esa parte", "para ahorrar tokens", "no regeneres todo", "hazme el cambio puntual",
  "entrega solo la sección", "camino más eficiente".
user-invocable: true
metadata:
  version: 1.0
  fecha: 2026-06-28
  origen: sugerencia del usuario (editar solo la subsección «Hipótesis técnica» del informe QVP)
---

# Skill `eficiencia-generacion-respuestas`

Hacer lo justo, bien, con el mínimo gasto. La calidad no se negocia; el desperdicio sí.

## Reglas de oro (en orden de impacto)
1. **Entrega el DELTA, no el todo.** Si el usuario revisa un documento y pide cambiar una parte,
   produce SOLO esa parte (sección, cuadro o página) en un archivo aparte «… para integrar», listo
   para pegar — no reconstruyas el informe entero.
2. **Reutiliza lo ya hecho.** Antes de re-investigar o re-extraer, revisa memoria, referencias y
   artefactos previos. Datos ya obtenidos (precios, bookmarks, dumps) no se vuelven a pedir.
3. **No releas archivos grandes.** Para Excel/JSON/PDF pesados, extrae solo el rango/hoja/celdas que
   importan a un `.txt` y lee eso; nunca el binario completo ni los 7 MB del bookmarks.json.
4. **Verifica con muestreo, no exhaustivo.** Renderiza 1–3 páginas representativas, no todas.
5. **Lotea operaciones independientes** en una sola tanda (varias herramientas en un mensaje).
6. **Evita el adorno.** Sin recapitular lo ya establecido, sin opciones que no se van a tomar, sin
   relectura "de confirmación" de algo que la herramienta ya validó.
7. **Texto para iterar; visual solo para decidir/compartir** (ver [[entrega-visual-html-vs-texto]]).

## Anti-patrones (evitar)
- Regenerar un DOCX/PDF de 15 páginas para cambiar un párrafo.
- Volver a buscar en la web algo que ya está en una referencia de memoria.
- Leer un archivo completo cuando basta una hoja o un encabezado.
- Repetir el contexto del proyecto en cada respuesta.

## Criterio de decisión
Antes de actuar, preguntar: «¿cuál es la pieza mínima que resuelve esto y cómo la entrego ya lista
para usar?». Si el usuario puede integrar manualmente un fragmento pequeño, esa casi siempre es la
ruta más barata y más rápida. Cuando convenga, ofrecer esa opción explícitamente.
