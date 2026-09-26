---
name: calificacion-fondos-multilaterales-impacto
description: >
  Doctrina y procedimiento para CALIFICAR un proyecto ante una entidad
  financiera multilateral de desarrollo (BID / BID Lab, CAF, IAF, FIDA,
  GIZ, AECID) y lograr que lo valide y le asigne fondos. Cubre el
  diagnóstico de elegibilidad real (¿a quién financia de verdad este
  fondo?), la traducción del proyecto al lenguaje de inversión de
  impacto, la guía de cumplimiento, y el empaquetado documental.
  Invocar cuando el usuario diga «postular a un fondo», «convocatoria
  BID/CAF», «calificación ante entidad financiera», «fondos
  disponibles», «nota de inversión de impacto», o cuando aparezca un
  link de convocatoria de un organismo multilateral.
---

# Calificación de proyectos ante fondos multilaterales de impacto

## 1. La regla que evita el error más caro

> **Antes de escribir una sola línea, determinar A QUIÉN FINANCIA
> REALMENTE el fondo.**

La mayoría de las postulaciones fracasan porque el postulante no es
elegible y nadie lo verificó. Las tres categorías:

| El fondo financia… | Postulante elegible | Ejemplo real |
|---|---|---|
| **Gestoras de fondos (LP)** | Firma gestora de VC/PE, no el proyecto | BID Lab — Convocatoria Fondos de Venture Capital |
| **Empresas / soluciones con retorno** | Empresa, spin-off o vehículo invertible | CAF — Fondo de Impacto VELA |
| **Entidades públicas o sin fines de lucro** | Fundación, ONG, contraparte estatal | Cooperación Técnica No Reembolsable de CAF |

**Caso testigo (2026-07-21, EcuaLedger/FBSE):** la convocatoria de
Venture Capital del BID Lab financia **gestoras de fondos**, no
fundaciones ni proyectos. Una fundación NO es postulante directo. La
ruta real resultó ser **LACChain** (la red blockchain del propio BID)
más la ventanilla de cooperación técnica. Detectarlo a tiempo ahorró
una postulación condenada.

## 2. Segunda regla: impacto CON retorno ≠ donación

Los fondos de impacto (VELA, FIIALC, BID Lab) **invierten**, no
donan. Todo material debe leerse como **oportunidad de inversión
escalable**. La secuencia obligatoria de una nota de inversión:

```
problema → solución → población objetivo → teoría de cambio →
métricas de impacto → monto solicitado → RETORNO / SOSTENIBILIDAD
```

Si falta el último eslabón, el fondo no puede asignar capital aunque
el impacto sea excelente. **La brecha típica de una fundación es no
tener vehículo invertible**: resolverla con (a) solución licenciable
con ingresos (SaaS), (b) spin-off empresarial, o (c) co-inversión en
el vehículo que despliega la infraestructura.

## 3. Procedimiento

1. **Leer la convocatoria oficial**, no solo el resumen de terceros.
   Extraer: organismo, instrumento, a quién financia, sectores,
   geografía, montos, deadline, criterios de evaluación, URL oficial.
2. **Diagnóstico de elegibilidad** → tabla de rutas de encaje
   ordenadas por viabilidad (alta / media / baja) con el esfuerzo que
   exige cada una. Recomendar explícitamente cuál abrir primero.
3. **Matriz de cumplimiento**: criterio del fondo × ¿cumple? ×
   evidencia o brecha. Ser honesto con las brechas — son el plan de
   trabajo, no una debilidad que ocultar.
4. **Inventario de activos reutilizables**: casi siempre ya existe
   70–80 % del contenido en propuestas anteriores. Reempaquetar, no
   reescribir ([[eficiencia-generacion-respuestas]]).
5. **Requisitos institucionales transversales** (siempre exigidos):
   personería jurídica y estatuto con fines compatibles,
   representante legal vigente, cumplimiento antilavado (UAFE en
   Ecuador), cuenta bancaria institucional, cartas de intención de
   aliados, capacidad de contrapartida en especie (20–30 %).
