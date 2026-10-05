---
name: estilo-entregables-publicos-fbse
description: |
  Reglas editoriales y de contenido, decididas por Francisco Duque el 4-oct-2026, para TODO
  entregable público de la FBSE sobre EcuaLedger Soberana (IBPP): cartas, paquetes para
  autoridades, PDF unificados, presentaciones y publicaciones. Cubre:
  - formato: márgenes, tablas indivisibles con encabezado repetido, justificado, numeración;
  - limpieza: sin notas al autor;
  - línea discursiva: Nuevo Ecuador, Ley Fintech como logro del Presidente, protagonismo de las autoridades;
  - doctrina: tesis de la secuencia, gobernanza cuatripartita, identidad digital, absolutos, «Cero costo, sin gas fees», inglés con traducción;
  - firma.
  Incluye el generador reproducible (fbse_lib + build_*).

  Úsala ANTES de redactar o regenerar cualquier pieza para autoridades o para publicar.
trigger_phrases:
  - "entregable para autoridad"
  - "carta FBSE"
  - "documento público FBSE"
  - "paquete unificado"
  - "regenera los entregables"
idioma_de_salida: español neutro, usted
nivel_madurez: aplicada (4-oct-2026)
fuente: hilo JRPFM (paquetes Farinango B-016, Basantes B-017, Ministro MDEP B-018)
---

# Estilo de entregables públicos de la FBSE

## Formato
- Tamaño carta, márgenes de 2,5 cm. Hoja membretada: logo oficial en el encabezado y dirección
  institucional en el pie.
- **Texto corrido y viñetas justificados**; **títulos centrados**.
- **Celdas de tabla sin justificar**, alineadas a la izquierda; encabezado de tabla centrado.
- **Tablas más anchas que la caja de texto: 17,6 cm**, centradas.
- **Tablas enteras en una carilla.** Si no caben, en la carilla siguiente se repite la fila de
  encabezado y **ninguna fila se parte** (`tblHeader` + `cantSplit` + `keep_with_next`). Se acepta
  que una página termine 1 o 2 cm por encima del margen inferior.
- **Numeración abajo a la izquierda.** En el PDF unificado va una sola numeración global, del tipo
  «Página N de T · EcuaLedger Soberana».
- Portada propia: logo de la FBSE, ideograma de EcuaLedger (mapa del Ecuador, nodos en red,
  anillo 25-25-25-25) y destinatario.

## Limpieza (documento público)
- **Sin notas al autor:** nada en letra pequeña gris o cursiva, ni rótulos violeta de piezas de
  NotebookLM. En el generador: variable `FBSE_PUBLICO=1`, que omite los párrafos en gris.
- Códigos sin «propuesto» (por ejemplo, «Código: B-017 / FBSE-JPRFM / 2026»).
- No repetir piezas: la infografía ya va dentro de la lección, así que no se incluye suelta.
- Cuestionario: primero **sin respuestas**; al final, **con la elección correcta** y su justificación.

## Línea discursiva
- **Nuevo Ecuador:** la propuesta se inscribe en la visión del Gobierno del Presidente Daniel Noboa
  Azín. La acompañan:
  - el PND 2025-2029 «Ecuador no se detiene»;
  - la Política de Transformación Digital 2025-2030, que nombra blockchain;
  - el Decreto 387 (servicios tecnológicos);
  - el Decreto 425 (Ministerio de Desarrollo Económico y Productivo).
- **Ley Fintech = antecedente positivo del propio Presidente.** Como asambleísta y presidente de la
  Comisión de Desarrollo Económico, la tramitó, presentó su informe al Pleno y la condujo hasta su
  aprobación (2022): un logro de su gestión. No escribir «presentó la ley», porque la iniciativa
  fue de otra asambleísta; sí «presentó su informe» y «la condujo hasta su aprobación».
- **Protagonismo de las autoridades:** la propuesta nace en la FBSE; el anuncio lo hace la Presidenta
  de la Comisión de Régimen Económico, alineada con la iniciativa presidencial; la FBSE es apoyo técnico.

## Doctrina de contenido
- **Tesis de la secuencia (sorites):** papel → bit → token → comercialización; por tanto, el
  documento hecho bit y token puede comercializarse con seguridad jurídica (derechos patrimoniales
  susceptibles de circulación). Va siempre en recuadro, con el **paso a paso** y la salvaguarda
  contra las reformas aisladas:
  - **orden:** cada eslabón se apoya en el anterior;
  - **integridad:** pasa el mismo derecho, sin repudio;
  - **soberanía:** registro y jurisdicción en el Ecuador;
  - **compacidad:** varios caminos, un solo orden.
- **Gobernanza cuatripartita** (25 % Estado, privado, academia y cooperativas) en todo documento. La
  lámina tripartita del «Riel de Certeza» quedó sustituida en la v2.
- **Identidad digital:** es integral, incorpora la firma electrónica y es un derecho universal,
  permanente y definitivo desde el nacimiento o desde que se accede a la identidad digital otorgada
  por el Estado para el uso de la IBPP.
- **Absolutos:** se mantienen como fortaleza («certeza jurídica absoluta», «riesgo nulo de ataque
  del 51 %», «grado militar»…).
- **Costo:** «Cero costo, sin gas fees (comisiones por transacción)». Siempre en dólares; nunca
  criptomonedas.
- **Inglés:** solo con su traducción a continuación (glosario automático `glosar()`).
- **Marco propio:** las tres leyes propuestas. El Paraguay es solo modelo de referencia.

## Firma
Scolg. Francisco Duque, Mba. · Presidente · Fundación Blockchain Soberana del Ecuador (FBSE) ·
Quevedo, Los Ríos · fundacionblockchainsoberana@gmail.com · **Tel. +593 993 879 355**.

## Generador reproducible
`E:\vars\var 9 FBSE\Tokenizacion Activos Reales - RWA\1 Matriz de Acuerdos\JRPFM\_generador_paquetes\`

| Script | Qué genera |
|---|---|
| `fbse_lib.py` | Estilo base |
| `build_paquetes.py` | Cartas, beneficios, anexo y hojas de ruta por institución |
| `build_unificado.py` | PDF unificados |
| `build_nlm_pdfs.py` | Lección y mapa mental |
| `build_riel_v2.py` | Riel de Certeza v2 |
| `build_linkedin.py` | Publicaciones de LinkedIn |
| `build_estrategia.py` | Estrategia |

Ejecución de las versiones finales, desde esa carpeta (las rutas de salida van con barra invertida,
porque Word las exige):
```bash
FBSE_PUBLICO=1 FBSE_FINAL=1 FBSE_SIN_PAGINA=1 FBSE_BASE="<carpeta temporal>\final" python build_paquetes.py
FBSE_PUBLICO=1 FBSE_FINAL=1 FBSE_SIN_PAGINA=1 python build_unificado.py
```
Al terminar, ejecutar [[espejo-doble-ruta-var9-fbse]].

## Vecindad en la red
[[espejo-doble-ruta-var9-fbse]] · [[agenda-gobierno-noboa-alineacion-ibpp]] · [[mapa-estado-ecuador-ibpp]] ·
[[memo-institucional-juridico-fbse]] · [[documentos-encuadrados-margenes]] · [[humanizacion-texto-sin-firma-ia]]
