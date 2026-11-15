---
name: sala-limpia-reimplementacion-licita
description: |
  Rehacer lo que se admira sin copiarlo. Fija la distinción entre reconstruir a
  partir del COMPORTAMIENTO observable —lo que una página o un producto hace a la
  vista de cualquiera— y partir del material ajeno: código, archivos, código
  fuente de la página, activos. La primera vía es la sala limpia y es lícita y
  defendible; la segunda es derivada y arrastra la licencia y la autoría del
  original. Aporta la compuerta previa a clonar un diseño y el modo de declarar
  por escrito qué se tomó y qué no.

  Casos de invocación: «quiero una web como la de ese competidor», «clonemos este
  panel», «¿puedo usar este repositorio en un entregable de cliente?», «me
  gusta cómo lo hace tal empresa, hágalo igual», «¿esto es copia o inspiración?».

trigger_phrases:
  - "sala limpia"
  - "clonar un diseño"
  - "copiar una web"
  - "hazlo igual que"
  - "¿esto es copia?"
  - "reimplementar"
idioma_de_salida: español neutro técnico-instruccional
nivel_madurez: maestra
fuente: clase magistral 32 del Aula (14-nov-2026)
---

# Sala limpia: rehacer sin copiar

## Acerca de mí (cargar al arrancar)
Leer `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\user_role.md`.
Clase que la originó:
`G:\Mi unidad\5 Clases-Magistrales-HTML\04-ia-y-sistemas\32-tres-escalones-y-el-limite-declarado.html`.

## Doctrina central

> **Lo que hace defendible una reimplementación no es la calidad del resultado:
> es la vía por la que se llegó.** Dos páginas idénticas pueden tener estatus
> jurídico opuesto según de dónde salió la segunda.

| Vía | De qué se parte | Qué se produce | Estatus |
|---|---|---|---|
| **Sala limpia** | Solo del **comportamiento observable**: lo que se ve, lo que responde, lo que cualquiera percibe usándolo | Obra propia que **se parece** | Lícita y defendible. Lo que coincide es la función, no la expresión |
| **Derivada** | Del **material**: código, HTML fuente, hojas de estilo, imágenes, fuentes tipográficas, archivos del proyecto | Obra **derivada** del original | Arrastra la licencia, la autoría y las restricciones del original |

**La sala limpia no es un recinto ni un entorno aislado.** Es una **regla sobre lo que la
herramienta —o la persona— acepta mirar y lo que rehúsa mirar.** Una herramienta que
anuncia «modo sala limpia» y a la vez le enseña el código fuente no está en sala limpia:
está mal nombrada.

🚦 **Un parecido no se vuelve lícito porque el resultado sea bueno, ni ilícito porque sea
malo.** La pregunta es siempre la misma: **¿qué se miró para hacerlo?**

## La compuerta previa (hacer ANTES de tocar nada)

Cuatro preguntas, por escrito, antes de abrir el navegador o el repositorio:

1. **¿Qué quiero exactamente de ese original?** Si la respuesta es «todo», no hay
   intención propia: hay encargo de copia. Nombrar dos o tres cosas concretas
   (la jerarquía de la portada, el ritmo de los precios, el flujo de alta en tres pasos).
2. **¿Puedo describirlo sin mirar el material?** Si se puede describir de memoria y por
   fuera, es comportamiento. Si hace falta abrir el inspector, es expresión.
3. **¿Qué licencia tiene lo que voy a mirar?** Y leerla en el **texto del propio
   proyecto**, no en la ficha de la plataforma — ver [[metadatos-que-ocultan-el-dato-decisivo]].
4. **¿A quién va el resultado?** Una práctica personal y un entregable de cliente no
   tienen el mismo riesgo. El segundo exige declaración escrita.

**Si las cuatro no se pueden responder, no se empieza.** La compuerta cuesta cinco minutos;
un entregable retirado de un cliente cuesta la relación.

## Cómo se declara (el párrafo que acompaña al entregable)

Un entregable hecho en sala limpia lleva su propia declaración, breve y verificable:

> **Origen.** Esta página se construyó observando el comportamiento público de
> `<original>` el `<fecha>`: la organización de su portada y su recorrido de compra.
> No se usó su código, su hoja de estilos, sus imágenes ni sus fuentes tipográficas.
> Lo que coincide es la función; la redacción, la paleta, la retícula y el código son
> propios.

Tres propiedades de este párrafo: **dice la fecha** (el original cambia), **nombra lo que
sí se tomó** (no se esconde el parecido) y **enumera lo que no se tocó** (es falsable: se
puede comprobar comparando archivos).

🚦 **Una declaración que solo dice «de elaboración propia» no declara nada.** Declarar es
nombrar la frontera, no afirmar virtud.

## Lo que la sala limpia NO cubre

Es una regla de **expresión**, y por eso deja tres cosas fuera de su alcance:

| Queda fuera | Por qué | Qué lo rige |
|---|---|---|
| **Marcas y signos distintivos** | Un logo, un nombre o un color registrado no se vuelven libres por reconstruirse mirando | Derecho de marcas |
| **Patentes** | Protegen la función, que es precisamente lo que la sala limpia sí reproduce | Derecho de patentes |
| **Contratos y términos de uso** | Un acuerdo firmado puede prohibir lo que la ley permitiría | El contrato, que manda sobre la regla general |

