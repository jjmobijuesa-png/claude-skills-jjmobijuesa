---
name: auditoria-corrida-financiera-inmobiliaria
description: |
  Criterios para AUDITAR y para PRESENTAR una corrida financiera inmobiliaria
  antes de una decisión de crédito, inversión o aprobación. Destila las
  observaciones reales de un revisor externo a las corridas de San Sebastián y
  Belén (28-sep-2026): dónde suele fallar la FORMA (terminología, denominador,
  KPIs no reconstruibles) aunque la matemática esté bien, y cómo blindar el
  supuesto tributario del IVA. Sirve para revisar una corrida ajena y para no
  cometer esos errores al armar la propia.
trigger_phrases:
  - "revisa esta corrida financiera"
  - "audita el modelo financiero del proyecto"
  - "observaciones a la presentación financiera"
  - "está bien calculada la utilidad / el margen / el EBITDA"
  - "cómo presento la devolución de IVA"
  - "prepara la corrida para el comité de crédito"
idioma_de_salida: español (Ecuador), trato de usted
nivel: aplicada
dominio: finanzas inmobiliarias / auditoría de modelos
metadata:
  version: 2.0
  fecha: 2026-10-31
  origen: observaciones del revisor a San Sebastián y Belén (28-sep-2026) + Informe de Evaluación Financiera v2 de San Sebastián (29-oct-2026) + 12 preguntas del revisor respondidas por el CEO (30-oct-2026)
  relacionada:
    - principios-financieros-puros
    - control-versiones-entregables
    - modelo-tres-estados-integrado
    - wolfram-forensic-engine
    - cfo-virtual-44-agentes
    - modelo-excel-sistema-vivo
    - bonos-vivienda-ecuador-2026
    - analisis-variaciones-cascada
    - cierre-verificado-integridad
    - gobernanza-datos-financieros-ia
---

# Skill `auditoria-corrida-financiera-inmobiliaria`

## Doctrina en una frase
La matemática suele estar bien; lo que hunde una corrida ante un comité es la
**FORMA**: un término mal usado, un denominador cambiado, un KPI que no se
reconstruye, o un beneficio incierto tratado como caja segura. Audite (y arme)
por la forma, no solo por la aritmética.

## Los siete criterios (cada uno nació de una observación real)

### 1 · «Utilidad bruta» es un término reservado — no lo use para el resultado final
Utilidad bruta = **ingresos − costo de ventas (construcción)**, ANTES de gastos
operativos y financieros. Si a un número ya le restó terreno, infraestructura,
indirectos, ventas y el **costo financiero**, eso NO es utilidad bruta: es
**«resultado antes de participación e IR»** (o utilidad operativa según el caso).
👉 Muestre la utilidad bruta real (24% típico) Y el resultado antes de impuestos,
con nombres distintos. Un comité de crédito nota el término flojo al instante.

### 2 · Los márgenes se calculan sobre VENTAS, no sobre «ventas + beneficios»
Meter una recuperación tributaria (devolución de IVA) o un subsidio en el
denominador de «ingresos» **infla o deforma** todos los márgenes. Divida por las
**ventas (PVP)**. Y presente dos márgenes netos: **con** y **sin** el beneficio
tributario, para que se vea que el proyecto se sostiene sin él.
- Ej. real: 9,6% (÷ ventas+IVA) era en verdad **10,1% ÷ ventas** (5,0% sin IVA).

### 3 · Todo KPI de portada debe reconstruirse de las partidas visibles
Si el lector no puede rehacer el EBITDA (o cualquier KPI) sumando y restando lo
que ve en la lámina, **no lo presente sin el puente**, o retírelo. Un KPI que
«sale de un anexo» que nadie ve resta credibilidad justo donde busca darla.
- Ej. real: EBITDA $2,18 M no cuadraba con las partidas visibles ($1,996 M);
  se retiró de la presentación y se dejó como métrica interna del libro.

### 4 · La devolución de IVA NO es caja segura del día 1 — preséntela con escenarios
La devolución existe para VIS/inmobiliario calificado, pero el SRI paga el IVA
**efectivamente pagado, elegible y respaldado**, con trámite de hasta 90 días.
Nunca la incorpore como ingreso cierto. Modélela como:
```
IVA generado/pagado elegible − IVA usado como crédito tributario − IVA no elegible = IVA recuperable
```
y muestre **tres escenarios**: A pleno · B sin IVA (piso) · C parcial (p. ej. 50%).
El habilitante del 100% suele ser: fideicomiso al 100% del flujo + registro del
ente rector (MIT) + facturas del proyecto. Ver [[bonos-vivienda-ecuador-2026]].

