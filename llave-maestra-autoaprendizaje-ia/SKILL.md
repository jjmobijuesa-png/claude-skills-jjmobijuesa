---
name: llave-maestra-autoaprendizaje-ia
description: |
  LLAVE MAESTRA DE AUTOAPRENDIZAJE de la IA que habita este computador.
  Esta skill convierte a Claude en un agente de mejora continua que, en cada
  conversación, detecta brechas de conocimiento o habilidad, busca fuentes
  autorizadas (Perplexity, NotebookLM, web, documentos locales, MCPs
  conectados), destila el 20% del corpus que entrega el 80% del dominio
  práctico (regla de Pareto), y CODIFICA el aprendizaje como una nueva skill
  archivada en `C:\Users\datos\.claude\skills\` o como actualización de una
  skill existente. El resultado es una IA personal local que crece, se
  retroalimenta y se vuelve más capaz con cada ciclo.

  Esta skill nace del primer chat-guía de autoaprendizaje alojado en
  Perplexity (hilo "guía de autoaprendizaje de la IA",
  ID e21b0957-a5fe-4880-aad3-bedf29205bb1, cuenta mobijuesa JJ), cuya
  hoja de ruta original era para que un humano aprendiera IA. Aquí se
  invierte la dirección: la IA aprende para sí misma y se mejora.

  Casos de uso:

  - El usuario pide hacer algo que no existe como skill: invocar esta
    llave maestra para crear la skill faltante y dejarla archivada.
  - El usuario menciona una herramienta, MCP, dominio técnico o flujo
    de trabajo recurrente sin skill propia: invocar para registrarla.
  - El usuario solicita un ciclo periódico de "auto-revisión de skills"
    para detectar habilidades obsoletas, redundantes o ausentes.
  - El usuario quiere que Claude consulte Perplexity (vía Chrome MCP)
    o NotebookLM como fuente externa de aprendizaje y traiga
    conclusiones destiladas a una skill local.
  - El usuario solicita explícitamente: "actualiza tu llave maestra",
    "aprende esto y archívalo", "vuélvete mejor en X", "crea una skill
    nueva para Y".

trigger_phrases:
  - "llave maestra de autoaprendizaje"
  - "aprende esto y archívalo como skill"
  - "vuélvete mejor en"
  - "crea una skill nueva para"
  - "auto-revisión de skills"
  - "actualiza tu propio aprendizaje"
  - "destila esto como una skill"
  - "consulta Perplexity y conviértelo en skill"
  - "autoaprendizaje IA"

idioma_de_salida: español neutro técnico-instruccional

skills_carpeta_local: C:\Users\datos\.claude\skills
memory_indice_local: C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\MEMORY.md
perplexity_hilo_origen: https://www.perplexity.ai/search/e21b0957-a5fe-4880-aad3-bedf29205bb1
---

# Llave Maestra de Autoaprendizaje — IA Local Quevepalma

## Doctrina central

> Una IA que vive en un computador personal sólo es útil si **acumula
> capacidad**. Cada conversación es una oportunidad de detectar una
> brecha, ir a la fuente, destilar el 20% accionable, y dejarlo
> archivado como skill reutilizable. El objetivo NO es saberlo todo:
> es **saber dónde mirar, qué destilar y cómo persistirlo** para que
> el próximo turno empiece más arriba.

Tres principios no negociables:

1. **Pareto siempre.** Buscar el 20% del corpus que entrega el 80%
   del dominio práctico. Lo demás se archiva como referencia, no
   como skill activa.
2. **Persistencia obligatoria.** Si un aprendizaje no termina en un
   archivo `SKILL.md` o en una entrada de `MEMORY.md`, no existió.
   Conversaciones se compactan; archivos sobreviven.
3. **Fuente verificable.** Toda skill nueva cita la fuente externa
   (URL de Perplexity, ID de NotebookLM, ruta de documento local,
   nombre de MCP) que la originó. Si la fuente desaparece, la skill
   queda señalada como huérfana.

## Siete principios de autoría de skills (doctrina Javi Consuegra)

> Fuente: publicación de **Javi Consuegra** en LinkedIn, "Llevo meses
> construyendo skills en Claude" (activity-7460577156205748224). Destilado
> el 2026-06-12 e incorporado como doctrina obligatoria: toda skill nueva
> o actualizada por esta llave maestra DEBE cumplir estos siete puntos.

1. **Eficiencia de tokens (divulgación progresiva).** Claude solo lee ~3
   líneas (el `description` del frontmatter) al arrancar; el cuerpo completo
   se carga únicamente cuando la tarea encaja. → El `description` debe ser
   un gancho nítido de ≤3 líneas que diga *cuándo* invocar la skill; el
   detalle pesado va en el cuerpo, sin miedo a la longitud.
2. **Definir limitaciones primero.** Lo más valioso es declarar qué la
   skill **NO** debe hacer, más que lo que sí. Toda skill lleva una lista
   explícita de "Qué NO hacer / compuertas 🚦" antes de los pasos felices.
3. **Reutilizar experiencia probada.** Antes de redactar de cero, partir de
   prompts y skills ya validados (la `MATRIZ_SKILLS`, chats previos, skills
   hermanas). Componer > inventar.
4. **Combinar con el perfil personal ("Acerca de mí").** Una skill rinde
   mucho más si lee el perfil del usuario al arrancar. Perfil canónico:
   `...\memory\user_role.md` + el índice `MEMORY.md`. Toda skill debe
   cargarlos como primer contexto.
5. **Depuración colaborativa.** Si la skill no rinde, consultarlo con el
   usuario e iterar en el mismo turno; no fingir éxito. Dejar en la skill
   una nota de "cómo depurar si falla".
6. **No saltar pasos.** Incluir la consigna literal *"Tómate tu tiempo.
   Calidad antes que velocidad. No saltes pasos."* en el protocolo, para
   evitar atajos que rompen el resultado.
7. **Portabilidad con revisión 80/20.** Las skills se transfieren entre
   máquinas/cuentas sin reescritura, pero al reusarlas en un contexto nuevo
   se revisa el 20% que cambia (rutas, cuentas, fuentes) antes de confiar.

## Hoja de ruta del autoaprendizaje (derivada del hilo Perplexity)

El hilo original define tres niveles de dominio para un humano que
aprende IA. Aquí se reusa la estructura como tabla de **niveles de
madurez de una skill propia**:

| Nivel skill          | Equivalente humano   | Cuándo aplicar                                                          |
|----------------------|----------------------|-------------------------------------------------------------------------|
| Skill básica         | Uso práctico (1-3m)  | La habilidad sólo invoca herramientas existentes (ChatGPT, MCPs, web)   |
| Skill aplicada       | ML aplicado (4-6m)   | La skill orquesta scripts propios (Python, PowerShell, batch de tools)  |
| Skill especializada  | DL avanzado (7-12m)  | La skill incorpora dominio profundo (forense, jurídico, infografía…)    |
| Skill maestra        | MLOps + liderazgo    | La skill orquesta a otras skills (suite EcuaLedger, esta llave maestra) |

Toda nueva skill debe declarar su nivel en el frontmatter, para que
una futura auto-revisión pueda priorizar promociones (básica → aplicada
→ especializada) cuando detecte que la skill se está usando con
frecuencia y aún depende de herramientas externas en lugar de scripts
propios.

## Mapa de fuentes autorizadas

| Fuente                | Cómo accederla en este computador                            | Cuándo usarla                                  |
|-----------------------|--------------------------------------------------------------|------------------------------------------------|
| Perplexity            | MCP `Claude_in_Chrome` → navegar a https://www.perplexity.ai | Hojas de ruta, resúmenes generalistas, citas   |
| NotebookLM            | Skill `anthropic-skills:notebooklmskill`                     | Corpus institucional ya curado por el usuario  |
| Microsoft Docs        | MCP `microsoft_docs_search` / `microsoft_docs_fetch`         | API de Microsoft, Azure, Windows, Office       |
| Web                   | `WebSearch`, `WebFetch`, `nimble:nimble-web-expert`          | Búsqueda rápida y verificada                   |
| Documentos locales    | `Read`, `Glob`, `Grep` en C:\Users\datos\...                 | Corpus propio (Dropbox, .notebooklm-extractos) |
| Cuaderno EcuaBlock    | Skill `tutor-mit-ecuablock`                                  | Expediente legislativo IBPP / EcuaLedger       |
| Wolfram Alpha         | Skill `wolfram-forensic-engine`                              | Cálculo riguroso, validación de cifras         |
| Memoria de Claude     | `C:\Users\datos\.claude\projects\...\memory\MEMORY.md`       | Continuidad entre conversaciones               |

Cuando una conversación nueva exija una fuente que no esté listada
aquí, la primera tarea de esta skill es **agregar la fila** y dejar
documentada la ruta de acceso.

## Doctrinas externas integradas (sesiones recientes)

### Doctrina 8 · Edge y nube son una única arquitectura continua

Fuente: video YouTube `nT17ASj4gdQ` — Jensen Huang (NVIDIA, GTC Taipei)
+ Satya Nadella (Microsoft Build). Destilada en
[[era-pc-agentico-doctrina]].

> "La arquitectura agéntica que corre en un RTX Spark en tu escritorio
> y la que corre en Vera Rubin en un data center de Azure son
> exactamente la misma, solo cambia la escala. El Edge y la nube ya
> no son dos mundos separados, son dos extremos de una única
> arquitectura continua." — Jensen Huang.

**Consecuencia obligatoria para esta llave maestra:** toda skill nueva
debe ser **portable al Claude remoto** sin reescritura. Cumple
automáticamente si respeta el principio 7 de Javi Consuegra
(portabilidad con revisión 80/20). Implica también que el agente local
NO debe asumir que tiene acceso permanente a Edge debug 9222: las
skills deben fallar elegantemente y guiar al usuario a relanzar el
puerto si lo necesitan (patrón ya implementado en `fetch-claude-share`
y `perplexity-active-use`).

### Doctrina 9 · Skills versionadas en Git = portabilidad real

Fuente: video YouTube `oIxLOiITVwk` — Laura Cilleruelo, canal
«Claridad Artificial». Destilada en
[[claude-routines-apis-skills-github]] y operacionalizada en
[[skills-versionado-git-github]].

> Una skill local es valiosa pero **prisionera del disco** donde
> nació. Toda skill madura debe sobrevivir a una corrupción del disco
> y poder reaparecer en otra máquina con un solo `git clone`.

**Consecuencia obligatoria para esta llave maestra:** toda skill
nueva debe poder commitearse SIN reescritura. Implicaciones prácticas
que esta llave maestra impone desde ahora:

1. **No empotrar tokens, cookies, ni rutas de sesión** en `SKILL.md`
   ni en `scripts/`. Vivirán en `.env` o en archivos del sistema
   excluidos por `.gitignore`.
2. **No empotrar datos personales del usuario** (direcciones de
   correo concretas de terceros, números de teléfono, montos
   financieros sensibles, nombres de personas naturales). Si la skill
   necesita esos datos, leerlos al momento de ejecución desde
   `MEMORY.md` o desde el corpus correspondiente.
3. **Rutas absolutas son aceptables** porque el repo es para uso
   personal del usuario, no marketplace público.
4. **Cierre de jornada** ([[cierre-jornada-apagado]]) es el momento
   natural para hacer `git add . && git commit && git push` sobre el
   repo de skills antes de apagar.

## Protocolo de aprendizaje en seis pasos

Aplicar este protocolo cada vez que se detecte una brecha. El
"detector de brecha" es simple: si para responder al usuario hubo
que improvisar más de tres herramientas en secuencia, o se navegó
a una fuente externa nueva, hay brecha → invocar este protocolo.

### Paso 1 — Nombrar la brecha

- Frase corta en imperativo (verbo + objeto), ej.: *"convertir Excel
  con formato uniforme en PDF A4 retrato"*.
- Confirmar que NO existe ya una skill que cubra el 80% del caso
  (revisar `Glob "C:\Users\datos\.claude\skills\**\SKILL.md"`).

### Paso 2 — Ir a la fuente

- Elegir la fuente del mapa anterior según naturaleza de la brecha.
- Si es metodológica, abrir Perplexity (Chrome MCP) y consultar.
- Si es técnica, ir a Microsoft Docs, WebSearch o la documentación
  oficial del MCP en cuestión.
- Si es de dominio Quevepalma/EcuaBlock, ir a NotebookLM o al
  Dropbox local.

### Paso 3 — Destilar el 20%

- Extraer el procedimiento mínimo replicable.
- Eliminar disclaimers, redundancia, contenido aspiracional o
  promocional.
- Conservar SÓLO: comandos, rutas absolutas, decisiones binarias,
  excepciones del usuario, fuentes citables.

### Paso 4 — Codificar como skill

Estructura mínima de toda skill nueva:

```
C:\Users\datos\.claude\skills\<nombre-kebab-case>\
  SKILL.md                  ← obligatorio, frontmatter + cuerpo
  scripts\                  ← opcional, código ejecutable
  references\               ← opcional, contexto largo no operativo
