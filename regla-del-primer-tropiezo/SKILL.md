---
name: regla-del-primer-tropiezo
description: |
  SKILL META, SIEMPRE ACTIVA. Regla constitucional de esta casa: **el segundo
  intento nunca se improvisa**.

  Cuando una acción falla a la primera —un comando que devuelve error, una
  sesión caducada, un selector que no encuentra nada, un archivo que no abre,
  una API que responde 401— el agente NO debe probar una segunda variante de
  su propia cosecha. Debe DETENERSE y consultar primero el inventario que esta
  casa ya construyó: `skills_index.md` (154 skills), `MEMORY.md` y los
  archivos de `memory/`, y el árbol `~/.claude/skills/`.

  El costo de no hacerlo es medible: el 9-sep-2026 el agente quemó seis
  intentos y más de veinte minutos reautenticando NotebookLM, cuando la
  solución exacta estaba escrita en dos skills propias. Ver §6.

  Se aplica TAMBIÉN de forma preventiva: al recibir cualquier comando o
  prompt, antes de la primera acción, verificar si el inventario ya cubre el
  caso.

  Y no es solo un índice de consulta: el §4 enseña a CREAR la solución nueva a
  partir de lo que ya existe —buscar por mecanismo y no por síntoma, los cuatro
  operadores de transferencia, y la regla del salto A → C con su compuerta de
  verificación—. El objetivo no es evitar repetir trabajo: es deducir la salida
  desde material adyacente y llegar antes.

trigger_phrases:
  - "no te sale a la primera"
  - "revisa tu memoria y tus skills"
  - "ya habías hecho esto antes"
  - "no es la primera vez"
  - "consulta el inventario"
idioma_de_salida: español neutro
nivel_madurez: constitucional
metadata:
  type: meta
  version: 1.2
  created: 2026-09-09
  actualizada: 2026-09-09 (v1.1 §4 salto A→C · v1.2 §9 la red como grafo + §10 plasticidad; alcance global vía ~/.claude/CLAUDE.md)
  origen: fallo real de reautenticación NotebookLM en la sesión del costeo QVP semana 37
  relacionada: llave-maestra-autoaprendizaje-ia, eficiencia-generacion-respuestas, baculo-mision-soberana
---

# Skill `regla-del-primer-tropiezo`

> **Siempre activa.** No hace falta invocarla. Es una compuerta de
> comportamiento, no una tarea.

## 1. La doctrina, en una frase

**El primer intento puede improvisarse. El segundo, jamás.**

Un fallo no es una invitación a probar otra variante: es una **señal de que
hay que ir a buscar**. Esta casa lleva más de un año destilando skills y
memoria precisamente para que el agente no vuelva a resolver desde cero lo
que ya resolvió. Improvisar el segundo intento desperdicia ese capital y,
peor, le hace creer al usuario que el problema es nuevo.

## 2. El disparador exacto

Se activa ante **cualquiera** de estas señales, en cualquier herramienta:

- Un comando devuelve error, código distinto de cero o un mensaje de fallo.
- Una sesión, token o cookie aparece caducada, inválida o redirige a login.
- Un selector, ruta, ID o nombre de archivo no se encuentra.
- Una salida está vacía, truncada o es evidentemente incorrecta.
- Una operación excede su tiempo esperado o se cuelga.
- El usuario dice, en cualquier forma, «ya hicimos esto» o «revisa tu memoria».

También se activa **antes del primer intento** cuando el pedido menciona una
herramienta, cuenta, ruta o flujo recurrente de esta casa (NotebookLM, Gemini,
DeepSeek, Perplexity, WhatsApp, LinkedIn, X, Gmail, Edge, Excel/Word por COM,
Quevepalma, Mobijuesa, Belén, EcuaLedger…).

## 3. El protocolo — tres minutos, en este orden

**Paso 0 · Parar.** No lanzar la segunda variante. Nombrar en voz alta, para
uno mismo, qué falló exactamente.

**Paso 1 · Barrer el índice de skills** (es el más barato y el que más rinde):

```bash
grep -i -n "<palabra clave>" "C:/Users/datos/.claude/projects/C--Users-datos-Downloads/memory/skills_index.md"
```

**Paso 2 · Barrer la memoria compartida:**

```bash
grep -ril "<palabra clave>" "C:/Users/datos/.claude/projects/C--Users-datos-Downloads/memory/"
```

Leer `MEMORY.md` completo si el término aparece ahí: sus banderas 🚦 suelen
contener justamente la trampa en la que se acaba de caer.

**Paso 3 · Barrer el cuerpo de las skills**, no solo sus nombres. La solución
casi siempre vive en una sección «Cómo depurar si falla» de una skill que se
llama de otra cosa:

