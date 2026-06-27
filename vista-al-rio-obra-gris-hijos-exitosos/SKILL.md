---
name: vista-al-rio-obra-gris-hijos-exitosos
description: |
  Pivote estratégico del Edificio Vista al Río (INMOBILIARIA JUEZ & JUEZ,
  Quevedo) tras OLA 1 + OLA 2 cerradas con solo 2 respuestas y sin compra:
  vender los 24 departamentos restantes en MODALIDAD OBRA GRIS para mejorar
  el precio acquible del mercado, dejando que el cliente personalice la
  "obra muerta" (acabados) a media-alta gama según su gusto.

  Nicho objetivo identificado: HIJOS DE EMPRESARIOS MAYORES EXITOSOS
  (médicos, agricultores, comerciantes) que han retornado a Quevedo a
  continuar/reabrir los negocios de sus padres y están ganando bien;
  tienen intereses económicos arraigados en la ciudad.

  Mecánica comercial: brochure ejecutivo SIN PRECIO inicialmente; el
  precio se revela en la conversación, después de medir interés genuino,
  para sostener anclaje alto y abrir margen de negociación.

  Triggers:
  - "obra gris Vista al Río"
  - "pivote comercial Vista al Río"
  - "brochure sin precio para hijos retornados"
  - "personalización de acabados Vista al Río"
  - "landing / página web Vista al Río"
  - "html autocontenido del edificio"
  - "render con firma Vista al Río"
  - "prompts de render Vista al Río"

  Casos de uso:
  - Generar brochure personalizado por prospecto (concept board + ficha
    técnica + CTA sin precio).
  - Identificar/segmentar "hijos retornados" en la base calificada de
    Quevedo (OCUAFI gerencial + edad estimada 30-45 + ingreso ≥ USD 4.500).
  - Producir los prompts para renders fotorrealistas de los 3 estilos
    base (Contemporáneo, Lujo Cálido, Tropical Sofisticado).
---

# Vista al Río — Pivote Obra Gris + Hijos Retornados Exitosos

## 1. Diagnóstico que disparó el pivote

| Indicador | Valor |
|---|---|
| OLAS enviadas (1+2) | 184 invitaciones (52 PREMIUM/ALTO + 132 MEDIO-ALTO) |
| Respuestas | **2** (de ~171 entregados) |
| Conversión a interés de compra | **0%** |
| Lectura | El precio cerrado de USD 200.000 a entrega llave en mano no encaja con la disposición real a pagar del segmento alcanzable por email frío. |

## 2. Pivote comercial — la propuesta nueva

### A. Modalidad: **obra gris** + **personalización por el cliente**
- La promotora entrega el departamento en obra gris (estructura + paredes + instalaciones básicas + pisos en hormigón).
- El cliente termina la **obra muerta** (acabados: pisos, baños, cocina, carpintería, iluminación) **a su gusto**, contratando a quien quiera, en media o alta gama.
- **Precio del bien baja**, encaja con presupuestos de profesionales jóvenes pujantes.
- **Diferenciación**: el comprador se siente "dueño desde el primer ladrillo", no compra un producto enlatado.

### B. Nicho objetivo: **hijos retornados exitosos de Quevedo**
- **Quiénes**: hombres y mujeres de 30 a 45 años, hijos/herederos de médicos, agricultores, comerciantes prósperos de Quevedo.
- **Por qué regresan**: continuar el negocio familiar, abrir una clínica/consultorio propio, modernizar la finca, montar una sucursal.
- **Por qué compran este edificio**: quieren vivienda **moderna y segura** en Quevedo (su ciudad), no salir hacia Guayaquil; quieren personalizar su espacio; tienen ingresos altos pero sensibilidad al precio inicial.
- **Cómo detectarlos en la base**: combinación de OCUAFI gerencial/medical + ingreso ≥ USD 4.500 + dirección registrada en Quevedo (Los Ríos) + edad estimada por cédula 30-45.

### C. Mecánica del brochure: **sin precio inicial**
- El brochure muestra: producto, ubicación, plan de pago (estructura, no monto), beneficios de personalización, los 3 estilos de inspiración.
- **El precio se revela en conversación**, después de:
  1. Confirmar interés genuino.
  2. Conocer presupuesto del prospecto (anclar arriba o abajo del rango).
  3. Coordinar visita a obra.
