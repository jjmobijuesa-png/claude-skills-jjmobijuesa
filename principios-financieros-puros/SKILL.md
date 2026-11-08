---
name: principios-financieros-puros
description: |
  Principios financieros invariantes que sirven de piso para autocorregirse cuando un cálculo
  «da bien» pero puede estar mal: devolución DEL capital ≠ rendimiento SOBRE el capital, costo
  hundido, costeo completo, IVA contenido, propiedad de inversión, balance que cuadra por
  construcción, flujo incremental para TIR/VAN. Cada principio trae su disparador (cuándo
  sospechar) y su comprobación barata (Python o Wolfram). Úsela al revisar cualquier modelo
  financiero propio o ajeno, y siempre que una cifra mejore «demasiado».
trigger_phrases:
  - "verifica los principios financieros"
  - "la utilidad salió muy alta"
  - "esto es utilidad o recuperación de capital"
  - "autocorrígete en los cálculos"
  - "comprueba con Wolfram"
idioma_de_salida: español (Ecuador), trato de usted
metadata:
  version: 1.0
  fecha: 2026-10-31
  origen: corrección de la v1 de San Sebastián (utilidad escondida, IVA ×0,15, urbanización sin costear)
  relacionada:
    - auditoria-corrida-financiera-inmobiliaria
    - control-versiones-entregables
    - wolfram-forensic-engine
    - modelo-tres-estados-integrado
    - rigor-matematico-filtro-pseudociencia
    - cuantificar-antes-de-pedir
---

# Skill `principios-financieros-puros`

## Doctrina en una frase
Cuando un número mejora, primero se sospecha del número. Los principios de abajo no dependen del
proyecto: si un modelo los viola, el modelo está mal aunque cuadre.

## Los principios, con su disparador y su comprobación

| # | Principio | Disparador (sospechar cuando…) | Comprobación barata |
|---|---|---|---|
| 1 | **Devolución DEL capital ≠ rendimiento SOBRE el capital.** Retorno = capital recuperado + utilidad, y la utilidad ya descontó ese capital | aparece «utilidad escondida», «retorno total» o una suma de capital + utilidad | ¿El capital sumado está en el costo? Σ costos ∋ capital. Si no está, el retorno está inflado justo por ese capital |
| 2 | **Costo hundido**: lo ya pagado no es egreso futuro de caja, pero sí costo del producto (costeo completo) | terreno o urbanización propios como salida en el mes 1, o fuera del costo | Flujo: no está; PyG: sí está; balance: patrimonio en especie |
| 3 | **El balance cuadra por construcción**: Activo = Pasivo + Patrimonio. Si no cuadra, falta o sobra una partida | cualquier control ≠ 0 | Caja + activos retenidos − deuda − (capital + aportes + utilidad) = 0. La diferencia ES el error (−$16.049 = IR mal agregado + eléctrica mal prorrateada) |
| 4 | **IVA contenido en un precio con IVA** = P × t / (1 + t) | «IVA = precio × 0,15» sobre un contrato llave en mano con IVA | Wolfram: `p*0.15/1.15` vs `p*0.15` (13 % de sobreestimación) |
| 5 | **Beneficio incierto ≠ caja cierta**: devoluciones y subsidios con relación, tope, rezago y escenario sin ellos | el proyecto «solo cierra» con la devolución | Correr el escenario sin devolución; reportar las dos cifras |
| 6 | **Activo retenido ≠ gasto**: lo que no se vende se capitaliza (NIC 40) | unidades de renta dentro del costo de lo vendido | Utilidad ↑ en el costo capitalizado; balance ↑ en el mismo monto |
| 7 | **TIR/VAN sobre flujo incremental**: t0 = costo de oportunidad (valor del capital invertido); terminal = valor de lo retenido | TIR altísima con capital propio «gratis» | t0 ≠ 0; VAN a la tasa del promotor; payback contado desde t0 |
| 8 | **Una suma de partes = el total**: prorrateos que suman 1, MAX(0,·) solo sobre el total | Σ etapas ≠ total; IR por etapa ≠ IR del proyecto | Validar Σ de cada fila (lo hace el validador de [[control-versiones-entregables]]) |
| 9 | **El crecimiento consume caja antes de generarla** (Altimira) | «nunca en rojo» sin decir con qué financiamiento | Mínimo del flujo acumulado sin financiamiento = necesidad real; runway = (aporte + línea) ÷ burn |
| 10 | **Los umbrales se fijan antes de ver el resultado** | el veredicto cambia de «no» a «sí» al mover el umbral | Umbral escrito con fecha; si no se cumple, se dice y se muestran palancas |

## Recetas Wolfram (copiar y ajustar)
```wolfram
(* retorno = capital + utilidad, con el capital DENTRO del costo *)
ventas = 13744900; capital = 600000 + 1773417.45; otros = 9836878.58;
uai = ventas - (capital + otros - 432291.10 - 598119.25); neta = 0.75 uai; {neta, capital + neta}
(* IVA contenido *)  p = 7642634.70; {p*0.15/1.15, 0.60 p*0.15/1.15}
(* cuota francesa *)  pmt[pv_, i_, n_] := pv (i/12)/(1 - (1 + i/12)^-n); pmt[61330*0.95 - 482*14, 0.0299, 240]
```

## Cómo depurar si falla
- **Una cifra mejoró sin que cambiara un supuesto**: buscar doble conteo (principio 1) antes que nada.
- **Motor y Excel difieren**: el balance (principio 3) da el monto exacto del error; buscar una partida
  de ese tamaño en prorrateos (8) y agregaciones con MAX.
- **El revisor cita otras cifras**: reconstruirlas con versiones anteriores antes de discutir
  ([[auditoria-corrida-financiera-inmobiliaria]] criterio 16).

## Relacionadas
[[auditoria-corrida-financiera-inmobiliaria]] · [[control-versiones-entregables]] · [[wolfram-forensic-engine]] ·
[[modelo-tres-estados-integrado]] · [[rigor-matematico-filtro-pseudociencia]] · [[cuantificar-antes-de-pedir]]
