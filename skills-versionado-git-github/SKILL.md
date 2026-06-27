---
name: skills-versionado-git-github
description: |
  Plan operativo para convertir `C:\Users\datos\.claude\skills\` en un
  repositorio Git versionado y publicarlo en GitHub privado de
  jjmobijuesa, sincronizando entre máquinas. Producto del consejo del
  video `oIxLOiITVwk` (Laura Cilleruelo) sumado al estado real del
  disco — 60+ skills sin control de versiones, riesgo de pérdida ante
  cualquier corrupción.

  Esta skill NO ejecuta nada por sí sola: prepara los artefactos
  (`.gitignore`, README de inventario, lista de archivos a excluir
  por contener secretos) y le da al usuario los comandos exactos para
  init + first commit + remote add + push, dejando el último paso
  bajo confirmación humana porque GitHub es operación visible al
  exterior.

trigger_phrases:
  - "versionar mis skills"
  - "git skills"
  - "subir skills a GitHub"
  - "skills marketplace personal"
  - "sincronizar skills entre PCs"

idioma_de_salida: español neutro técnico
nivel_madurez: aplicada
fuente: sesión 2026-06-26 destilada del video oIxLOiITVwk + auditoría del estado real de `C:\Users\datos\.claude\skills\`
---

# Versionado de skills en Git/GitHub

## Doctrina

Toda skill madura debe sobrevivir a una corrupción del disco. La única
forma confiable es **control de versiones distribuido**. GitHub
privado del usuario es el destino natural.

Compatible con la doctrina Javi Consuegra §7 ("Portabilidad con
revisión 80/20") y con la doctrina Jensen Huang (la arquitectura
agéntica Edge↔nube es la misma — necesita que las skills viajen).

## Fase 0 — Auditoría previa (qué NO debe subirse)

Antes de cualquier `git init`, identificar archivos sensibles que
pueden haber quedado entre las skills:

| Patrón | Razón |
|---|---|
| `*.txt` con `cookies` en nombre | Cookies de sesión |
| `*.env`, `.env*` | Variables de entorno con credenciales |
| `cookies.txt`, `storage_state.json` | Sesiones Playwright/CDP |
| `*token*`, `*secret*`, `*credentials*` | Cualquier credencial |
| `__pycache__/`, `*.pyc` | Bytecode innecesario |
| `*.sqlite`, `*.db` | Bases de datos locales |
| `*.log` | Logs con datos del usuario |

## Fase 1 — `.gitignore` estricto (preparar)

Crear en `C:\Users\datos\.claude\skills\.gitignore`:

```
# === Secretos (NUNCA versionar) ===
*.env
.env*
*token*
*secret*
*credentials*
*api_key*
cookies.txt
*.cookies
storage_state.json
*storage_state*

# === Sesiones / caches ===
browser_profile*/
*.sqlite
*.sqlite-journal
*.db
__pycache__/
*.pyc
*.pyo

# === Outputs grandes / generados ===
*.log
*.tmp
_RnD/MATRIZ_SKILLS_Y_AUTODIAGNOSTICO_backup_*.xlsx

# === Datos del usuario en references/ (caso a caso) ===
# Revisar antes de quitar este patrón:
*/references/bookmarks-curados-fdc-ec.md
```

## Fase 2 — README de inventario

Crear `C:\Users\datos\.claude\skills\README.md`:

```markdown
# Skills de Claude — jjmobijuesa

Inventario de skills personales para Claude Code, organizadas por
familia funcional. Documentación maestra en `MEMORY.md` (fuera de
este repo, en el directorio `memory/`).

## Familias

- Maestras (autoaprendizaje, autoreflexión, llave maestra)
- Intereses curados (auto-destiladas de bookmarks X.com)
- Quevepalma (control financiero, comité)
- EcuaLedger Soberana (FBSE, UTEQ, DARPA, Gerko)
- Vista al Río (inmobiliario)
- Herramientas (fetch, transcribe, audit, rebrand)
- Doctrinas (era PC agéntico, Hitchhiker AI)

## Cómo se usa

1. Clonar este repo a `~/.claude/skills/` en cualquier máquina con
   Claude Code.
2. Verificar que `MEMORY.md` separado esté en `~/.claude/projects/...`.
3. Las skills aparecen automáticamente en el listado de Skill tool.

## Licencia y privacidad

Repo PRIVADO. Curación personal del usuario. No redistribuir.
```

## Fase 3 — Comandos para el usuario (NO ejecutar sin confirmación)

```bash
cd "C:/Users/datos/.claude/skills"

# 1. Verificar archivos sensibles uno por uno
ls -la **/* 2>/dev/null | grep -iE "cookie|token|secret|\.env|storage_state" | less

# 2. Iniciar repo + ignore
git init -b main
# .gitignore + README.md ya creados por esta skill

# 3. Primer staging — revisar diff antes de commit
git add .gitignore README.md
git add */SKILL.md
git status   # ← REVISAR aquí

# 4. Si todo limpio:
git commit -m "Initial commit: 60+ skills destiladas (2026-06-26)"

# 5. Conectar con GitHub privado (el usuario lo crea primero en
#    https://github.com/new como repo PRIVADO):
git remote add origin git@github.com:<usuario_gh>/claude-skills-jjmobijuesa.git

# 6. Push inicial
git push -u origin main
```

## Fase 4 — Política de commits diarios (opcional)

Para sincronización continua, añadir a `Startup\` un `.bat`:

```bat
@echo off
cd /d "C:\Users\datos\.claude\skills"
git add -A
git diff --cached --quiet || git commit -m "auto: %DATE% %TIME%"
git push origin main 2>nul
```

Pero esto puede subir cookies si el `.gitignore` falla → mejor
manual al final de cada día con [[cierre-jornada-apagado]].

## Compuertas 🚦

1. **NO ejecutar `git push` sin auditar `git status`** — la primera
   subida debe revisarse archivo por archivo.
2. **Repo PRIVADO siempre** — verificar dos veces antes del `git
   push` inicial.
3. **NO subir el `MEMORY.md`** del directorio `memory/` — vive en
   otro path y contiene metadatos del usuario.
4. **NO subir `_RnD/` matrices con backup** — son herramientas
   internas.
5. **NO subir references con bookmarks curados** — son personales.
6. **Si una skill referencia un archivo local con ruta absoluta**,
   eso queda en el repo — aceptable; el usuario es el único
   destinatario.
7. **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

## Cómo depurar si falla

- `git push` rechazado → repo remoto requiere autenticación; ver
  https://docs.github.com/en/authentication.
- `cookies.txt` apareció en el commit → `git rm --cached cookies.txt`,
  añadir al `.gitignore`, force-push con cuidado.
- Skill no se actualiza al clonar en otra máquina → verificar que
  `~/.claude/skills/` no tenga symlinks raros.

## Relacionado

- [[claude-routines-apis-skills-github]] — capa de uso remoto.
- [[era-pc-agentico-doctrina]] — marco arquitectónico.
- [[cierre-jornada-apagado]] — momento natural del commit diario.
- [[llave-maestra-autoaprendizaje-ia]] — toda skill nueva debe pasar
  por aquí antes de ser commiteada.
