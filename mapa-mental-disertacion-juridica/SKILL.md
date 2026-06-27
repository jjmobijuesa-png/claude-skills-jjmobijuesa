---
name: mapa-mental-disertacion-juridica
description: |
  Genera el prompt y la configuración del chat que convierten al
  cuaderno NotebookLM EcuaLedger Soberana - IBPP en un GENERADOR DE
  DISERTACIONES ORALES de 30 minutos sobre el programa, listas para
  defender ante audiencias institucionales.

  La skill produce dos artefactos copy-paste:
  1. Un prompt de Mapa Mental personalizado con la estructura del
     discurso (gancho, tres tesis, tres anclajes, cierre, Q&A).
  2. Una configuración del chat (persona "Orador parlamentario
     constitucionalista") con instrucción persistente de longitud
     larga.

  Cada nodo terminal del mapa mental, al hacerle click en NotebookLM,
  generará el guión completo de ese tramo del discurso (con tiempos
  estimados, gancho, anclajes, citas comparadas y transición), de modo
  que toda la disertación es navegable como una mesa de control.

  Derivada del video YouTube ID bOlroS23mN4 (caso de uso #3 del autor,
  adaptado al expediente legislativo ecuatoriano).

trigger_phrases:
  - "prepárame una disertación sobre EcuaLedger"
  - "mapa mental para disertar 30 minutos"
  - "genera disertación oral EcuaLedger Soberana"
  - "aplica la skill mapa-mental-disertacion-juridica"

idioma_de_salida: español neutro parlamentario

---

# Mapa Mental — Disertación Jurídica EcuaLedger Soberana

## Filosofía

Una disertación de 30 minutos no se improvisa: se **arquitectura**.
Esta skill genera, en dos artefactos copy-paste, la arquitectura
completa de una disertación sobre el programa EcuaLedger Soberana,
adaptada a tres duraciones (15, 30 o 45 minutos) y a cinco audiencias
(Pleno, Comisión, Presidencia, prensa, academia).

El mapa mental es el **set de fichas del orador**: cada nodo es una
beat verbal, con tiempo asignado, y cada click genera el guión
completo de ese tramo.

## Paso 0 — Confirmación de parámetros

Antes de generar nada, preguntar al usuario:

> 1. **Duración**: 15, 30 o 45 minutos.
> 2. **Audiencia**: Pleno, Comisión, Presidencia, prensa, academia.
> 3. **Énfasis**: arquitectura jurídica completa, defensa
>    constitucional, integración paraguaya, RWA agroexportador,
>    soberanía monetaria.
> 4. **Estilo**: clásico institucional, contemporáneo divulgativo o
>    académico riguroso.

## Paso 1 — Configuración del chat (copiar al cuaderno)

```
Configurar chat → Personalizado → pegar:

Actúa como un constitucionalista ecuatoriano experto, asesor de la
Comisión Especializada Permanente de Régimen Económico y Tributario,
especializado en mercados financieros, mercado de valores, fe pública
digital y soberanía digital. Estás preparando una disertación oral
de <DURACION> minutos para presentar el programa EcuaLedger Soberana
ante <AUDIENCIA>. El énfasis de esta disertación es <ENFASIS>. El
estilo de la disertación es <ESTILO>.

Para cada nodo del mapa mental que se te invoque, genera el guión
oral completo de ese tramo del discurso, con:

  1. Tiempo asignado al tramo (en minutos y segundos).
  2. Gancho inicial de tres frases máximo.
  3. Desarrollo de la tesis con anclajes constitucionales
     explícitos (citar artículo y nombrar la institución).
  4. Al menos un dato del modelo comparado paraguayo (Ley 6822/21
     o Ley 7572/25).
  5. Una transición a la siguiente beat en una sola frase.

No menciones a personas naturales (asambleístas, ministros). Cita
artículos de la Constitución de la República y leyes específicas.
Habla en tono parlamentario, en primera persona del singular.
Lenguaje sin tecnicismos no explicados. Respuestas largas y aptas
para ser leídas en voz alta.

Longitud de respuesta: Más larga
Guardar.
```

## Paso 2 — Prompt del Mapa Mental personalizado (copiar al panel)

```
Panel de Estudio → Mapa Mental → ícono de flecha → pegar:

Actúa como arquitecto de discursos parlamentarios. Genera un mapa
mental en español detallado que estructure una DISERTACIÓN ORAL de
<DURACION> minutos sobre el programa EcuaLedger Soberana ante
<AUDIENCIA>, con énfasis en <ENFASIS> y estilo <ESTILO>.

El nodo raíz se titula: "Disertación EcuaLedger Soberana ante
<AUDIENCIA>".

De ese nodo raíz parten exactamente SEIS nodos principales,
correspondientes a las seis beats del discurso. Cada beat lleva su
tiempo asignado entre paréntesis:

  1. APERTURA Y CONTEXTUALIZACIÓN ( <DURACION/15> min )
     Subniveles: gancho histórico-comparado, posicionamiento del
     orador y de la materia, mapa de las tres etapas.

  2. PRIMERA TESIS - LA FE PÚBLICA DIGITAL ES EL CIMIENTO
     ( <DURACION/5> min )
     Subniveles: Ley 6822/21 Py como referente, equivalencia
     funcional, DTE, sandbox como puente, anclaje Arts. 16, 18, 66
     CRE.

  3. SEGUNDA TESIS - LA REFORMA AL MERCADO FINANCIERO PRESERVA LA
     SOBERANÍA MONETARIA ( <DURACION/5> min )
     Subniveles: 35 artículos integrados, EPE sobre saldos en
     dólares, VNE digital para MIPYMEs, exclusiones, facultad de
     restricción, anclaje Arts. 303, 308, 313, 314 CRE.

  4. TERCERA TESIS - EL MERCADO TOKENIZADO ABRE UNA GENERACIÓN
     PRODUCTIVA ( <DURACION/5> min )
     Subniveles: Ley 7572/25 Py como referente, Bolsa Soberana de
     Productos (cacao, banano, camarón, oro, energía), FFD, SECAS,
     régimen MIPYMEs, seguro de ciberseguridad obligatorio, anclaje
     Arts. 283, 285.3, 321, 322 CRE.

  5. CIERRE Y LLAMADO A LA ACCIÓN ( <DURACION/15> min )
     Subniveles: cronograma 2026-2051, indicadores de éxito, llamado
     a la sincronización legislativa, frase-firma del programa.

  6. RESERVA - PREGUNTAS PREVISIBLES Y RESPUESTAS LISTAS
     ( <DURACION/10> min de reserva, no parte del discurso )
     Subniveles: ¿es esto criptomoneda?, ¿reemplaza al dólar?, ¿quién
     paga la infraestructura?, ¿qué pasa con la protección de datos?,
     ¿qué hace EcuaLedger que no haga la Ley Fintech?

Cada nodo terminal debe ser una BEAT VERBAL accionable: cuando se le
haga click, el chat configurado generará el guión oral completo de
ese tramo. No agregues notas explicativas dentro del mapa: limítate
a títulos accionables.
```

## Paso 3 — Sesión de entrenamiento

Tras configurar chat y generar el mapa mental, el usuario navega el
mapa de izquierda a derecha (apertura → tesis 1 → tesis 2 → tesis 3
→ cierre → reserva Q&A) y hace click en cada nodo terminal. Cada
click produce el guión completo de ese tramo en estilo persistente.

Cuando una beat genera un guión particularmente bueno, **guardarlo
como nota** desde el chat de NotebookLM. Las notas guardadas se
pueden convertir en fuentes y enriquecer el corpus para la próxima
sesión.

## Paso 4 — Entrega de la disertación

El usuario ensaya el discurso en voz alta una sola vez, cronometrando
cada beat. Si una beat se va de tiempo, regenerar el nodo
correspondiente con la instrucción de "reducir a <tiempo> minutos".

## Variantes por audiencia (sustituir en el prompt)

| Audiencia | Modificaciones al prompt del mapa |
|-----------|-----------------------------------|
| **Pleno** | Beat 4 (Tercera Tesis) acentúa beneficios distribuidos a las provincias agroproductoras. Beat 5 (Cierre) llama explícitamente a la votación. Reserva Q&A incluye objeción de "tecnocracia". |
| **Comisión** | Beat 2-4 desarrollan articulado específico (Arts. y numerales exactos). Reserva Q&A incluye dudas técnicas sobre sandbox y normativa secundaria. |
| **Presidencia** | Beat 1 enfatiza posicionamiento internacional. Beat 5 enfatiza el legado generacional. Reserva Q&A incluye objeciones de coalición. |
| **Prensa** | Beats acortados, lenguaje sin tecnicismos. Cada beat termina con frase-titular citable. Reserva Q&A incluye preguntas hostiles. |
| **Academia** | Beat 1 incluye estado del arte comparado. Beats 2-4 citan literatura académica del corpus cuando exista. Reserva Q&A incluye consultas de método. |

## Salida estándar de la skill

Tres artefactos:

1. Instrucción de configuración de chat (copiar a NotebookLM).
2. Prompt del Mapa Mental personalizado (copiar a Panel de Estudio).
3. Checklist de ensayo previo a la entrega:
   - Cronometrar cada beat.
   - Guardar como nota las beats más fuertes.
   - Imprimir el mapa expandido como guión visual de respaldo.
   - Repasar la reserva Q&A en voz alta dos veces.

## Antipatrones

- ❌ Generar el mapa mental sin configurar primero el chat.
- ❌ Pedir un mapa con más de seis nodos principales (sobrecarga oral).
- ❌ Olvidar la beat de reserva Q&A.
- ❌ Mencionar personas naturales en el guión.
- ❌ No cronometrar el ensayo.

## Skills hermanas

- `entrenador-experto-notebooklm-ecualedger` — skill maestra.
- `defensa-apologetica-juridica` — para la beat de reserva Q&A
  cuando se prevén objeciones fuertes.
- `aprendizaje-pareto-juridico` — si el usuario aún no domina el
  20% crítico del contenido.
