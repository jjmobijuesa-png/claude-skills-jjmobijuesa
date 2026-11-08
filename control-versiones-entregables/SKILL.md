---
name: control-versiones-entregables
description: |
  Control de versiones y cadena de publicación de un paquete de entregables financieros (libro Excel +
  PDF + presentación): nomenclatura vN (AAAA-MM-DD), carpeta por versión, fuente única de cifras
  (JSON leído del libro guardado por Excel) y validador que prueba que cada cifra y cada concepto
  citado vale lo mismo en todos los documentos. Úsela antes de entregar cualquier versión nueva.
trigger_phrases:
  - "crea la nueva versión de los entregables"
  - "revisa que los valores sean los mismos en todos los entregables"
  - "asegura que los datos cuadren en cada documento"
  - "actualiza la presentación con la nueva versión"
  - "nueva carpeta de entregables"
idioma_de_salida: español (Ecuador), trato de usted
metadata:
  version: 1.0
  fecha: 2026-10-31
  origen: paquete v2 de San Sebastián (Mobijuesa), 30/31-oct-2026
  relacionada:
    - auditoria-corrida-financiera-inmobiliaria
    - principios-financieros-puros
    - cierre-verificado-integridad
    - modelo-excel-sistema-vivo
    - wolfram-forensic-engine
    - regla-del-primer-tropiezo
---

# Skill `control-versiones-entregables`

## Doctrina en una frase
**Una cifra = un valor en todos los documentos.** Nada se teclea a mano en un entregable: todo sale
de UNA fuente (el libro recalculado y guardado por Excel), y un validador lo prueba antes de entregar.

## 1 · Nomenclatura y carpetas
- Nombre: `<nombre> vN (AAAA-MM-DD).<ext>`. La versión va en el nombre, nunca solo en el contenido.
- Carpeta por versión: `00 ENTREGABLES - vN` junto a la anterior; la anterior no se toca.
- Cada libro lleva una hoja `CONTROL DE VERSIONES` (versión, fecha, cambio, origen, verificación).
- Por qué: el revisor del 29-oct-2026 auditó la v6 creyendo que era la v1 (sus cifras salían al dólar
  de la v6). La confusión de versiones fue la causa raíz de media auditoría.

## 2 · La cadena de publicación (en este orden, siempre)
```
motor (Python) → libro (openpyxl, fórmulas vivas) → Excel COM: CalculateFull + guardar (valores en caché)
   → fuente_vN.json (lee el libro GUARDADO) → PDF A4 + láminas HTML + presentación (leen el JSON)
   → validador (libro ⇄ PDF ⇄ presentación) → «TODO CUADRA» → recién ahí se entrega
```
Scripts de referencia (plantillas San Sebastián v2; adaptar ruta `D`, hojas y conceptos):