Es decir: **la sala limpia resuelve la pregunta del copyright y no resuelve las otras tres.**
Confundirlas es el error más caro de este terreno.

## Qué NO hacer / compuertas 🚦

- 🚦 **No abrir el inspector del navegador «solo para ver cómo lo hacen».** A partir de ese
  momento la sala dejó de estar limpia y no hay forma de volver atrás. Si se abrió, se dice.
- 🚦 **No pegar el código ajeno «de referencia» en el proyecto propio**, ni siquiera
  comentado o en una rama aparte. El rastro queda.
- 🚦 **No fiarse del nombre del modo de una herramienta.** Comprobar qué le entra de verdad:
  si recibe una URL y descarga la página, no está trabajando por comportamiento.
- 🚦 **No reusar activos ajenos: tipografías, iconos, fotos, ilustraciones.** Son material,
  y son lo primero que un tercero detecta porque se identifican por el archivo.
- 🚦 **No clonar lo distintivo.** Reconstruir la **función** es lícito; reproducir lo que
  **identifica** al original ante su público lo hace indefendible aunque se haya hecho
  sin mirar nada.
- 🚦 **No entregar un trabajo de este tipo sin su párrafo de origen.** Sin declaración, un
  parecido legítimo es indistinguible de una copia.

## Protocolo de uso

1. **Escribir las cuatro preguntas de la compuerta** y responderlas. Si falla alguna, parar.
2. **Observar por fuera y tomar notas en palabras**, no en capturas de código: qué secciones
   hay, en qué orden, qué decide el usuario en cada paso, dónde está el precio.
3. **Cerrar la fuente.** Antes de escribir una línea, dejar de mirar el original.
4. **Construir desde las notas**, con la casa de estilo propia (en esta casa, `DESIGN.md`
   del Aula y [[entrega-visual-html-vs-texto]]).
5. **Comparar al final solo para verificar la función**, nunca para ajustar la apariencia.
   Si en ese cotejo aparece la tentación de igualar un detalle visual, no se toca.
6. **Redactar el párrafo de origen** con fecha y frontera, y adjuntarlo al entregable.

## Cómo depurar si falla

- **«El resultado salió casi idéntico y no miré el código»:** es posible y es lícito cuando
  la función es muy restrictiva (un formulario de alta, una tabla de precios). Lo que lo
  sostiene es la declaración y el poder mostrar el proceso. Guardar las notas del paso 2.
- **«Ya abrí el código fuente antes de preguntar»:** no se finge la sala limpia. Dos salidas
  honestas: declarar la obra como derivada y revisar la licencia, o parar, dejar pasar el
  proyecto a otras manos y partir de nuevo desde cero con notas propias.
- **«La licencia dice una cosa en la plataforma y otra en el repositorio»:** manda el texto
  del proyecto. Ver [[metadatos-que-ocultan-el-dato-decisivo]].
- **«El cliente pide explícitamente que quede igual que la del competidor»:** eso no es una
  reimplementación, es un encargo de copia. Decirlo en una línea, ofrecer lo que sí se puede
  hacer —la misma función con expresión propia— y dejar la decisión por escrito.
- **«La herramienta dice sala limpia y no sé si le creo»:** darle una URL y mirar su tráfico.
  Si descarga la página, no lo está.

## Portabilidad (revisar el 20 % al reusar)
El mecanismo no es de software. **Vale para un plano, un modelo financiero, un contrato, un
material docente y un proceso de obra:** rehacer a partir de lo que se ve es obra propia;
rehacer a partir del archivo ajeno es derivada. Lo que cambia al reusar es qué cuenta como
«comportamiento observable» en ese oficio —en un plano es la implantación construida, no el
DWG— y cuál es el cuerpo legal aplicable.

## Reuso (no empezar de cero)
Para separar lo que una herramienta garantiza de lo que sugiere,
[[bucle-verificacion-garantia-vs-sugerencia]]. Para montar la defensa cuando alguien discute
el parecido, [[defensa-apologetica-juridica]] y [[estrategia-implementacion-juridica]]. Para
construir la página propia por pasos, [[pagina-web-cuatro-pasos-con-ia]] y
[[entrega-visual-html-vs-texto]]. Para decidir si una herramienta ajena entra al hábitat,
[[cosechar-repositorios-de-agentes]] y [[auditar-skills-antes-de-instalar]].

## Ejemplos de invocación
- «Quiero una web como la de ese competidor.»
- «Clonemos este panel que me gustó.»
- «¿Puedo usar este repositorio en un entregable de cliente?»
- «Me gusta cómo lo hace tal empresa, hágalo igual.»
- «¿Esto que hicimos es copia o es inspiración?»

## Vecindad en la red
Jurídico: [[defensa-apologetica-juridica]], [[estrategia-implementacion-juridica]],
[[memo-institucional-juridico-fbse]].
Garantías y licencias: [[bucle-verificacion-garantia-vs-sugerencia]],
[[cosechar-repositorios-de-agentes]], [[auditar-skills-antes-de-instalar]].
Construcción: [[pagina-web-cuatro-pasos-con-ia]], [[entrega-visual-html-vs-texto]],
[[estilo-entregables-publicos-fbse]].
Hermanas de la clase 32: [[escalera-prompting-prueba-del-techo]],
[[metadatos-que-ocultan-el-dato-decisivo]].
