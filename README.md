# claude-skills-jjmobijuesa

Inventario personal de **skills de Claude Code** del usuario jjmobijuesa,
versionadas para portabilidad entre máquinas.

> **Repo PRIVADO**. Toda skill aquí dentro vive y respira en
> `~/.claude/skills/` de la máquina del usuario. Clonarlo a esa ruta
> restaura el agente local.

## Origen

Las skills se han ido destilando entre marzo y junio de 2026 mediante
la doctrina `llave-maestra-autoaprendizaje-ia` ("detectar brecha →
ir a la fuente → destilar el 20% → archivar como skill"). Cada
conversación con Claude que requirió aprender algo nuevo dejó
sedimento aquí.

## Cómo se usa

1. Clonar este repo en una máquina Windows con Claude Code instalado:
   ```bash
   cd ~/.claude/
   git clone git@github.com:jjmobijuesa-png/claude-skills-jjmobijuesa.git skills
   ```
2. Las skills aparecen automáticamente al iniciar Claude Code.
3. La memoria global (`MEMORY.md`) vive en
   `~/.claude/projects/<sanitized-cwd>/memory/` — repo separado.

## Estructura

```
skills/
├── llave-maestra-autoaprendizaje-ia/    # Doctrina central
├── agente-local-autoreflexivo-bookmarks/ # Meta-skill del bucle
├── intereses-*/                         # 17 skills auto-destiladas
├── <skill>/SKILL.md                     # Frontmatter + cuerpo
├── <skill>/scripts/                     # Código ejecutable opcional
└── <skill>/references/                  # Contexto largo opcional
```

## Familias de skills publicadas

| Familia | Skills |
|---|---|
| **Doctrinas** | llave-maestra, agentic-ai-hitchhiker, era-pc-agentico, agente-local-autoreflexivo |
| **Herramientas captura** | fetch-claude-share, perplexity-active-use, youtube-corpus, claude-routines-apis |
| **Documentación** | documentos-encuadrados-margenes, xlsx-a4-portrait-merge-pdf, correccion-ortografica-rae, glosario-ecualedger-corrector, aceptar-revisiones-docx |
| **EcuaLedger Soberana** | entrenador-experto-notebooklm-ecualedger, estrategia-implementacion-juridica, redaccion-humana-legislativa, mapa-mental-disertacion-juridica, defensa-apologetica-juridica, aprendizaje-pareto-juridico, articulacion-inter-comision-legislativa, sintesis-ejecutiva-mesa-presidencial, memo-institucional-juridico-fbse, inteligencia-politica-estrategica-multivectorial, rebrand-terminologia-ecuablock, metodo-mit-notebooklm-riguroso, tutor-mit-ecuablock |
| **Intereses (auto-destiladas)** | 17 skills `intereses-*` (geopolítica, IA, finanzas, espiritualidad, etc.) |
| **Doctrinas externas integradas** | osint-shadow-broker-tiempo-real, youtube-academy-gemini-creador, inventario-extensiones-edge-jjmobijuesa, skills-versionado-git-github |
| **NotebookLM** | auditor-integral-notebooklm, notebooklm-reorganize |
| **Gmail** | gmail-attachments, gmail-send-playwright |
| **Diseño / Comunicación** | infografia-creativa-ecuador-digital, neuro-oratoria-presentacion-persuasiva, presentacion-prezi-qvp |
| **Auditoría** | auditoria-cognitiva-reflexiva |
| **Cierre** | cierre-jornada-apagado |

## Modelo "split público/privado"

A partir de la iteración 2 (2026-06-27), las skills sensibles ya no
se excluyen totalmente del repo. En su lugar, cada una de ellas tiene
la estructura:

```
<skill-sensible>/
├── SKILL.md              ← PÚBLICO (doctrina, frontmatter, placeholders)
└── private/              ← LOCAL (.gitignore lo excluye)
    ├── SKILL_FULL.md     ← Copia íntegra con los datos reales
    ├── references/       ← Casos, tablas, queries con PII
    ├── scripts/          ← Código con emails/tokens hardcoded
    └── templates/        ← Plantillas de outreach con BCC reales
```

El patrón global `*/private/` en `.gitignore` excluye ese subdirectorio
de cualquier skill, presente o futura. La doctrina metodológica viaja
en el repo; los datos duros del caso del usuario se quedan en disco.

Skills con split en esta iteración:

- `triage-inbox-rapido-jjmobijuesa/`
- `comite-cuarto-guerra-qvp/`
- `estratega-ventas-inmobiliario-vista-al-rio/`
- `vista-al-rio-obra-gris-hijos-exitosos/`
- `control-financiero-semanal-qvp/`
- `memoria-financiera-inteligenciada/`
- `politica-retiros-socio-propietario/`
- `analisis-cognitivo-intervenciones-qvp/`
- `wolfram-forensic-engine/`

Quedan totalmente excluidos del repo (no aplican split):

- `_RnD/` — laboratorio interno de auto-diagnóstico.
- `*/references/bookmarks-curados-fdc-ec.md` y similares — curación
  personal del usuario.

## Doctrinas que rigen este repo

1. **Persistencia obligatoria** — ninguna skill existe hasta tener
   `SKILL.md` commiteado.
2. **Edge↔nube continuo** — toda skill debe ser portable a un
   Claude remoto sin reescritura.
3. **Fuente verificable** — cada skill cita la fuente externa
   (Perplexity, NotebookLM, YouTube ID, paper arXiv, post LinkedIn).
4. **No PII de terceros en el repo** — datos de colegas, prospectos,
   pacientes, contrapartes legales viven SOLO en disco local.

## Licencia

Sin licencia abierta. Uso personal del propietario del repo.
Curación intelectual; no redistribuir.

## Tamaño

- **67 skills publicadas** en este repo (58 + 9 saneadas en iter 2).
- **9 skills con `private/`** cuya doctrina sí está en el repo pero los
  datos duros se quedan en disco.
- Total disco (con `private/` incluido): ~1.6 MB.
- Repo público sin `private/`: ~1.3 MB.

---

_Generado por la skill [`skills-versionado-git-github`](skills-versionado-git-github/SKILL.md) el 2026-06-27._
