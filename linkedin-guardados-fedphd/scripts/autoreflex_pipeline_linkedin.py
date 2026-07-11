# -*- coding: utf-8 -*-
"""
Pipeline autoreflexivo LinkedIn — hermano del pipeline X.com.

Operacionaliza la `llave-maestra-autoaprendizaje-ia` sobre los
guardados de LinkedIn de fedphd@gmail.com.

Doctrina (idéntica a la de X.com; ver `autoreflex_pipeline.py`):
  1. Lee guardados.json (fresco tras `extraer_guardados.py`).
  2. Clasifica por tema usando los mismos buckets de
     `clasificar_guardados.py`.
  3. Para cada tema con volumen ≥ umbral:
       - Si EXISTE la skill `intereses-lkd-<tema>` → augmenta su
         `references/fuentes-linkedin-<fecha>.md`.
       - Si NO existe → crea esqueleto SKILL.md nivel "básica"
         con top autores + posts semilla.
  4. Actualiza `MEMORY.md` con la entrada de la skill nueva.
  5. Registra cada decisión en `linkedin-autoreflex.log`.

Umbrales (calibrados al volumen LinkedIn ~432 vs X.com 5550):
  - 20 posts en un tema → crear skill nueva `intereses-lkd-<slug>`.
  - 10 posts en un tema → augmentar references de skill existente.

Compuertas duras 🚦:
  - NO sobreescribe SKILL.md existentes.
  - NO crea skills duplicadas (Glob previo).
  - NO mueve archivos del usuario, sólo añade.
  - NO expone PII de terceros (solo autor público del post + URL
    canónica; los guardados son curación pública del usuario).
"""
import argparse
import datetime as dt
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT_DATA = Path(r"E:\vars\var 5\LinkedIn-guardados")
ROOT_SKILLS = Path(r"C:\Users\datos\.claude\skills")
MEMORY_INDEX = Path(
    r"C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\MEMORY.md"
)
SRC_JSON = ROOT_DATA / "guardados.json"
LOG = ROOT_DATA / "linkedin-autoreflex.log"

THEMES = {
    "finanzas-control": [
        "ebitda", "ratio", "flujo de caja", "margen", "rentabilidad",
        "bancab", "cfo", "capital de trabajo", "dscr", "roe", "roa",
        "apalanc", "retiros", "dividendo", "costos", "tesorer",
    ],
    "ia-agentes": [
        "inteligencia artificial", " ia ", "llm", "agente", "prompt",
        "gpt", "claude", "machine learning", "modelo", "copilot", "skill",
    ],
    "blockchain-fintech": [
        "blockchain", "token", "rwa", "cripto", "dlt", "web3", "fintech",
        "stablecoin", "smart contract",
    ],
    "cognicion-metacognicion": [
        "mental", "cognitiv", "sesgo", "metacogn", "pensamiento", "habito",
        "neurocien", "decisi", "kahneman",
    ],
    "liderazgo-estrategia": [
        "liderazgo", "estrategia", "gestion", "equipo", "poder",
        "negociaci", "management", "ceo",
    ],
    "empresa-familiar-pyme": [
        "empresa familiar", "pyme", "socio", "propietario", "sucesion",
        "familiar",
    ],
    "juridico-legislativo": [
        "ley", "constituci", "reforma", "asamblea", "norma", "regulaci",
        "decreto",
    ],
}

# Slugs para skills (kebab-case, prefijo lkd para distinguir de X.com)
SLUG_PREFIX = "intereses-lkd-"

DESCRIPTIONS = {
    "finanzas-control": "Finanzas, control financiero, ratios y ebitda",
    "ia-agentes": "IA, LLMs, agentes y prompt engineering",
    "blockchain-fintech": "Blockchain, tokenización RWA y fintech",
    "cognicion-metacognicion": "Cognición, metacognición y sesgos",
    "liderazgo-estrategia": "Liderazgo, gestión y estrategia",
    "empresa-familiar-pyme": "Empresa familiar y PYME",
    "juridico-legislativo": "Jurídico-legislativo y regulatorio",
}


