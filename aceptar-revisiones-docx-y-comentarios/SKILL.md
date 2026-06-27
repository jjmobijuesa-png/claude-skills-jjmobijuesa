---
name: aceptar-revisiones-docx-y-comentarios
description: |
  Observa, lee, analiza, interpreta y edita documentos DOCX que han
  sido revisados con TRACK CHANGES (control de cambios) y COMENTARIOS
  en el margen derecho por un revisor humano (típicamente Andrés).
  Acepta automáticamente todas las inserciones, elimina todas las
  deleciones (letras en rojo tachadas), interpreta cada comentario
  para aplicar la recomendación al texto (recortar, reformular,
  eliminar secciones) y deja el documento limpio sin huella de
  revisión visible.

  Producto final: DOCX limpio sin `<w:ins>`, sin `<w:del>`, sin
  `<w:commentRangeStart/End>`, sin `word/comments.xml`, sin
  `<w:commentReference>`, y con las recomendaciones de los
  comentarios sustantivos aplicadas como ediciones reales.

  Esta skill se destila del proceso aplicado al paquete EcuaLedger
  Soberana donde Andrés revisó 4 de las 5 cartas con ~100 cambios
  cada una (mayormente acentos) y 4 comentarios sustantivos. El
  modelo es reutilizable para cualquier documento revisado por un
  asesor político-jurídico.

trigger_phrases:
  - "acepta las revisiones de Andrés"
  - "limpia los track changes del DOCX"
  - "aplica los comentarios y elimina las letras tachadas"
  - "interpreta los comentarios y edita el documento"
  - "aplica la skill aceptar-revisiones-docx-y-comentarios"

idioma_de_salida: español neutro institucional-jurídico

---

# Aceptar revisiones DOCX (Track Changes + Comentarios)

## Filosofía

Un revisor humano experimentado (asesor político, abogado, editor
institucional) edita un DOCX dejando tres tipos de huella:

1. **Inserciones** en color (típicamente rojo) que indican texto
   nuevo que debe quedarse.
2. **Deleciones tachadas** que indican texto que debe quitarse.
3. **Comentarios en el margen derecho** que indican recomendaciones
   sustantivas: eliminar una sección, reformular un argumento,
   recortar una mención inoportuna, etc.

Un asistente digital de propósito general no sabe qué hacer con esos
tres tipos de huella. Esta skill enseña al sistema a procesarlos
correctamente, dejando un documento listo para envío sin
**ninguna** huella visible de revisión.

## Paso 0 — Inspección preliminar

Antes de procesar, generar un **reporte de revisiones** que
identifique:

- Cuántas inserciones (`<w:ins>`) hay y por qué autor.
- Cuántas deleciones (`<w:del>`) hay y por qué autor.
- Cuántos comentarios (`word/comments.xml`) hay y por qué autor.
- Para cada comentario: el texto del comentario y el párrafo al que
  está vinculado.

Esto se hace leyendo el ZIP del DOCX:

```python
import zipfile, re
with zipfile.ZipFile(docx_path, 'r') as z:
    doc = z.read('word/document.xml').decode('utf-8')
    cm = z.read('word/comments.xml').decode('utf-8') if 'word/comments.xml' in z.namelist() else ''

# Autores
authors_ins = set(re.findall(r'<w:ins[^>]+w:author="([^"]+)"', doc))
authors_del = set(re.findall(r'<w:del[^>]+w:author="([^"]+)"', doc))
```

## Paso 1 — Clasificar comentarios en dos clases

Los comentarios se clasifican según su naturaleza:

| Clase | Característica | Acción |
|-------|----------------|--------|
| **Cosmético** | Sobre acento, ortografía, formato | Solo eliminar el comentario; los track changes ya hicieron la corrección |
| **Sustantivo** | Recomienda eliminar / reformular / recortar sección | Aplicar la recomendación al texto antes de eliminar el comentario |

Ejemplos de comentarios **sustantivos** detectados en EcuaLedger:

- *"No considero apropiado sugerir los procesos internos de decisión"* → **eliminar la sección entera** que sugiere procesos internos.
- *"Evento Cerrado, no es oportuno mencionar"* → **eliminar la mención del evento** del párrafo señalado.
- *"No es necesario mencionar esto, mas bien son vías paralelas"* → **eliminar la frase** que menciona alternativas.
- *"No pueden analizar la matriz en tanto no es uso público"* → **revisar y reformular** referencias al documento interno.

## Paso 2 — Aceptar track changes mecánicamente

A nivel XML, sin abrir Word:

```python
# 1) Eliminar w:del completos (incluido w:delText)
doc = re.sub(r'<w:del\s[^>]*>.*?</w:del>', '', doc, flags=re.DOTALL)

# 2) Mantener el contenido de w:ins (quitar wrapper)
doc = re.sub(r'<w:ins\s[^>]*>(.*?)</w:ins>', r'\1', doc, flags=re.DOTALL)
```

Esto preserva las inserciones de Andrés (acentos corregidos, texto
agregado) y elimina las deleciones (letras viejas sin acento).

## Paso 3 — Eliminar las marcas de comentarios

A nivel XML:

```python
doc = re.sub(r'<w:commentRangeStart\s[^/]*/>', '', doc)
doc = re.sub(r'<w:commentRangeEnd\s[^/]*/>', '', doc)
doc = re.sub(r'<w:commentReference\s[^/]*/>', '', doc)
# Limpiar w:r vacíos resultantes
doc = re.sub(r'<w:r>\s*</w:r>', '', doc)
doc = re.sub(r'<w:r\s[^>]*>\s*</w:r>', '', doc)
```