### 5 · Una sola cifra oficial por concepto — concilie los costos unitarios
Si aparecen $26.167, $27.104 y $27.349 por vivienda en tres lugares, el modelo
pierde autoridad aunque uno sea el correcto. **Reconcilie a una sola cifra**
oficial (costo directo total ÷ unidades) y úsela en todo el libro y el deck.

### 6 · No confunda margen ACUMULADO con margen ANUAL
Un spread de cartera del «21%» sobre el capital inicial durante 10 años **no es**
un margen financiero anual del 21%. Dígalo completo: «margen acumulado estimado
de $X, equivalente al Y% del monto inicial durante el plazo de N años».

### 7 · VAN sin su flujo es una afirmación, no un cálculo
Un VAN necesita el **flujo mensual** (desembolsos, ventas, IVA, terreno,
construcción, gastos, impuestos, amortización, residual) en un anexo verificable.
Y en flujos **no convencionales** (la cobranza entra antes que el gasto) la TIR
simple no es interpretable: use **MIRR** y dígalo. Ver [[modelo-excel-sistema-vivo]].

### 8 · Un cambio de UN supuesto obliga a re-verificar TODA la cadena — en el libro Y en cada entregable
Cuando mueve una sola palanca (agregar un costo, cambiar el IVA, el precio, el plazo), **cada cifra
derivada cambia**: EBITDA, participación, IR, utilidad, márgenes, VAN, costo unitario, y las mismas
cifras repetidas en el deck, los HTML y los PDF. El error clásico es actualizar el resultado final
(la utilidad) y dejar el EBITDA o los indirectos viejos → el revisor lo caza al instante porque
**ya no reconstruye** (criterio 3). Regla: tras cualquier ajuste, **lea las cifras vivas del libro
recalculado** y **re-escanee cada entregable** por los números viejos antes de enviar; no confíe en
un reemplazo parcial hecho de memoria. Ver [[cierre-verificado-integridad]].
- Ej. real (Belén, 28-sep): incorporar el auditor bajó el EBITDA, pero un reemplazo incompleto dejó
  el deck con EBITDA viejo + utilidad nueva → inconsistencia detectada por el revisor. Se corrigió
  recalculando el libro y escaneando el deck: las cifras viejas solo debían sobrevivir en la lámina
  de *escenarios*, nunca en la línea base.

## v2.0 — Ocho criterios más (Informe de Evaluación v2, San Sebastián, 29/30-oct-2026)

### 9 · Recuperar el capital NO es utilidad — el retorno es capital recuperado + utilidad
Terreno y urbanización ya invertidos entran al **costo** (costeo completo) y se recuperan dentro del
PVP. La utilidad neta ya los descontó. Retorno al propietario = **capital recuperado + utilidad neta**.
Sumar las dos cosas es correcto; llamar «utilidad» a la suma, o devolver un capital que **nunca se cargó
como costo**, es doble conteo. Ver [[principios-financieros-puros]] §1.
- Ej. real (v1, 28-oct): la urbanización de $1,77 M no estaba en el costo, pero el «retorno total»
  sumaba $2,3 M de capital: retorno inflado en $1,7 M. v2: costo completo, neta $1,92 M, retorno $4,30 M.

### 10 · El capital ya invertido es aporte EN ESPECIE: va al costo, no a la caja
Un terreno propio no «sale» en el mes 1 del flujo: es costo hundido para la caja y costo de ventas
para el PyG. En el flujo va como memo; en el balance, como patrimonio en especie.

### 11 · El IVA contenido en un precio con IVA es P × t/(1+t), y lo recuperable es una fracción
Si el contrato es llave en mano «con IVA», el IVA es P×0,15/1,15 (no P×0,15). Lo recuperable es la
relación estimada sobre ese IVA (p. ej. 60 %), con tope y rezago de 90 días; preséntelo también en
el escenario **sin** devolución (criterio 4).

### 12 · Las unidades retenidas para renta son propiedad de inversión, no costo de lo vendido
Capitalícelas a costo (NIC 40) en el balance y separe su renta (con vacancia, mantenimiento,
administración, seguros y predial: rendimiento **neto**, no bruto).

