---
name: universidad-abierta-catalogo
description: |
  CATÁLOGO Y RUTAS DE ACCESO al conocimiento universitario abierto: 50 fuentes
  inventariadas, verificadas por HTTP y clasificadas en 8 pilares (método,
  matemática, computación, ciencias, humanidades, datos/IA, biblioteca,
  herramientas), más la secuencia real de asignaturas MIT con sus URL canónicas.

  Responde a la pregunta «¿de dónde saco esto y cómo entra a la casa?». No
  enseña —para eso está [[programa-estudio-profundo-mit]]— sino que dice qué
  fuente usar, con qué prioridad, con qué licencia y por qué ruta técnica
  (WebFetch, navegador Edge, API/RSS, yt-dlp, descarga local).

  Invocarla SIEMPRE antes de buscar a ciegas en internet un tema académico:
  primero el catálogo, después la web abierta.

trigger_phrases:
  - "dónde estudio esto"
  - "qué fuente uso para aprender X"
  - "busca en la universidad abierta"
  - "catálogo de recursos educativos"
  - "curso gratuito de X"
  - "consulta el catálogo de las 50 fuentes"
  - "verifica esta fuente académica"
idioma_de_salida: español
nivel_madurez: aplicada
dominio: acceso al conocimiento / biblioteca
metadata:
  version: 1.0
  fecha: 2026-09-05
  origen: lista de 50 recursos entregada por el usuario, inventariada y verificada por HTTP el 2026-09-05
  datos: "E:\\vars\\var 5\\Universidad-Abierta\\catalogo-50-fuentes.json"
  helper: "E:\\vars\\var 5\\Universidad-Abierta\\consultar_universidad.py"
  agente: estudios-generales
  relacionada: programa-estudio-profundo-mit, metodo-mit-notebooklm-riguroso, llave-maestra-autoaprendizaje-ia, auditoria-evidencia-cuatro-niveles
---

# Skill `universidad-abierta-catalogo`

## Doctrina

Cincuenta enlaces sueltos no son una biblioteca: son una lista. Una biblioteca tiene
**catálogo** (qué hay), **signatura** (dónde está y en qué estado) y **regla de préstamo**
(cómo entra el material a la casa). Esta skill convierte la lista en biblioteca.

Tres hallazgos de la verificación del 2026-09-05 justifican que exista:

1. **Tres dominios de la lista no existen.** `paulsonlinemathnotes.com`, `philosophize.org`
   y `crashcourse.org` fallan en DNS. Sus direcciones reales son `tutorial.math.lamar.edu`,
   `philosophizethis.org` y `thecrashcourse.com`.
2. **Una redirección invierte el sentido.** `online.berkeley.edu` lleva a
   `extension.berkeley.edu`, que es **educación continua de pago**, no recursos abiertos.
   Lo abierto está en `open.berkeley.edu`.
3. **Cuatro sitios devuelven 403 a cualquier bot** (OpenLearn, FutureLearn, Feynman
   Lectures, BioInteractive). Un agente que use WebFetch concluirá que están caídos. No lo
   están: exigen navegador real.

De ahí la regla: **ningún agente de esta casa cita una fuente académica sin que esté en el
catálogo o haya sido verificada por HTTP en el momento.**

## Cómo se consulta (siempre por el helper, nunca leyendo el JSON entero)

```bash
python "E:/vars/var 5/Universidad-Abierta/consultar_universidad.py"                    # panorama
python "E:/vars/var 5/Universidad-Abierta/consultar_universidad.py" --pilar P2         # matemática
python "E:/vars/var 5/Universidad-Abierta/consultar_universidad.py" --prioridad 5      # columna vertebral
python "E:/vars/var 5/Universidad-Abierta/consultar_universidad.py" --query calculo    # texto libre
python "E:/vars/var 5/Universidad-Abierta/consultar_universidad.py" --mit              # malla MIT verificada
python "E:/vars/var 5/Universidad-Abierta/consultar_universidad.py" --json --pilar P6  # para otro agente
```

## Los 8 pilares

