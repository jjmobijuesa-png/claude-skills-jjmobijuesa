# Marco inicial — Juntas de Política y Regulación, estándares de Basilea e IBPP

**Archivo principal provisional del hilo.** Redactado por la sesión nube el 2026-10-02,
antes de tener acceso a los documentos de la carpeta de Drive. Todo lo marcado
**[verificar]** se contrasta contra los documentos y el Registro Oficial vigente
antes de usarlo en un memo dirigido a la Asamblea.

Programa de referencia: EcuaLedger Soberana — IBPP (Infraestructura Blockchain Pública
Permisionada). Arquitectura legislativa ya fijada en el repo (skill
`articulacion-inter-comision-legislativa`): Plano I (LOFPD), Plano II (reforma
COMYF/LMV/COPLAFIP), Plano III (reglamento IBPP, Ejecutivo).

---

## 1. Mapa institucional (quién regula qué)

| Órgano | Competencia relevante para la IBPP | Base |
|---|---|---|
| Junta de Política y Regulación **Monetaria** | Política monetaria, sistema nacional de pagos, regulación del BCE, medios de pago | COMYF reformado por la Ley Orgánica Reformatoria al COMYF para la Defensa de la Dolarización (2021) |
| Junta de Política y Regulación **Financiera** | Regulación prudencial de bancos, cooperativas (con la SEPS), seguros y valores; servicios financieros tecnológicos | Ídem; Ley Fintech (2022) **[verificar artículos]** |
| Banco Central del Ecuador | Liquidación final, sistema de pagos, custodia de reservas | CRE Arts. 302-303; COMYF |
| SB / SEPS / SCVS | Supervisión de entidades; SCVS para valores tokenizados | CRE Art. 213; COMYF; LMV |
| COSEDE | Seguro de depósitos y fondo de liquidez | COMYF |

**Punto de redacción:** la sigla JPRFM corresponde a la Junta única del COMYF de 2014.
Desde la reforma de 2021 son **dos juntas**. Todo texto dirigido a la Asamblea debe
asignar cada mandato a la junta correcta; un mandato a una junta inexistente es un
defecto de técnica legislativa que la Comisión detectará. **[verificar si hubo reformas
posteriores a 2021 que alteren esta división]**

## 2. Qué pide hoy Basilea (BIS / BCBS / CPMI) y cómo encaja una red permisionada

| Estándar | Contenido útil | Consecuencia para la IBPP |
|---|---|---|
| BCBS — tratamiento prudencial de exposiciones a criptoactivos (SCO60, 2022; enmiendas 2024; vigencia prevista 1-ene-2026) | Grupo 1a: activos tradicionales tokenizados (mismo capital que el subyacente). Grupo 1b: stablecoins con mecanismo eficaz. Grupo 2: el resto, ponderación de hasta 1250 % y límite de exposición. Recargo por riesgo de infraestructura en redes sin permisos. | Diseñar la IBPP para que lo que registre califique como **Grupo 1a**: títulos, garantías y depósitos tokenizados con el mismo derecho jurídico que el activo tradicional. Sin token nativo especulativo. **[verificar: el BCBS anunció una revisión acelerada de partes del estándar; confirmar su estado a la fecha]** |
| CPMI-IOSCO — Principios para Infraestructuras del Mercado Financiero (PFMI) y su guía para arreglos de stablecoins | Gobierno, firmeza de la liquidación (*settlement finality*), riesgo operativo, acceso | Si la IBPP liquida o registra valores, es una IMF: necesita regla de firmeza jurídica en la ley, no solo técnica |
| BCBS — Principios de resiliencia operativa (2021) y Principios Básicos revisados (2024) | Terceros críticos, continuidad, ciberseguridad | Los operadores de nodos son proveedores críticos: licencia, auditoría y plan de salida |
| BIS — visión de "libro mayor unificado" y Proyecto Agorá | Depósitos tokenizados + dinero de banco central en una plataforma programable | Argumento de política pública: la IBPP sigue la dirección del BIS, no la del mercado cripto |
| FSB — recomendaciones sobre criptoactivos y stablecoins (2023) | Misma actividad, mismo riesgo, misma regulación | Neutralidad tecnológica en la definición legal |

