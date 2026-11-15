---
name: metadatos-que-ocultan-el-dato-decisivo
description: |
  Toda ficha, tarjeta, resumen o vista previa automática elige UN valor donde el
  original tiene varios, y lo que descarta suele ser justo lo que decide. Esta
  skill fija el mecanismo —el resumen no miente, simplifica, y la simplificación
  cae siempre del mismo lado— y da la prueba de cuatro pasos para no citar una
  ficha como si fuera la fuente. Casos reales verificados: el acortador que
  devuelve página de cortesía en vez de redirección, el campo único de licencia
  que oculta una licencia doble, el inventario repartido en tres plataformas y
  el dato atrapado dentro de una imagen.

  Casos de invocación: «la ficha dice tal licencia», «¿a dónde lleva este enlace
  acortado?», «la vista previa muestra otra cosa», «cité la tarjeta del
  repositorio», «el resumen y el documento no coinciden».

trigger_phrases:
  - "metadatos"
  - "la ficha dice"
  - "enlace acortado"
  - "vista previa"
  - "dato decisivo"
  - "la tarjeta del repositorio"
idioma_de_salida: español neutro técnico-instruccional
nivel_madurez: maestra
fuente: clase magistral 32 del Aula (14-nov-2026)
---

# Los metadatos ocultan el dato decisivo

## Acerca de mí (cargar al arrancar)
Leer `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md`.
Clase que la originó:
`G:\Mi unidad\5 Clases-Magistrales-HTML\04-ia-y-sistemas\32-tres-escalones-y-el-limite-declarado.html`.

## Doctrina central

> **Un resumen automático no miente: simplifica. Y la simplificación cae siempre del
> mismo lado —el que cabe en un campo—.** Donde el original dice dos cosas, la ficha
> escoge una; la que descarta es, con una frecuencia incómoda, la que decidía.

La trampa no es la mala fe de la plataforma. Es **estructural**: una ficha tiene un campo
`licencia`, un campo `título`, un campo `descripción`. Cuando la realidad no es un valor
único, el campo no se parte: **se recorta**. Y el recorte queda indistinguible de un dato
completo, porque se presenta con el mismo formato.

🚦 **Una ficha no es una fuente. Es una fuente comprimida con pérdida, y la pérdida no está
señalada.** Citarla equivale a citar de oído.

## Los cuatro casos verificados (14-nov-2026)

| Caso | Qué muestra la capa de arriba | Qué hay debajo | Cómo se ve |
|---|---|---|---|
| **Acortador `lnkd.in`** | Un enlace que parece llevar a un sitio | **No hay redirección HTTP**: devuelve **200** con una página de cortesía, y el destino real va dentro del cuerpo de la respuesta | Un cliente automático que solo sigue redirecciones **cree haber llegado** y se queda en la cortesía |
| **Campo único de licencia** | La plataforma informa **una** licencia | El proyecto la declara **doble** en su propio texto (`MIT OR Apache-2.0`): el usuario elige | Comparando la ficha con el `README` y el archivo de licencia del propio proyecto |
| **Inventario repartido** | Una lista de ocho elementos como si fueran homogéneos | Viven en **tres plataformas distintas**, con condiciones, precios y accesos diferentes | Comprobando los ocho uno por uno, no el primero y por analogía el resto |
| **Dato dentro de una imagen** | Una captura que «ya trae la información» | El texto está en píxeles: no se busca, no se cita literalmente, no se verifica | El dato no aparece al buscar la cadena en la página |

**El patrón común:** en los cuatro, **la capa de resumen era correcta en su propio
formato y falsa como afirmación sobre el mundo.**

## La prueba de cuatro pasos

Antes de citar cualquier ficha, tarjeta, vista previa o resumen automático:

1. **¿Este dato puede tener más de un valor a la vez?** Licencias, precios por región,
   versiones, autorías, idiomas, estados. Si puede, el campo único **ya es sospechoso**.
2. **¿Qué dice el texto que el autor escribió?** No la ficha de la plataforma: el `README`,
   el pie de la página, el archivo de licencia, el documento original.
3. **¿Lo comprobé uno por uno o lo extendí por analogía?** Un inventario se verifica
   elemento a elemento. El primero no responde por los otros siete.
4. **¿El dato es texto buscable o está dentro de una imagen?** Si está en una imagen, o se
   transcribe declarándolo, o no se cita como verificado.

**Los pasos 1 y 2 atrapan los dos primeros casos; el 3 y el 4, los dos últimos.** Los
cuatro cuestan minutos. Un entregable corregido delante del cliente cuesta la credibilidad
del resto del documento.

## El fallo que más duele: corregir al autor estando equivocado

El caso de la licencia doble tiene una moraleja asimétrica. La ficha decía **una** licencia;
el autor había escrito **dos**. Si se hubiera confiado en la ficha, el entregable habría
**«corregido» al autor** —con tono de autoridad— y la corrección habría sido el error.

🚦 **Antes de señalar un error ajeno, verificar en la fuente del autor, no en la capa que la
resume.** Una corrección equivocada no es un error simétrico a no corregir: **destruye la
confianza en todo el documento**, incluidas las partes que estaban bien.

## Qué NO hacer / compuertas 🚦

