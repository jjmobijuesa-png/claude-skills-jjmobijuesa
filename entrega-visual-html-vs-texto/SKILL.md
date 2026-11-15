---
name: entrega-visual-html-vs-texto
description: |
  Doctrina de ENTREGA del agente local: el cuello de botella invisible al usar IA no
  es el modelo ni el prompt, es CÓMO se entrega el resultado. Texto plano para PENSAR
  e iterar; HTML/visual interactivo para VER, entender y compartir (un tercio del
  cerebro es "máquina de ver"). Decide el formato según la fase, no por defecto.
trigger_phrases:
  - "entrégamelo visual"
  - "pásalo a HTML"
  - "hazlo visual / interactivo"
  - "informe bonito para compartir"
  - "¿texto o visual?"
  - "preséntalo para decidir / para el jefe / para el cliente"
idioma_de_salida: español
nivel: aplicada
dominio: meta / entrega-de-resultados
metadata:
  version: 1.0
  fecha: 2026-06-27
  origen: YouTube playlist "IA" de jjmobijuesa, video 5Uh2yRLCisk ("Anthropic revela el TRUCO…") — artículo de Tarik (Anthropic) + Andrej Karpathy
  fuente: https://www.youtube.com/watch?v=5Uh2yRLCisk
  relacionada: era-pc-agentico-doctrina, auditoria-cognitiva-reflexiva, documentos-encuadrados-margenes
---

# Skill `entrega-visual-html-vs-texto`

## Acerca de mí (cargar al arrancar)
Lee `...\memory\user_role.md` y `MEMORY.md`. Esta es una **doctrina de cómo entrega resultados el
agente local autorreflexivo** de este computador, no una tarea puntual.

## Doctrina central
Llevamos años mejorando *cómo hablarle* a la IA (prompts, contexto). El salto que casi nadie aplica
es optimizar **cómo recibimos** lo que genera. **Un tercio del cerebro es "máquina de ver"**
(Karpathy): la visión es una autopista de 10 carriles; entregar texto plano es meter todo el tráfico
por un carril bici. El **formato de entrega es el cuello de botella invisible** — no el modelo, no el
prompt. Tres niveles de ventaja del formato visual/HTML: (1) **estética/profesional**; (2)
**comprensión** (diagramas SVG, pestañas, timelines, tarjetas, semáforos de riesgo se entienden mucho
mejor que 150 líneas de texto que nadie lee entera); (3) **compartir** (se abre en cualquier
navegador/móvil, PDF en un clic, enlace; "la información que no se comparte bien no se usa").

## 🚦 Actualización 14-nov-2026: hay TIPOS, ya no sólo HTML a mano

La doctrina de arriba sigue siendo correcta —el formato de entrega es el cuello
de botella— pero **su implementación quedó una generación atrás**. Verificado
contra esta cuenta el 14-nov-2026: hay **7 tipos de Artifact publicados**, y
varios hacen mejor que una página escrita a mano lo que antes se escribía a mano.

**La regla nueva, en una línea: si existe un tipo para lo que va a entregar, no
se escribe HTML a mano.**

| Si va a entregar… | Tipo | En vez de |
|---|---|---|
| Tablero, KPIs, informe recurrente de cifras | **Data** | Un HTML de gráficos hecho a mano |
| Tabla, seguimiento, presupuesto que alguien va a llenar | **Sheets** | Un `.xlsx` suelto, salvo que pidan el archivo |
| Presentación | **Slides** | Un `.pptx` o láminas HTML |
| Memo, informe o plan que se seguirá editando | **Docs** | Un `.docx` suelto |
| Lluvia de ideas, mapa, relaciones a mover | **Whiteboard** | Un diagrama estático |
| Landing, maqueta, pieza visual | **Design** | HTML a mano |

**Ventaja que no se ve a simple vista:** en el tipo **Data**, cada número muestra
de dónde salió. Eso es trazabilidad por construcción, y es exactamente lo que
pide [[auditoria-evidencia-cuatro-niveles]] y [[segundo-cerebro-anclaje-verificable]].

### 🚦 Lo que NO se migra

- **Las clases magistrales del Aula.** Son 48 HTML en 11 carpetas con casa de
  estilo propia en su `DESIGN.md` y viven como archivos en Drive. Son un corpus
  deliberado, no un entregable suelto. Siguen escribiéndose a mano.
- **Lo que el usuario pida como archivo.** Si dice «dame el `.xlsx`» o «el
  `.html`», se entrega el archivo. El tipo no es un atajo para no obedecer.