def classify(text):
    tl = " " + (text or "").lower() + " "
    hits = [k for k, kws in THEMES.items() if any(w in tl for w in kws)]
    return hits or ["sin-clasificar"]


def log(msg):
    ts = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")
    print(msg)


def top_authors(posts, n=10):
    c = Counter(
        (p.get("author") or "?").strip() for p in posts if p.get("author")
    )
    return c.most_common(n)


def seed_examples(posts, n=8):
    lines = []
    for p in posts[:n]:
        a = (p.get("author") or "?").strip()
        s = re.sub(r"\s+", " ", p.get("text") or "")[:180]
        u = p.get("url") or ""
        lines.append(f"- **{a}** · {s} … <{u}>")
    return "\n".join(lines)


def create_skill(slug, tema, posts):
    """Crea skill esqueleto nivel 'básica'."""
    skill_dir = ROOT_SKILLS / slug
    if skill_dir.exists():
        return False, "ya existe"
    skill_dir.mkdir(parents=True)
    fecha = dt.date.today().isoformat()
    desc = DESCRIPTIONS.get(tema, tema)
    top = top_authors(posts)
    top_md = "\n".join(f"  - {a}: {n} posts" for a, n in top) or "  - (n/d)"
    seeds = seed_examples(posts)

    md = f"""---
name: {slug}
description: |
  Skill de consulta y curación temática sobre "{desc}" a partir de las
  PUBLICACIONES GUARDADAS de LinkedIn (cuenta fedphd@gmail.com).
  Auto-destilada por el pipeline autoreflexivo LinkedIn el {fecha}
  desde {len(posts)} posts guardados. Hermana de la skill X.com
  `intereses-{tema.replace('lkd-', '')}`.
trigger_phrases:
  - "qué guardé en LinkedIn sobre {tema}"
  - "autores de LinkedIn sobre {desc.lower()}"
  - "posts LinkedIn {tema}"
idioma_de_salida: español
nivel: básica
dominio: aprendizaje / consulta
metadata:
  version: 1.0
  fecha: {fecha}
  origen: pipeline autoreflexivo LinkedIn (autoreflex_pipeline_linkedin.py)
  fuente: E:\\vars\\var 5\\LinkedIn-guardados\\guardados.json
  relacionada: linkedin-guardados-fedphd, agente-local-autoreflexivo-bookmarks
---

# Skill `{slug}`

## Doctrina

Skill auto-destilada desde los guardados de LinkedIn del usuario
fedphd@gmail.com. NO firma las opiniones de los autores curados —
son señal de qué le importa al usuario. Cada consulta debe citar
URL canónica del post.

## Autores top del tema (LinkedIn)

{top_md}

## Posts semilla ({len(posts)} en total a la fecha)

{seeds}

## Cómo consultar

Para respuestas frescas sobre "{desc}" desde LinkedIn:

```bash
# Consultar el JSON global
python "C:/Users/datos/.claude/skills/linkedin-guardados-fedphd/scripts/clasificar_guardados.py"
# Revisar la sección "{tema}" del análisis generado
```

## Reglas

- Solo lectura de guardados públicos. Nunca publicar.
- Citar URL canónica (`linkedin.com/feed/update/urn:li:activity:...`).
- No atribuir opinión del autor curado al usuario.
"""
    (skill_dir / "SKILL.md").write_text(md, encoding="utf-8")
    return True, f"creada ({len(posts)} posts semilla)"