```bash
grep -ril "<palabra clave>" "C:/Users/datos/.claude/skills/"
```

**Paso 4 · Leer ENTERA la skill que aparezca.** No los primeros 2.000
caracteres. El fallo del 9-sep-2026 ocurrió por leer una skill a medias y
aplicar su §2 al perfil equivocado. Ver §6.

**Paso 5 · Recién ahora, actuar.** Si el inventario no tiene la respuesta,
improvisar está permitido — y entonces se abre el deber del paso 6.

**Paso 6 · Codificar lo aprendido.** Si se resolvió algo que el inventario no
cubría, aplicar [[llave-maestra-autoaprendizaje-ia]]: aumentar la skill
pertinente o crear una nueva, y dejar el puntero en `MEMORY.md`. Un fallo que
no deja skill es un fallo que se va a repetir.

## 4. Del inventario a la solución NUEVA — saltar de A a C

> Criterio del usuario, 9-sep-2026: *«que te permita resolver y sobre todo
> crear una solución a partir de lo que tienes, pudiendo deducir o inferir la
> solución y saltar de A a la C si te es posible».*

Este es el corazón de la skill, y lo que la separa de un simple índice. **El
inventario casi nunca contiene el caso exacto. Contiene la FORMA del caso.**
Buscar solo coincidencias literales desperdicia el 90 % de lo que hay
guardado.

### 4.1 Buscar por MECANISMO, no por síntoma

El síntoma es local; el mecanismo es transferible. «Authentication expired» es
un síntoma que solo aparece en NotebookLM. «El perfil persistente sobrevive
mucho más que el snapshot exportado» es un mecanismo, y vale igual para
WhatsApp por CDP, Gemini, X, LinkedIn y Gmail — todas las sesiones de esta
casa.

Regla práctica: al barrer el inventario, buscar **dos o tres términos de
mecanismo** además del término literal. Si el síntoma es «el selector no
encuentra nada», los mecanismos candidatos son *lista virtualizada*, *DOM
cambiado*, *iframe*, *render diferido*.

### 4.2 Los cuatro operadores de transferencia

| Operador | En qué consiste | Ejemplo real de esta casa |
|---|---|---|
| **Por mecanismo** | Misma causa profunda, herramienta distinta | Cosechar cookies del perfil vivo → sirve para NotebookLM, Gemini y cualquier sesión Google |
| **Por estructura** | Misma forma de problema, dominio distinto | «Lista virtualizada → captura acumulativa con scroll» resolvió WhatsApp; sirve igual para LinkedIn, X y cualquier feed |
| **Por inversión** | La herramienta dice que falló; preguntar si su **precondición** realmente falló | El `login` expiró por timeout **y aun así la sesión estaba viva dentro del perfil** |
| **Por composición** | Dos medias respuestas en dos skills distintas forman una entera | `auditor-integral` dio la ruta correcta (`profiles/default`) + `login-reauth` dio la técnica (cosecha del persistente) |

### 4.3 La regla del salto A → C

**Sí, saltar.** Cuando el mecanismo está identificado, no hay que recorrer los
pasos intermedios solo por prolijidad. Deducir el destino y probarlo directo
es más rápido, más barato y suele ser más correcto.

**Pero el salto tiene una compuerta, y es innegociable:**

> 🚦 **Se salta a C si —y solo si— el aterrizaje se puede verificar con una
> comprobación barata.** Un salto sin verificación no es deducción: es
> improvisar con más confianza, que es exactamente lo que esta skill existe
> para impedir.

En la práctica: antes de saltar, escribir la comprobación. *«Si mi inferencia
es correcta, `notebooklm list` devuelve los cuadernos»*. *«Si es correcta, el
archivo tiene más de 50 cookies y una SID»*. Si no se puede formular una
comprobación de una línea, no es un salto: es una apuesta, y entonces toca
recorrer B.

### 4.4 El movimiento más rentable: dudar de los INSUMOS, no del modelo

Cuando algo cuadra en teoría pero no en la realidad, el error casi nunca está
en el método: está en los números que se le metieron. Antes de rehacer el
razonamiento, **ir a buscar el dato real**.

Ejemplo del mismo día, en otro frente: DeepSeek y Gemini analizaron la
propuesta de costeo de Quevepalma y ambos concluyeron que el método habilitaba
a vender más barato. Los dos razonaron bien. Los dos usaron los números de
ejemplo de la diapositiva como si fueran la realidad. Bastó abrir el cuadro de
seguimiento de la propia empresa —un salto A → C, saltándose toda la
verificación de su lógica— para descubrir que el margen real era de +10 y −12
en lugar de +40 a +60, **y que la conclusión cambiaba de signo**. El hallazgo
no salió de razonar mejor: salió de ir a buscar el insumo.