## 3. Restricciones constitucionales y legales de Ecuador

1. **Soberanía monetaria y dolarización** (CRE Arts. 302-303; COMYF). La IBPP no puede
   emitir ni hacer circular una unidad que funcione como moneda. Solución: el token es
   **representación registral de un derecho preexistente** (depósito en dólares, valor,
   garantía), nunca medio de pago alternativo. Es la patología 4 de
   `articulacion-inter-comision-legislativa`.
2. **Actividad financiera como servicio de orden público** (CRE Art. 308): solo por
   entidades autorizadas. Los operadores de nodos que validen operaciones financieras
   necesitan un estatus regulatorio definido.
3. **Protección de datos** (LOPDP): en una red pública permisionada los datos personales
   van fuera de la cadena; en la cadena, solo huellas (*hash*) y referencias.
4. **Equivalencia funcional y prueba** (Ley de Comercio Electrónico, Firmas y Mensajes de
   Datos; COGEP): el registro en la IBPP debe tener valor probatorio expreso.

## 4. Lo que la reforma debe decir (aportes concretos)

| # | Aporte | Dónde va |
|---|---|---|
| A1 | Definir la IBPP por función (registro distribuido con nodos autorizados), no por marca tecnológica | Plano I |
| A2 | Asignar a la **Junta Monetaria** la regulación de pagos y liquidación sobre la IBPP, y a la **Junta Financiera** la regulación prudencial de exposiciones, con plazos en disposiciones transitorias | Plano II |
| A3 | Ordenar que la regulación prudencial siga el estándar BCBS de criptoactivos, con clasificación expresa de los activos de la IBPP como tokenizados tradicionales | Plano II |
| A4 | Regla legal de firmeza de la liquidación y de oponibilidad del registro | Plano II |
| A5 | Régimen de operadores de nodo: autorización, requisitos, responsabilidad, auditoría | Plano II / III |
| A6 | Prohibición de token nativo con función monetaria; salvaguarda del Art. 303 | Plano II |
| A7 | Espacio de pruebas regulatorio coordinado entre las dos juntas y las superintendencias | Plano II / III |
| A8 | Datos personales fuera de la cadena; derecho de supresión resuelto en la capa fuera de la cadena | Plano III |

## 5. Estrategia de implementación (borrador)

1. **Fase 0 — diagnóstico normativo** (este hilo): inventario de resoluciones vigentes de
   ambas juntas que la reforma deroga, modifica o deja fuera; matriz de brechas frente a Basilea.
2. **Fase 1 — trámite legislativo**: competencia primaria en Régimen Económico, consulta
   obligatoria en la comisión de Soberanía (ya mapeado en el repo); calificación del CAL.
3. **Fase 2 — normativa secundaria**: resoluciones de las juntas dentro del plazo de la
   transitoria; reglamento IBPP.
4. **Fase 3 — piloto en *sandbox***: un caso de bajo riesgo y alto valor probatorio
   (registro de garantías o anclaje documental) antes de cualquier liquidación de valores.
5. **Fase 4 — producción** con evaluación de cumplimiento PFMI.

## 6. Preguntas abiertas para el usuario

1. ¿Qué significa "excluida en una serie de reformas": competencias de las juntas que las
   reformas dejan fuera, o resoluciones de las juntas que quedan excluidas de la reforma?
2. ¿Qué reformas concretas se están asesorando (número de proyecto o nombre)?
3. ¿Qué documento de Basilea es "las nuevas directrices"? (estándar de criptoactivos,
   revisión de 2025-2026, Principios Básicos, otro).
4. ¿El destinatario del producto es una comisión específica?