- 🚦 **No citar una ficha como fuente.** Se cita el texto del autor; la ficha se usa para
  encontrarlo, nunca para afirmarlo.
- 🚦 **No dar por resuelto un enlace acortado porque un cliente automático devolvió 200.**
  Comprobar el destino en el cuerpo de la respuesta o abrirlo en el navegador integrado.
  Ver [[regla-del-primer-tropiezo]] antes de intentar una segunda variante propia.
- 🚦 **No extender por analogía en inventarios.** Ocho elementos son ocho comprobaciones.
  Y si quedan sin confirmar, **se dice cuáles**: ver cobertura declarada en
  [[auditoria-evidencia-cuatro-niveles]].
- 🚦 **No citar texto atrapado en una imagen sin declararlo.** Transcribir y decir que se
  transcribió; con páginas largas, [[feedback_pdf_escaneado_ocr_rapidocr]].
- 🚦 **No tomar el título de la vista previa por el título del documento.** Son dos campos
  distintos y los fija gente distinta.
- 🚦 **Nunca corregir públicamente a un autor sin haber leído su propio texto.**

## Protocolo de uso

1. **Separar lo que se tiene en dos columnas:** «leído en la fuente del autor» y «leído en
   una capa de resumen». Casi siempre la segunda columna es la más larga.
2. **Aplicar la prueba de cuatro pasos** a cada dato de la segunda columna que vaya a
   sostener una conclusión. A los demás, no: eso sería inventariar por inventariar.
3. **Mover a la primera columna lo que se confirme**, con la cita del texto original.
4. **Lo que no se pueda confirmar, se declara sin confirmar y con nombre propio.** No se
   borra ni se disimula: se nombra. Una laguna declarada es evidencia; una laguna tapada es
   un error en espera.
5. **Fechar la comprobación.** Las cifras de una plataforma cambian: lo medido hoy no
   describe lo de hace nueve días. Ver [[prediccion-con-reloj]].

## Cómo depurar si falla

- **«El acortador me devuelve 200 y no sé a dónde va»:** no es un error de red, es una
  página de cortesía. El destino está en el cuerpo. Si el cliente de línea de comandos no
  lo deja ver, abrirlo en el navegador integrado — **cambio de mecanismo, no tercera
  variante del mismo**.
- **«La ficha y el documento se contradicen»:** manda el documento del autor. Siempre. Y la
  contradicción misma es un hallazgo que vale escribir.
- **«Tengo veinte elementos y no puedo comprobarlos todos»:** comprobar los que sostienen
  la conclusión y **declarar la cobertura**: «5 de 8 confirmados; los 3 restantes, sin
  confirmar». Eso es un entregable honesto; «8 elementos» a secas no lo es.
- **«El dato solo existe en una captura de pantalla»:** transcribirlo, declarar que viene de
  una imagen y, si decide algo importante, buscar la fuente en texto antes de usarlo.
- **«Ya publiqué citando la ficha y estaba mal»:** corregir en una línea, sin ceremonia,
  diciendo qué dato cambia y qué conclusión se mantiene.

## Portabilidad (revisar el 20 % al reusar)
El mecanismo no es de plataformas digitales. **Es el de cualquier capa que resume un
original en campos de tamaño fijo:** una ficha catastral frente a la escritura, una partida
presupuestaria frente al contrato, un asiento contable frente a la factura, un resumen de
expediente frente al expediente. Lo que cambia al reusar es cuál es «el texto del autor» en
ese dominio; lo que no cambia es que el campo único miente por omisión cuando la realidad
tiene dos valores.

## Reuso (no empezar de cero)
Ante el primer fallo de resolución, [[regla-del-primer-tropiezo]] —barrer antes de
improvisar la segunda variante—. Para la jerarquía de anclaje de una afirmación,
[[segundo-cerebro-anclaje-verificable]]. Para los niveles y la cobertura de la evidencia,
[[auditoria-evidencia-cuatro-niveles]]. Para la fecha de arranque de toda cifra,
[[prediccion-con-reloj]]. Para cortar por párrafo cuando la fuente es mixta,
[[corte-por-parrafo-fuente-mixta]]. Para la crítica de fuentes,
[[historiografia-cinco-filtros-fuentes]].

## Ejemplos de invocación
- «La ficha dice que la licencia es tal, ¿lo pongo así?»
- «¿A dónde lleva este enlace acortado?»
- «La vista previa muestra otro título.»
- «Cité la tarjeta del repositorio, ¿está bien?»
- «El resumen y el documento no coinciden.»

## Vecindad en la red
Verificación: [[segundo-cerebro-anclaje-verificable]],
[[auditoria-evidencia-cuatro-niveles]], [[prediccion-con-reloj]],
[[historiografia-cinco-filtros-fuentes]], [[bucle-verificacion-garantia-vs-sugerencia]].
Lectura de fuentes: [[corte-por-parrafo-fuente-mixta]],
[[feedback_pdf_escaneado_ocr_rapidocr]], [[leer-libro-excel-completo-una-pasada]].
Método: [[regla-del-primer-tropiezo]], [[llave-maestra-autoaprendizaje-ia]].
Hermanas de la clase 32: [[escalera-prompting-prueba-del-techo]],
[[sala-limpia-reimplementacion-licita]].
