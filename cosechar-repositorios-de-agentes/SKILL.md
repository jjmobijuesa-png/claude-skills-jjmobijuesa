---
name: cosechar-repositorios-de-agentes
description: >-
  Protocolo de cinco pasos para incorporar al hábitat lo que aparece en catálogos de
  repositorios, paquetes de skills y listas de «herramientas que debe conocer»: resolver y
  verificar en el origen, leer la descripción PROPIA del proyecto y no la del divulgador,
  extraer el MECANISMO en vez del producto, reescribirlo con las compuertas de la casa, y
  medir el costo en el presupuesto del listado antes de añadir. Incluye la compuerta
  central: NUNCA instalar un paquete grande de skills ajenas, porque al desbordar el
  presupuesto se apagan en silencio las que ya funcionan. Invocar ante cualquier hilo,
  lista o repositorio que proponga adoptar herramientas de agente.
trigger_phrases:
  - "instalo este paquete de skills"
  - "mira estos repos de GitHub"
  - "herramientas que todo X debería conocer"
  - "vale la pena adoptar esta herramienta"
  - "integrar esto en nuestras skills"
  - "paquete de habilidades para Claude Code"
idioma_de_salida: español
nivel_de_madurez: aplicada
dominio: agentes-ia / gobierno del inventario
fuente:
  - "Post de @thegreatest_sv en X, 31-oct-2026 — https://x.com/thegreatest_sv/status/2116587002493542781 (leído y verificado el 7-nov-2026)"
  - "Verificación: los 7 enlaces resueltos desde t.co y consultados contra api.github.com el 7-nov-2026"
  - "Material de estudio de la casa: G:\\Mi unidad\\5 Clases-Magistrales-HTML\\04-ia-y-sistemas\\26-cosechar-repositorios-agentes.html"
relacionada: skills-empaquetar-procedimiento, auditar-skills-antes-de-instalar, llave-maestra-autoaprendizaje-ia, segundo-cerebro-anclaje-verificable, bucle-verificacion-garantia-vs-sugerencia, gobernanza-datos-financieros-ia
---

## Acerca de mí (cargar al arrancar)
Leer `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md` y
`MEMORY.md`. Skill de **gobierno del inventario**: decide qué entra a la red y con qué
condición. Complementa a [[auditar-skills-antes-de-instalar]], que mira la seguridad de
una pieza concreta; esta mira el **costo de sistema** de incorporarla.

## Doctrina central

**La regla, en una línea: un repositorio no se instala, se cosecha.**

**Los cinco pasos:**

1. **Resolver y verificar en el origen.** Desplegar los acortadores y consultar cada
   proyecto donde vive: existencia, adopción, licencia, **fecha del último movimiento**,
   asuntos abiertos. Para GitHub basta `https://api.github.com/repos/<dueño>/<nombre>`.
2. **Leer la descripción propia del proyecto — y «propia» significa el README y la ayuda
   de su herramienta, no el rótulo de una línea.** Hay tres niveles y no dicen lo mismo:
   | Nivel | Quién lo escribe y para qué | Cuánto fiarse |
   |---|---|---|
   | Lo que dice el divulgador | Para que usted haga clic | Nada. Es el punto de partida del cotejo, no una fuente |
   | El rótulo de una línea del repositorio | El autor, para que quepa | Orienta. **No alcanza para concluir** |
   | El README | El autor, para que se entienda | Bien. Aquí aparecen las distancias reales |
   | **`--help` de su propia herramienta** | El programa, enumerando lo que hace | **El único que no puede mentir** |
   🚦 **Caso que lo enseñó, y que costó una corrección publicada (7-nov-2026):** se conclu-
   yó que una herramienta «no hacía lo que el hilo decía» a partir de su rótulo de una
   línea. El README mostró después que sí hacía buena parte de ello, y **la ayuda del CLI
   mostró lo que de verdad importaba y no estaba en ninguna de las dos descripciones: que
   no era un programa independiente, sino una habilidad cuya extracción ejecuta el agente
   anfitrión**, con el consiguiente gasto de cupo propio y escritura dentro del inventario.
   **La objeción decisiva casi nunca está en el rótulo: está en cómo se ejecuta.**
3. **Identificar el MECANISMO, no el producto.** Lo transferible es «sistema de diseño
   declarado en un archivo único que el agente lee» o «grafo con cada arista explicada».
   **El mecanismo sobrevive al repositorio**; el paquete, no.
4. **Reescribirlo en el estilo de la casa, con sus compuertas.** Las skills ajenas no
   traen la gobernanza de datos, el navegador único, las cuentas ni la voz de esta casa.
   Lo que entra tiene que poder convivir con lo que ya hay, y quedar enlazado en la red.
5. **Medir el costo en el listado antes de añadir.** Cada skill nueva consume presupuesto
   de activación **de todas las demás**.

**La pregunta correcta nunca es «¿esto es bueno?» sino «¿es mejor que lo que
desplazaría?».** Cuando no se tiene nada, instalar es barato. Con una red de más de 180
nodos y cero huérfanas, cada incorporación se paga con la salud del conjunto.

## Qué NO hacer / compuertas 🚦