- **Nada va a carpetas compartidas** (vale igual aquí): ver
  [[estilo-entregables-publicos-fbse]].

### Lo que NO tiene esta cuenta, aunque circule en redes

Comprobado el 14-nov-2026, a propósito de una infografía de terceros sobre
«5 herramientas nuevas de Claude»:

- **Claude Meetings** es de planes Team y Enterprise. Este es un plan Pro. Lo que
  sí hay es un **conector de reuniones** por MCP, que es otra cosa y ya funciona.
- **Conectores de Adobe**: las skills están, pero **el servidor pide autorización**
  (`/mcp`). **Atlassian** no aparece en esta instalación.

**Mecanismo, que es lo que transfiere:** una infografía de LinkedIn no establece
qué tiene su cuenta. **Se comprueba listando los tipos**, igual que la
disponibilidad de un modelo se comprueba con `/model` y no con un hilo viral.
Mismo criterio que [[cosechar-repositorios-de-agentes]] y
[[regla-del-primer-tropiezo]].

## Criterio: cuándo SÍ y cuándo NO (analogía RAW/JPG) — 🚦 no devolver visual por defecto
Como un fotógrafo dispara en **RAW para trabajar** y exporta **JPG para entregar**:
- **Texto plano (RAW) = para PENSAR e ITERAR:** rápido, barato, fácil de editar. Úsalo mientras se
  exploran ideas, se ajustan supuestos, se corrige.
- **HTML/visual (JPG) = para VER, ENTENDER y COMPARTIR:** cuando hay un resultado/punto clave que el
  humano debe **revisar, decidir o enseñar a otro** (jefe, cliente, comité, Directorio).
- El HTML **también es herramienta de iteración**: muéstralo como panel, detecta incoherencias que en
  texto no se ven (huecos, solapes), y pide iterar sobre el propio HTML.

## Protocolo
> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**
1. **Detecta la fase:** ¿el usuario está pensando/iterando (→ texto) o necesita ver/decidir/compartir (→ visual)?
2. **Si visual:** genera un artefacto HTML interactivo con `mcp__visualize__show_widget` (dashboards, diagramas, tablas, formularios) o la skill **anthropic-skills:web-artifacts-builder** para apps/HTML autocontenido; usa SVG para diagramas de flujo, pestañas para fases, timeline horizontal, tarjetas de métricas y **semáforos** (rojo/ámbar/verde) para riesgos.
3. **Para imprimir/enviar formal:** Word/PDF encuadrado con **documentos-encuadrados-margenes**; "PDF en un clic".
4. **Itera en el medio elegido** hasta que el humano decida; recién entonces exporta el entregable final.

## Aplicación al agente local autorreflexivo
Cuando el agente entregue **análisis financieros (QVP), informes al Directorio, planes (Alfa Lab),
defensas/Q&A, comparativos o tableros**, y un humano deba revisarlos/decidir → **HTML visual** (no
muro de texto). En **modo IA-AUTO / razonamiento interno** → texto. Esto reduce la curva de lectura
humana (alineado con la doctrina de "prompt de la IA para la IA").

## Qué NO hacer / compuertas 🚦
- 🚦 No entregar SIEMPRE visual: malgasta tokens y entorpece la iteración. El criterio manda.
- No incrustar datos sensibles en HTML que se vaya a compartir sin autorización.
- No sustituir la verdad por estética: el visual debe reflejar fielmente los datos (sin maquillar cifras).

## Cómo depurar si falla
Si el visual confunde más que el texto, casi siempre es exceso de adornos o mala jerarquía → simplifica
(una idea por bloque, semáforos, jerarquía clara). Si el humano sigue sin leerlo, pregúntale qué
decisión necesita tomar y diseña el visual alrededor de ESA decisión.

## Portabilidad / Reuso
Implementación estable: `show_widget` (visualize) + `web-artifacts-builder` + `documentos-encuadrados-margenes`.
Encaja con [[era-pc-agentico-doctrina]] (el agente como nueva app) y [[auditoria-cognitiva-reflexiva]]
(humano-en-el-bucle: el visual existe para que el humano DECIDA mejor).

## Ejemplos de invocación
- «Este análisis de QVP pásalo a un tablero HTML con semáforos para el comité.»
- «Estoy iterando el plan; déjamelo en texto y solo cuando cerremos, hazlo visual.»
- «Convierte el plan de migración en un HTML con diagrama SVG, pestañas por fase y timeline.»