6. **Secuencia de acción a 90 días** con hitos fechados.
7. **Advertencias de precisión**: estados en curso nunca como
   aprobados; citas normativas verificadas en redacción vigente;
   cifras estimadas marcadas como tales.

## 4. Entregables estándar

Organizar en carpeta dedicada del proyecto:

```
Fondos Disponibles/
├── 00_Compilado_Especificaciones_y_Cumplimiento/
│   ├── 00_ESPECIFICACIONES_FONDOS.md
│   └── 01_GUIA_CUMPLIMIENTO.md
├── 01_Borrador_Proyecto/
│   └── BORRADOR_Proyecto_<nombre>_v1.docx
└── <Un subfolder por fondo>/
```

El .docx se genera con `python-docx` (disponible en esta máquina):
portada institucional, numeración de página inferior derecha desde la
pág. 2 ([[numeracion-paginas-informes]]), tablas con encabezado navy
`0F2E54`, firma del usuario.

**Scripts incluidos en esta skill (`scripts/`):**

| Script | Uso |
|---|---|
| `build_borrador_docx.py` | Plantilla del borrador institucional completo (portada + 8 secciones + tablas + firma). Editar contenido y ejecutar. |
| `md2docx.py` | Conversor Markdown → Word. `python md2docx.py archivo1.md archivo2.md` genera los `.docx` junto a cada fuente. Respeta encabezados (1–4), tablas, viñetas, listas numeradas, casillas `- [ ]` → ☐/☒, negritas, cursivas, código, citas y reglas horizontales. |

⚠️ Al imprimir a consola desde Python en esta máquina, el encoding
`cp1252` falla con caracteres Unicode (guiones no separables, ☐, —).
Escribir siempre la salida a un archivo UTF-8 y leerlo, en vez de
`print()` directo.

## 5. Fondos ya mapeados (actualizar al reutilizar)

| Fondo | Financia a | Deadline / estado | Nota |
|---|---|---|---|
| **BID Lab — VC Funds** | Gestoras de fondos VC | 30-sep-2026, inversiones 2027 | Fintech/climate/agtech/health/edtech |
| **BID — LACChain** | Nodos e infraestructura blockchain | Permanente | Puerta natural de proyectos blockchain |
| **CAF — Fondo VELA** | Empresas, fondos y soluciones | Lanzado 21-jul-2026 | US$100–150M; Sonen Capital + Fondo de Fondos; inclusión financiera, agricultura regenerativa, biodiversidad, salud, educación |
| **CAF — FIIALC** | Proyectos de impacto | Vigente | Usado en la propuesta CAF-Ecuador |
| **CAF — Coop. Técnica No Reembolsable** | Contraparte pública soberana | Vigente | Requiere beneficiario estatal |

## 6. Compuertas 🚦

1. **No afirmar elegibilidad sin haber leído la convocatoria oficial.**
2. **No prometer que un fondo "seguro" aprobará**: el rol es preparar
   la calificación, no garantizarla.
3. **Mantener en condicional** todo estado en trámite (ISO, convenios
   no firmados, personería en reforma).
4. **Diferenciar fondos parecidos** del mismo organismo antes de citar
   cifras (ej. VELA US$100–150M vs fondo de biodiversidad ~US$300M).
5. **Nunca presentar infraestructura blockchain soberana como
   criptomoneda o activo especulativo** — es infraestructura pública
   digital con seguridad jurídica.
6. Tómate tu tiempo. Calidad antes que velocidad.

## Relacionado

- [[project_fondos_bid_vela_ecualedger]] — caso de aplicación completo.
- [[baculo-mision-soberana]] — la Carta de Misión abre todo proyecto económico.
- [[memoria-financiera-inteligenciada]] — «caja > utilidad»; disciplina de decir la verdad financiera.
- [[eficiencia-generacion-respuestas]] — reutilizar artefactos, entregar el delta.
- [[numeracion-paginas-informes]] · [[documentos-encuadrados-margenes]] — formato de entregables.
- [[llave-maestra-autoaprendizaje-ia]] — doctrina que originó esta skill.
