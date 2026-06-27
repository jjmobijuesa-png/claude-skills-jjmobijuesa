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

## Lo que NO está en este repo

Por privacidad de terceros, confidencialidad profesional y prudencia
financiera, las siguientes skills viven SOLO en el disco local del
usuario y **no se suben aquí** (ver `.gitignore` para la lista
exacta):

- `triage-inbox-rapido-jjmobijuesa/` — contiene correos de colegas,
  contables, abogados, contactos bancarios.
- `estratega-ventas-inmobiliario-vista-al-rio/` — listas de
  prospectos inmobiliarios.
- `vista-al-rio-obra-gris-hijos-exitosos/` — perfiles segmentados.
- `comite-cuarto-guerra-qvp/` — correos de equipo y agenda interna.
- `control-financiero-semanal-qvp/`, `memoria-financiera-inteligenciada/`,
  `politica-retiros-socio-propietario/`, `analisis-cognitivo-intervenciones-qvp/`
  — datos financieros internos de Quevepalma.
- `wolfram-forensic-engine/references/` — caso forense EPACEM /
  Oro Juez bajo confidencialidad.
- `_RnD/` — matriz interna de auto-diagnóstico.

Estas skills son **refactorizables**: su doctrina metodológica
puede volverse pública moviendo los datos duros a un archivo externo
fuera del repo. Iteración futura.

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

- ~55 skills publicadas en este repo.
- ~10 skills retenidas en local por las razones del bloque anterior.
- Total disco: ~1.6 MB.

---

_Generado por la skill [`skills-versionado-git-github`](skills-versionado-git-github/SKILL.md) el 2026-06-27._