### 4.5 Deducir de la estructura, no solo de la memoria

Cuando una magnitud es un cociente, su sensibilidad es una derivada, y eso se
calcula: no hace falta buscarlo. `costo de aceite = precio de fruta ÷
rendimiento` implica que un punto de rendimiento vale `precio ÷ rendimiento²`.
Con la fruta a 195,16 y rendimiento 21,7 %, eso da 41 dólares por tonelada —
cuatro veces todo el margen comercial de la semana. Ese dato no estaba en
ningún archivo de la casa: **se dedujo de la forma de la ecuación**. Ese es el
tipo de salto que hay que buscar.

## 5. Qué NO hacer / compuertas 🚦

- 🚦 **No encadenar variantes.** Tres intentos seguidos de la misma familia
  (tres perfiles de navegador, tres selectores, tres rutas) es la firma
  inconfundible de que esta regla se está incumpliendo.
- 🚦 **No declarar un bloqueo sin haber barrido el inventario.** Decirle al
  usuario «esto no se puede» cuando la solución está escrita en su propia
  casa es el peor resultado posible de esta skill.
- 🚦 **No confiar en el nombre de la skill.** El arreglo de NotebookLM vivía en
  `auditor-integral-notebooklm`, no en `notebooklm-login-reauth`. Buscar por
  contenido, no por título.
- 🚦 **No leer skills a medias.** Ver §5.
- **No convertir esto en parálisis.** Son tres minutos de búsqueda, no una
  auditoría. Si el barrido no devuelve nada, seguir adelante.

## 6. El caso que originó esta skill (9 de septiembre de 2026)

**Tarea:** generar una diapositiva de costeo en el cuaderno «Toma d Decisiones
QVP» de NotebookLM.

**Fallo inicial:** `notebooklm list` → *Authentication expired*.

**Lo que el agente hizo mal — seis intentos improvisados:**

1. Refresco desde `~/.notebooklm-mobijuesa360@gmail.com/browser_profile` → `SESSION_DEAD`.
2. Tres perfiles Edge en modo headless → los tres muertos.
3. Dos perfiles Edge en modo headed → los dos muertos.
4. `login --browser-cookies edge` → *Could not decrypt edge cookies* (app-bound
   encryption; **esto ya estaba advertido en `notebooklm-login-reauth` §4**).
5. `notebooklm login --browser msedge` → cinco minutos de espera y timeout.
6. Mover la ventana al frente con PowerShell para que el usuario iniciara sesión.

**Lo que dijo el usuario:** *«no es la primera vez que has ejecutado este
pedido, revisa tu memoria integral y las skills»*.

**Dónde estaba la respuesta, todo el tiempo:**

- `auditor-integral-notebooklm` §«Cómo depurar si falla» decía que el CLI lee
  **`profiles/default/storage_state.json`** —no el del perfil nombrado— y traía
  el script exacto de cosecha con `channel="msedge"`.
- `notebooklm-login-reauth` §2 decía que el perfil **persistente** sobrevive
  mucho más que el snapshot, y que hay que cosechar de ahí.

**La solución real, en un intento:** una vez que el usuario inició sesión
dentro del Edge que abrió la CLI, el perfil persistente
`~/.notebooklm/profiles/mobijuesa360@gmail.com/browser_profile` quedó con la
sesión viva aunque la CLI no la hubiera *detectado*. Bastó abrirlo headless,
soltar los `SingletonLock` huérfanos y volcar `ctx.storage_state()` a los dos
destinos. Resultado: 78 cookies, SID válido, sesión operativa.

Script de referencia: `C:\Users\datos\war_room_tmp\cosechar_nlm.py`.

**La lección transferible, que va más allá de NotebookLM:** cuando una
herramienta «no detecta» un estado, ese estado puede existir igual. Verificar
el estado real antes de concluir que la operación falló.

## 7. La métrica

Dos condiciones, y las dos son falsables:

**Métrica 1 — el barrido.** Se cumple si, ante cualquier fallo, **entre el
intento 1 y el intento 2 hay un barrido del inventario**. No se cumple si hay
dos acciones correctivas seguidas sin una lectura de skills o memoria en medio.

**Métrica 2 — el salto.** Se cumple si el segundo intento **ataca el mecanismo**
y no el síntoma. La firma del incumplimiento es reconocible: tres variantes de
la misma familia —tres perfiles, tres selectores, tres rutas— es recorrer A, A′,
A″ sin haber llegado nunca a B, mucho menos a C.

Contraste del 9-sep-2026, que sirve de calibración: en el frente de NotebookLM
hubo **seis** intentos de la misma familia y cero barridos, hasta que el usuario
intervino. En el frente del costeo, el mismo día, hubo **un** salto A → C —ir a
buscar el costo real de la semana en lugar de auditar el razonamiento de los
otros dos modelos— y ese salto produjo todo el hallazgo. Mismo agente, mismo
día, dos métodos, dos resultados.

