---
name: articulacion-inter-comision-legislativa
description: |
  Diseña la ARQUITECTURA DE COORDINACIÓN entre dos o más comisiones
  especializadas de la Asamblea Nacional del Ecuador (u otros
  órganos colegiados análogos) que tienen competencias concurrentes
  sobre un mismo expediente legislativo.

  Su producto típico es:
  - Mapa de competencias (primaria vs. consulta obligatoria).
  - Identificación de patologías de superposición regulatoria.
  - Articulación con el CAL para trámite conexo.
  - Propuesta de redacción para evitar conflictos de normas.

  Destilada del memo B-012 del paquete EcuaLedger Soberana (Comisión
  Soberanía vs. Comisión Régimen Económico), donde se construyó la
  arquitectura inter-comisión más precisa del paquete.

  Skill hija de `inteligencia-politica-estrategica-multivectorial`,
  invocable cuando dos órganos pueden colisionar sobre un mismo
  expediente.

trigger_phrases:
  - "diseña arquitectura inter-comisión"
  - "coordinar comisiones con competencias concurrentes"
  - "evitar superposición regulatoria entre Comisiones"
  - "aplica la skill articulacion-inter-comision-legislativa"

idioma_de_salida: español neutro institucional-jurídico

---

# Articulación Inter-Comisión Legislativa

## Filosofía

Cuando dos comisiones de la Asamblea Nacional tienen competencias
concurrentes sobre un mismo expediente, el resultado natural es
**superposición regulatoria**: dos leyes que regulan el mismo objeto
con criterios distintos, duplicando carga de cumplimiento y debilitando
la supervisión efectiva.

La inteligencia política previene esa superposición **antes** de que
se produzca, mediante una **arquitectura inter-comisión** que distingue
con precisión tres niveles de competencia:

1. **Competencia primaria** — cuál comisión es proponente y conoce el
   proyecto en primer debate.
2. **Consulta obligatoria** — cuál comisión recibe el proyecto para
   pronunciarse en aspectos específicos antes del segundo debate.
3. **Coordinación voluntaria** — cuál comisión recibe el proyecto
   para conocimiento y posible aporte facultativo.

## Las cuatro patologías de superposición regulatoria

Aprender a anticiparlas es la base del oficio.

| # | Patología | Síntoma | Mitigante |
|---|-----------|---------|-----------|
| **1** | **Superposición regulatoria** | Dos cuerpos legales regulan el mismo objeto con criterios distintos | Cláusula de remisión expresa entre las dos leyes; definiciones técnicas compartidas |
| **2** | **Sobreinclusión del perímetro** | Definición amplia captura actividades innovadoras sin control material | Definir el objeto por **función**, no por **tecnología** (neutralidad tecnológica) |
| **3** | **Patología probatoria** | Documentos electrónicos sin equivalencia funcional plena dejan la prueba a sana crítica judicial | Aprobar primero la ley habilitante (equivalencia funcional) o incorporar **norma puente** |
| **4** | **Incompatibilidad con soberanía monetaria** | Confundir activo digital con medio de pago vulnera Art. 303 CRE | Separar token de derecho preexistente vs. moneda alternativa con claridad |

## Paso 0 — Mapa de competencias del problema

> 1. **¿Qué comisión es proponente?** — La que conoce primero el
>    proyecto. Su competencia es **primaria**.
> 2. **¿Qué otras comisiones tienen agenda concurrente?** — Las que
>    han tratado un objeto análogo o complementario.
> 3. **¿Qué partes específicas del proyecto coinciden con la agenda
>    concurrente?** — Identificar artículos, capítulos, definiciones.
> 4. **¿Qué órgano ejecutivo administrará el régimen?** — Para
>    proyectar coordinación con la Función Ejecutiva.

## Paso 1 — Arquitectura de tres planos

Una vez mapeado el problema, distribuir las decisiones en tres
planos verticales:

```
PLANO I  — Ley habilitante transversal
           (norma marco que ambas comisiones necesitan)
           Aprobación conjunta de las DOS comisiones.

PLANO II — Reformas sectoriales especializadas
           Competencia de la comisión proponente,
           con consulta obligatoria a la otra en aspectos
           específicos (régimen sancionatorio, definiciones,
           coordinación operativa).

PLANO III — Reglamento operativo
            Competencia del Ejecutivo (Junta de Política y
            Regulación, Ministerio rector), bajo monitoreo
            de ambas comisiones.
```

