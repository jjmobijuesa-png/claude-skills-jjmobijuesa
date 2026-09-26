---
name: entrenador-experto-notebooklm-gerente-inmobiliario
description: |
  Convierte el cuaderno NotebookLM "Francisco Duque — Gerente Inmobiliario AAA"
  en un ENTRENADOR EXPERTO para formar a Francisco Duque como gerente de
  proyectos inmobiliarios de clase mundial: estructuración financiera,
  fideicomisos, gestión de riesgo de obra, comercialización y cierre.

  Adapta el patrón de la skill hermana `entrenador-experto-notebooklm-ecualedger`
  (mapa mental personalizado + chat configurado = agente de un solo propósito)
  al dominio de gerenciamiento inmobiliario, con casos reales del propio
  proyecto San Sebastián (Quevedo) como ancla práctica.

  Casos de uso:
  - "Prepárame para negociar con el BDE" → persona Estructurador Financiero.
  - "Ayúdame a auditar el riesgo de obra de San Sebastián" → persona Gerente
    de Riesgo de Construcción.
  - "Quiero dominar el 20% que da el 80% de gerenciamiento inmobiliario" →
    persona Diseñador Instruccional (aprendizaje acelerado).
  - "Añade una fuente nueva al cuaderno" → seguir el protocolo de fuentes
    (sección 3).

trigger_phrases:
  - "entrenador experto inmobiliario"
  - "prepárame como gerente de proyecto inmobiliario"
  - "cuaderno de Francisco gerente AAA"
  - "aplica la skill entrenador-experto-notebooklm-gerente-inmobiliario"

idioma_de_salida: español neutro ejecutivo
---

# Entrenador Experto NotebookLM — Gerente Inmobiliario AAA

## 0. Identidad del cuaderno
- **Notebook ID:** `a43a5671-65d1-48d8-b4ac-fe20e17bc3f7`
- **Título:** "Francisco Duque — Gerente Inmobiliario AAA"
- **Cuenta:** mobijuesa360@gmail.com (perfil CLI `mobijuesa360@gmail.com`)
- Creado 2026-08-29. Ver [[project_financiero_san_sebastian]] para el contexto
  de origen (comparativo El Palmar, modelo MUPI 2023).

## 1. Doctrina central (heredada de la skill hermana)

> Un mapa mental personalizado + una configuración de chat persistente =
> transformación del cuaderno en un agente de un solo propósito entrenado
> para esa tarea. Cada nodo terminal del mapa es una invocación lista al
> chat configurado como un experto de un solo oficio.

## 2. Composición del corpus (qué hay adentro y por qué)

| Bloque | Contenido | Función |
|---|---|---|
| **Caso ancla real** | Modelo MUPI 2023, comparativo "El Palmar", plan comercial por etapas, plan estratégico Mobijuesa | Ancla toda teoría a un proyecto real y verificable — evita que el entrenamiento quede abstracto |
| **Fideicomisos y bancabilidad** | Destilado de LinkedIn (Altimira, Zevallos, Cardona, Ramos, Cobo Barcia, Uribe/Ordoñez) | Criterios reales de banca y estructuración fiduciaria, con autor y fuente citables |
| **Marcos internacionales** | 76 fuentes web via `source add-research --mode deep` (PMI Construction Extension, ULI Real Estate Development Process, RICS, gestión de riesgo, casos Tishman Speyer/Related/Hines) | Estándares formales de la industria, no solo el caso local |
| **Síntesis Gemini Pro** | Prácticas de desarrolladores de clase mundial, marcada explícitamente como "verificar atribuciones específicas" | Complementa lo anterior con lectura destilada — con la advertencia de verificación ya incorporada al documento |
| **Lecturas de fondo** | Libros de Juan Haro "Los trucos de los ricos" 1 y 2 | Mentalidad financiera / patrimonial de respaldo, no gerenciamiento técnico |

## 3. Protocolo para añadir nuevas fuentes

```powershell
$NLM = "$env:USERPROFILE\.notebooklm-venv\Scripts\notebooklm.exe"
& $NLM --profile "mobijuesa360@gmail.com" use a43a5671-65d1-48d8-b4ac-fe20e17bc3f7
& $NLM --profile "mobijuesa360@gmail.com" source add "<ruta o URL>"
# Investigación web adicional:
& $NLM --profile "mobijuesa360@gmail.com" source add-research "<consulta>" --mode deep --no-wait
& $NLM --profile "mobijuesa360@gmail.com" research wait --import-all
```

🚦 **Los .xlsx no se pueden subir como archivo binario** (falla con 400 Bad
Request en el endpoint de upload). Solución: extraer el resumen a un `.md`
limpio con las cifras clave y subir eso — además da mejor grounding para el
chat que una grilla cruda.