- Anclaje: "Plan financiero a la medida según unidad seleccionada y nivel de acabados."

## 3. Tres estilos de inspiración para el cliente

Concept boards generados en `concepts/`:
- **Contemporáneo Minimalista** — paleta gris claro + blanco + madera natural; líneas limpias; mucha luz.
- **Lujo Cálido** — mármol travertino + nogal + dorado mate; ambiente acogedor de alta gama.
- **Tropical Sofisticado** — verde botánico + rattan natural + blanco; vista al río como protagonista.

## 4. Cómo se genera el brochure por prospecto

1. Tomar nombre y datos del prospecto.
2. Personalizar saludo (Dr./Ing./Sr.).
3. Insertar los 3 concept boards.
4. Plan de pago **sin total**, solo estructura (20% entrada, 30% cuotas, 50% hipotecario).
5. CTA: "*Para conocer el plan financiero a su medida, agendemos una llamada con el Gerente General.*"

## 5. Activos que esta skill produce
- `concept_board_contemporaneo.svg/png`
- `concept_board_lujo_calido.svg/png`
- `concept_board_tropical_sofisticado.svg/png`
- `prompts_render_fotorrealista.md` (3 prompts en inglés técnico)
- `brochure_obra_gris_template.html` (parametrizable por prospecto)

## 6. Conectores recomendados (no activos, sugeridos)
- **Generador de imagen IA** (cualquiera de: Midjourney, DALL-E 3, Imagen 3, Leonardo) — para producir renders fotorrealistas desde los prompts.
- **Canva** (`plugin:marketing:canva` ya aparece en la base como conector) — autenticar y usar para componer brochures editables con los renders.
- **Apollo / ZoomInfo** (`plugin:apollo:apollo`, `plugin:sales:zoominfo`) — enriquecer la base con edad y vínculos familiares para detectar "hijos retornados".

## 7. Reglas no negociables
- **Nunca** poner precio en el brochure inicial.
- **Nunca** mencionar "obra gris" como ahorro sino como **personalización exclusiva**.
- **Siempre** ofrecer visita a obra + llamada con el Gerente General.
- **Siempre** mantener la firma de **Soclg. Francisco Duque, MBA** y el teléfono **+593 99 387 9355**.

## 8. Landing web autocontenida — neuromarketing Klaric (nicho hijos exitosos)

> Desarrollado en sesión 2026-06-15. Doctrina: *Véndele a la mente, no a la gente* (J. Klaric).

### 8.1 Entregables y rutas
- **Fuente editable (carpeta + imágenes):** `E:\vars\var 8\2 Edif Vista al Rio\1 Planos Edf VISTA AL RIO\9 Renders\Vista-al-Rio-Landing\` (`index.html` + `renders/` = 17 imágenes). Copia de trabajo idéntica en `C:\Users\datos\Downloads\Vista-al-Rio-Landing\`.
- **Archivo AUTÓNOMO para WhatsApp/correo:** `Vista-al-Rio.html` (~7 MB) — las 17 imágenes incrustadas en Base64; es UN solo archivo que abre en cualquier celular/tablet/PC **sin la carpeta `renders/`**. Copias en Downloads raíz y en la carpeta del proyecto.
- **ZIP de deploy a hosting (sin el autónomo):** `…\9 Renders\Vista-al-Rio-Landing-deploy.zip` (~5,2 MB; `index.html` + `renders/`). Manual: `…\Vista-al-Rio-Landing\DEPLOY_HOSTING.md`. Recomendación: Cloudflare Pages drag-and-drop, slug `vista-al-rio` → `https://vista-al-rio.pages.dev`. Alternativa rápida sin cuenta: Netlify Drop (`app.netlify.com/drop`). El autónomo de 7 MB queda como respaldo offline.
- **Renders fuente:** `…\1 Planos Edf VISTA AL RIO\9 Renders` (interiores/amenities jun-2026 + exteriores 2021).