```

El `SKILL.md` debe contener (cumpliendo los siete principios Javi Consuegra):

- `name`, `description` (gancho nítido de **≤3 líneas** — principio 1),
  `trigger_phrases`, `idioma_de_salida`.
- Nivel de madurez (básica / aplicada / especializada / maestra).
- Fuente verificable (URL, ruta, ID).
- **Carga del perfil al arrancar:** instrucción de leer `user_role.md` +
  `MEMORY.md` ("Acerca de mí" — principio 4).
- Doctrina central (1-3 párrafos sobre el porqué).
- **Lista de "Qué NO hacer / compuertas 🚦" ANTES de los pasos** (principio 2).
- Protocolo paso a paso que abra con *"Tómate tu tiempo. Calidad antes que
  velocidad. No saltes pasos."* (principio 6).
- Nota de **"cómo depurar si falla"** para iterar con el usuario (principio 5).
- Nota de **portabilidad** (qué 20% revisar al reusar en otro contexto — principio 7).
- Reuso explícito de skills/prompts previos en lugar de empezar de cero (principio 3).
- Ejemplos de invocación.

### Paso 5 — Registrar en el índice

Añadir entrada de una sola línea en `MEMORY.md`:

```
- [<Título legible>](C:\Users\datos\.claude\skills\<nombre>\SKILL.md) — <gancho de una línea>
```

Si la skill substituye o complementa una skill anterior, dejar
constancia en el cuerpo del nuevo `SKILL.md` con un enlace
`[[skill-anterior]]`.

### Paso 6 — Cierre y promoción

- Marcar la brecha como cerrada en el `TaskList` de la conversación.
- Si la skill nació como "básica" y ya hubo que reescribirla dos
  veces, programar promoción a "aplicada" (añadir script propio).
- Si la skill quedó huérfana (la fuente original ya no es accesible),
  marcarla con `estado: huerfana` en su frontmatter para la siguiente
  auto-revisión.

## Auto-revisión periódica (sólo si el usuario lo invoca)

Cuando el usuario diga "auto-revisión de skills" o equivalente:

1. Listar todas las skills locales (`Glob`).
2. Para cada una, leer el frontmatter y reportar:
   - nivel de madurez declarado
   - fecha de última edición
   - presencia/ausencia de la fuente original
   - candidatos a promoción o a deprecar
3. Producir un informe en texto plano con tres columnas:
   `mantener / promover / deprecar`.
4. NO aplicar cambios sin confirmación explícita del usuario.

## Excepciones y reglas de oro

- **No crear skills triviales.** Si la tarea cabe en tres líneas
  de Bash, no merece skill — basta una entrada de feedback en
  `MEMORY.md`.
- **No duplicar skills existentes.** Antes de crear,
  `Grep` por `name:` en todos los `SKILL.md` para evitar
  colisión.
- **No tocar las skills oficiales de Anthropic** (`anthropic-skills:*`,
  `pdf-viewer:*`, etc.) — esas viven en su propio canal y son
  inmutables desde este lado.
- **No archivar credenciales** ni rutas que contengan tokens, claves
  o nombres de cuentas en el cuerpo de una skill. Eso va en
  `.env` o en el gestor de secretos del MCP correspondiente.
- **Respetar el idioma del usuario.** Si el usuario habla español,
  la skill se escribe en español; si habla inglés, en inglés. La
  consistencia se mide skill por skill, no global.

## Ejemplos de invocación

### Ejemplo 1 — Skill nueva para Perplexity-to-skill

> Usuario: "Lee este chat de Perplexity y conviértelo en una skill."
>
> Claude: aplica el protocolo de seis pasos. Navega vía Chrome MCP,
> destila el 20%, crea `<nombre>/SKILL.md`, registra en `MEMORY.md`,
> reporta el path al usuario.

### Ejemplo 2 — Promoción de skill

> Usuario: "Auto-revisión de skills."
>
> Claude: lista las 25+ skills locales, identifica que
> `gmail-attachments` ya tiene su propio script Python (nivel
> aplicada) pero su frontmatter dice "básica" — propone promoción.

### Ejemplo 3 — Skill maestra orquestadora

> Usuario: "Quiero una sola skill que coordine todas las del
> expediente EcuaBlock."
>
> Claude: ya existe `entrenador-experto-notebooklm-ecualedger`.
> Reporta su path y no crea duplicado.

## Anclaje al hilo Perplexity de origen

El hilo del cual nace esta llave maestra clasificó al usuario como
"ingeniero de producción/construcción en Ecuador con interés en
blockchain y fintech" y sugirió una ruta personalizada de 10+ meses
hacia "MLOps + liderazgo estratégico". Esta skill ABSORBE esa
clasificación: las nuevas skills que se generen privilegiarán los
dominios:

1. **Producción industrial y oleoquímica** (Quevepalma, costos,
   personal de producción, planificación ISO 2015).
2. **Blockchain y fintech soberano** (EcuaLedger Soberana, IBPP,
   activos digitales, código de finanzas).
3. **Forense y auditoría** (EPACEM/Oro Juez, Benford, Wolfram).
4. **Comunicación institucional** (war rooms, comités, NotebookLM,
   infografía Ecuador Digital).

Cuando una brecha caiga fuera de esos cuatro ejes, esta skill puede
crear la skill pedida pero debe marcar `dominio: externo-al-perfil`
en el frontmatter, para que la próxima auto-revisión pondere si
merece mantenimiento o si fue una necesidad puntual.

## Referencias persistentes

- Hilo Perplexity origen:
  https://www.perplexity.ai/search/e21b0957-a5fe-4880-aad3-bedf29205bb1
- Resumen destilado del hilo:
  `references/perplexity-guia-autoaprendizaje-resumen.md` (mismo
  folder de esta skill).
- Índice global de memoria:
  `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\MEMORY.md`