## Paso 4 — Aplicar recomendaciones sustantivas

Para cada comentario clasificado como **sustantivo**, identificar el
rango exacto del texto al que se aplica (usando
`<w:commentRangeStart>` y `<w:commentRangeEnd>` del XML antes de
limpiarlos) y aplicar la edición correspondiente:

- *Eliminar sección*: borrar todos los `<w:p>` que comprenden la
  sección.
- *Eliminar frase*: regex narrow sobre el texto del párrafo.
- *Reformular*: reemplazar el texto con la versión propuesta por el
  comentario (cuando el comentario lo sugiere) o con una versión
  inferida por la skill.

## Paso 5 — Eliminar el archivo comments.xml y sus relaciones

A nivel ZIP:

```python
# Crear nuevo ZIP sin comments.xml
with zipfile.ZipFile(src, 'r') as zin, zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zout:
    for item in zin.namelist():
        if item == 'word/comments.xml':
            continue  # No copiar
        data = zin.read(item)
        # Limpiar Content_Types.xml y document.xml.rels
        if item == '[Content_Types].xml':
            data = re.sub(rb'<Override[^/]*PartName="/word/comments\.xml"[^/]*/>', b'', data)
        if item == 'word/_rels/document.xml.rels':
            data = re.sub(rb'<Relationship[^/]*Target="comments\.xml"[^/]*/>', b'', data)
        # Reemplazar document.xml ya procesado
        if item == 'word/document.xml':
            data = cleaned_doc_xml.encode('utf-8')
        zout.writestr(item, data)
```

## Paso 6 — Verificación final

Reabrir el DOCX limpio y confirmar:

- `<w:ins` ocurrencias = 0
- `<w:del` ocurrencias = 0
- `word/comments.xml` no existe
- Las recomendaciones sustantivas fueron aplicadas (ej.: sección
  eliminada cuenta menos párrafos que el original)

## Paso 7 — Convertir a PDF

Usar el patrón del proyecto: copia al directorio corto (≤ 255 chars
total), convierte con `docx2pdf`, copia el PDF de vuelta al destino
largo. Evita el límite de Windows para Word.

## Casos resueltos (EcuaLedger Soberana — 4 documentos)

| Doc | Autor TC | Inserts | Deletes | Comentarios | Acción sustantiva |
|-----|----------|--------:|--------:|:-----------:|-------------------|
| B-011 | ANDRES | 87 | 98 | 2 (cosméticos) | Solo aceptar TC + eliminar comentarios |
| B-012 | ANDRES | 59 | 64 | 2 (1 cosmético + 1 sustantivo) | Aceptar TC + eliminar sección IV "PROPUESTA DE ARQUITECTURA INTER-COMISION" |
| B-013 | — | 0 | 0 | 0 | Sin cambios |
| B-014 | ANDRES | 106 | 105 | 0 | Solo aceptar TC |
| B-015 | ANDRES | 68 | 66 | 0 | Solo aceptar TC |

## Reglas inviolables

- ✅ Nunca abrir Word para aceptar TC (lo hacemos vía XML, más
  determinista).
- ✅ Preservar siempre las inserciones del revisor (son sus
  correcciones).
- ✅ Eliminar siempre las deleciones (es texto que el revisor
  declaró redundante).
- ✅ Clasificar cada comentario antes de actuar (cosmético vs.
  sustantivo).
- ✅ Documentar qué comentario sustantivo se aplicó cómo (para
  trazabilidad).
- ✅ Eliminar `word/comments.xml` y sus relaciones (no dejar
  huella).
- ✅ Verificar al final que el DOCX no tiene `<w:ins>` ni
  `<w:del>`.

## Antipatrones

- ❌ Aceptar TC abriendo Word manualmente (no escalable, error
  humano).
- ❌ Eliminar inserciones (perdería las correcciones del revisor).
- ❌ Preservar las marcas de comentarios sin eliminarlas (deja
  metadatos en el DOCX).
- ❌ Aplicar a ciegas cualquier comentario sustantivo sin
  interpretar (puede borrar contenido válido).
- ❌ Olvidar limpiar `[Content_Types].xml` y `document.xml.rels`.

## Skills hermanas

- `documentos-encuadrados-margenes` — para asegurar que el DOCX
  limpio se mantiene dentro de los márgenes A4 al imprimirse.
- `memo-institucional-juridico-fbse` — generador del DOCX que
  típicamente se revisa.
- `inteligencia-politica-estrategica-multivectorial` — orquestadora
  del paquete diplomático-legislativo que pasa por esta revisión.
- `redaccion-humana-legislativa` — filtro QA post-aceptación.

## Plantilla del script

El script de referencia está en `script-referencia.py` de esta
skill, parametrizable por:

- `SRC_DIR`: carpeta de DOCX a procesar.
- `DST_DIR`: carpeta de salida.
- `COMENTARIOS_SUSTANTIVOS_POR_ARCHIVO`: dict con las acciones
  específicas a aplicar.
- `SHORT_TMP`: directorio temporal de path corto para conversión PDF.

## Aplicabilidad fuera de EcuaLedger

Cualquier paquete de cartas o documentos legislativos revisados por
un asesor con track changes y comentarios. En la Matriz de Acuerdos,
las cartas a la próxima instancia recibirán revisiones análogas. La
skill se ejecuta una vez y deja la carpeta lista para envío.