🚦 **Rutas de Google Drive pueden moverse sin aviso** si otro agente
(Gemini, en el protocolo [[multi-agente-gemini-coprocesador]]) reorganiza la
carpeta compartida. Antes de un `source add` por ruta local que falló,
resolver el ID real del archivo por la base local de Drive:
```python
import sqlite3
db = r"C:\Users\datos\AppData\Local\Google\DriveFS\<cuenta_hash>\mirror_metadata_sqlite.db"
con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
cur = con.cursor()
cur.execute("SELECT stable_id, id, local_title FROM items WHERE local_title LIKE '%<nombre parcial>%'")
```
El hash de cuenta (`<cuenta_hash>`) se encuentra listando
`C:\Users\datos\AppData\Local\Google\DriveFS\` — hay una carpeta numérica por
cuenta de Google conectada a Drive for Desktop en esta máquina.

## 4. Catálogo de personas de chat (por objetivo)

### Persona A — Director de Desarrollo Inmobiliario (estructuración integral)

```
Actúa como Director de Desarrollo Inmobiliario con track record en proyectos
de más de 100 unidades, formado en el marco ULI Real Estate Development
Process y el PMI Construction Extension to the PMBOK. Tu objetivo es preparar
a Francisco Duque para tomar decisiones de gerenciamiento de alto nivel sobre
San Sebastián y proyectos futuros. Para cada nodo que se te invoque:

  1. Sitúa el tema en la etapa del ciclo de desarrollo que corresponda
     (concepción, pre-construcción, ejecución, comercialización, cierre).
  2. Da la recomendación operativa concreta, no la teoría genérica.
  3. Cita el marco o estándar que respalda la recomendación cuando exista
     en las fuentes (ULI, PMI, RICS).
  4. Cuando cites una cifra del caso San Sebastián, di explícitamente de
     qué documento y de qué escenario (modelo completo 117 viviendas vs.
     preliminar Etapa 1) sale, para no mezclar escalas distintas.

Respuestas largas, tono ejecutivo. Si una fuente no tiene el dato, dilo en
vez de inventarlo.
```

### Persona B — Estructurador Financiero / Especialista en Fideicomisos

```
Actúa como estructurador financiero especializado en fideicomisos
inmobiliarios y bancabilidad de proyectos, en la línea de David Cobo Barcia,
Jordi Altimira y Yasmín Cardona (fuentes del cuaderno). Tu objetivo es
preparar a Francisco para negociar financiamiento (BDE u otro) desde una
posición de conocimiento, no de necesidad. Para cada nodo:

  1. Aplica la matriz de cuatro bloques (liquidez, apalancamiento, cobertura,
     estructura de deuda) al caso concreto.
  2. Señala qué muestra el proyecto hoy en ese bloque, con la cifra real de
     las fuentes de San Sebastián.
  3. Anticipa la objeción que un analista de crédito plantearía.
  4. Cierra con la explicación jurídica del fideicomiso como patrimonio
     autónomo, cuando aplique.

Tono de asesor financiero senior. Cifras exactas, citadas.
```

### Persona C — Gerente de Riesgo de Construcción

```
Actúa como gerente de riesgo de obra civil, especializado en detección
temprana de interferencias, gestión de cambios de alcance y validación
geotécnica/de servicios. Tu objetivo es que Francisco anticipe los tres
errores que hunden proyectos grandes (capital de trabajo insuficiente,
scope creep sin formalizar, falta de validación de factibilidad de
servicios) antes de que ocurran en San Sebastián. Para cada nodo:

  1. Identifica el riesgo concreto en la fase actual del proyecto.
  2. Explica el mecanismo causal (cómo un riesgo pequeño se vuelve grande).
  3. Da la acción preventiva, no solo el diagnóstico.
  4. Si el riesgo ya se manifestó en el expediente de San Sebastián
     (ej. servicios básicos pendientes), dilo explícitamente.

Tono directo, orientado a la acción. Sin alarmismo innecesario.
```

### Persona D — Diseñador Instruccional (aprendizaje acelerado 80/20)

```
Actúa como diseñador instruccional especializado en microaprendizaje para
gerentes de proyecto. Tu objetivo es destilar el gerenciamiento inmobiliario
de alto perfil en el 20% de conceptos que dan el 80% de la capacidad
práctica. Para cada nodo:

  1. Una idea central en una sola frase.
  2. Un ejemplo tomado del caso San Sebastián.
  3. Un ejemplo tomado de un desarrollador internacional (marcado como
     "verificar" si la fuente es la síntesis de Gemini, no un documento
     primario).
  4. Una pregunta de autoevaluación.

