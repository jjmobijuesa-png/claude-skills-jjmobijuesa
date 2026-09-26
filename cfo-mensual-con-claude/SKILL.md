---
name: cfo-mensual-con-claude
description: |
  Monta y opera un "CFO mensual con Claude": un SISTEMA de 7 workflows que
  corren en orden y que, cada mes, ingiere las facturas del mes + los estados
  de cuenta, clasifica, CONCILIA banco vs facturas, detecta gastos sin factura,
  arma el P&L / flujo por rubro, deja las reclamaciones de cobro en BORRADOR,
  genera un dashboard HTML y prepara el paquete para la gestoria. Sobre esa base
  añade la capa propia del usuario: INDICADORES DE BANCABILIDAD (DSCR, carga de
  deuda, runway) alineados a la doctrina financiera de LinkedIn (banca financia
  CAPACIDAD DE PAGO, no EBITDA) y al plan de fondos (Sistema del 1%).
  No es un prompt: es un sistema que se monta una vez y se repite en ~20 min/mes.
trigger_phrases:
  - "cierre financiero del mes"
  - "corre el CFO"
  - "CFO mensual"
  - "concilia el banco del mes"
  - "cierre de mes con Claude"
  - "actualiza el flujo con los estados de cuenta"
  - "dashboard financiero del mes"
  - "monta el CFO"
idioma_de_salida: espanol
nivel: aplicada
dominio: finanzas / control / operacion
metadata:
  version: 1.0
  fecha: 2026-08-01
  origen: >
    Pedido del usuario (2026-08-01). Destilada del post de LinkedIn de
    Alvaro Pescador Ruiz "Monte un CFO con Claude" (7 workflows), fundida con
    el sistema de Finanza Integral que el usuario y Claude construyeron a mano
    en esta sesion (pipeline Produbanco/fedphd + indicadores de bancabilidad).
  fuente_inspiracion: https://www.linkedin.com/posts/alvaro-pescador-ruiz-9632181b9_mont%C3%A9-un-cfo-con-claude-cada-mes-analiza-share-7487769076128223232-BFXW/
  relacionada:
    - memoria-financiera-inteligenciada
    - intereses-lkd-finanzas-control
    - project-finanza-integral-perfil-millonario
    - gmail-attachments
    - entrega-visual-html-vs-texto
    - control-financiero-semanal-qvp
---

# Skill `cfo-mensual-con-claude`

## Acerca de mi (cargar al arrancar)
Lee `C:\Users\datos\.claude\projects\C--Users-datos-Downloads\memory\MEMORY.md` y el pointer
`project_finanza_integral_perfil_millonario.md`. El espacio vivo es
`E:\vars\var 11-11 Finanza Integral` (indice `INDICE_FINANZA_INTEGRAL.md`). El libro operativo es
`03 Flujo de Caja\Flujo de Efectivo 2026.xlsx` (hojas: Indicadores, Flujo, Resumen Bancario,
Conciliacion, Reglas). Cuenta principal analizada: Produbanco 02013011800 (correo **fedphd@gmail.com**,
que el conector Gmail MCP NO ve → se usa el perfil Playwright dedicado `browser_profile_fedphd`).

## Doctrina central (la tesis del post de Pescador)
- **No es un prompt, es un SISTEMA de 7 workflows que corren EN ORDEN.** Cada workflow es un paso
  reproducible; se monta una vez y se repite cada mes en ~20 minutos.
- **Le sueltas dos cosas:** la carpeta de facturas del mes (`02 Egresos`) y el/los estado(s) de cuenta.
- 🚦 **Human-in-the-loop, siempre.** Nada toca el banco, nada se envia solo. Los correos (a proveedores
  por facturas faltantes, o de reclamacion de cobro) quedan en **BORRADOR**. **El OK siempre es del usuario.**
  (Coincide con las reglas de seguridad de Claude: no ejecutar acciones irreversibles sin confirmacion.)
- **La gestoria te dice cuanto pagas de impuestos; este sistema te dice que rubro te desangra la caja y
  donde se escapa el dinero.** El objetivo del usuario va mas alla: **lograr BANCABILIDAD** y alimentar el
  **Sistema del 1%** (plan de manejo de fondos).

## Capa propia que ANADIMOS al modelo del post (diferencial del usuario)
- **Indicadores de bancabilidad** (no estaban en el post): DSCR, carga de deuda/ingreso, margen de caja
  libre, tasa de ahorro, cobertura operativa, runway. Doctrina LinkedIn: **el banco financia CAPACIDAD DE
  PAGO (flujo de caja), no utilidad ni EBITDA** ([[intereses-lkd-finanzas-control]]).
- **Puente al Sistema del 1%**: cada cierre mide si ya hay excedente recurrente para arrancar la Fase 1
  (5 cuentas, DSCR≥1.2, carga<40%, ahorro≥20%).

## Los 7 workflows (corren en orden) — adaptados al sistema del usuario

> Antes de correr: si el archivo maestro `Muchas Gracias 2026.xlsx` esta cifrado, descifrar copia de
> trabajo con `scripts\descifrar_xlsx.py` (clave `2020`, `msoffcrypto-tool`). Ver
> [[project-finanza-integral-perfil-millonario]].

**W1 — Ingerir y clasificar facturas del mes.**
Leer los PDF/escaneos de `02 Egresos` (pypdf; OCR de Adobe Scan ya trae capa de texto). Extraer
proveedor, base, IVA, total, fecha. Clasificar por rubro con la hoja `Reglas` (vendedor→concepto→rubro).

