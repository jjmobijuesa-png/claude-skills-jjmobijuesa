---
name: conciliacion-multicuenta-fdc
description: |
  Concilia la caja REAL de Francisco Duque cuando el dinero vive repartido en varias
  cuentas: la corriente Produbanco 02013011800 (operativa) y la de ahorros Produbanco
  20002966261 a nombre de Diana Villavicencio (RESERVA DE SEGURIDAD, dinero suyo).
  Regla madre: **las transferencias ENTRE cuentas propias son NEUTRAS** — no son ingreso
  ni gasto, solo cambian de bolsillo. Contarlas infla el gasto y esconde la caja.
  Produce la posicion de caja consolidada, corrige el flujo del mes y recalcula runway.
trigger_phrases:
  - "concilia las cuentas"
  - "caja consolidada"
  - "cuanto tengo en total"
  - "conciliacion multicuenta"
  - "cuenta alterna"
  - "cuenta de seguridad"
  - "posicion de caja real"
idioma_de_salida: espanol
nivel: aplicada
dominio: finanzas / conciliacion
metadata:
  version: 1.0
  fecha: 2026-08-17
  origen: >
    Pedido del usuario (2026-08-17) tras aportar los estados de las dos cuentas en
    `04 Patrimonio y Balance\Estado de cuenta varios`. Antes de esto, el flujo trataba
    el traslado de 2.000 a la cuenta alterna como si fuera gasto, y medía el runway
    con una sola cuenta.
  relacionada:
    - cfo-mensual-con-claude
    - gastos-whatsapp-gracias-totales
    - project-finanza-integral-perfil-millonario
---

# Skill `conciliacion-multicuenta-fdc`

## Las cuentas (mapa verificado)
| # | Cuenta | Titular | Rol | Evidencia |
|---|---|---|---|---|
| 1 | **Produbanco corriente 02013011800** | Francisco Duque Cedeño (CI 1203120884) | **Operativa**: recibe el depósito de honorarios y paga el día a día | Estado julio 2026 |
| 2 | **Produbanco ahorros 20002966261** | Diana Johanna Villavicencio Rivera (CI 1205144692) | **Reserva de seguridad** — dinero de Francisco. Se abastece la operativa desde aquí cuando hace falta | Estado agosto 2026 |
| 3 | Banco del Pacífico cta. cte. | Francisco Duque | Residual (saldo informado 7,26) | Informado por el usuario |
| 4 | B. Pacífico — ETRIEK ECUADOR S.A. | La compañía | **NO consolida**: es de la sociedad, no del patrimonio personal | Informado por el usuario |

🚦 La cuenta 2 está a nombre de un tercero. Es dinero del usuario, pero **no es demostrable
ante un banco como activo propio**. Para bancabilidad hay que decirlo así, no ocultarlo.

## Regla madre: los traslados no son gasto
Cuando sale dinero de la cuenta 1 hacia la 2 (o al revés) **no ocurre nada económico**:
cambia de bolsillo. El error de contarlo como gasto produce dos distorsiones:
1. **Infla el egreso** del mes en que sale.
2. **Infla el ingreso** del mes en que vuelve, haciendo creer que hubo una entrada nueva.

Ambas dan una lectura falsa del flujo operativo y del runway.

## Como identificar un traslado
- **En la operativa:** `TRANSFERENCIA INTERBANCARIA B.L.` o `TRANSFERENCIA CTAS TERCEROS`
  cuyo destino sea la cuenta de reserva (contraparte **Diana Villavicencio** en la
  notificación de Produbanco).
- **En la reserva:** `TRANSFERENCIA INTERBANCARIA B.L.` de salida en fechas y montos que
  reaparecen como crédito en la operativa.
- 🚦 Regla de emparejamiento: **mismo monto ± tarifa (0,41) y fecha ±2 días**.
- `DB AUTOMATICO AHORRO INCREMENTAL` y `APORTE AUTOMATICO AHO META` tampoco son gasto:
  son ahorro programado — traslado a otro producto del mismo banco.

## Procedimiento
1. Cargar el estado de **cada** cuenta del periodo (`04 Patrimonio y Balance\Estado de cuenta varios`).
2. **Control duro por cuenta:** suma de movimientos = Saldo Final − Saldo Inicial.
   Si no cuadra, el parseo está incompleto: NO continuar.
3. Emparejar traslados entre cuentas y **marcarlos como NEUTROS**.
4. Calcular la **posición de caja consolidada** = suma de saldos de las cuentas propias.
5. Recalcular el flujo operativo del mes **excluyendo los traslados**.
6. Recalcular **runway** = caja consolidada / gasto operativo mensual.

## Hallazgo que motivo esta skill (julio-agosto 2026)
- El 17-jul salieron **2.000** de la operativa a la reserva. Se estaba leyendo como si la
  caja se hubiera ido; en realidad seguía siendo del usuario.
- Al 1-ago la reserva tenía **1.649,97** y la operativa **583,64**:
  **caja consolidada 2.233,61**, casi cuatro veces lo que mostraba una sola cuenta.
- En agosto la reserva devolvió **945,00** a la operativa en tres tramos (345 · 300 · 300).
  Eso **no es ingreso**: es consumo de reserva. Contarlo como entrada haría creer que
  agosto mejoró cuando en realidad la reserva se está agotando.

## Que NO hacer 🚦
- 🚦 No sumar la cuenta de ETRIEK al patrimonio personal: es de la sociedad.
- 🚦 No presentar la cuenta de la reserva como activo propio ante un banco sin explicar
  la titularidad. Se documenta o no se usa.
- 🚦 No celebrar un mes «positivo» que en realidad se financió vaciando la reserva.
  Separar siempre **flujo operativo** de **variación de reserva**.
- No asumir que un traslado volvió: verificarlo en el estado de la cuenta destino.