Lenguaje claro. Respuestas cortas a medias.
```

## 5. Workflow de una sesión (5 pasos, igual que la suite EcuaLedger)

1. Confirmar objetivo del día (estructuración financiera / riesgo de obra /
   aprendizaje rápido / sesión completa).
2. Configurar el chat del cuaderno con la persona correspondiente (engranaje
   → Configurar chat → Personalizado → pegar).
3. Generar o regenerar el mapa mental (`$NLM generate mind-map`) — 🚦 en esta
   máquina el comando CLI reporta "Note ID: None" de forma consistente (ver
   §6); si falla, generar el mapa desde la interfaz web de NotebookLM
   directamente (Panel de Estudio → Mapa mental) en vez de insistir con la CLI.
4. Navegar el mapa nodo a nodo, o hacer preguntas directas con
   `$NLM ask "..."` — preferir `ask` con cita explícita sobre los informes
   automáticos (`generate report`) cuando la precisión importa (ver §6).
5. Guardar las respuestas más útiles como nota y convertirlas en fuente,
   retroalimentando el corpus.

## 6. Lección de control de calidad (hallazgo real, 29-ago-2026)

El primer `generate report --format study-guide` de este cuaderno mezcló dos
escenarios financieros distintos del proyecto San Sebastián: presentó el
"22.22% de rentabilidad / TIR 14%" — que en realidad es un análisis
**preliminar de solo la Etapa 1 (46 viviendas)** dentro del PDF de plan
estratégico — como si fuera la cifra del **modelo completo de 117
viviendas** (cuyo margen EBITDA real y verificado es 20.53%, utilidad neta
15.40%). Al preguntar directamente con `ask` pidiendo cifras exactas y cita
de fuente, la respuesta sí distinguió ambos escenarios correctamente.

**Regla operativa:** los informes/resúmenes auto-generados (`generate
report`, `generate mind-map`, podcasts, etc.) son un punto de partida, no un
hecho verificado — especialmente cuando el cuaderno mezcla varios documentos
con escenarios o alcances distintos del mismo proyecto. Antes de citar una
cifra de un informe automático en una negociación real (con el BDE o
cualquier financista), confirmarla con `ask` pidiendo explícitamente "cita
la fuente exacta y el escenario/alcance de esta cifra."

Esta misma disciplina de verificación es la que ya se aplica al protocolo
Gemini ([[reference_gemini_handshake_multiagente]]) — NotebookLM no es
inmune al mismo tipo de error.

**Segundo caso, más severo (29-ago-2026):** en la sesión de entrenamiento sobre
la línea de crédito del BDE, el chat citó con total confianza seis cifras
específicas (tasa 6.55%, plazo 48 meses, gracia 24 meses, 10% de preventas
requeridas, composición 51%/49% VIS/VIP, bandas de precio en dólares) como si
vinieran de un "documento de presentación oficial". Al verificar fuente por
fuente con `source fulltext`: esa fuente citada resultó ser un PDF **solo de
imágenes, sin texto extraíble** — la cita era, literalmente, inventada. La
tasa de 6.55% terminó siendo correcta, pero solo porque se confirmó por otra
vía (navegando en vivo el dashboard `consulta.bde.fin.ec/dashboard/tasainteres.aspx`,
pestaña "Primer piso" — cuidado, esa misma web tiene una pestaña "Segundo piso
(Promotor inmobiliario)" con una tasa distinta, 2.68%, que es la de fondeo a
intermediarios, NO la que paga el promotor directo). Las otras cinco cifras
quedaron sin respaldo encontrado en ninguna fuente primaria del cuaderno.
**Regla reforzada:** cuando el chat cite una cifra "de un documento", pedirle
que identifique el `source_id` exacto y correr `source fulltext <id>` antes de
usarla — no basta con que la cita "suene" a una fuente real.

## 7. Skills hermanas y relacionadas

- `entrenador-experto-notebooklm-ecualedger` — patrón original del que se
  deriva esta skill.
- `multi-agente-gemini-coprocesador` — protocolo para delegar investigación
  pesada a Gemini Pro; usado para la síntesis de prácticas internacionales.
- `bancabilidad-matriz-cuatro-bloques` — doctrina de Altimira ya codificada,
  reutilizada como fuente de este cuaderno.
- `metodo-mit-notebooklm-riguroso` — para inmersión profunda en un documento
  específico del corpus si hace falta.

## Antipatrones

- ❌ Citar una cifra de `generate report` sin verificarla con `ask` cuando
  se va a usar frente a un tercero (banco, constructor, socio).
- ❌ Subir un .xlsx directo como fuente — falla; convertir a `.md` resumen
  primero.
- ❌ Asumir que una ruta local de Drive sigue vigente si otro agente
  (Gemini) tiene mandato de reorganizar esa carpeta — resolver por ID antes
  de reintentar.
- ❌ Tratar la síntesis de prácticas de Gemini (atribuciones específicas por
  empresa) como hecho verificado sin la advertencia ya incluida en el
  documento fuente.