### 8.2 Estructura y palancas reptilianas (Klaric)
| Sección | Palanca |
|---|---|
| Barra "6 de 30 vendidos" | escasez / miedo a la pérdida |
| Hero "Lo lograste, ahora vívelo frente al río" | estatus + elevación |
| Manifiesto "el éxito merece una vista" | código simbólico (depto = prueba del éxito) |
| Galerías interior/exterior | lenguaje sensorial (vende imágenes, no m²) |
| Penthouse "pieza única" | exclusividad extrema |
| "Para ti / para ellos" | orgullo + devolverles todo a los padres |
| Datos duros (24, $2.000/mes, plusvalía) | el neocórtex justifica la emoción |
| Banda obra gris | cierra la brecha del nicho ("tú escribes el final") |
| Testimonios | prueba social de tribu |

Copy del hero (subtítulo) vigente: "El hogar que tu esfuerzo merece — y el lugar donde tus padres por fin **disfruten** con la mejor vista de Quevedo. Solo quedan 24 de 30."

### 8.3 Mapeo render → sección (17)
- Hero (estelar): `Render 7` → hero-penthouse.
- Interiores: `Render 1` sala atardecer · `Render 1-1` anochecer · `Render 2` sunset sofá curvo · `Render 3` tropical · `Render 4` cocina isla · `Render 5` dormitorio máster (YA trae firma) · `Render 6` sala+terraza.
- Penthouse band (noche doble altura): `Render 1-2`.
- Amenities: `terraza` (piscina infinita) · `piscina` pool deck · `gimnacio` · `comedor` (salón social/coworking) · `terraza doble altura` (lobby).
- Exteriores (3 mejores 2021): `ok 3` frente al río · `ok 2` lateral · `ok 4` acceso.

### 8.4 Firma "tal cual" (técnica clave)
- Los generadores de imagen NO reproducen un logo exacto → **NO** pedir la firma en el prompt.
- El `Render 5` (dormitorio) trae la firma quemada *Edificio / Vista al Río / QUEVEDO, LOS RÍOS, ECUADOR* (abajo-izq). Se **replica idéntica en CSS** (`.firma`: `f-pre` / `f-name` bold / `f-loc` dorado) sobre TODAS las demás imágenes; al dormitorio NO se le superpone.
- Exteriores claros → variante `.render.light .firma` en color río-profundo (texto oscuro) para legibilidad sobre fondos claros.
- En los prompts de render nuevos se reserva "a clean lower corner for a brand signature overlay (no text generated by the model)".

### 8.5 Imágenes a full color
- Sin `filter` de saturación/contraste; hero a `opacity:1`; el velo oscuro se reduce a un scrim radial mínimo SOLO en la esquina de la firma. Las imágenes se ven tal cual están renderizadas.

### 8.6 Ubicación portable (sin API key)
- Coordenadas reales: **-1.034067, -79.466126** (resueltas del link `maps.app.goo.gl/iGZ22Kng1o5qND9V6`).
- Mapa: `https://www.google.com/maps?q=-1.034067,-79.466126&hl=es&z=17&output=embed`
- Aérea satelital: el mismo con `&t=k`.
- "Cómo llegar": `https://www.google.com/maps/dir/?api=1&destination=-1.034067,-79.466126`
- Google Earth: `https://earth.google.com/web/search/-1.034067,-79.466126`
- Son URLs públicas: funcionan en cualquier dispositivo con internet, sin relación con este computador.

### 8.7 Generar el archivo autónomo (Base64)
Script reutilizable en `references/build_html_autocontenido.ps1` (lee `index.html`, incrusta cada `renders/<archivo>` como `data:` URI, escribe `Vista-al-Rio.html`). Verificación obligatoria: `Refs renders/ restantes = 0`.

### 8.8 Suite de prompts de render
Master + 5 variantes de luz/ambiente + terraza/amenities/penthouse estelar y tabla de variantes en `references/prompts_render_vista_al_rio.md`.


---

## Datos privados del caso

Los correos, nombres concretos, queries específicas y cifras del caso
del usuario están en `private/SKILL_FULL.md` (excluido del repo por
`.gitignore`). Esta versión pública conserva la doctrina metodológica
con placeholders en lugar de PII.

Para usar la skill con los datos reales, la versión en `private/` se
carga automáticamente cuando Claude detecta los triggers documentados
en el frontmatter.
