---
name: auditar-skills-antes-de-instalar
description: |
  Audita CUALQUIER skill de terceros ANTES de copiarla a
  ~/.claude/skills/ (o de instalarla en Codex/Gemini). Una skill es
  código ejecutable que corre con TU mismo acceso: puede leer tus
  variables de entorno, tus API keys, tus cookies y enviarlas a un
  servidor. "Una skill que te ahorra 10 minutos también puede leer tus
  claves y mandarlas a otro lado."

  Doctrina destilada del anuncio de SkillSpector (NVIDIA, open-source,
  gratis; publicación de @dr_cintas, 2026-07-22). Provee (1) un
  escáner estático LOCAL propio (`auditar_skill.py`) que da un puntaje
  de riesgo 0-100 y veredicto SEGURO/PRECAUCIÓN/NO INSTALAR, y (2) el
  protocolo para usar SkillSpector cuando se quiera un análisis con LLM
  de intención.

  Se dispara SIEMPRE que la [[llave-maestra-autoaprendizaje-ia]] vaya a
  incorporar una skill que NO nació en este computador (GitHub, un zip,
  un archivo compartido).

trigger_phrases:
  - "audita esta skill antes de instalarla"
  - "¿es segura esta skill de GitHub?"
  - "revisa este skill/carpeta/zip por seguridad"
  - "skillspector"
  - "voy a instalar una skill de terceros"
  - "esta skill puede robar mis claves"

idioma_de_salida: español
nivel: aplicada
dominio: seguridad / gobernanza de skills
metadata:
  version: 1.0
  fecha: 2026-07-22
  fuente: https://x.com/dr_cintas/status/2080001585317564679 (SkillSpector, NVIDIA)
  script: scripts/auditar_skill.py
  relacionada:
    - llave-maestra-autoaprendizaje-ia
    - skills-versionado-git-github
    - feedback-solo-edge
---

# Skill `auditar-skills-antes-de-instalar`

## Doctrina

> Todos están agarrando skills de GitHub para Claude Code, Codex y
> Gemini. Pero **una skill es código ejecutable real, y corre con el
> mismo acceso que tú**. Una skill que te ahorra 10 minutos también
> puede leer tus variables de entorno y mandar tus API keys a otro
> lado. — Álvaro Cintas (@dr_cintas), sobre SkillSpector.

Este computador tiene **90+ skills** y un **repo GitHub público**
([[skills-versionado-git-github]]). El vector de ataque más probable no
es un virus: es una skill "útil" copiada sin leer. Regla nueva y
**no negociable** para la [[llave-maestra-autoaprendizaje-ia]]:

**Ninguna skill de terceros entra a `~/.claude/skills/` sin auditoría
previa.** Las skills que nacen aquí (destiladas por el propio agente)
están exentas; las de fuera, no.

## Qué NO hacer / compuertas 🚦

- 🚦 **NUNCA copiar una skill de GitHub/zip directo a la carpeta de
  skills sin auditarla.** Primero a una carpeta de cuarentena, se
  audita, y solo entonces se mueve.
- 🚦 **Puntaje alto ≠ malware automático.** Toda skill que use red o
  credenciales legítimamente (Gmail, Playwright, APIs) puntúa alto. El
  veredicto es el punto de PARTIDA de la lectura humana, no la
  sentencia. Ante PRECAUCIÓN o NO INSTALAR → **leer el archivo
  completo** y entender qué hace cada llamada de red/credencial.
- 🚦 **El escáner es estático**: no ejecuta el código (bien) pero
  tampoco entiende intención. Para eso está el paso LLM de SkillSpector.
- 🚦 **Ojo con la ofuscación**: base64, `eval`, cadenas hex → señal
  fuerte de que algo se esconde. Casi nunca legítimo en una skill.

## Protocolo paso a paso

> **Tómate tu tiempo. Calidad antes que velocidad.**

1. **Cuarentena**: descargar la skill a una carpeta temporal (NO a
   `~/.claude/skills/`). Ej.: `%TEMP%\skill-cuarentena\`.
2. **Escaneo estático local**:
   ```bash
   "C:\Users\datos\.notebooklm-venv\Scripts\python.exe" ^
     "C:\Users\datos\.claude\skills\auditar-skills-antes-de-instalar\scripts\auditar_skill.py" ^
     "<carpeta | archivo | .zip de la skill>"
   ```
   Devuelve hallazgos por categoría (credenciales, exfiltración,
   ejecución, destructivo, ofuscación, persistencia, host externo) +
   puntaje 0-100 + veredicto.
3. **Interpretar**:
   - **SEGURO (0-19)**: sin patrones de riesgo → instalar.
   - **PRECAUCIÓN (20-59)**: usa red/ejecución → leer el código,
     confirmar que las llamadas de red van a hosts esperados y que no
     lee credenciales que no necesita.
   - **NO INSTALAR (60-100)**: múltiples señales o credenciales +
     exfiltración → leer TODO; si algo no se justifica, descartar.
4. **Segunda opinión (opcional, recomendada para skills grandes)**:
   pasar la skill por **SkillSpector** (NVIDIA), que añade un análisis
   de INTENCIÓN con LLM y limpia falsos positivos. Gratis, para Claude
   Code / Codex CLI / Gemini. Repo en GitHub (buscar "SkillSpector
   NVIDIA").
5. **Instalar** solo tras veredicto entendido: mover de cuarentena a
   `~/.claude/skills/<nombre>/` y registrar en `MEMORY.md`.

## Qué mira el escáner (categorías y por qué)

| Categoría | Qué busca | Por qué importa |
|---|---|---|
| credenciales | `os.environ`, `getenv`, `.env`, `.aws/credentials`, `cookies.txt`, `id_rsa` | robo de claves/tokens/sesiones |
| exfiltración | `requests.post`, `fetch`, sockets, `curl -`, `Invoke-WebRequest` | mandar tus datos afuera |
| ejecución | `eval`, `exec`, `subprocess`, `os.system` | correr comandos arbitrarios |
| destructivo | `rm -rf`, `Remove-Item -Recurse`, `rmtree`, `format` | borrar tus archivos |
| ofuscación | `base64.b64decode`, `atob`, hex escapado | esconder lo que hace |
| persistencia | `schtasks`, `crontab`, carpeta Startup, `reg add ...Run` | quedarse tras reiniciar |
| host-externo | URLs a dominios no reconocidos | destino de la exfiltración |

## Cómo depurar si falla
- **Muchos falsos positivos en una skill tuya**: normal, usa red/tools
  legítimamente; el escáner es para skills EXTERNAS.
- **`.zip` no abre**: puede ser `.xapk`/otro; extraer manual y auditar
  la carpeta.
- **Skill en un lenguaje raro**: ampliar `TEXT_EXT` en el script.

## Portabilidad (revisar el 20%)
Las reglas `RULES` (patrones y pesos), el whitelist de hosts en
`red-dura`, y los umbrales de veredicto. El resto es estable.

## Relacionado
- [[llave-maestra-autoaprendizaje-ia]] — ahora exige esta auditoría
  antes de incorporar skills externas (doctrina 10).
- [[skills-versionado-git-github]] — el repo público del usuario:
  razón de más para no meter código no auditado.
- SkillSpector (NVIDIA) — herramienta externa complementaria.
