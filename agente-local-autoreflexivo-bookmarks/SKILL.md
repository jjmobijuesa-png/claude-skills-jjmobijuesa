---
name: agente-local-autoreflexivo-bookmarks
description: |
  META-SKILL que documenta y orquesta el bucle persistente de aprendizaje
  basado en los bookmarks de X.com del usuario (@fdc_ec). NO es consciencia
  artificial — es un agente local autoreflexivo: cada vez que el usuario
  guarda un bookmark, el sistema lo captura, lo clasifica por tema, y si
  un umbral se cruza, augmenta una skill existente o crea una skill
  esqueleto nueva. El resultado es un inventario de skills que crece de
  forma autónoma con la curación del usuario, manteniendo a Claude
  alineado con sus intereses sin intervención manual.

  Casos de invocación:
  - "qué pasó con mis bookmarks", "cuándo fue el último refresh",
    "ejecuta el pipeline autoreflexivo".
  - El usuario menciona un tema y queremos saber qué tiene curado:
    invocar esta skill primero para conocer la arquitectura, luego la
    skill `intereses-<tema>` correspondiente.
  - Auditoría: revisar `autoreflex.log`, los snapshots, y el inventario
    de skills auto-destiladas.

trigger_phrases:
  - "agente local autoreflexivo"
  - "bucle de bookmarks"
  - "pipeline autoreflexivo"
  - "auditar mis intereses"
  - "qué hay en X-com guardados"
  - "refrescar el mapa de intereses"

idioma_de_salida: español neutro técnico-instruccional
nivel_madurez: maestra
fuente: sesión 2026-06-23 export 5550 bookmarks de @fdc_ec
---

# Agente Local Autoreflexivo — Bookmarks @fdc_ec

## Doctrina central

> Un agente local no es consciente, pero **acumula capacidad si su
> curación humana se persiste como skills**. Cada bookmark que el
> usuario guarda en X.com es una señal débil de un tema que le importa;
> cuando esas señales se acumulan sobre el mismo eje, el sistema las
> destila como skill y Claude entra en cada conversación nueva ya
> alineado con esos intereses.

Esta skill **no analiza**: orquesta el bucle. El análisis pertenece a
las skills hijas `intereses-*` que el pipeline crea.

## Arquitectura del bucle

```
┌────────────────────────────────────────────────────────────────────┐
│  1. CAPTURA (watch_bookmarks.py)                                   │
│     Edge en localhost:9222 (CDP) → tab dedicada                    │
│     → cada 5 min navega a x.com/i/bookmarks                        │
│     → intercepta respuestas GraphQL Bookmark*                      │
│     → diff vs bookmarks.json → append novedades                    │
└─────────────────────────┬──────────────────────────────────────────┘
                          │ si new_recs > 0
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  2. ANALIZA (analizar_temas.py)                                    │
│     5550+ bookmarks → 17 temas con regex + co-ocurrencias          │
│     → mapa_de_intereses.{md,json}                                  │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  3. DESTILA (autoreflex_pipeline.py)                               │
│     - Para cada tema con ≥100 bookmarks: crea skill esqueleto      │
│       intereses-<tema>/ con SKILL.md + references/                 │
│     - Para cada tema con ≥50 y skill ya existente: augmenta su     │
│       references/bookmarks-curados-fdc-ec.md                       │
│     - Actualiza MEMORY.md                                          │
│     - Loguea decisiones en autoreflex_last_run.json                │
└─────────────────────────┬──────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────────────┐
│  4. CONSULTA (consulta-bookmarks-fdc-ec skill)                     │
│     Cualquier sesión futura de Claude puede invocar                │
│     consultar_intereses.py para responder con la curación real.    │
└────────────────────────────────────────────────────────────────────┘
```

## Archivos y rutas canónicas

