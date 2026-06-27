---
name: consulta-bookmarks-fdc-ec
description: |
  Skill de consulta sobre los 5.550+ bookmarks de X.com que el usuario
  @fdc_ec ha curado. Cuando una conversación nueva necesite usar la voz,
  los autores curados, o ejemplos concretos de un tema que el usuario ha
  estado investigando, invocar esta skill para correr el helper
  consultar_intereses.py y citar tweets reales con su URL canónica.

  NO inventar tweets. NO atribuir opiniones del autor al usuario (es
  curación, no firma). NO usar este archivo como fuente de verdad
  general sobre el tema — sólo como reflejo de qué le importa al usuario.

trigger_phrases:
  - "qué tengo guardado sobre"
  - "muéstrame mis bookmarks de"
  - "qué cuentas sigo sobre"
  - "mis bookmarks de X sobre"
  - "consulta mis intereses"
  - "qué he curado sobre"

idioma_de_salida: español neutro
nivel_madurez: aplicada
fuente: bookmarks @fdc_ec exportados 2026-06-23 (5550 inicial)
---

# Consulta de bookmarks @fdc_ec

## Cuándo usar

Cuando el usuario o un agente derivado necesite **respaldar una
afirmación con su propia curación**: "según las cuentas que sigo en X,
el tema X se discute así". El output no debe inventar — debe citar
tweets reales con su URL canónica.

## Cómo usar

### Modo CLI (cualquier sesión Claude)

```bash
# Buscar dentro de un tema
python "E:/vars/var 5/X-com guardados/consultar_intereses.py" \
       --tema "ia" --top 10

# Buscar por autor
python "E:/vars/var 5/X-com guardados/consultar_intereses.py" \
       --autor MentalidadFeroz --top 5

# Buscar por keyword (regex permitido)
python "E:/vars/var 5/X-com guardados/consultar_intereses.py" \
       --query "disciplin|hábito"

# Combinar
python "E:/vars/var 5/X-com guardados/consultar_intereses.py" \
       --tema "espiritual" --query "logos|verbo"

# Listar todos los temas con conteo
python "E:/vars/var 5/X-com guardados/consultar_intereses.py" \
       --listar-temas

# Output JSON para parseo programático
python "E:/vars/var 5/X-com guardados/consultar_intereses.py" \
       --tema "geopolit" --top 20 --json
```

### Modo skill (invocación directa)

Si la pregunta cae claramente en un tema, invocar la skill hija
correspondiente que ya tiene `references/cuentas-top.md` y
`references/muestras.md` pre-cargados:

- `intereses-geopolitica-soberania`
- `intereses-educacion-aprendizaje`
- `intereses-espiritualidad-religion`
- `intereses-ia-llms`
- `intereses-vida-masculina`
- `intereses-productividad-habitos`
- `intereses-liderazgo-estrategia`
- `intereses-historia-arquetipos`
- `intereses-negocios-emprendimiento`
- `intereses-mentalidad-desarrollo`
- `intereses-finanzas-mercados`
- `intereses-salud-cuerpo`
- `intereses-filosofia`
- `intereses-blockchain-web3`
- `intereses-geopolitica-latam`
- `intereses-pensamiento-critico`

## Datos disponibles por bookmark

Cada registro en `bookmarks.json` tiene:

```
{
  "id":             "rest_id del tweet",
  "url":            "https://x.com/<author>/status/<id>",
  "author_handle":  "screen_name",
  "author_name":    "nombre mostrado",
  "created_at":     "Mon Jun 22 20:55:46 +0000 2026",
  "lang":           "en | es | ...",
  "text":           "texto completo (incluye long-form)",
  "media":          [{"type": "photo"|"video", "url": "..."}],
  "quoted":         {... mismo shape recursivo si hay tweet citado ...},
  "metrics":        {"favorite_count": int, "retweet_count": int, ...},
  "is_long_form":   true|false,
  "tombstone":      false (5550 bookmarks: 0 tombstones)
}
```

## Compuertas 🚦

1. **Citar URL canónica** siempre que se atribuya una idea.
2. **No suponer firma del usuario.** Curar ≠ aprobar; el usuario puede
   tener bookmarks de cuentas con las que disiente para estudiarlas.
3. **Si el archivo no existe** o `python` no responde, devolver
   honestamente "no puedo consultar ahora" — NUNCA inventar tweets.
4. **No leer `bookmarks.json` directamente con `Read`** salvo para
   muestras pequeñas: tiene ~7 MB y satura contexto. Usar siempre el
   helper CLI.

## Relacionado

- [[agente-local-autoreflexivo-bookmarks]] — meta-skill que mantiene
  el archivo vivo.
- [[llave-maestra-autoaprendizaje-ia]] — doctrina padre.
