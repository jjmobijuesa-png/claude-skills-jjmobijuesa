---
name: lectura-planos-lotes-superpuestos
description: >
  Deducir el uso de cada lote de un proyecto inmobiliario (vivienda, departamentos
  en condominio, parqueo, área comunal) comparando/superponiendo dos planos .jpg:
  la capa de lotes numerados y la capa de uso (colores de techo). Incluye el
  criterio de color de techo y el método de lectura de imágenes sin agotar el cupo.
metadata:
  type: reference
---

# Leer planos de lotes superpuestos para deducir el uso

Cuando el proyecto tiene **dos imágenes del mismo plano** —una con los lotes
numerados por manzana y otra con el uso pintado (colores de techo / sombreado de
condominios / parqueos)— se puede deducir lote por lote qué se construye en cada
uno sin pedírselo al usuario. Esto nació del proyecto **San Sebastián** (Mobijuesa,
Quevedo), donde había 108 departamentos en 7 condominios + 87 viviendas.

## Criterio de color de techo (San Sebastián, validado por Francisco 2026-10-26)

| Señal en el plano de uso | Significado |
|---|---|
| **Techo rojo** | Vivienda de **95 m²** (VIP) |
| **Techo blanco** | Vivienda de **112 m²** (VIP) |
| Bloque/sombra de condominio (varios lotes contiguos agrupados) | **Departamentos** (VIS 2.º segmento, con bono Yapa) |
| Franja/celda sin techo, junto a vía interna | **Parqueo** o área de circulación |
| Polígono grande central con piscina/pérgola | **Área comunal** (ya presupuestada aparte) |

Regla de cierre: **si en la matriz fuente un lote no es vivienda ni parqueo ni
comunal, fue absorbido por un condominio de departamentos.** Los condominios ocupan
varios lotes contiguos; el resto de lotes quedan como viviendas por color de techo.

### Mapa validado de San Sebastián (108 deptos en 23 lotes)

| Condominio | Dep | Manzana | Lotes |
|---|---|---|---|
| 1 | 18 | Mz 1 | 3, 4, 5 |
| 2 | 18 | Mz 2 | 6, 7, 8 |
| 3 | 12 | Mz 2 | 1, 2, 3, 4 |
| 4 | 18 | Mz 3 | 16, 15, 14 |
| 5 | 18 | Mz 3 | 13, 12, 11 |
| 6 | 12 | Mz 3 | 5, 6, 7 |
| 7 | 12 | Mz 4 | 1, 2, 3, 4 |

Área por unidad: condominio de 18 dep → 1098.22/18 = 61.0122 m²;
de 12 dep → 757.11/12 = 63.0925 m². Viviendas: 76 de 95 m² + 11 de 112 m² = 87.

## Método de lectura sin agotar el cupo de imágenes

El `Read` de imágenes se agota (~30 por sesión, «media removed: request limit» —
ver `feedback_pdf_escaneado_ocr_rapidocr`). Por eso:

1. **Si los planos son PDF**, renderizar a PNG con PyMuPDF a DPI alto solo la página
   del plano, y leer esa:
   ```python
   import fitz
   doc = fitz.open(ruta_pdf)
   doc[pagina].get_pixmap(dpi=200).save(salida_png)
   ```
2. **Leer primero el plano de lotes numerados** (una lectura) y anotar en texto la
   numeración por manzana. Luego **leer el plano de uso** (otra lectura) y anotar los
   colores por posición. No releer: trabajar sobre las dos transcripciones.
3. **Superponer mentalmente por coordenadas de manzana**, no pixel a pixel: cada
   manzana es una rejilla de lotes; el condominio es el grupo contiguo sombreado.
4. Si una zona es dudosa, usar `zoom`/recorte de esa región una sola vez en lugar de
   releer todo el plano.
5. Cerrar con la **regla de cierre** de arriba y cuadrar contra el total de la matriz
   fuente (en SS: 108 + 87 = 195). Si no cuadra, revisar qué lotes se contaron doble.

## Cómo depurar si falla

- **«media removed: request limit»**: ya se agotó el cupo de imágenes. No reintentar
  el `Read`; pasar a `rapidocr-onnxruntime` para extraer los números de lote del PNG,
  o pedir al usuario el conteo de la manzana dudosa en una línea.
- **Colores ambiguos** (rojo vs. teja vs. naranja): no adivinar el metraje; confirmar
  con el usuario el criterio de color una sola vez y anotarlo aquí como variante del
  proyecto.
- **Los dos planos no están a la misma escala/rotación**: anclar por la numeración de
  manzanas y por hitos (vía principal, área comunal), no por superposición exacta.
- **Totales no cuadran**: casi siempre un lote de condominio se contó también como
  vivienda. Restar los lotes de condominios (en SS: 23) antes de repartir viviendas.

## Enlaces

Relacionadas: [[feedback_pdf_escaneado_ocr_rapidocr]] (cupo de imágenes + OCR),
[[feedback_leer_video_local_frames]] (extraer fotogramas), [[modelo-excel-sistema-vivo]]
(cómo baja este detalle al libro de presupuesto), [[project_financiero_san_sebastian]].
