---
name: skills-empaquetar-procedimiento
description: >-
  Cuándo y cómo empaquetar un procedimiento repetido en una skill, y cuándo NO (regla o
  hook). Cubre la estructura de carpeta, los campos de frontmatter que de verdad cambian
  el comportamiento, los cinco límites numéricos y el fallo silencioso de las
  instalaciones grandes: al desbordar el presupuesto del listado SE DESCARTAN
  DESCRIPCIONES —empezando por las menos usadas— y la skill existe sin activarse.
  Invocar al crear, auditar o depurar skills, y en cualquier inventario de más de 100.
trigger_phrases:
  - "crear una skill"
  - "mi skill no se activa"
  - "la skill se activa de más"
  - "regla, skill o hook"
  - "auditar mis skills"
  - "tengo demasiadas skills"
  - "frontmatter de SKILL.md"
idioma_de_salida: español
nivel_de_madurez: aplicada
dominio: agentes-ia / autoría de capacidades
fuente:
  - "Documentación oficial de Anthropic, «Agent Skills in Claude Code» — https://code.claude.com/docs/en/skills (alrededor de 107.000 caracteres, leída en sus dos mitades; verificada por HTTP el 12-oct-2026)"
  - "Material de estudio de la casa: G:\\Mi unidad\\5 Clases-Magistrales-HTML\\04-ia-y-sistemas\\20-skills-claude-code.html"
relacionada: arnes-agentico-bucle-y-contexto, memoria-agente-claude-md-reglas, mcp-conexion-ambitos-y-frontera, llave-maestra-autoaprendizaje-ia
---

## Acerca de mí (cargar al arrancar)
Leer `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md` y
`MEMORY.md`. Es la skill **sobre las skills**: cierra la serie de los documentos núcleo y
es la que más directamente gobierna este inventario, que supera las 170.

## Doctrina central

**El criterio para crear una, en una línea:** cuando usted lleva tiempo **pegando las
mismas instrucciones o el mismo procedimiento en el chat**.

**La razón técnica:** a diferencia del contenido de `CLAUDE.md`, **el cuerpo de una skill
se carga solo cuando se usa**. Al inicio de la sesión solo pesa la descripción.

**La decisión de tres vías, que conviene tener resuelta de antemano:**

| Vía | Cuándo | Naturaleza |
|---|---|---|
| **Regla** (`.claude/rules/`) | Debe estar siempre, o al tocar ciertos archivos | Contexto |
| **Skill** | Es propia de una tarea | Contexto, pero por demanda |
| **Hook** | Debe cumplirse **sin depender del criterio del modelo** | **Garantía** |

**Los cinco números:** `SKILL.md` por debajo de **500 líneas** · descripción más
`when_to_use` cortadas a **1.536 caracteres** combinados · al compactar se reinsertan hasta
**5.000 tokens por skill** con presupuesto combinado de **25.000** · el **listado** de
nombres y descripciones tiene un presupuesto del **1% de la ventana de contexto**.

**De veinte campos de frontmatter, todos opcionales, solo `description` es recomendado** —
y es el que de verdad determina si la skill existe en la práctica, porque es lo que el
agente usa para decidir si cargarla. **Los campos desconocidos se ignoran en silencio**:
una errata deja un campo muerto que nadie advierte.

## Qué NO hacer / compuertas 🚦

- 🚦 **El fallo silencioso de los inventarios grandes.** El listado contiene **siempre
  todos los nombres**, pero al desbordar su presupuesto **se descartan descripciones**,
  empezando por las skills menos invocadas. Sin descripción no hay activación automática:
  **la skill está instalada y nunca se usa.** Con más de 100 skills esto ya no es
  hipotético. Medir con `/doctor`; buscar las inservibles con `/skill-doctor`.
- 🚦 **`allowed-tools` NO es permiso de sesión.** Concede permiso **solo hasta su mensaje
  siguiente** y no restringe las demás herramientas. Para permiso duradero, reglas de
  permiso en la configuración.
- 🚦 **Para acciones con efectos secundarios, `disable-model-invocation: true`.** Es la
  recomendación expresa de la fuente, y vale para todo lo que publique, envíe, borre o
  escriba fuera.
