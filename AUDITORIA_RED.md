# Auditoría de integridad de la red de skills

Fecha: 2026-09-26 · Base auditada: commit `ab61205` (Iter 4) · Alcance: 158 `SKILL.md`, 79 scripts (60 `.py`, 16 `.ps1`, 3 `.bat`).

Esta auditoría solo ve la mitad de la red que vive en este repositorio. Las notas de memoria
(`C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\`) no son accesibles desde aquí:
su existencia en disco **no se verificó**.

## 1. Resumen ejecutivo

| Indicador | Antes | Después |
|---|---:|---:|
| Menciones `[[destino]]` | 858 | 857 |
| Destinos únicos | 187 | 180 |
| A. Interno resuelto | 137 | 137 |
| B. Fuera de alcance (memoria o plugin) | 34 | 40 |
| C. Discrepancia de grafía | 12 (6 pares) | 0 |
| D. Colgante | 4 | 3 |
| Scripts fantasma | 0 | 0 |
| Skills con frontmatter defectuoso | 0 | 0 |
| Archivos modificados | | 5 `SKILL.md` + este informe |

- Ningún enlace interno a skill está roto: los 137 destinos internos resuelven a carpeta existente.
- Ningún enlace a memoria se borró, se redirigió ni se convirtió en texto.
- Quedan 5 decisiones marcadas como **requiere criterio de Francisco** (sección 4).

## 2. Clasificación de los 187 destinos únicos (estado previo a la reparación)

| Cubo | Destinos únicos | Menciones | Criterio aplicado |
|---|---:|---:|---|
| A. Interno resuelto | 137 | 775 | Existe carpeta `<destino>/SKILL.md` |
| B1. Memoria, grafía canónica | 20 | 40 | Prefijo `project_`, `feedback_`, `reference_`, `user_` |
| B2. Memoria, grafía con guion sin par | 13 | 17 | Prefijo `project-`, `feedback-`, `reference-` y ninguna variante con guion bajo en el repo |
| B3. Skill de plugin externo | 1 | 4 | `anthropic-skills:notebooklmskill` |
| C. Discrepancia de grafía | 12 | 18 | Mismo destino con guion y con guion bajo |
| D. Colgante | 4 | 4 | Ninguno de los anteriores |
| **Total** | **187** | **858** | |

Comprobaciones de grafía adicionales: 0 destinos difieren solo en mayúsculas; 0 difieren solo en acentos;
0 destinos internos escritos con guion bajo frente a una carpeta con guion.

### B1. Memoria con grafía canónica (20)

| Destino | Menciones |
|---|---:|
| `project_alfalab_uteq` | 13 |
| `reference_gemini_handshake_multiagente` | 4 |
| `project_caso_epacem_orojuez` | 2 |
| `project_diagnostico_explorador_windows` | 2 |
| `project_financiero_san_sebastian` | 2 |
| `reference_amjad_replit_emprendimiento_ia` | 2 |
| `reference_youtube_ia_cowork_jjmobijuesa` | 2 |
| `feedback_office_32bit_python_64bit_com` | 1 |
| `feedback_vba_injection_bloqueado` | 1 |
| `project_erp_antirobo_qvp` | 1 |
| `project_flujo_caja_bodegas_mobijuesa` | 1 |
| `project_fondos_bid_vela_ecualedger` | 1 |
| `project_mobijuesa_inmobiliaria` | 1 |
| `project_plan_marketing_san_sebastian` | 1 |
| `project_vista_al_rio_landing` | 1 |
| `reference_clases_magistrales_mit` | 1 |
| `reference_cuaderno_darpa` (con alias `\|Alfa Lab`) | 1 |
| `reference_cuaderno_ibpp_paraguaya` | 1 |
| `reference_revision_critica_regimen_qvp` | 1 |
| `user_role` | 1 |

Ninguna referencia a índices (`skills_index`, `skills_network`, `MEMORY`) aparece en formato `[[ ]]`;
se citan como rutas de texto.

### B2. Memoria con guion y sin variante con guion bajo (13) — no tocado

| Destino | Dónde |
|---|---|
| `feedback-aprendido` | `whatsapp-web-cdp-lectura-envio:137` |
| `feedback-monitor-primario-apagado` | `ui-tars-desktop-control-local:101` |
| `feedback-notebooklm-cuenta` | `auditor-integral-notebooklm:36` |
| `feedback-reauth-notebooklm-cosecha` | `notebooklm-login-reauth:53` |
| `project-finanza-integral-perfil-millonario` | `cfo-mensual-con-claude:75` |
| `reference-cuaderno-toma-decisiones-qvp` | `auditor-integral-notebooklm:26`, `auditoria-cognitiva-reflexiva:34`, `:96` |
| `reference-dbs-oro-tokenizado-pablogomez` | `entrenador-experto-notebooklm-ecualedger:313` |
| `reference-ebitda-bancabilidad-walterzevallos` | `control-financiero-semanal-qvp:88` |
| `reference-linkedin-finanzas-lote-fedphd` | `memoria-financiera-inteligenciada:233` |
| `reference-linkedin-ia-cognicion-lote-fedphd` | `agentic-ai-hitchhiker-guide:90`, `auditoria-cognitiva-reflexiva:70` |
| `reference-ratios-preguntas-gestion-dacosta` | `memoria-financiera-inteligenciada:225` |
| `reference-retiros-socio-gavilanez` | `memoria-financiera-inteligenciada:220` |
| `reference-tipos-flujo-caja-jordialtimira` | `control-financiero-semanal-qvp:93`, `memoria-financiera-inteligenciada:212` |

Son claramente notas de memoria, pero su grafía no coincide con la convención de disco. No se tocaron
porque no forman par dentro del repo (ver decisión 4.1).

### B3. Skill de plugin externo (1)

`[[anthropic-skills:notebooklmskill]]` (4 menciones: `analisis-cognitivo-intervenciones-qvp:34`,
`perplexity-active-use:171`, `youtube-academy-gemini-creador:124`, `youtube-corpus-jjmobijuesa:121`).
No es memoria ni skill del repo: es la skill `notebooklmskill` del plugin `anthropic-skills`, que sí está
instalada en el entorno del usuario. Fuera de alcance, correcta.

### C. Discrepancias de grafía (6 pares, 12 destinos)

| Destino canónico | Variante con guion (menciones) | Variante con guion bajo (menciones) |
|---|---|---|
| `feedback_solo_edge` | 1 (`linkedin-guardados-fedphd:31`) | 4 |
| `feedback_uso_bookmarks_archivo` | 1 (`linkedin-guardados-fedphd:47`) | 2 |
| `reference_apalancamiento_financiero_lopezmartin` | 1 (`memoria-financiera-inteligenciada:127`) | 1 |
| `reference_cuaderno_palantir` | 1 (`agentic-ai-hitchhiker-guide:106`) | 2 |
| `reference_ebitda_radiografia_zevallos` | 1 (`memoria-financiera-inteligenciada:229`) | 1 |
| `reference_gemini_pro_mobijuesa360` | 1 (`gemini-active-use:61`) | 2 |

Todos son destinos de memoria. 0 pares corresponden a skills internas.

Origen probable (hipótesis, no verificada): `regla-del-primer-tropiezo/mapear_red_skills.py` normaliza
todo destino con `slug()`, que convierte `_` en `-`. Su sección «Enlaces rotos» imprime por tanto las notas
de memoria con guion; si esa salida se usó para escribir enlaces nuevos, explica las variantes con guion.

### D. Colgantes (4)

| Destino | Dónde | Candidato más cercano (Levenshtein) | Diagnóstico |
|---|---|---|---|
| `arquitectura-financiera-escalonada` | `temple-y-sistema:202` | `arquitectura-consejo-multiagente` (18) | Sin candidato razonable en skills. `cuantificar-antes-de-pedir:173-174` la cita como «memoria compartida»: probablemente es nota de memoria sin prefijo. Ver 4.3 |
| `nombre` | `regla-del-primer-tropiezo:300` | `xlsx-to-pdf-a4` (13) | Marcador de plantilla. **Eliminado** |
| `skill-anterior` | `llave-maestra-autoaprendizaje-ia:286` | `gemini-active-use` (12) | Marcador de plantilla dentro de una instrucción. Ver 4.2 |
| `wikilink` | `regla-del-primer-tropiezo:317` | `gemini-active-use` (14) | Marcador de plantilla en tabla. Ver 4.2 |

Colgantes reales tras la reparación: **3**, y ninguno apunta a una skill que falte escribir.

## 3. Reparaciones aplicadas

| # | Archivo | Línea | Antes | Después | Motivo |
|---:|---|---:|---|---|---|
| 1 | `linkedin-guardados-fedphd/SKILL.md` | 31 | `[[feedback-solo-edge]]` | `[[feedback_solo_edge]]` | Cubo C, memoria |
| 2 | `linkedin-guardados-fedphd/SKILL.md` | 47 | `[[feedback-uso-bookmarks-archivo]]` | `[[feedback_uso_bookmarks_archivo]]` | Cubo C, memoria |
| 3 | `memoria-financiera-inteligenciada/SKILL.md` | 127 | `[[reference-apalancamiento-financiero-lopezmartin]]` | `[[reference_apalancamiento_financiero_lopezmartin]]` | Cubo C, memoria |
| 4 | `memoria-financiera-inteligenciada/SKILL.md` | 229 | `[[reference-ebitda-radiografia-zevallos]]` | `[[reference_ebitda_radiografia_zevallos]]` | Cubo C, memoria |
| 5 | `agentic-ai-hitchhiker-guide/SKILL.md` | 106 | `[[reference-cuaderno-palantir]]` | `[[reference_cuaderno_palantir]]` | Cubo C, memoria |
| 6 | `gemini-active-use/SKILL.md` | 61 | `[[reference-gemini-pro-mobijuesa360]]` | `[[reference_gemini_pro_mobijuesa360]]` | Cubo C, memoria |
| 7 | `regla-del-primer-tropiezo/SKILL.md` | 300 | ``un `[[nombre]]` que apunta`` | `un wikilink que apunta` | Marcador de plantilla |

- 7 líneas cambiadas en 5 archivos. Ningún otro contenido tocado.
- Verificación posterior: 180 destinos únicos, 0 pares con guion y guion bajo, 137 internos resueltos.
- El grafo que calcula `mapear_red_skills.py` no cambia (su `slug()` ya unificaba las grafías): 158 nodos,
  606 aristas, 1 racimo, 0 huérfanas antes y después.

## 4. Requiere criterio de Francisco

### 4.1 Trece destinos de memoria con guion y sin par (cubo B2)
- **Opción A:** pasarlos a guion bajo, igual que el cubo C.
- **Opción B:** dejarlos como están.
- **Recomendación:** A, pero solo después de comprobar en disco que el archivo existe con guion bajo.
  No se aplicó porque no hay evidencia en el repo de cómo se llama cada archivo.

### 4.2 Marcadores `[[skill-anterior]]` y `[[wikilink]]`
- **Opción A:** quitarles los corchetes igual que a `[[nombre]]` (por ejemplo, «con un enlace
  wikilink a la skill anterior»).
- **Opción B:** dejarlos, porque son instrucciones que enseñan la sintaxis.
- **Recomendación:** A. `mapear_red_skills.py` los cuenta como enlaces rotos en cada regeneración.
  No se aplicó porque la orden solo cubría `[[nombre]]`.

### 4.3 `[[arquitectura-financiera-escalonada]]`
- **Opción A:** es una nota de memoria sin prefijo: dejarla (quedaría en B).
- **Opción B:** es una skill pendiente de escribir: dejarla como colgante hasta crearla.
- **Recomendación:** A, confirmando que existe `arquitectura-financiera-escalonada.md` en `memory\`.

### 4.4 Dos rutas relativas de scripts que pertenecen a otra skill
- `agente-gui-autoaprobado-windows:87` cita `scripts/vbe_window.ps1`, que vive en `excel-macro-vba-embebido-gui/scripts/`.
- `compra-fruta-semanal-qvp:37` ejecuta `python scripts/download_all_zip.py`, que vive en `gmail-attachments/scripts/`.
- **Opción A:** escribir la ruta completa, como ya hacen otras 9 skills.
- **Opción B:** dejarlas; el contexto inmediato nombra la skill dueña.
- **Recomendación:** A en `compra-fruta-semanal-qvp`, porque es un comando ejecutable y falla si se lanza desde otra carpeta.

### 4.5 Cifra oficial de skills
Ver sección 7: decidir si el número de referencia es el del índice (154) o el del repo (158) y regenerar el índice.

## 5. Scripts fantasma

| Indicador | Valor |
|---|---:|
| Menciones `scripts/<archivo>.py\|ps1\|bat` en `SKILL.md` | 91 |
| Pares únicos (skill, script) | 78 |
| Resueltos en la propia skill | 67 |
| Resueltos con ruta explícita a otra skill | 9 |
| Resueltos por contexto en otra skill (ruta relativa, ver 4.4) | 2 |
| **Fantasma (no existen en el repo)** | **0** |

Referencias cruzadas con ruta explícita, todas existentes:
- `gmail-send-playwright/scripts/send.py` desde `cierre-jornada-apagado`.
- `pdf-escaneado-listo-para-imprimir/scripts/normalizar_a4.py` desde `impresion-local-hp-diagnostico`.
- `linkedin-guardados-fedphd/scripts/clasificar_guardados.py` desde las 7 `intereses-lkd-*`.

No verificado: scripts dentro de `*/private/` (excluidos por `.gitignore`), por ejemplo `send_drafts_attach.py`
citado en `triage-inbox-rapido-jjmobijuesa` sin ruta `scripts/`.

## 6. Frontmatter

| Comprobación | Resultado |
|---|---:|
| Skills con bloque `---` de frontmatter | 158 / 158 |
| Con `name:` | 158 / 158 |
| Con `description:` | 158 / 158 |
| `name:` igual al nombre de la carpeta | 158 / 158 |
| Discrepancias | **0** |

## 7. Descuadre 154 frente a 158

**Descartado dentro del repo:**
- Carpetas duplicadas: 0. Los 158 `name:` son únicos y coinciden con su carpeta.
- `_RnD`: 0. Está en `.gitignore` y no existe en el árbol.
- Plantillas: 0 carpetas sin `SKILL.md`; 0 carpetas de plantilla. Las 18 `intereses-*` de X.com comparten
  estructura (93 a 96 % de vocabulario común) pero cada una trata un tema distinto: no son duplicados.
- Skills absorbidas o marcadas obsoletas: 0.

**Evidencia encontrada:**

| Iteración | Commit | Cifra declarada | `SKILL.md` reales en el árbol | Diferencia |
|---|---|---:|---:|---:|
| 1 | `de90886` | 58 | 61 | +3 |
| 2 | `608d1a5` | 67 | 69 | +2 |
| 3 | `8dbcd00` | 88 (en disco) | 87 | -1 |
| 4 | `ab61205` | 154 (en disco) | 158 | +4 |

- La cifra declarada nunca ha coincidido con el árbol real; el mensaje del commit `ab61205` dice
  «154 skills en disco» en el mismo commit que deja 158.
- `regla-del-primer-tropiezo` cita `skills_index.md (154 skills)` y una red de «592 aristas» al 9-sep-2026.
  Ejecutar hoy el propio `mapear_red_skills.py` sobre el repo da **158 nodos y 606 aristas**. El índice y el
  mapa de memoria son anteriores al contenido actual del repo.

**Conclusión:** la causa más probable es **4 skills sin registrar en `skills_index.md`**, incorporadas
después de su última regeneración. No puedo nombrarlas: el índice está fuera del repo y **no se pudo
verificar**. Para obtener los nombres exactos en la máquina del usuario:

```powershell
$idx = Get-Content "C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\skills_index.md" -Raw
Get-ChildItem "C:\Users\datos\.claude\skills" -Directory |
  Where-Object { Test-Path (Join-Path $_.FullName "SKILL.md") } |
  Where-Object { $idx -notmatch [regex]::Escape($_.Name) } |
  Select-Object -ExpandProperty Name
```

Si el comando devuelve 4 nombres, esa es la respuesta. Si devuelve 0, la diferencia está en carpetas del
repo que ya no existen en disco (la sincronización añade pero no borra).

## 8. Método

- Extracción: regex `\[\[([^\]]*)\]\]` sobre los 158 `SKILL.md`; el destino es el texto antes de `|` o `#`.
- Cubo C: agrupación por destino en minúsculas, sin acentos y con `_` igual a `-`.
- Distancia de edición: Levenshtein contra los 158 nombres de carpeta.
- Scripts: regex `scripts[/\\]<archivo>.(py|ps1|bat)`, resolviendo el prefijo de carpeta cuando la ruta lo trae.
- Grafo: `regla-del-primer-tropiezo/mapear_red_skills.py` con la raíz apuntada al repo.