| Script | Qué hace |
|---|---|
| `recalc_com.py <entrada> <salida>` | Excel propio (`DispatchEx`), `CalculateFull`, cuenta errores reales (#REF!, #DIV/0!; ignora «####» de ancho) y guarda con valores |
| `fuente_v2.py` | Lee el libro entregado por etiqueta (no por fila fija) y escribe `fuente_v2.json` con valores y textos ya formateados |
| `cruce_v2.py` | Validador: coherencia interna del libro, huella de las láminas de imagen, matriz concepto × documento, y barrido de cifras/conceptos de la versión anterior. Sale con código 1 si algo falla |

## 3 · Qué valida el cruce (y por qué cada punto)
1. **Dentro del libro**: la misma cifra en todas las hojas (ventas en RESUMEN = PyG = CRONOGRAMA =
   Σ lista de precios = SENSIBILIDAD base), Σ etapas = total en cada fila, balance = 0, caja del
   flujo = caja del balance, retorno = capital + utilidad.
2. **Láminas de imagen**: su texto es el HTML de origen y la huella SHA-1 de la imagen insertada
   debe ser la del render. Sin eso, una imagen vieja pasa cualquier revisión de texto.
3. **Gráficos nativos** de PowerPoint: categorías y valores se leen como texto. ⚠️ Son un canal de
   datos aparte: el 31-oct-2026 un gráfico de cuotas de la v1 ($284 / $295) sobrevivió a un
   reemplazo de textos perfecto. Solo lo cazó la exportación visual.
4. **Matriz concepto × documento**: para cada concepto (ventas, utilidad, retorno, TIR, VAN, pico
   del crédito, precios, cuotas, canon…), el valor del libro debe aparecer en cada documento que lo
   cita.
5. **Barrido de la versión anterior**: lista explícita de cifras y frases viejas («utilidad
   escondida», «nunca en rojo», «m² vendible», precios viejos) que no deben quedar en ningún documento.

## 4 · Cómo depurar si falla
- **El cruce falla por formato, no por dato**: normalice antes de comparar («$ 1.923.761» =
  «$1.923.761»; «−» = «-»; minúsculas porque el CSS pone títulos en mayúsculas).
- **Búsqueda por etiqueta que encuentra la fila equivocada**: «TIR anual» encontró antes «TIR anual
  mínima» (el umbral). Use coincidencia exacta cuando una etiqueta es prefijo de otra.
- **Excel y motor difieren por pocos miles**: busque prorrateos que no suman 1 (la eléctrica repartida
  por participación sin excluir la etapa 1 perdía $21.398) y MAX(0,·) aplicado por etapa en vez de al
  total (el IR por etapa no suma el IR del proyecto).
- **Notas que empiezan con «=»**: openpyxl las guarda como fórmula y Excel «repara» el libro. Toda nota
  pasa por `T()`, que antepone «Cálculo: ».
- **Reemplazar textos con regex sobre una plantilla HTML deja restos de la versión anterior**.
  Escriba la lámina completa desde la fuente única; conserve solo el CSS de la plantilla.
- **Texto nuevo más largo que la caja** de una lámina: se monta sobre la línea siguiente. Exporte
  las láminas cambiadas con PowerPoint COM (`Slide.Export`) y mírelas; acorte el texto, no la letra.
- **«Al centavo» (exigencia del CEO, 02-nov-2026)**: tolerancia del validador = $0,005, no $1. Un control de
  balance de −0,23 que «se ve en cero» por el formato de pesos es un error real: era un insumo redondeado (área de
  costo 1.098,22/18 a 4 decimales), que dejaba la etapa 1 en $796.593,60 frente a los $796.593,82 del contrato NES y la
  construcción en $7.642.634,70 frente al ancla de $7.642.635,55. Regla: **no redondear insumos ni valores intermedios**
  al escribir el libro (interés, costo capitalizado, flujo de la TIR); redondear solo al mostrar. Los PDF y las láminas
  toman las cifras del LIBRO (fuente JSON), nunca del motor; el validador compara motor = libro al centavo.
- **Un patrón de la versión anterior que es prefijo de la nueva** («del libro v2.» dentro de «del libro v2.1») da
  falsos positivos: incluya el carácter que sigue.
- **Dos fuentes del mismo supuesto** (canon $280 en el libro vs $350 + IVA en el plan comercial):
  gana la fuente documentada (memoria / plan), el libro se corrige y se anota en NOTAS.

## 5 · Checklist de entrega
- [ ] Carpeta `00 ENTREGABLES - vN` y nombres con `vN (AAAA-MM-DD)`.
- [ ] Libro recalculado y guardado por Excel: 0 errores reales, control del balance = 0.
- [ ] Motor = Excel = Wolfram en las cifras clave (utilidad, retorno, margen).
- [ ] `fuente_vN.json` regenerado desde el libro ENTREGADO (el validador lo comprueba por nombre).
- [ ] PDF y presentación regenerados desde la fuente; láminas cambiadas exportadas y revisadas a ojo.
- [ ] `cruce` → «TODO CUADRA».
- [ ] Hoja CONTROL DE VERSIONES y relevo (`ESTADO.md`) actualizados.

## Relacionadas
[[auditoria-corrida-financiera-inmobiliaria]] · [[principios-financieros-puros]] ·
[[cierre-verificado-integridad]] · [[modelo-excel-sistema-vivo]] · [[wolfram-forensic-engine]] ·
[[regla-del-primer-tropiezo]]