- 🚦 **Un comando inyectado con `!` que termine distinto de cero ABORTA la invocación
  entera** (salvo el código 1 de comandos de búsqueda y comparación). Si una skill «no hace
  nada», es lo primero que hay que mirar.
- 🚦 **`context: fork` sin tarea concreta devuelve casi nada**, porque el subagente recibe
  el `SKILL.md` pero **no la conversación**.

## Protocolo de uso

1. **Antes de crear:** ¿es repetición real, o un encargo único? Si es único, no es skill.
2. **Clasificar en las tres vías** antes de escribir una línea.
3. **Redactar la descripción primero**, diciendo *qué hace* y *cuándo usarla*, con el caso
   de uso al principio: se corta a 1.536 caracteres y es lo único que el agente ve de
   entrada.
4. **Cuerpo por debajo de 500 líneas**, lo importante arriba —al compactar solo sobrevive
   el principio— y el material extenso en archivos enlazados. Los guiones, a `scripts/`:
   **se ejecutan y no gastan contexto**.
5. **Si tiene efectos secundarios:** `disable-model-invocation: true`.
6. **Periódicamente:** `/doctor` para el costo del listado, `/skill-doctor` para las que
   no se usan.

## Cómo depurar si falla

- **No se activa:** revisar que la descripción tenga las palabras que usted diría; que
  aparezca al preguntar qué skills hay; invocarla a mano. **Si el YAML está mal formado**,
  el cuerpo se carga con metadatos vacíos: el `/nombre` funciona pero la activación
  automática no. Se ve con `--debug`, y hay un validador para los frontmatter que no parsean.
- **Firma visible de un frontmatter que no parsea:** en el listado, la skill aparece **con
  el primer encabezado del cuerpo como descripción** (p. ej. «Acerca de mí (cargar al
  arrancar)»). Si se lee eso en el listado, el YAML está roto — no hace falta nada más para
  diagnosticarlo.
- **La causa número uno en esta máquina: una ruta de Windows con barras simples dentro de
  un escalar entre comillas dobles.** `"… G:\Mi unidad\5 Clases…"` convierte `\M` y `\5` en
  secuencias de escape inválidas y el parser aborta el documento entero. Por eso las rutas
  en `fuente:` se escriben **siempre con `\\`**, o se evita la comilla doble. Comprobación
  de una línea, antes de dar por buena cualquier skill nueva:
  ```bash
  python -c "import io,yaml;print(yaml.safe_load(io.open(r'<ruta>/SKILL.md',encoding='utf-8').read().split('---')[1])['name'])"
  ```
  🚦 **Y no intentar la corrección con `sed` ni con un heredoc**: el mismo backslash se
  come en la capa del shell y se gastan dos intentos sin avanzar. Reescribir el archivo con
  la herramienta de escritura literal. (Caso que lo documentó: 29-oct-2026, las tres skills
  destiladas de las clases 21-23.)
- **Se activa de más:** descripción más específica, o `disable-model-invocation: true`.
- **Se deja de seguir a media sesión:** tres causas distintas — regla que debía ser hook;
  orientación redactada como instrucción puntual en vez de para toda la tarea; o
  compactación, que conserva solo el principio (volver a invocarla).
- **Desapareció:** mirar la papelera del directorio de skills, con retención por omisión de
  30 días.

## Portabilidad (revisar el 20% al reusar)
Los nombres de campo y los comandos de diagnóstico son del producto; **el criterio de
repetición, la decisión de tres vías y el fallo del listado por presupuesto** valen para
cualquier sistema de capacidades cargadas por descripción.

## Reuso (no empezar de cero)
Para el ciclo de detectar brecha, destilar y archivar, [[llave-maestra-autoaprendizaje-ia]].
Para el método ante fallos, [[regla-del-primer-tropiezo]]. Para la frontera con las
instrucciones permanentes, [[memoria-agente-claude-md-reglas]].

## Ejemplos de invocación
- «¿Esto merece ser una skill?»
- «Tengo 170 skills, ¿se están activando todas?»
- «Mi skill no se dispara aunque el nombre aparece.»

## Vecindad en la red
Cierra la serie: [[arnes-agentico-bucle-y-contexto]],
[[memoria-agente-claude-md-reglas]], [[mcp-conexion-ambitos-y-frontera]].
Gobierno del inventario: [[llave-maestra-autoaprendizaje-ia]], [[regla-del-primer-tropiezo]].
