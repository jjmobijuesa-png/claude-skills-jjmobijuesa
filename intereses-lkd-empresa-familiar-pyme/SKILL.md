---
name: intereses-lkd-empresa-familiar-pyme
description: |
  Skill de consulta y curación temática sobre "Empresa familiar y PYME" a partir de las
  PUBLICACIONES GUARDADAS de LinkedIn (cuenta fedphd@gmail.com).
  Auto-destilada por el pipeline autoreflexivo LinkedIn el 2026-07-05
  desde 31 posts guardados. Hermana de la skill X.com
  `intereses-empresa-familiar-pyme`.
trigger_phrases:
  - "qué guardé en LinkedIn sobre empresa-familiar-pyme"
  - "autores de LinkedIn sobre empresa familiar y pyme"
  - "posts LinkedIn empresa-familiar-pyme"
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

# Skill `intereses-lkd-empresa-familiar-pyme`

## Doctrina

Skill auto-destilada desde los guardados de LinkedIn del usuario
fedphd@gmail.com. NO firma las opiniones de los autores curados —
son señal de qué le importa al usuario. Cada consulta debe citar
URL canónica del post.

## Autores top del tema (LinkedIn)

  - Javi Consuegra: 2 posts
  - Alexandre Perini: 2 posts
  - UpGrade: 1 posts
  - David Cobo Barcia: 1 posts
  - Marc Vidal: 1 posts
  - ESTEBAN URIBE JARAMILLO: 1 posts
  - Javier Gavilanez: 1 posts
  - Mejora: 1 posts
  - Yasmín Araceli Cardona Garcia: 1 posts
  - Jordi Altimira: 1 posts

## Posts semilla (31 en total a la fecha)

- **UpGrade** · UpGrade 149 seguidores 6 días • 🚨 SEÑALES que anticipan problemas financieros 🚨 💾 Guarda esta guía para revisar resultados, balance y caja Los estados financieros suelen avisar ant … <https://www.linkedin.com/feed/update/urn:li:activity:7475072723703013376>
- **David Cobo Barcia** · David Cobo Barcia • 2º Consultor Estratégico en Fideicomisos Mercantiles | Especialista en Fideicomisos Inmobiliarios y Financiamiento de Proyectos | Profesor MBA en Finanzas y Est … <https://www.linkedin.com/feed/update/urn:li:activity:7475514077683982337>
- **Marc Vidal** · Marc Vidal • 2º Conferenciante y consultor en transformación digital. Analista económico y divulgador tecnológico. LinkedIn Top Voices. Top 100 Forbes Influencers Economía. Top100  … <https://www.linkedin.com/feed/update/urn:li:activity:7475114187078311936>
- **ESTEBAN URIBE JARAMILLO** · ESTEBAN URIBE JARAMILLO • 2º Director Comercial de Negocios Fiduciarios en Alianza Fiduciaria - @momentofiduciario 2 semanas • Un minuto de Fiducia: Muchas personas dedican toda un … <https://www.linkedin.com/feed/update/urn:li:activity:7471169540773576704>
- **Javier Gavilanez** · Estado: con conexión Javier Gavilanez • 1er Gerente de Operaciones | Deltamontero | Asesor Financiero | Estrategia Tributaria | Control Interno | Eficiencia Financiera | Generación … <https://www.linkedin.com/feed/update/urn:li:activity:7473347568140386304>
- **Mejora** · Mejora 149 seguidores 2 semanas • 🚨 CAPEX y OPEX son muy diferentes 🚨 Y esa es una de las trampas financieras más peligrosas para una PyME. Porque muchas empresas ven que el negoci … <https://www.linkedin.com/feed/update/urn:li:activity:7472173682430390272>
- **Yasmín Araceli Cardona Garcia** · Yasmín Araceli Cardona Garcia • 3er+ Directora de Finanzas | Contraloría Estratégica | Gobierno Corporativo | Control Financiero | Capital de Trabajo | Transformación Empresarial 2 … <https://www.linkedin.com/feed/update/urn:li:activity:7471301180212785153>
- **Jordi Altimira** · Jordi Altimira • 2º Entrepreneur. Investor. Lecturer. Founder en UpBizor, Lanzame Capital & BMF Business School. CFO as a service | Financiación | Lanzadera Lover 2 semanas • 📊 ¿QU … <https://www.linkedin.com/feed/update/urn:li:activity:7472241524211187713>

## Cómo consultar

Para respuestas frescas sobre "Empresa familiar y PYME" desde LinkedIn:

```bash
# Consultar el JSON global
python "C:/Users/datos/.claude/skills/linkedin-guardados-fedphd/scripts/clasificar_guardados.py"
# Revisar la sección "empresa-familiar-pyme" del análisis generado
```

## Reglas

- Solo lectura de guardados públicos. Nunca publicar.
- Citar URL canónica (`linkedin.com/feed/update/urn:li:activity:...`).
- No atribuir opinión del autor curado al usuario.
