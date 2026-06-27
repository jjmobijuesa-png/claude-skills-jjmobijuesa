---
name: rebrand-terminologia-ecuablock
description: |
  Renombra terminológico seguro y trazable de los documentos del programa
  EcuaBlock / EcuaLedger Soberana (Ecuador, IBPP). Aplica reemplazos
  controlados por reglas word-boundary regex sobre DOCX, PDF, MD, scripts
  Python generadores y metadatos de NotebookLM, manteniendo intactas las
  excepciones técnico-jurídicas (Fundación Blockchain Soberana del Ecuador,
  Cámara Paraguaya de Blockchain, etc.).

  Casos de uso:
  - Renombrar el programa entero de "EcuaBlock" a "EcuaLedger Soberana"
    (o cualquier futura rebrand) preservando excepciones nominales.
  - Rebautizar el cuaderno NotebookLM y sus etiquetas.
  - Sincronizar el cambio en todos los documentos del folder
    "Proyecto Marco Regulatorio Asamblea" sin tocar la LOFPD ni su
    reglamento (que la Presidencia maneja manualmente).
  - Verificar la integridad del rebrand con conteo de ocurrencias antes
    y después.

  Esta skill NO toca la LOFPD ni el Reglamento Técnico LOFPD por defecto.
  Ese parámetro es ajustable con `--include-lofpd` solo cuando el usuario
  lo solicite explícitamente.

trigger_phrases:
  - "rebautizar EcuaBlock"
  - "renombrar EcuaBlock a"
  - "rebrand del programa"
  - "cambiar nombre del programa legislativo"
  - "aplica la skill rebrand-terminologia-ecuablock"

idioma_de_salida: español neutro técnico-jurídico

---

# Rebrand terminológico EcuaBlock → EcuaLedger Soberana (y futuros)

## Filosofía

Un cambio de marca en un expediente legislativo en curso debe cumplir:

1. **Trazabilidad bidireccional**: cada documento renombrado lleva una
   nota explícita del cambio.
2. **Excepciones taxativas**: nombres propios de entidades reales
   (Fundación Blockchain Soberana del Ecuador, Cámara Paraguaya de
   Blockchain) no se tocan.
3. **Versionado**: el documento renombrado pasa a `vN+1` y el `vN`
   anterior se elimina (folder + NotebookLM) sólo cuando el usuario lo
   ratifica.
4. **Cero ruido en filtros de redacción humana**: el reemplazo no debe
   introducir términos sensibles ni dobles espacios.

## Reglas word-boundary

El rebrand se ejecuta con un orden estricto, del patrón más específico
al más general, para evitar reemplazos parciales:

```python
REBRAND_RULES = [
    (r"\bEcuaBlock\s*-\s*IBPP\b", "EcuaLedger Soberana - IBPP"),
    (r"\bEcuaBlock\b",            "EcuaLedger Soberana"),
    (r"\becuablock\b",            "EcuaLedger Soberana"),
    (r"\bEcuablock\b",            "EcuaLedger Soberana"),
    (r"\bECUABLOCK\b",            "ECUALEDGER SOBERANA"),
]
```

Para futuros rebrand, parametrizar con:

```python
def rebrand(text, old="EcuaBlock", new="EcuaLedger Soberana"):
    rules = [
        (rf"\b{old}\s*-\s*IBPP\b", f"{new} - IBPP"),
        (rf"\b{old}\b",            new),
        (rf"\b{old.lower()}\b",    new),
        (rf"\b{old.capitalize()}\b", new),
        (rf"\b{old.upper()}\b",    new.upper()),
    ]
    for pat, repl in rules:
        text = re.sub(pat, repl, text)
    return text
```

## Excepciones (no tocar)

Los siguientes términos quedan **fuera** del rebrand bajo cualquier
circunstancia:

| Término | Razón |
|---------|-------|
| `Fundación Blockchain Soberana del Ecuador` | Razón social registrada — nombre propio |
| `FBSE` | Acrónimo de la fundación — nombre propio |
| `Cámara Paraguaya de Blockchain` | Entidad real — referencia externa |
| `LegalLedger` | Red blockchain pública peruana — marca registrada |
| `Hyperledger Fabric`, `Hyperledger Besu` | Marcas técnicas internacionales |

