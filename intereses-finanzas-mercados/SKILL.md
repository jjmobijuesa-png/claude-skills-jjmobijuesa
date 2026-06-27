---
name: intereses-finanzas-mercados
description: |
  Skill de consulta y curación temática sobre 'Finanzas / mercados / inversión'.
  Destilada automáticamente por el pipeline autoreflexivo desde 466
  bookmarks de X.com guardados por @fdc_ec en
  `E:\vars\var 5\X-com guardados\bookmarks.json`. Cuando el usuario o un agente
  necesite referencia rápida sobre este tema (qué cuentas ha curado el usuario,
  qué tweets ancla tiene archivados, qué tono predomina), invocar esta skill.
trigger_phrases:
  - "qué tengo guardado sobre finanzas / mercados / inversión"
  - "bookmarks sobre finanzas / mercados / inversión"
  - "muéstrame mi curación de finanzas / mercados / inversión"
idioma_de_salida: español neutro
nivel_madurez: basica
fuente: pipeline autoreflexivo (autoreflex_pipeline.py)
generada: 2026-06-23 22:50
---

# Finanzas / mercados / inversión — Skill de consulta de bookmarks

## Doctrina

Esta skill no produce análisis nuevo; expone la curación que el usuario ya hizo
sobre el tema. Es una **biblioteca personal indexada**, no un experto. Cuando se
invoque, leer `references/cuentas-top.md` para ver las voces que el usuario sigue
y `references/muestras.md` para el tono.

## Cómo usarla

Para responder a una pregunta del usuario sobre este tema con su propia voz:

1. Leer `references/cuentas-top.md` y `references/muestras.md`.
2. Si la pregunta requiere búsqueda fina, correr:
   ```
   python "E:/vars/var 5/X-com guardados/consultar_intereses.py" \
          --tema "Finanzas / mercados / inversión" --query "<keyword>"
   ```
3. Citar tweets concretos con su URL canónica.

## Volumen actual

- **466** bookmarks marcados con este tema.
- **25** cuentas distintas curadas.

## Compuertas 🚦

- No inventar tweets que no estén en el archivo.
- No suponer que la opinión del autor es la opinión del usuario; es curación, no firma.
- Si el archivo de bookmarks ya no existe o el tema se vació, marcar la skill como huérfana.

## Relacionado

- Skill maestra: [[llave-maestra-autoaprendizaje-ia]]
- Pipeline que la generó: [[agente-local-autoreflexivo-bookmarks]]
- Helper de consulta: `E:\vars\var 5\X-com guardados\consultar_intereses.py`