def augment_skill(slug, tema, posts):
    """Añade references/fuentes-linkedin-<fecha>.md a skill existente."""
    skill_dir = ROOT_SKILLS / slug
    if not skill_dir.exists():
        return False, "skill no existe"
    refs = skill_dir / "references"
    refs.mkdir(exist_ok=True)
    fecha = dt.date.today().isoformat()
    dest = refs / f"fuentes-linkedin-{fecha}.md"
    if dest.exists():
        return False, "ya augmentada hoy"

    top = top_authors(posts)
    top_md = "\n".join(f"- {a}: {n}" for a, n in top) or "- (n/d)"
    seeds = seed_examples(posts, n=15)

    md = f"""# Fuentes recientes desde LinkedIn ({fecha}) — {tema}

Snapshot del pipeline autoreflexivo LinkedIn. **{len(posts)} posts**
del tema `{tema}` capturados hasta {fecha}.

## Autores top

{top_md}

## Posts

{seeds}

---
_Auto-generado. No editar a mano — se regenera en el próximo run._
"""
    dest.write_text(md, encoding="utf-8")
    return True, f"augmentada ({len(posts)} posts)"


def update_memory_index(new_skills):
    """Añade líneas al MEMORY.md para las skills nuevas creadas."""
    if not new_skills or not MEMORY_INDEX.exists():
        return
    body = MEMORY_INDEX.read_text(encoding="utf-8")
    if "## Skills `intereses-lkd-*`" in body:
        # Ya hay sección — no duplicar
        return
    new_lines = ["", "## Skills `intereses-lkd-*` (LinkedIn)", ""]
    new_lines.append(
        "Auto-destiladas desde los guardados de LinkedIn (fedphd@gmail.com) "
        "por el pipeline autoreflexivo LinkedIn."
    )
    new_lines.append("")
    for slug, tema, n in new_skills:
        desc = DESCRIPTIONS.get(tema, tema)
        new_lines.append(f"- [{slug}](C:\\Users\\datos\\.claude\\skills\\{slug}\\SKILL.md) — {desc} ({n} posts semilla).")
    # Insertar antes de la sección Project
    if "\n## Project\n" in body:
        body = body.replace("\n## Project\n", "\n".join(new_lines) + "\n\n## Project\n")
    else:
        body += "\n" + "\n".join(new_lines) + "\n"
    MEMORY_INDEX.write_text(body, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--min-create", type=int, default=20,
        help="Umbral mínimo para crear skill nueva (default 20)"
    )
    ap.add_argument(
        "--min-augment", type=int, default=10,
        help="Umbral mínimo para augmentar skill existente (default 10)"
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not SRC_JSON.exists():
        log(f"ERROR: {SRC_JSON} no existe. Corre extraer_guardados.py antes.")
        sys.exit(1)

    data = json.loads(SRC_JSON.read_text(encoding="utf-8"))
    log(f"Pipeline LinkedIn: {len(data)} posts en guardados.json")

    buckets = defaultdict(list)
    for d in data:
        for th in classify(d.get("text", "")):
            buckets[th].append(d)

    new_skills_created = []
    n_aug = 0
    for tema, posts in sorted(buckets.items(), key=lambda x: -len(x[1])):
        if tema == "sin-clasificar":
            continue
        slug = SLUG_PREFIX + tema
        exists = (ROOT_SKILLS / slug).exists()

        if args.dry_run:
            action = "CREATE" if not exists else "AUGMENT"
            log(f"[DRY] {action} {slug}: {len(posts)} posts")
            continue

        if not exists and len(posts) >= args.min_create:
            ok, msg = create_skill(slug, tema, posts)
            log(f"CREATE {slug}: {msg}")
            if ok:
                new_skills_created.append((slug, tema, len(posts)))
        elif exists and len(posts) >= args.min_augment:
            ok, msg = augment_skill(slug, tema, posts)
            log(f"AUGMENT {slug}: {msg}")
            if ok:
                n_aug += 1
        else:
            log(f"SKIP {slug}: {len(posts)} posts (bajo umbral)")

    if new_skills_created and not args.dry_run:
        update_memory_index(new_skills_created)
        log(f"MEMORY.md actualizado con {len(new_skills_created)} entradas nuevas")

    log(f"FIN — creadas: {len(new_skills_created)}, augmentadas: {n_aug}")


if __name__ == "__main__":
    main()