| | Pilar | Fuentes ancla |
|---|---|---|
| **P1** | Método y pensamiento | Saylor (certificado gratis), OpenLearn, TED (como laboratorio de forma) |
| **P2** | Matemática | OpenStax, 3Blue1Brown, Paul's Notes, Khan (reparación en español) |
| **P3** | Computación y sistemas | CS50, nand2tetris, Teach Yourself CS, roadmap.sh |
| **P4** | Ciencias naturales | Feynman, HyperPhysics, LibreTexts, TU Delft, PhET |
| **P5** | Humanidades | Open Yale Courses, SEP, IEP, Aeon, Philosophize This! |
| **P6** | Datos e IA | fast.ai, d2l.ai, Distill.pub |
| **P7** | Biblioteca y fuentes | MIT OCW, Class Central, arXiv, Quanta |
| **P8** | Herramientas | Desmos, GeoGebra, Wolfram Alpha |

## Matriz de rutas de acceso — cómo entra cada cosa a la casa 🚦

| Ruta | Cuándo | Herramienta | Fuentes |
|---|---|---|---|
| `webfetch` | Sitio abierto que responde 200 | WebFetch / WebSearch | la mayoría |
| `edge-cdp` | **403 a bots** | Edge logueado en puerto 9222 (ver [[feedback_solo_edge]]) | OpenLearn, FutureLearn, Feynman, BioInteractive |
| `api` | Hay RSS o API | `curl` al feed | Quanta (`/feed/`), arXiv (`export.arxiv.org/api/query`), Wolfram |
| `yt` | El material es video | yt-dlp + transcripción → [[youtube-corpus-jjmobijuesa]] | 3Blue1Brown, CrashCourse |
| `descarga` | Conviene archivarlo offline | descargar una vez a `E:\vars\var 5\Universidad-Abierta\biblioteca\` | OpenStax, Paul's Notes, d2l.ai, nand2tetris |
| `notebooklm` | Corpus para estudiar a fondo | subir a un cuaderno y aplicar [[metodo-mit-notebooklm-riguroso]] | transcripciones de Open Yale, PDFs de OpenStax |

**Un solo sitio del catálogo merece vigilancia automática: Quanta Magazine** (RSS activo,
calidad sostenida). El resto son fondos estables: se consultan, no se vigilan. Distill.pub
está en hiato desde 2021 y Open Yale cerró catálogo en 2012: son archivos, no flujos.

## Compuertas 🚦

- **No inventar cursos ni URL.** Si un curso no está en el catálogo, verificar con HTTP antes
  de nombrarlo. La invención de una URL de OCW es indetectable para el usuario y letal.
- **arXiv es preprint, no ciencia revisada.** Antes de citar, aplicar
  [[auditoria-evidencia-cuatro-niveles]].
- **Distinguir gratuito de gratuito-con-anzuelo.** Brilliant y Math Academy son de pago;
  Coursera y edX solo dan modo oyente y cada vez más restringido. Están en el catálogo con
  prioridad 1 justamente para no volver a caer.
- **Respetar licencia.** OpenStax y Aeon (CC BY / CC BY-ND) permiten reproducir con
  atribución; las Feynman Lectures no permiten descarga masiva; OCW es CC BY-NC-SA: nada de
  esto entra en un producto comercial sin revisar la cláusula NC.
- **Nivel escolar ≠ nivel universitario.** Khan, Physics Classroom y Learn.Genetics son
  rampas de acceso, no currículo.

## Mantenimiento

Reverificar el catálogo cada seis meses (o cuando una consulta devuelva un enlace muerto):

```bash
python -c "import json;d=json.load(open(r'E:\vars\var 5\Universidad-Abierta\catalogo-50-fuentes.json',encoding='utf-8'));[print(r['url']) for r in d['recursos']]" | \
  xargs -P 10 -I{} curl -sS -L --max-time 12 -o /dev/null -w "%{http_code} {}\n" {}
```

Si algo cambió: actualizar el JSON, subir la versión en `meta.version` y anotar la fecha.

## Relacionado

- Currículo y estudio profundo: [[programa-estudio-profundo-mit]]
- Protocolo de estudio con corpus cerrado: [[metodo-mit-notebooklm-riguroso]]
- Agente que la gobierna: `estudios-generales` (`~/.claude/agents/estudios-generales.md`)
- Coprocesador para barridos: [[multi-agente-gemini-coprocesador]] — con la divergencia
  registrada en `E:\vars\var 5\Universidad-Abierta\notas\2026-09-05_divergencias-gemini.md`
- Curación personal del usuario sobre el tema: [[intereses-educacion-aprendizaje]]