## 8. Reuso (no empezar de cero)

- Para **codificar** lo aprendido tras resolver: [[llave-maestra-autoaprendizaje-ia]].
- Para decidir **el camino más barato** que resuelve el prompt: [[eficiencia-generacion-respuestas]].
- Para no pedirle al usuario lo que se puede averiguar solo: [[cuantificar-antes-de-pedir]].
- Para el marco de misión: [[baculo-mision-soberana]].

## 9. La red integrada — no es una lista, es un grafo

El inventario no es un catálogo de 154 entradas independientes: es una **red con 467
aristas y un racimo central de 136 skills**. La asociación análoga —que es la materia
prima de la creatividad— necesita saber qué está conectado con qué; sobre una lista plana
no hay nada que asociar.

**El mapa:** `memory/skills_network.md`. Trae los cubos (por dónde pasa el tráfico), los
racimos (vecindades temáticas), las huérfanas (capital muerto) y los enlaces rotos
(skills pendientes de escribir). Se regenera cuando cambie el corpus:

```bash
"C:/Users/datos/.notebooklm-venv/Scripts/python.exe" \
  "C:/Users/datos/.claude/skills/regla-del-primer-tropiezo/mapear_red_skills.py"
```

**Cómo se usa en el barrido del §3.** Al fallar algo, además de buscar el término:

1. Ubicar en qué **racimo** cae el problema y leer a sus vecinos, aunque se llamen distinto.
2. Entrar por un **cubo** si no hay pista: `llave-maestra-autoaprendizaje-ia` (grado 51),
   `agente-local-autoreflexivo-bookmarks` (30), `memoria-financiera-inteligenciada` (21),
   `cuantificar-antes-de-pedir` (17), `metodo-hamming-preguntas-fundamentales` (17).
3. Revisar las **huérfanas**: una skill que nadie enlaza suele contener justo lo que nadie
   recordaba tener.
4. Mirar los **enlaces rotos** del área: un wikilink que apunta a una skill inexistente
   es un problema que ya se detectó antes y quedó sin escribir.

## 10. Plasticidad — la red se recompone, no solo se amplía

> Criterio del usuario, 9-sep-2026: *«incluso si eso requiere una reconfiguración, tal
> plasticidad neuronal para recomponer la red de skills integrada y mejorarlas, tal espiral
> abierta ascendente».*

Añadir una skill nueva a cada hallazgo engorda la lista pero no mejora la red: produce un
catálogo cada vez más largo y cada vez menos navegable. Una red que solo crece se degrada.
**Está autorizado —y es parte del trabajo— rehacer el cableado.**

**Los cinco movimientos permitidos:**

| Movimiento | Cuándo | Qué se hace |
|---|---|---|
| **Enlazar** | Se usaron dos skills juntas y no se citaban | Agregar `[[wikilink]]` recíproco |
| **Fusionar** | Dos skills se solapan y siempre se leen juntas | Una absorbe a la otra; la absorbida queda como puntero |
| **Escindir** | Una skill acumuló dos doctrinas distintas | Partirla; cada parte enlaza a la otra |
| **Elevar** | Un truco local resultó valer para toda la casa | Promoverlo a skill propia y enlazarlo desde el racimo |
| **Podar** | Una huérfana quedó obsoleta o su herramienta murió | Marcarla obsoleta con la fecha y el motivo. **No borrar en silencio.** |

**La compuerta de la plasticidad:** 🚦 no se recompone en caliente, a mitad de una tarea
del usuario. Se anota el cambio propuesto, se termina el encargo, y se recompone al
cerrar. Reconfigurar la red mientras se corre por ella es cómo se rompen las dos cosas.

**La espiral, explícita.** Cada vuelta debe dejar la red mejor conectada, no solo más
grande: `fallo → barrido → salto A→C → solución → codificar → RECABLEAR → regenerar el
mapa`. El indicador de que la espiral sube y no gira en plano es que **las huérfanas
bajen y las aristas suban** entre una regeneración del mapa y la siguiente. Al 9-sep-2026 se dio la **primera vuelta**: de 467 aristas / 17 racimos / 15 huérfanas a **592 aristas · 1 racimo · 0 huérfanas**. Esa es la nueva línea base. Las quince huérfanas no eran capacidades nuevas: eran capacidades pagadas que la red no alcanzaba.

## 11. Ejemplos de invocación

Rara vez se invoca: se cumple. Pero el usuario puede forzarla con:

- «No es la primera vez que haces esto, revisa tus skills.»
- «Antes de seguir probando, barre la memoria.»
- «¿Ya tenemos algo escrito sobre esto?»
