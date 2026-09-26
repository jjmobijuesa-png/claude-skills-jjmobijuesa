---
name: gobernanza-datos-financieros-ia
description: |
  Decide QUÉ DATO puede salir del computador hacia un modelo de IA y cuál no,
  antes de pegarlo. Clasifica en cuatro niveles (público, interno, confidencial,
  de tercero), define la técnica de desidentificación para cada uno y fija dónde
  puede procesarse cada nivel: Claude Code local, Gemini en la nube, un chat
  compartido, o en ningún sitio.

  Nace de un hueco real: esta casa maneja cifras de socios, clientes, la COAC,
  bancos y contrapartes en litigio, y las procesa a diario con IA. El riesgo no
  es que el modelo «aprenda»: es que un dato de un tercero termine en un hilo
  compartido, en una carpeta espejo de Drive o en un informe que se reenvía.

  Regla que gobierna todo: el dato de un TERCERO no es del usuario, y el
  consentimiento para que él lo tenga no es consentimiento para procesarlo fuera.

trigger_phrases:
  - "puedo pasarle estos datos a la IA"
  - "esto es confidencial"
  - "anonimiza esta información"
  - "qué datos puedo subir a Gemini / a un chat compartido"
  - "gobernanza de datos"
  - "clasifica la sensibilidad de este archivo"
idioma_de_salida: español
nivel_madurez: aplicada
dominio: gobernanza de datos / riesgo
metadata:
  version: 1.0
  fecha: "2026-09-05"
  origen: "hueco detectado al destilar el canal Nicolas Boucher Finance (video fJIU2_dflJI, confidencialidad de datos al usar IA), decidido expresamente por el usuario"
  relacionada: cfo-virtual-44-agentes, cfo-mensual-con-claude, orquestacion-multimodelo-mobijuesa360, multi-agente-gemini-coprocesador, auditoria-evidencia-cuatro-niveles, memoria-financiera-inteligenciada
---

# Skill `gobernanza-datos-financieros-ia`

## Doctrina

El riesgo de usar IA con datos financieros casi nunca es el que se teme. No es que el modelo
«memorice» un balance: es que **el dato cambia de custodio sin que nadie lo decida**. Un número que
nació en una conciliación bancaria termina en un hilo compartido por enlace; una tabla con nombres de
compradores acaba en una carpeta espejo que dos asistentes de IA leen; un informe con el precio de un
proveedor se reenvía a quien negocia contra ese proveedor.

**La pregunta correcta no es «¿es seguro el modelo?» sino «¿de quién es este dato y quién podrá verlo
después de que yo lo pegue?».**

Y una asimetría que manda sobre las demás: **los datos propios son suyos y usted decide; los datos de
terceros no lo son.** Que un cliente le haya dado su cédula para una promesa de compraventa no
autoriza a pasarla por un servicio de terceros. Ese consentimiento cubre un uso, no todos.

## Los cuatro niveles

| Nivel | Qué es | Ejemplos en esta casa | Dónde puede procesarse |
|---|---|---|---|
| **N1 · Público** | Ya publicado o publicable sin daño | Tasas del BCE, precio internacional de la palma, marco legal VIS, catálogo académico | Cualquier modelo, cualquier hilo, sin restricción |
| **N2 · Interno** | Propio y sin terceros identificables | Costo por m² propio, cronograma de obra, presupuesto interno, plantillas | Claude local y Gemini con cuenta propia. **No en hilos compartidos por enlace** |
| **N3 · Confidencial propio** | Propio y con daño si se filtra | Caja consolidada, DSCR, deuda y saldos, márgenes reales, estrategia de negociación, claves | **Solo procesamiento local.** Nunca en un hilo compartido ni en carpeta espejo sin cifrar |
| **N4 · De tercero** | No es suyo, aunque lo tenga | Cédulas y datos de compradores, nómina, cifras de socios y de la COAC, documentos de contraparte en litigio, precios de proveedores bajo acuerdo | **Desidentificar antes de cualquier uso.** El dato crudo no sale del computador |

## Protocolo — antes de pegar

> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

1. **Clasificar en voz alta.** «Esto es N3» o «esto es N4». Si duda entre dos niveles, es el más alto.
2. **Preguntar por el destino, no por la herramienta:** ¿esto va a quedar en un hilo que puede
   compartirse por enlace, en una carpeta que otro asistente lee, o en un informe que se reenvía?
