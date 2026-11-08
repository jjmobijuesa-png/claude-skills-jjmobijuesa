---
name: memoria-agente-claude-md-reglas
description: >-
  Cómo se gobierna lo que un agente recuerda entre sesiones: los tres ámbitos de
  CLAUDE.md y su CONCATENACIÓN de la raíz hacia abajo, el objetivo de menos de 200 líneas
  (los archivos largos no solo gastan más, OBEDECEN PEOR), las tres trampas de las
  importaciones `@ruta`, el mecanismo `.claude/rules/` con `paths` que sí aligera, y el
  techo de 200 líneas o 25 KB de la memoria automática, que se cruza SIN AVISO. Invocar
  al escribir o auditar instrucciones persistentes.
trigger_phrases:
  - "dónde escribo esta regla"
  - "auditar mi CLAUDE.md"
  - "el CLAUDE.md está muy largo"
  - "claude.md vs rules vs skill"
  - "memoria automática"
  - "se me carga toda la memoria?"
  - "importaciones con arroba"
idioma_de_salida: español
nivel_de_madurez: aplicada
dominio: agentes-ia / instrucciones persistentes
fuente:
  - "Documentación oficial de Anthropic, «How Claude remembers your project» — https://code.claude.com/docs/en/memory (verificada por HTTP el 12-oct-2026)"
  - "Material de estudio de la casa: G:\\Mi unidad\\5 Clases-Magistrales-HTML\\04-ia-y-sistemas\\18-memoria-claude-code.html"
relacionada: arnes-agentico-bucle-y-contexto, skills-empaquetar-procedimiento, mcp-conexion-ambitos-y-frontera, memoria-compartida-sesiones
---

## Acerca de mí (cargar al arrancar)
Leer `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md` y
`MEMORY.md`. Opera dentro del marco de [[arnes-agentico-bucle-y-contexto]]: esta skill es
el **mecanismo que decide qué cruza la frontera entre sesiones**. Su contraparte para el
trabajo por tarea es [[skills-empaquetar-procedimiento]].

## Doctrina central

**Dos sistemas, no uno.** Lo que usted escribe (`CLAUDE.md`) y lo que el agente escribe
solo (memoria automática). Ambos se cargan en cada sesión; **ninguno de los dos es
configuración que se imponga**: son contexto.

**Los tres ámbitos se CONCATENAN, no se sobrescriben.**

| Ámbito | Ruta | Quién lo ve |
|---|---|---|
| Usuario | `~/.claude/CLAUDE.md` | Solo usted, en todos sus proyectos |
| Proyecto | `./CLAUDE.md` o `./.claude/CLAUDE.md` | El equipo, por control de versiones |
| Local | `./CLAUDE.local.md` | Solo usted, en ese proyecto (al `.gitignore`) |

Se cargan el del directorio de trabajo **y todos los de arriba**, en orden **de la raíz
hacia abajo**: lo más cercano a donde se lanzó el agente se lee al final. Dentro de cada
nivel, el `.local.md` va después. Los de subdirectorios entran **cuando el agente toca un
archivo de ese subdirectorio**.

**La regla que más se ignora:** apuntar a **menos de 200 líneas por archivo**, porque los
más largos consumen más contexto **y reducen la adherencia**. Pasado cierto punto,
escribir más reglas hace que se cumplan menos. Es un problema de obediencia, no de espacio.

**Si dos instrucciones se contradicen, el agente elige una de forma arbitraria** y no
avisa del conflicto.

## Qué NO hacer / compuertas 🚦

- 🚦 **Importar NO aligera.** `@ruta` expande el archivo al arrancar: organiza, no abarata.
  Lo único que aligera de verdad es **`.claude/rules/` con el campo `paths`**, que limita
  la carga a los archivos que coinciden con el patrón.
- 🚦 **El techo de la memoria automática se cruza en silencio.** Se cargan **las primeras
  200 líneas o 25 KB, lo que primero se cumpla**. Lo que sobra no entra, y **no hay aviso,
  ni error, ni señal**: el agente opera con un índice incompleto creyendo que lo tiene todo.
  **Medir antes de suponer.**
- 🚦 **Tres trampas de las importaciones:** (1) no reducen contexto; (2) una ruta con
  espacios exige **barra invertida antes de cada espacio**, y entre comillas **no se
  importa en absoluto**; (3) la recursión tiene un máximo de **cuatro saltos**. Para
  mencionar una ruta sin importarla, encerrarla entre acentos graves.
- 🚦 **Una importación externa** —cuya ruta resuelve fuera del directorio de trabajo—
  **pide aprobación una vez**; si se declina, queda desactivada y el diálogo no vuelve.

## Protocolo de uso

1. **Medir antes de escribir:** líneas y KB del archivo de usuario y del índice de memoria.
   Un vistazo basta para saber si queda margen.
2. **Clasificar la instrucción en tres vías:**
   - **Regla** (`.claude/rules/`) si debe estar siempre, o siempre que se toquen ciertos
     archivos — con `paths` si es lo segundo.
   - **Skill** si es propia de una tarea → [[skills-empaquetar-procedimiento]].
   - **Hook** si debe cumplirse **sin depender del criterio del modelo**.
3. **Al crecer:** partir por tema en `.claude/rules/` en lugar de alargar el archivo único.
4. **Periódicamente:** revisar y eliminar lo caduco y lo contradictorio.

## Cómo depurar si falla

- **«La regla está escrita y no se cumple»:** puede ser adherencia (archivo demasiado
  largo), contradicción con otra instrucción, o que la regla necesitara ser un hook.
- **«Parte de mi memoria no aparece»:** medir el índice contra los dos techos. Al cruzarlos
  no hay error, solo ausencia.
- **«La importación no trae nada»:** revisar espacios sin barra invertida, comillas, o que
  se hayan superado los cuatro saltos.
- **Un repositorio ya preparado para otros agentes** funciona sin cambios: el `AGENTS.md`
  se lee como instrucciones de proyecto cuando no hay `CLAUDE.md`.

## Portabilidad (revisar el 20% al reusar)
Los nombres de archivo y las rutas son del producto; **la concatenación por jerarquía, el
tope de adherencia y la distinción entre contexto y garantía** son generales.

## Reuso (no empezar de cero)
Para la memoria entre dispositivos y sesiones, [[memoria-compartida-sesiones]]. Para no
desperdiciar la ventana, [[ahorro-de-tokens]]. Para el marco donde todo esto vive,
[[arnes-agentico-bucle-y-contexto]].

## Ejemplos de invocación
- «¿Mi CLAUDE.md está demasiado largo?»
- «¿Esto va a reglas, a skill o a hook?»
- «¿Se está cargando entero mi índice de memoria?»

## Vecindad en la red
Hermanas de la serie: [[arnes-agentico-bucle-y-contexto]],
[[mcp-conexion-ambitos-y-frontera]], [[skills-empaquetar-procedimiento]].
Gobierno de la casa: [[regla-del-primer-tropiezo]], [[memoria-compartida-sesiones]].