**W2 — Descargar estados y conciliar banco vs facturas.**
- Descargar estados Produbanco del mes desde fedphd: `scripts\descargar_estados_produbanco.py`
  (perfil `browser_profile_fedphd`; los estados son PDF adjuntos en correos "Estado de Cuenta
  Produbanco - Grupo Promerica"). Guardar en `10 Documentos de Respaldo\Estados de Cuenta\...`.
- Parsear movimientos: `scripts\parsear_estados.py`. 🚦 **OJO: los meses vienen en ESPANOL**
  (Ene/Abr/Ago/Dic). **Control duro de reconciliacion:** suma de movimientos del mes = Saldo Final −
  Saldo Inicial (si no cuadra, el parseo esta incompleto — NO continuar).
- Cargar movimientos a la hoja `Conciliacion` (autoclasificador por palabra clave, col F = formula,
  col H = parser). Marcar el movimiento que NO tiene factura detras.

**W3 — Enriquecer y cazar gastos sin factura.**
- Enriquecer los movimientos opacos ("COMPRA ESTABLECIMIENTO", "TRANSFERENCIA") con el comercio/
  contraparte real: cosechar notificaciones transaccionales de fedphd
  (`scripts\enriquecer_notificaciones.py` → cosecha + cruce por monto+fecha±2d + MISMO TIPO; sin
  fallback por monto para evitar falsos positivos).
- Listar los consumos SIN factura fisica en `02 Egresos`. Por cada uno, **redactar el correo al
  proveedor pidiendo la factura — y dejarlo en BORRADOR** (Gmail MCP `create_draft` o Playwright).
  Cada factura faltante es IVA que no se deduce.

**W4 — P&L / flujo del mes por rubro (y por cliente/negocio donde aplique).**
Actualizar `Flujo 2026`: reemplazar el presupuesto (azul) por el real (negro) del mes cerrado. Para los
negocios del usuario con ventas (lotes Belen, Mobijuesa), calcular margen por linea/cliente y senalar
quien hace perder dinero.

**W5 — Pendiente de cobro con reclamacion en borrador.**
Cruzar ventas facturadas vs cobradas (BASE COBRANZA / lotes). Por cada cliente moroso, **redactar la
reclamacion — en BORRADOR**. El usuario aprueba y envia. (Voz y tono: [[voz-y-tono-usuario]], firma
Francisco Duque.)

**W6 — Dashboard HTML + indicadores de bancabilidad.**
- Reconstruir/actualizar la hoja `Indicadores` (`scripts\construir_indicadores.py`): panel semaforo
  (DSCR, carga de deuda, margen, ahorro, cobertura operativa, runway) + matriz categoria×mes +
  distribucion de egresos + comparativa con el mes/ano anterior.
- Entregar tambien un **dashboard HTML autocontenido** que se abre en el navegador
  ([[entrega-visual-html-vs-texto]]: HTML para decidir, no para iterar). Facturacion, margen, caja,
  DSCR, y comparativa mes anterior.

**W7 — Paquete para la gestoria + resumen de IVA.**
Carpeta ordenada del mes (facturas + estados + resumen), con el resumen de IVA soportado/generado.
"Reenviar y listo" — pero el envio lo autoriza el usuario.

## Protocolo de datos: que necesito y con que frecuencia
| Frecuencia | Insumo | Fuente | Para |
|---|---|---|---|
| Semanal (vie) | Facturas/recibos escaneados | → `02 Egresos` | Nombrar consumos (W1, W3) |
| Semanal | Saldos reales de cuentas | 1 linea WhatsApp/correo | Runway, saldo (W6) |
| Mensual (>30) | Estados Produbanco (auto fedphd) + Poramerica | correo fedphd | W2 |
| Mensual | Estado de la cuenta de las cuotas grandes (La Nuestra 1097 / Mobijuesa 942 — NO salen por Produbanco) | esa cuenta | Cerrar el 73% del egreso que no pasa por Produbanco |
| Trimestral | Avance de ventas de lotes (cuantos, precio, cuanto entro) | usuario | Palanca de bancabilidad (W4, W6) |
| Cuando ocurra | Nuevos prestamos / refinanciamientos / pagos de deuda vencida | usuario | Recalcular DSCR y carga |

## Que NO hacer / compuertas 🚦
- 🚦 **Nunca** ejecutar transferencias, pagos ni tocar el banco. Solo LEER estados y movimientos.
- 🚦 Correos a proveedores y reclamaciones de cobro: **siempre BORRADOR**; el envio lo autoriza el usuario.
- 🚦 No continuar el cierre si la reconciliacion dura (suma mov = Saldo Final − Inicial) NO cuadra.
- Precision > cantidad al enriquecer: mejor 63 movimientos bien nombrados que 118 con falsos positivos.
- No `Read` del maestro cifrado de 21 MB completo → trabajar sobre la copia descifrada y por hojas.
- La cuenta Produbanco es un CONDUCTO: gran parte de su egreso son transferencias/retiros (movimientos de
  fondos, no consumo). El gasto real vive en el flujo `Gracias 2026` y en las otras cuentas.

## Montaje (una vez) y cadencia
1. Verificar assets (`scripts\`) + perfil `browser_profile_fedphd` logueado (si no, `gmail-attachments\login.py fedphd`).
2. Cada fin de mes: correr W1→W7 en orden (~20 min). Entregar libro actualizado + dashboard HTML + borradores.
3. Registrar el cierre en `11 Reportes y Cierres`. Actualizar el pointer del proyecto en `MEMORY.md`.

## Fuente
Inspiracion: post de **Alvaro Pescador Ruiz** en LinkedIn, "Monte un CFO con Claude" (7 workflows,
human-in-the-loop, borradores). Curar ≠ firmar: se cita la URL, no se atribuye al usuario.
Capa de bancabilidad e indicadores: aporte propio del sistema Finanza Integral del usuario.