Y si hay un eje transversal (por ejemplo, anti-lavado de activos),
agregar:

```
PLANO ANTI-LAVADO — Ley complementaria
                   Competencia primaria de la comisión transversal,
                   redactada como Ley complementaria al Plano I,
                   adoptando definiciones técnicas compartidas.
```

## Paso 2 — Articulación con el CAL

El Consejo de Administración Legislativa es la instancia que decide
el trámite. Solicitar al CAL que:

1. **Califique los proyectos como conexos** (artículo de la Ley
   Orgánica de la Función Legislativa correspondiente).
2. **Ordene el debate por bloques** en el orden lógico de los planos.
3. **Asigne coautoría a las dos comisiones** en el Plano I (norma
   habilitante).
4. **Reciba el documento maestro** que articula los proyectos como
   insumo técnico de calificación.

## Paso 3 — Redacción de la cláusula puente

Para evitar que la superposición se reproduzca en la práctica, todos
los proyectos del paquete deben incluir una **cláusula puente** o
**remisión expresa**:

> "Las anotaciones, firmas, sellos y documentos electrónicos a los
> que se refiere la presente Ley se rigen supletoriamente por la Ley
> Orgánica {nombre del Plano I} y por su normativa secundaria."

> "La presente Ley se aplica a los sujetos obligados conforme a la
> Ley Orgánica {nombre de la ley transversal de su comisión},
> evitando duplicación de obligaciones formales."

## Paso 4 — Catálogo de definiciones técnicas compartidas

El producto técnico más valioso de la articulación es un **catálogo
de definiciones técnicas compartidas** que ambas comisiones adoptan
por remisión. Reduce de inmediato el riesgo de superposición.

Para el caso EcuaLedger Soberana, las definiciones críticas
compartidas son:
- Proveedor de Servicios de Activos Virtuales (PSAV)
- Custodio cualificado
- Intermediario digital cualificado
- Protocolo descentralizado
- Red permisionada
- Nodo validador con personalidad jurídica
- Off-chaining del PII

## Paso 5 — Sesión técnica conjunta

Convocar a la contraparte técnica (FBSE o equivalente) a una sesión
**conjunta** de ambas comisiones, donde se presenta la arquitectura.
Ahí se firman los **acuerdos de trabajo conjunto** y se sella la
coordinación.

## Producto final de la skill

Una nota técnica de máximo 4 páginas que contiene:

1. Mapa de las comisiones involucradas y su perímetro de competencia.
2. Los tres (o cuatro) planos de la arquitectura.
3. La propuesta de articulación con el CAL.
4. Las cuatro patologías anticipadas con sus mitigantes.
5. La cláusula puente y el catálogo de definiciones compartidas.
6. La convocatoria a sesión técnica conjunta.

## Skills hermanas

- `inteligencia-politica-estrategica-multivectorial` — skill maestra.
- `memo-institucional-juridico-fbse` — para redactar el memo
  destinado a cada una de las comisiones articuladas.
- `sintesis-ejecutiva-mesa-presidencial` — si el conflicto inter-
  comisión debe escalarse a Presidencia para arbitraje.
- `estrategia-implementacion-juridica` — la guía maestra que sirve
  de base técnica común.

## Antipatrones

- ❌ Asumir que dos comisiones se coordinarán solas — no lo harán.
- ❌ Permitir que ambas redacten su propio proyecto sin remisión.
- ❌ Definir el objeto por tecnología (riesgo de obsolescencia).
- ❌ Pedir competencia primaria sobre todo a una sola comisión
  (genera resistencia).
- ❌ Omitir la cláusula puente.
- ❌ No convocar a sesión técnica conjunta.

## Caso resuelto

**B-012 → Comisión Soberanía + B-011 → Comisión Régimen Económico:**

Construcción de la arquitectura de cuatro planos:
- Plano I (LOFPD) — aprobación conjunta.
- Plano II (Reforma COMYF/LMV/COPLAFIP) — Régimen Económico primaria, Soberanía consulta obligatoria en Art. 207 sancionatorio.
- Plano III (Reglamento IBPP) — Ejecutivo bajo monitoreo de ambas.
- Plano Anti-Lavado — Soberanía primaria, complementaria de LOFPD.

Catálogo compartido de definiciones para PSAV, custodio, etc.
Sesión técnica conjunta convocada con la FBSE.
Cláusula puente incorporada en cada proyecto.

Resultado: cero patologías de superposición, cero zonas grises de
competencia, dos comisiones con misión clara y distinguida.
