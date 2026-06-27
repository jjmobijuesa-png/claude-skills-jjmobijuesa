---
name: analisis-multi-tema-bookmarks
description: |
  Router multi-tema sobre los 5.550+ bookmarks de @fdc_ec. Dado un
  prompt libre del usuario (pregunta, comparación, brief, análisis),
  identifica qué temas del corpus la cruzan, agrupa los bookmarks
  relevantes con score por relevancia, y devuelve un digest listo para
  síntesis. NO es la skill que responde — es la skill que CONSULTA el
  corpus y entrega evidencia. La síntesis final la produce Claude con
  el digest en contexto. Cada análisis se persiste en
  `E:\vars\var 5\X-com guardados\analisis\` para acumular conocimiento
  entre sesiones.

trigger_phrases:
  - "analiza con mis bookmarks"
  - "qué tengo curado sobre"
  - "consulta mi archivo X sobre"
  - "responde con mi voz sobre"
  - "haz un análisis multi-tema"
  - "router de bookmarks"
  - "qué dicen mis fuentes sobre"

idioma_de_salida: español neutro
nivel_madurez: especializada
fuente: orquestador analizar_query.py + taxonomía de 18 temas
---

# Router multi-tema — bookmarks @fdc_ec

## Cuándo usar esta skill

Cuando el usuario haga una pregunta que cruza **más de un tema** o
requiera evidencia textual del corpus (con URL canónica). Ejemplos
reales del tipo de query que dispara esta skill:

- "Cómo levanto un esquema patrimonial legal en Ecuador" → cruza
  *patrimonial + geopolítica latam + negocios + finanzas*.
- "Qué dicen mis cuentas sobre IA agentic" → *IA + productividad + tecnología*.
- "Soberanía digital y blockchain en LATAM" → *blockchain + geopolítica
  + geopolítica latam*.
- "Mentalidad masculina, disciplina, virtudes clásicas" → *vida
  masculina + mentalidad + filosofía + historia*.

Si la query cae claramente en **un solo tema**, mejor invocar la skill
hija `intereses-<tema>` directa.

## Cómo invocarla — orquestador CLI

```bash
# Modo digest a stdout (markdown)
python "E:/vars/var 5/X-com guardados/analizar_query.py" \
       "tu pregunta libre" --top 15

# Modo JSON para parseo programático
python "E:/vars/var 5/X-com guardados/analizar_query.py" \
       "tu pregunta libre" --json --top 20

# Forzar un tema específico
python "E:/vars/var 5/X-com guardados/analizar_query.py" \
       --topic "patrimonial" --top 10

# Persistir el análisis en analisis/ y registrarlo en el índice
python "E:/vars/var 5/X-com guardados/analizar_query.py" \
       "tu pregunta" --top 20 --save-as nombre_corto
```

El score asignado a cada bookmark es:
- **+3** si una palabra clave de la query aparece en el texto
- **+2** por cada tema detectado que el bookmark también cubre
- **+1** si está entre los autores top del tema

## Patrón de síntesis (cómo Claude usa el digest)

Una vez que el orquestador devuelve el digest:

1. **Leer todos los hits** con sus URLs y métricas (likes/RT como señal
   de qué resonó).
2. **Agrupar por autor**: si un autor tiene 3+ hits es un especialista
   real sobre el cruce, no un match casual.
3. **Distinguir nivel**: ¿el bookmark es **descriptivo** (cómo se hace),
   **prescriptivo** (cómo debería hacerse), **caso real**, o
   **anti-patrón** (cómo se hace mal)?
4. **Marcar la frontera ética/legal** cuando el tema lo requiera (ej.
   patrimonial: legítimo vs. ilícito; geopolítica: análisis vs. activismo).
5. **Citar URL canónica de cada afirmación.**
6. **Identificar el hueco**: qué no está en el corpus que enriquecería
   la respuesta — pista al usuario sobre qué seguir.

## Persistencia entre sesiones

Cada análisis con `--save-as` produce:
- `E:\vars\var 5\X-com guardados\analisis\YYYY-MM-DD_<nombre>.md`
- Línea nueva en `E:\vars\var 5\X-com guardados\analisis\INDICE_ANALISIS.md`

Cualquier sesión futura puede:
1. Leer el índice de análisis ya hechos.
2. Reusar la síntesis si el corpus no cambió significativamente.
3. Regenerar si pasaron muchos bookmarks nuevos (umbral sugerido: >100
   nuevos desde la última fecha).

## Compuertas 🚦

1. **No inventar tweets.** Sólo los que devuelve `analizar_query.py`.
2. **Citar URL canónica siempre.**
3. **Curar ≠ firmar.** Aclarar al usuario que tener bookmark de X no
   implica acuerdo con su contenido.
4. **No leer `bookmarks.json` con `Read`.** Pesa 7 MB. Usar siempre el
   orquestador.
5. **Marcar la frontera ética cuando aplique** (legal/ilegal, factual/
   especulativo, descriptivo/prescriptivo).
6. **Si los temas detectados son 0**: avisar al usuario que la query no
   matchea la taxonomía y sugerir refinarla o añadir un tema nuevo a
   `analizar_temas.py`.

## Relacionado

- [[agente-local-autoreflexivo-bookmarks]] — meta-skill que mantiene el
  archivo vivo.
- [[consulta-bookmarks-fdc-ec]] — skill hermana para consultas simples.
- 17 skills `intereses-*` — para consultas mono-tema directas.
- [[llave-maestra-autoaprendizaje-ia]] — doctrina padre.
- `analisis/INDICE_ANALISIS.md` — índice acumulativo de análisis hechos.