### 13 · El cobro sigue a la ESCRITURA, y la escritura sigue a la obra terminada
Banco: escritura + 90 días; bono: + 30 días; IVA: pago de obra + 90 días. Las reservas se asignan
en orden de construcción. Esto mueve la necesidad de crédito más que cualquier otro supuesto
(San Sebastián: pico BDE $1,55 M → $3,21 M).

### 14 · «La caja nunca queda en rojo» solo vale CON su financiamiento dicho
Muestre el flujo acumulado sin financiamiento (su mínimo es la necesidad real), y luego cómo se
cubre: aporte propio de arranque + línea de crédito con su límite. Indicadores de caja
(J. Altimira): flujo operativo, flujo libre, ciclo de conversión, burn rate, runway.

### 15 · Sensibilidad sobre utilidad Y liquidez, y veredicto honesto contra umbrales fijados antes
Costos +5/+10 %, precios −5/−10 %, ventas +3/+6 meses, desembolsos +60 días, sin IVA. Si el
resultado no cumple los umbrales, se dice («condicionado, 2 de 4») y se muestran las palancas que
lo cierran: **nunca se mueve el umbral**.

### 16 · Reconstruir los números del revisor antes de responderle
Si el informe cita cifras que no son las suyas, reprodúzcalas al dólar con versiones anteriores:
casi siempre revisó otra versión. La causa raíz se arregla con [[control-versiones-entregables]].
- Ej. real: el informe del 29-oct citaba costos de $10.235.622; salían al dólar de la v6, no de la v1.

## Checklist rápido (antes de entregar una corrida a un comité)
- [ ] ¿El capital invertido está en el costo, y el retorno se presenta como capital + utilidad (no como utilidad)?
- [ ] ¿Terreno/urbanización propios fuera de la caja y dentro del costo y del patrimonio?
- [ ] ¿IVA contenido = P×t/(1+t); recuperable con relación, tope, rezago y escenario sin IVA?
- [ ] ¿Unidades de renta capitalizadas y rendimiento neto?
- [ ] ¿Cobros atados a la escritura (unidad terminada) con sus rezagos?
- [ ] ¿Necesidad de caja sin financiamiento visible, y cubierta por aporte + línea con límite?
- [ ] ¿Sensibilidad de utilidad y liquidez; veredicto contra umbrales previos?
- [ ] ¿Pasó el validador de [[control-versiones-entregables]] con «TODO CUADRA»?
- [ ] ¿Cada resultado se llama por su nombre contable correcto? (bruta ≠ antes de impuestos ≠ neta)
- [ ] ¿Los márgenes están sobre VENTAS? ¿Muestro neto con y sin beneficio tributario?
- [ ] ¿Cada KPI de portada se reconstruye de lo visible, o tiene su puente?
- [ ] ¿La devolución de IVA está en escenarios (con/sin/parcial), no como caja segura?
- [ ] ¿Una sola cifra oficial por concepto (costo unitario, ingresos, utilidad)?
- [ ] ¿Distingo margen acumulado de anual?
- [ ] ¿El VAN tiene su flujo anexo y uso MIRR si el flujo es no convencional?
- [ ] ¿Los controles del modelo vivo están en cero tras cualquier ajuste? ([[cierre-verificado-integridad]])
- [ ] ¿Tras cambiar un supuesto, releí las cifras vivas y re-escaneé CADA entregable (deck/HTML/PDF) por números viejos?

## Qué NO hacer
- No «ganar» el margen inflando el denominador ni el resultado con un nombre prestado.
- No presentar un KPI que usted mismo no puede reconstruir en la lámina.
- No prometer la devolución de IVA como dinero seguro sin el desglose tributario.
- No dejar tres cifras distintas del mismo concepto «porque una es la buena».

## Relacionadas
- [[cfo-virtual-44-agentes]] · [[modelo-excel-sistema-vivo]] · [[bonos-vivienda-ecuador-2026]]
- [[analisis-variaciones-cascada]] · [[cierre-verificado-integridad]] · [[gobernanza-datos-financieros-ia]]
- [[principios-financieros-puros]] · [[control-versiones-entregables]] · [[modelo-tres-estados-integrado]] · [[wolfram-forensic-engine]]
