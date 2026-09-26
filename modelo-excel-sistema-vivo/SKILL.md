---
name: modelo-excel-sistema-vivo
description: >
  Construir y mantener modelos financieros en Excel como un sistema vivo de
  fórmulas vinculadas, con separación explícita entre variables independientes
  (celdas editables, una sola palanca por concepto) y celdas dependientes
  (calculadas). Marca las independientes en amarillo pastel + comentario y las
  dependientes en azul pastel, con leyenda, y prueba el sistema cambiando una
  palanca. Úsala al crear o modificar libros como el de San Sebastián.
metadata:
  type: reference
---

# Modelo Excel como sistema vivo

Un modelo financiero es un **grafo de dependencias**, no una tabla de números.
La regla: **cada dato que puede variar vive en UNA sola celda independiente**, y
todo lo demás la referencia por fórmula. Cambiar esa celda debe recalcular todo
lo dependiente, sin edición manual en cascada.

## Independientes vs dependientes

- **Independiente (entrada editable):** SBU, costo $/m², markup, PVP/m² de un
  tipo de unidad, % financiado, tasa, meses de gracia/amortización, **monto del
  crédito**, caja inicial, fracciones de reparto del flujo. Amarillo pastel
  `FFF2CC` (BGR `0xCCF2FF`) + comentario que empiece por «VARIABLE INDEPENDIENTE».
- **Dependiente (calculada):** PVP, costos, márgenes, cuota, intereses, saldos,
  utilidad, controles. Azul pastel `DDEBF7` (BGR `0xF7EBDD`). No se editan.
- **Leyenda** visible junto a los parámetros: «amarillo = independiente editable ·
  azul = dependiente, no editar».

**Una sola palanca por concepto.** Si el usuario cambia el monto del crédito «en
la mañana», debe existir UNA celda (p. ej. `P60`) que sea la entrada, y el resto
(`P64=P60`, cuota, intereses, flujo, tabla de amortización) cuelga de ella. Nunca
dos celdas que haya que sincronizar a mano. Si una celda ya era fórmula-máximo
(80% de CD), se conserva como referencia y se agrega un control «¿entrada ≤ máx?».

## Vincular, no copiar

- Áreas desde los lados: `H = ROUND((Norte+Sur)/2*(Este+Oeste)/2, 2)` — celda viva;
  si el lote cambia de dimensiones, el área, el PVP y el ingreso se actualizan.
  Los lotes con lados partidos en el levantamiento se conservan estáticos y se
  marcan para verificación de campo (no inventar el área).
- Topes de programa con `MIN(fórmula, techo)` para no salirse de VIS/VIP.
- Controles que deben dar 0 (ingresos vs. consolidador, obra vs. presupuesto,
  intereses de la tabla vs. costo financiero, capital amortizado vs. monto).
- **MAPA DE VÍNCULOS** en la fila 2 de cada hoja nueva: de dónde lee y a dónde
  entrega.

## Comentarios

`celda.ClearComments()` y luego `celda.AddComment(texto)` vía COM
(`win32com DispatchEx`); `Comment.Shape.TextFrame.AutoSize = True`. Comentar al
menos todas las independientes maestras.

## Reordenar/mover hojas sin perderlas (bug de pywin32 tardío)

**`Worksheet.Move(After=<hoja>)` con argumento por PALABRA CLAVE se ignora en el
dispatch tardío de pywin32** → equivale a `Move()` sin argumentos → **la hoja se va a
un LIBRO NUEVO y se pierde al `Quit()`**. Ya costó perder dos hojas (BALANCE y
ESPECIFICACIONES) en esta caja. Firmas: tras un `Move`, la hoja desaparece de
`[s.Name for s in wb.Worksheets]` aunque el script no lance error.

**Regla:** para mover una hoja usar SIEMPRE el argumento **posicional `Before`**:

```python
ws.Move(wb.Worksheets(1))          # mueve ws ANTES de la hoja 1 (al frente) — FUNCIONA
```

Reordenar todo el libro sin pérdidas: recorrer el orden deseado **en reversa** y mover
cada hoja al frente, con **guardia de conteo** (si `Worksheets.Count` cambia, abortar y
cerrar SIN guardar). Verificar el orden en disco con openpyxl después. Nunca usar
`Move(After=…)` ni `Add(After=<obj>)` (también coloca mal); crear con `Add()` y
posicionar después con `Move(Before=…)` posicional. Orden lógico de un modelo:
**tablas de unidades que alimentan directo el consolidado (p. ej. VIVIENDAS, DEPARTAMENTOS)
→ presupuesto consolidado → informes dinámicos (PyG, Flujo, Balance, lecturas para el CEO)
→ explicaciones (normativa, especificaciones, memoria) → plano → ANEXOS de datos MUY
granulares (levantamiento de lotes, áreas/PVP por solar) → escenarios antiguos/antecedentes**
(ocultables o borrables al final). 🚦 Matiz aprendido (San Sebastián, 23-sep-2026): las hojas
de **datos granulares de origen** (lote por lote, precios por solar) NO van al frente sino
como **anexos al final** (antes de los antecedentes); el libro debe abrir en lo que el
lector/CEO necesita (unidades → consolidado → informes), no en el levantamiento de detalle.

## Balance vivo que cuadra por construcción

Un balance de proyecto cuadra si el patrimonio o el activo se define como RESIDUO:
`Total Pasivo+Patrimonio = Pasivo + Aporte propio + Utilidad neta`; una partida de
activo («posición neta por cobrar/realizar») = `(Pasivo+Patrimonio) − Caja`, de modo
que `Total Activo = Caja + esa partida = Pasivo+Patrimonio` y el CONTROL da 0 siempre.
Caja ← flujo, crédito por pagar ← flujo, utilidad ← PyG: los tres cuelgan del monto de
crédito, así que balance, flujo y PyG se mueven juntos al cambiar la palanca.

## Prueba del sistema (obligatoria antes de cerrar)

Cambiar una palanca (p. ej. el monto del crédito) → `CalculateFull()` → leer que
cuota, utilidad y la tabla de amortización cambiaron → **revertir**. Si no cambian,
la cadena está rota (una celda quedó en valor y no en fórmula).

Formato y pila COM segura: [[excel-formato-dolar-y-m2]] (dinero `$#.##0,00`, áreas
`" m²"`, `NumberFormatLocal`, respaldo previo, cerrar sin huérfanos). Cierre de la
respuesta: [[cierre-verificado-integridad]]. Ante fallo: [[regla-del-primer-tropiezo]].