| Ruta                                                                  | Función                                             |
|-----------------------------------------------------------------------|-----------------------------------------------------|
| `E:\vars\var 5\X-com guardados\bookmarks.json`                        | Archivo vivo; reescrito por watcher tras cada ciclo |
| `E:\vars\var 5\X-com guardados\bookmarks.csv`                         | Espejo para hoja de cálculo                         |
| `E:\vars\var 5\X-com guardados\mapa_de_intereses.{md,json}`           | Refrescado tras cada ciclo con novedades            |
| `E:\vars\var 5\X-com guardados\autoreflex_last_run.json`              | Última decisión del pipeline                        |
| `E:\vars\var 5\X-com guardados\watcher.log`                           | Log línea-a-línea del watcher                       |
| `E:\vars\var 5\X-com guardados\autoreflex.log`                        | Log del pipeline (CREATE/AUGMENT/SKIP)              |
| `E:\vars\var 5\X-com guardados\_snapshots\<fecha>/`                   | Snapshots fechados de respaldo                      |
| `E:\vars\var 5\X-com guardados\INVENTARIO.{md,json}`                  | Hashes SHA-256 + tamaños                            |
| `C:\Users\datos\.claude\skills\intereses-*\`                          | Skills hijas auto-destiladas                        |
| `E:\vars\var 5\X-com guardados\start_edge_debug.bat`                  | Relanza Edge con `--remote-debugging-port=9222`     |
| `E:\vars\var 5\X-com guardados\start_watch.bat`                       | Lanza el watcher                                    |

## Cómo se invoca (operación humana)

### Caso 1 — Tras reiniciar el computador

```bat
1) Doble-clic en start_edge_debug.bat
2) Espera a que Edge restaure los workspaces (tu sesión @fdc_ec está
   en `Finz`). Verifica que veas tu feed de X normal.
3) Doble-clic en start_watch.bat
4) La consola del watcher se queda abierta; minimízala.
```

### Caso 2 — Forzar un refresh manual

```bash
python "E:/vars/var 5/X-com guardados/autoreflex_pipeline.py" \
       --create-threshold 80 --augment-threshold 30
```

Baja los umbrales para que se generen skills en temas con menos
volumen. Útil para una corrida inicial o tras una purga.

### Caso 3 — Consultar un tema desde otra sesión de Claude

Cualquier sesión nueva puede llamar:

```bash
python "E:/vars/var 5/X-com guardados/consultar_intereses.py" \
       --tema "geopolitica" --top 15
```

O invocar la skill hija directamente:
`Skill(intereses-geopolitica-soberania)`.

## Limitaciones honestas

- **No es consciencia.** Es un bucle persistente con memoria
  compartida. La diferencia importa: si el watcher muere, no "se
  duerme"; simplemente deja de capturar.
- **Vive mientras Edge debug viva.** Si el usuario cierra Edge, el
  watcher loguea ERROR y muere. Solución: relanzar con los .bat.
- **El watcher de esta sesión Claude muere cuando la sesión termina.**
  Para persistencia entre reboots, registrar un Scheduled Task de
  Windows (pendiente — el usuario debe pedirlo explícitamente).
- **Polling cada 5 min.** Si guardas 25+ bookmarks entre polls, los del
  fondo podrían perderse; basta correr `export_bookmarks.py` para un
  re-scan completo desde cero.
- **Sin LLM en el pipeline.** La clasificación es por regex sobre la
  taxonomía de `analizar_temas.py`. Si un tema nuevo emerge (ej.
  "kayaking") no se detecta hasta que el usuario lo añada a `THEMES`.

## Compuertas 🚦

1. **NO crear skills duplicadas.** El pipeline hace `if slug in existing: skip`.
2. **NO sobreescribir SKILL.md existentes.** Sólo añade `.md` en
   `references/`.
3. **NO mover/borrar bookmarks.json sin snapshot previo.** El usuario
   tiene 5.550 entradas curadas; perderlas es destruir años de criba.
4. **NO subir nada a la nube** desde este pipeline. Todo es local.
5. **Si la taxonomía cambia, re-correr `analizar_temas.py` antes del
   pipeline** — si no, las skills nuevas se generarán con cuentas top
   desactualizadas.
6. **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

## Skills hijas auto-destiladas (estado al 2026-06-23)

Las 16 skills `intereses-*` creadas la primera corrida del pipeline:

- `intereses-geopolitica-soberania` (979 bookmarks)
- `intereses-educacion-aprendizaje` (917)
- `intereses-espiritualidad-religion` (759)
- `intereses-ia-llms` (722)
- `intereses-vida-masculina` (688)
- `intereses-productividad-habitos` (636)
- `intereses-liderazgo-estrategia` (610)
- `intereses-historia-arquetipos` (539)
- `intereses-negocios-emprendimiento` (507)
- `intereses-mentalidad-desarrollo` (472)
- `intereses-finanzas-mercados` (466)
- `intereses-salud-cuerpo` (438)
- `intereses-filosofia` (254)
- `intereses-blockchain-web3` (223)
- `intereses-geopolitica-latam` (156)
- `intereses-pensamiento-critico` (117)

Tema `intereses-tecnologia-programacion` (85) quedó debajo del umbral
de creación; aparecerá cuando supere 100.

## Relacionado

- [[llave-maestra-autoaprendizaje-ia]] — la doctrina padre.
- [[consulta-bookmarks-fdc-ec]] — skill hermana para consultar.
- [[auditoria-cognitiva-reflexiva]] — para auditar al propio agente.