Estas excepciones se preservan vía `re.sub` con captura previa y
sustitución por sentinela, rebrand normal, y restitución desde la
sentinela.

## Flujo de ejecución

### Paso 0 — Confirmación de alcance

> Voy a aplicar el rebrand `<old>` → `<new>` sobre el siguiente
> conjunto de documentos:
>
> - Etapa II Ley + Reglamento
> - Etapa III Opciones A y B + Reglamento
> - (Opcional: LOFPD + Reglamento LOFPD si `--include-lofpd`)
>
> Confirma con "rebrand ratificado" o indica correcciones.

### Paso 1 — Backup

Copiar a `~/dropbox/.../backups/rebrand-YYYYMMDD/` los `vN` antes de
proceder.

### Paso 2 — Regeneración de documentos

Aplicar `rebrand()` al MD fuente (o al texto extraído del DOCX `vN`),
generar `vN+1` DOCX + PDF, con nota de versión en encabezado:

> *(VERSIÓN N+1: rebrand `<old>` → `<new>` aplicado el `<fecha>`)*

### Paso 3 — Verificación

```python
# Conteo en cada documento generado
- ocurrencias_old_restantes: debe ser 0 (o sólo en metadatos de
  trazabilidad explícita)
- ocurrencias_new: debe ser > 0
- ocurrencias_excepciones_preservadas: == antes
```

Las únicas ocurrencias del término viejo permitidas son las de la
**línea de metadatos explicativa** en el encabezado del documento
nuevo (ej. *"renombrado de EcuaBlock a EcuaLedger Soberana"*), que son
necesarias para trazabilidad legislativa.

### Paso 4 — Limpieza folder

Eliminar `vN` (DOCX + PDF + MD si existe) del folder de etapa.

### Paso 5 — Limpieza NotebookLM

```bash
notebooklm source delete -n <NB> <ID_vN>
notebooklm source add -n <NB> --type file --title "<nombre_vN+1>" <ruta_vN+1.pdf>
```

### Paso 6 — Renombre del cuaderno y etiquetas

```bash
notebooklm rename -n <NB> "<new> - IBPP"
```

Para renombrar etiquetas (categorías del panel) usar la skill
`notebooklm-reorganize` y su `rename_panel`.

### Paso 7 — Filtro post-rebrand

Aplicar la skill `redaccion-humana-legislativa` a cada documento
regenerado para confirmar que el rebrand no introdujo léxico fetiche,
clichés ni términos sensibles.

## Entregable

| Artefacto | Ubicación |
|-----------|-----------|
| Documentos `vN+1` DOCX + PDF | folder de cada etapa |
| Script Python ejecutado | `~/.notebooklm-extractos/rebrand_<old>_<new>.py` |
| Reporte de verificación | output del filtro por documento |
| Backup de `vN` | `~/dropbox/.../backups/rebrand-YYYYMMDD/` |

## Casos resueltos por esta skill

- **2026-06-01 — EcuaBlock → EcuaLedger Soberana**: aplicado a 5
  documentos de Etapas II y III; cuaderno NotebookLM renombrado a
  "EcuaLedger Soberana - IBPP"; LOFPD y Reglamento LOFPD reservados
  para edición manual del usuario.

## Antipatrones (no hacer)

- ❌ Buscar y reemplazar sin word-boundary (rompe palabras compuestas).
- ❌ Reemplazar en mayúsculas, minúsculas y mixto en un solo regex.
- ❌ Tocar nombres propios de entidades sin autorización expresa.
- ❌ Mantener el `vN` antiguo sin eliminarlo (genera confusión).
- ❌ Renombrar el cuaderno antes de subir las nuevas fuentes.

## Skills hermanas

- `notebooklm-reorganize`: para mover fuentes entre etiquetas y
  renombrar etiquetas.
- `redaccion-humana-legislativa`: para validar la calidad textual del
  rebrand.
- `tutor-mit-ecuablock`: si el rebrand afecta el material de estudio,
  re-ejecutar la metodología MIT sobre el cuaderno renombrado.
