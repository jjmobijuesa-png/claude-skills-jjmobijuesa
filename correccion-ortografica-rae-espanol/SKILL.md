---
name: correccion-ortografica-rae-espanol
description: |
  Corrector ortográfico en español ajustado a las normas de la Real
  Academia Española (RAE) y la Asociación de Academias de la Lengua
  Española (ASALE). Detecta y corrige:

    1. Acentos faltantes (tildes diacríticas y prosódicas).
    2. Eñes mal escritas como "n" simple (Senor → Señor).
    3. Typos sistemáticos del proyecto (ej.: "Soberama" → "Soberana").
    4. Palabras duplicadas consecutivas ("que que", "la la") — el
       mismo control que Word ejecuta como autocorrección/alerta.
    5. Espacios anómalos: doble espacio, espacio antes de signo de
       puntuación, espacio después de paréntesis abierto, etc.
    6. Signos de puntuación de apertura faltantes en preguntas y
       exclamaciones (cuando aplica).
    7. Mayúsculas indebidas tras puntuación (cuando son detectables).

  La skill mantiene un diccionario curado de ~250 reglas
  word-boundary regex con foco en el vocabulario técnico-jurídico,
  institucional, legislativo y administrativo del corpus EcuaLedger
  Soberana, ampliable a cualquier corpus.

  Reutilizable para cualquier documento DOCX en español que requiera
  un pase rápido de corrección ortográfica RAE antes de envío
  oficial.

trigger_phrases:
  - "corregir ortografía RAE"
  - "aplicar reglas Real Academia Española"
  - "eliminar duplicados de palabras Word"
  - "spell-check español de los documentos"
  - "aplica la skill correccion-ortografica-rae-espanol"

idioma_de_salida: español neutro institucional-jurídico

---

# Corrección ortográfica RAE — Diccionario y reglas

## Filosofía

Un documento institucional que se envía a una instancia del Estado
debe estar **impecable ortográficamente**. Una sola palabra sin
tilde, una eñe convertida en n, una palabra duplicada por descuido,
y la solidez del argumento jurídico se devalúa.

Esta skill aplica un corrector ortográfico en español ajustado a las
normas RAE/ASALE, con foco en los errores tipográficos más
frecuentes que se producen cuando un texto pierde la codificación
UTF-8 durante una conversión, o cuando un revisor en máquina sin
teclado en español omite acentos.

## Las cuatro clases de error que se corrigen

| Clase | Ejemplo | Corrección |
|-------|---------|------------|
| **Acento faltante** | "Codigo", "Comision", "publica" | "Código", "Comisión", "pública" |
| **Eñe perdida** | "Senor", "Soberania" → "Soberanía" pero también "ano" → no se toca | "Señor"; reglas con contexto |
| **Typo sistemático** | "Soberama" (en el corpus EcuaLedger) | "Soberana" |
| **Palabra duplicada** | "que que sigue", "la la propuesta" | "que sigue", "la propuesta" |
| **Espacio anómalo** | " ,", "  " (doble), "( cosa" | ",", " " (simple), "(cosa" |

## El diccionario RAE (extracto representativo)

> El diccionario completo (≈ 250 reglas) está en
> `script-referencia.py` de esta skill. Aquí se documenta su
> estructura.

### Palabras técnico-jurídicas frecuentes

| Sin tilde | Con tilde (RAE) |
|-----------|------------------|
| Codigo | Código |
| Constitucion | Constitución |
| Disposicion | Disposición |
| Reformatoria (correcto) | Reformatoria |
| Tecnico | Técnico |
| Tecnica | Técnica |
| Republica | República |
| Politica | Política |
| Publica | Pública |
| Publico | Público |
| Soberania | Soberanía |
| Asesoria | Asesoría |
| Comision | Comisión |
| Comisiones | Comisiones (correcto, no lleva tilde) |
| Direccion | Dirección |
| Implementacion | Implementación |
| Tributario (correcto) | Tributario |
| Economico | Económico |
| Tributacion | Tributación |
| Tramite | Trámite |
| Articulo | Artículo |
| Numero | Número |
| Parrafo | Párrafo |
| Periodo | Período (o "periodo", ambas válidas; preferimos Período) |
| Solicitud (correcto) | Solicitud |

### Palabras institucionales del proyecto

| Forma errónea | Forma correcta |
|---------------|-----------------|
| Soberama | Soberana |
| EcuaLedger Soberama | EcuaLedger Soberana |
| Asesoria Constitucional | Asesoría Constitucional |
| Senor/a Presidente/a | Señor/a Presidente/a |

### Duplicados detectados por Word

Patrón general: `\b(\w+)\s+\1\b` (case-insensitive). Captura:
"que que", "la la", "y y", "el el", "de de", "se se", "no no", etc.

> **Cuidado**: hay duplicados legítimos como "Le di la papa a Juan"
> (en sentido figurado: "la la" no aparece), o nombres propios
> ("Wagga Wagga", "Pago Pago"). El corrector debe **alertar** estos
> casos en lugar de eliminar a ciegas.

## Anti-falsos positivos

Algunas reglas requieren contexto para no romper palabras válidas:

- `\bano\b` → "año" SOLO si el contexto sugiere tiempo (ej.: "el ano
  2026" → "el año 2026"). Si no hay contexto, no tocar (puede ser el
  ano anatómico — escenario raro en jurídico, pero seguro mejor
  pedir confirmación).
- `\bsene\b` → "señe" NO es palabra; mejor advertir.
- Acrónimos en mayúsculas no se tocan: FBSE, IBPP, JPRFM, MINTEL.
- Nombres propios extranjeros no se tocan: Hyperledger, Bitcoin,
  LegalLedger.

## Reglas de espaciado

| Regex | Reemplazo | Significado |
|-------|-----------|--------------|
| ` ,` | `,` | Espacio antes de coma |
| ` \.` | `.` | Espacio antes de punto |
| ` ;` | `;` | Espacio antes de punto y coma |
| ` :` | `:` | Espacio antes de dos puntos |
| `\(\s+` | `(` | Espacio tras paréntesis abierto |
| `\s+\)` | `)` | Espacio antes de paréntesis cerrado |
| `  +` | ` ` | Doble (o más) espacio reducido a uno |

## Workflow de la skill

### Paso 0 — Inventario de errores

Generar un reporte de diagnóstico antes de actuar:

```
DOC                  acentos_falt  duplicados  espacios  typos  total
B-011                          12           0         1     3     16
B-012                          16           1         0     5     22
...
```

### Paso 1 — Aplicación del diccionario

Para cada DOCX:
1. Leer texto de cada `<w:p>` (párrafo).
2. Aplicar las reglas word-boundary regex en orden.
3. Sobreescribir el primer `<w:r>` (run) del párrafo y vaciar los
   demás (preserva formato del primer run).

### Paso 2 — Eliminación de duplicados

Aplicar regex `\b(\w+)\s+\1\b` con flag IGNORECASE solo a palabras
de **3+ letras** (las cortas como "y y", "a a" pueden ser legítimas
en contextos enumerativos).

Para palabras de 1-2 letras, **alertar** sin eliminar.

### Paso 3 — Normalización de espacios

Aplicar las reglas de espaciado al final, después de los demás
ajustes (para limpiar espacios introducidos por correcciones).

### Paso 4 — Verificación

Re-ejecutar el reporte de diagnóstico del Paso 0. El total debe ser
0 o cercano a 0. Cualquier residuo se reporta para revisión humana.

## Casos especiales

- **Mayúsculas**: si la palabra está en mayúsculas (ej.: "CODIGO"),
  corregir a "CÓDIGO" (mantiene caja).
- **Title case**: "Codigo" → "Código", "codigo" → "código".
- **Acrónimos**: no tocar (regex incluye `(?![A-Z])` cuando aplica).

## Integración con la suite EcuaLedger

Esta skill se ejecuta como **última pasada** antes de generar el
PDF definitivo. El orden óptimo es:

1. `aceptar-revisiones-docx-y-comentarios` (limpiar TC y comentarios)
2. **`correccion-ortografica-rae-espanol`** ← esta skill
3. `documentos-encuadrados-margenes` (asegurar márgenes y
   justificación)
4. Conversión a PDF.

## Reglas inviolables

- ✅ Preservar el formato del primer run de cada párrafo.
- ✅ No tocar acrónimos en mayúsculas (FBSE, IBPP, BCE, MEF).
- ✅ No tocar nombres propios extranjeros.
- ✅ Aplicar duplicados solo a palabras de 3+ letras.
- ✅ Generar reporte before/after.
- ✅ Documentar typos sistemáticos del corpus en el diccionario.

## Antipatrones

- ❌ Aplicar el diccionario sin word-boundary (rompería palabras
  compuestas).
- ❌ Eliminar duplicados de 1-2 letras sin advertencia.
- ❌ Tocar acrónimos (FBSE → fbsé sería absurdo).
- ❌ Aplicar correcciones a contenido entre comillas literales
  (citas textuales pueden tener errores intencionales).
- ❌ Reescribir el documento entero en lugar de parchar in-place.

## Casos resueltos

**Junio 2026 — Paquete EcuaLedger Soberana B-011 a B-015:**
- B-011: 12 correcciones (Soberama→Soberana×3, Código, Comisión×2,
  Senor, Soberanía, República, etc.)
- B-012: 16 correcciones (Soberama×5, Asesoría, Comisión×2,
  Dirección, trámite, etc.)
- B-013: 2 correcciones (Constitución + espacio antes de coma).
- B-014: 6 correcciones (Senor, Pública×5).
- B-015: 8 correcciones (Comisión, Dirección, Senor, Pública×2,
  Soberanía, República).

Resultado: 5 cartas con ortografía RAE conforme, listas para envío
oficial.

## Skills hermanas

- `aceptar-revisiones-docx-y-comentarios` — pase previo (acepta
  revisiones del Asesor).
- `documentos-encuadrados-margenes` — pase posterior (asegura
  márgenes A4 y justificación).
- `redaccion-humana-legislativa` — filtro complementario para léxico
  no jurídico que no detecta este corrector ortográfico.
- `memo-institucional-juridico-fbse` — generador del DOCX que pasa
  por esta skill.
