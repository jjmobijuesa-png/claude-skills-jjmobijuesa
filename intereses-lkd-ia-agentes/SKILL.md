---
name: intereses-lkd-ia-agentes
description: |
  Skill de consulta y curación temática sobre "IA, LLMs, agentes y prompt engineering" a partir de las
  PUBLICACIONES GUARDADAS de LinkedIn (cuenta fedphd@gmail.com).
  Auto-destilada por el pipeline autoreflexivo LinkedIn el 2026-07-05
  desde 157 posts guardados. Hermana de la skill X.com
  `intereses-ia-agentes`.
trigger_phrases:
  - "qué guardé en LinkedIn sobre ia-agentes"
  - "autores de LinkedIn sobre ia, llms, agentes y prompt engineering"
  - "posts LinkedIn ia-agentes"
idioma_de_salida: español
nivel: básica
dominio: aprendizaje / consulta
metadata:
  version: 1.0
  fecha: 2026-07-05
  origen: pipeline autoreflexivo LinkedIn (autoreflex_pipeline_linkedin.py)
  fuente: E:\vars\var 5\LinkedIn-guardados\guardados.json
  relacionada: linkedin-guardados-fedphd, agente-local-autoreflexivo-bookmarks
---

# Skill `intereses-lkd-ia-agentes`

## Doctrina

Skill auto-destilada desde los guardados de LinkedIn del usuario
fedphd@gmail.com. NO firma las opiniones de los autores curados —
son señal de qué le importa al usuario. Cada consulta debe citar
URL canónica del post.

## Autores top del tema (LinkedIn)

  - Javi Consuegra: 14 posts
  - Miguel C.: 8 posts
  - Marc Vidal: 6 posts
  - Jordi Altimira: 6 posts
  - Walter Zevallos Bustamante: 5 posts
  - Rafael Sansores Majul: 5 posts
  - Nicolás Boucher: 5 posts
  - Yago C.: 4 posts
  - Kike Sanchis Alonso: 3 posts
  - Bojan Radojicic: 3 posts

## Posts semilla (157 en total a la fecha)

- **Santiago Covelli** · Santiago Covelli • 2º Applied AI \​ Co-Founder at Lulo Bank 1 día • #LecturasDeDomingo Esta semana quedó claro que lo que a un experto le tomaba semanas, una máquina ya lo hace en  … <https://www.linkedin.com/feed/update/urn:li:activity:7476982819714596865>
- **Kike Sanchis Alonso** · Kike Sanchis Alonso • 2º Estratega de Eficiencia Operativa con IA | Arquitecto de Agentes Autónomos para Empresas Marketing-SEO | Reducción de Costos y Automatización Core Seguro | … <https://www.linkedin.com/feed/update/urn:li:activity:7477074829188182016>
- **Walter Zevallos Bustamante** · Estado: localizable Walter Zevallos Bustamante • 3er+ Especialista en Finanzas Corporativas y Estructuración Empresarial | Planeamiento Fianciero | Gestión de Riesgos | BI & IA apl … <https://www.linkedin.com/feed/update/urn:li:activity:7466898052398796800>
- **Kike Sanchis Alonso** · Kike Sanchis Alonso • 2º Estratega de Eficiencia Operativa con IA | Arquitecto de Agentes Autónomos para Empresas Marketing-SEO | Reducción de Costos y Automatización Core Seguro | … <https://www.linkedin.com/feed/update/urn:li:activity:7476311006504329217>
- **Kike Sanchis Alonso** · Kike Sanchis Alonso • 2º Estratega de Eficiencia Operativa con IA | Arquitecto de Agentes Autónomos para Empresas Marketing-SEO | Reducción de Costos y Automatización Core Seguro | … <https://www.linkedin.com/feed/update/urn:li:activity:7475650502136057856>
- **Marc Vidal** · Marc Vidal • 2º Conferenciante y consultor en transformación digital. Analista económico y divulgador tecnológico. LinkedIn Top Voices. Top 100 Forbes Influencers Economía. Top100  … <https://www.linkedin.com/feed/update/urn:li:activity:7475114187078311936>
- **Marc Vidal** · Marc Vidal • 2º Conferenciante y consultor en transformación digital. Analista económico y divulgador tecnológico. LinkedIn Top Voices. Top 100 Forbes Influencers Economía. Top100  … <https://www.linkedin.com/feed/update/urn:li:activity:7475501720924561408>
- **Antonio Bolívar Paspuezán Chugá** · Antonio Bolívar Paspuezán Chugá • 3er+ Consultor en Gestión de Proyectos para el Desarrollo Sostenible | Especialista en Marco Lógico, Teoría de Cambio y Evaluación Financiera | Pl … <https://www.linkedin.com/feed/update/urn:li:activity:7471946467465834496>

## Cómo consultar

Para respuestas frescas sobre "IA, LLMs, agentes y prompt engineering" desde LinkedIn:

```bash
# Consultar el JSON global
python "C:/Users/datos/.claude/skills/linkedin-guardados-fedphd/scripts/clasificar_guardados.py"
# Revisar la sección "ia-agentes" del análisis generado
```

## Reglas

- Solo lectura de guardados públicos. Nunca publicar.
- Citar URL canónica (`linkedin.com/feed/update/urn:li:activity:...`).
- No atribuir opinión del autor curado al usuario.