- 🚦 **Nunca instalar un paquete grande de skills ajenas en bloque.** El listado de
  nombres y descripciones tiene presupuesto acotado y **al desbordarlo se descartan
  descripciones, empezando por las menos invocadas**. Sin descripción no hay activación
  automática: la skill existe y nunca se usa. Añadir cientos de golpe **no suma capacidad:
  apaga en silencio parte de la que ya hay**. Detalle del mecanismo en
  [[skills-empaquetar-procedimiento]].
- 🚦 **Antes de instalar, averiguar QUIÉN EJECUTA el trabajo.** Un paquete que se
  describe como herramienta puede ser, en realidad, una habilidad cuya extracción corre
  **dentro del agente de la casa**: gasta cupo propio, escribe en el inventario de
  habilidades y a veces pide una línea en el archivo de constitución. Eso no se ve en las
  estrellas ni en el rótulo. Se ve en el README, en `--help` y en las dependencias: **si los
  clientes de modelo están en extras opcionales, el paquete por sí solo no llama a ninguno
  — lo llama el anfitrión.** Comprobación de una línea: buscar si existe una vía sin modelo
  y qué tipos de archivo cubre.
- 🚦 **Nunca apuntar una herramienta de ingestión a material reservado.** Grafos,
  indexadores y «memorias» leen todo lo que se les señala. Expedientes, cédulas,
  escrituras y modelos financieros reales quedan fuera. Las pruebas se hacen sobre
  material de nivel 1 y 2 — el Aula, las skills — → [[gobernanza-datos-financieros-ia]].
- 🚦 **Las estrellas no miden calidad, pero la fecha del último empuje sí informa.** Un
  proyecto quieto varios meses en un terreno que cambia cada semanas es **fuente, no
  dependencia**: se cosecha su contenido y no se depende de él.
- 🚦 **Adopción muy por delante de la madurez = probar en copia.** Muchas estrellas, pocos
  meses de vida y cientos de asuntos abiertos describen un proyecto caliente, no uno
  estable.
- 🚦 **Atribución institucional contra cuenta personal.** «De la empresa X» cuando el
  repositorio vive en una cuenta personal cambia quién lo mantendrá. Comprobar el dueño.

## Protocolo de uso

Ante un catálogo, producir una **tabla de decisión** con una fila por pieza y tres
columnas: *qué es según el propio proyecto* · *decisión* · *razón y condición escrita*.
Decisiones admitidas, y solo estas cuatro:

| Decisión | Cuándo |
|---|---|
| **Adoptar el patrón** | El mecanismo resuelve un problema real del hábitat; se reescribe aquí |
| **Cosechar contenido** | El material vale, el proyecto no se mantiene o no hace falta como dependencia |
| **Observar · probar en copia** | Relevante pero inmaduro, o toca material sensible |
| **Descartar** | Resuelve un problema que aquí no existe. **Se escribe la razón** |

**La razón escrita del descarte es parte del entregable:** evita volver a decidir cuando
el mismo catálogo reaparezca con otro titular.

## Cómo depurar si falla

- **«Instalamos algo y ahora otras skills no se activan»:** presupuesto del listado
  desbordado. Retirar lo añadido y medir → `/doctor`, `/skill-doctor`.
- **«Concluí una distancia y resulta que no era tal»:** se leyó el rótulo de una línea en
  vez del README. **Corregir en público donde se afirmó**, no borrar: una corrección anotada
  enseña más que un acierto.
- **«La herramienta no hace lo que decía el hilo»:** se saltó el paso 2. La descripción
  del divulgador no es la del proyecto.
- **«El proyecto que adoptamos dejó de mantenerse»:** faltó mirar la fecha del último
  empuje, o se tomó como dependencia algo que debía cosecharse.
- **«No sabemos si ya decidimos sobre esto»:** la razón del descarte no quedó escrita.
- **«Indexó cosas que no debía»:** se apuntó a una carpeta sin clasificar antes el nivel
  del material.

## Portabilidad (revisar el 20% al reusar)
Los cinco pasos valen para cualquier catálogo —extensiones, bibliotecas, proveedores,
plantillas— porque el problema no es técnico sino de **costo de sistema**: toda
incorporación compite con lo instalado. Lo que cambia al reusar es dónde se verifica el
origen y cuál es el presupuesto que se desborda.

## Reuso (no empezar de cero)
Para el mecanismo del fallo silencioso y los cinco números,
[[skills-empaquetar-procedimiento]]. Para la seguridad de una pieza concreta antes de
instalarla, [[auditar-skills-antes-de-instalar]]. Para el ciclo de destilar y archivar,
[[llave-maestra-autoaprendizaje-ia]]. Para exigir origen rastreable,
[[segundo-cerebro-anclaje-verificable]]. Para separar garantía de sugerencia,
[[bucle-verificacion-garantia-vs-sugerencia]].

## Ejemplos de invocación
- «Mira estos siete repos, ¿los instalo?»
- «Hay un paquete con 273 skills para Claude Code.»
- «¿Esta herramienta nos sirve o nos estorba?»
- «¿Qué hacemos con esta lista de herramientas de IA?»

## Vecindad en la red
Gobierno del inventario: [[skills-empaquetar-procedimiento]],
[[auditar-skills-antes-de-instalar]], [[llave-maestra-autoaprendizaje-ia]].
Verificación y anclaje: [[segundo-cerebro-anclaje-verificable]],
[[bucle-verificacion-garantia-vs-sugerencia]], [[auditoria-evidencia-cuatro-niveles]].
Datos: [[gobernanza-datos-financieros-ia]].