3. **Desidentificar lo que sea N4** con la técnica que corresponda (abajo).
4. **Verificar que el análisis sigue siendo posible** con el dato desidentificado. Casi siempre lo es:
   para calcular una elasticidad no hace falta saber quién compró, solo cuánto y cuándo.
5. **Dejar rastro:** anotar en el informe qué se sustituyó, para poder reconstruirlo después.

## Técnicas de desidentificación, de menor a mayor pérdida

| Técnica | Cómo | Cuándo | Qué conserva |
|---|---|---|---|
| **Seudonimización** | «Comprador 07», «Proveedor B», «Banco 2» | Casi siempre; es la primera opción | Todo el análisis relacional |
| **Agregación** | Sumar por mes, por manzana, por cohorte | Cuando el detalle individual no aporta | Tendencias y comparaciones |
| **Escalado** | Multiplicar todas las cifras por un factor constante no revelado | Para discutir estructura sin revelar magnitud | Proporciones, márgenes y ratios **intactos** |
| **Redondeo por rangos** | «Entre 30.000 y 40.000» | Cuando la magnitud importa pero no el número | Orden de magnitud |
| **Supresión** | Sacar la columna | Último recurso: destruye análisis | Nada de esa variable |

**El escalado es la técnica infravalorada:** un modelo financiero multiplicado por un factor
arbitrario conserva TIR, márgenes, ratios y estructura de capital —todo lo que se quiere discutir—
y no revela ninguna cifra real. Sirve para pedir opinión sobre un modelo sin exponer el negocio.

## Reglas por destino en esta casa

- **Claude Code local** (este computador): admite N1, N2, N3. Es el único destino para N3.
- **Gemini con cuenta propia** ([[multi-agente-gemini-coprocesador]]): N1 y N2. Para N3 y N4, solo
  material ya desidentificado.
- **Hilos compartidos por enlace** (`claude.ai/share`, `chatgpt.com/share`): **N1 únicamente.** Un
  enlace compartido es público de hecho: no requiere sesión y se indexa.
- **Carpeta espejo de Drive** (`G:\Mi unidad`, compartida entre asistentes): N1 y N2. **Nada de N3
  sin cifrar y nada de N4 sin desidentificar** — es carpeta que otro asistente lee de forma automática.
- **Artefactos publicados**: N1 y N2. Aunque nazcan privados, están hechos para compartirse; si un día
  se comparte el enlace, el contenido va con él.

## Cinco errores que ya se pueden anticipar 🚦

1. **Pegar el Excel entero «para que tenga contexto».** El modelo necesita las columnas del análisis,
   no la hoja de nombres y cédulas que está en la pestaña de al lado.
2. **Creer que un enlace compartido es privado.** No lo es: quien tenga el enlace entra sin sesión.
3. **Desidentificar los nombres y dejar el identificador indirecto.** Un solo predio con esa superficie
   en esa manzana identifica al dueño igual que su nombre. Revisar unicidad, no solo nombres.
4. **Subir a la carpeta espejo el informe «para tenerlo a mano».** Esa carpeta es un canal entre dos
   asistentes: lo que entra ahí, se lee.
5. **Claves, tokens y credenciales en cualquier nivel.** No se clasifican: **nunca se pegan.** Si una
   clave llegó a un hilo, se rota, no se borra el mensaje.

## Cuando el dato es de un litigio

Documentos de contraparte (caso Epacem-Orojuez y similares) son **N4 con agravante**: además del
deber de reserva, su tratamiento puede discutirse en el proceso. Se procesan localmente, se citan
por identificador de foja y no se suben a ninguna nube compartida, ni siquiera desidentificados.

## Relacionado

- [[cfo-virtual-44-agentes]] · [[cfo-mensual-con-claude]] · [[memoria-financiera-inteligenciada]]
- [[orquestacion-multimodelo-mobijuesa360]] — qué modelo recibe qué
- [[analisis-variaciones-cascada]] y [[modelo-tres-estados-integrado]] — sus salidas suelen ser N3
- Origen y contexto: `E:\vars\var 5\Universidad-Abierta\notas\2026-09-05_destilacion-post-boucher.md`
