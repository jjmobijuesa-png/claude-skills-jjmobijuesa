---
name: wolfram-forensic-engine
description: "Computational knowledge engine for forensic-audit work. Use Wolfram|Alpha and the Wolfram Language kernel to (1) recompute and verify the auditee's arithmetic (totals, ratios, amortization tables, interest accruals), (2) detect anomalies (Benford's Law on transaction digits, outlier flagging, ratio drift between periods), (3) quantify opportunity cost and time-value of money on detected misappropriations, (4) adjust historical amounts for inflation or FX, (5) compute audit-sampling sizes for risk-based selection, (6) do precise date arithmetic on payment delays, debt aging, and statute-of-limitations. Triggers: 'recalcular', 'verificar las cifras del contador', 'detectar anomalías estadísticas', 'costo de oportunidad', 'tabla de amortización forense', 'ajustar por inflación', 'cuántos días desde', 'Benford', 'valor presente', 'compute forensic ratio'. Specifically tuned to the EPACEM / Oro Juez case but reusable for any audit-engagement."
user-invocable: true
---

# Wolfram Forensic Engine — Motor computacional para la auditoría

Conecta el expediente forense (datos contables, fechas, tasas, totales) al motor de cómputo simbólico/numérico de Wolfram, vía dos herramientas MCP complementarias:

- **WolframAlpha** — para consultas en lenguaje natural sobre entidades del mundo real (tasas de inflación históricas, cotizaciones FX, días entre fechas, datos de población/economía).
- **WolframLanguageEvaluator** — para evaluar expresiones precisas de Wolfram Language: valor presente/futuro, amortización completa, regresiones, ANOVA, Benford's Law, distribuciones estadísticas, simulación.
- **WolframContext** — para sembrar contexto semántico antes de una sesión larga (se usa una vez por hilo).

El kernel es **stateless** entre llamadas: cada evaluación parte de cero. Define todas las variables en la misma llamada o pasa los datos explícitos. Mantén las queries pequeñas y autocontenidas.

## Cuándo invocar este skill

Cualquier afirmación numérica del informe forense debe poder ser **reproducida por un tercero** con una sola llamada. Antes de citar un número, recompútalo aquí:

- Cuando aparezca una cifra del Contador que cierra el círculo de una hipótesis (recompute → publish only if matches)
- Cuando construyas una cédula de cuadre (banco vs libro vs soporte)
- Cuando estimes el impacto patrimonial de una inversión fallida o un préstamo a relacionada
- Cuando construyas la tabla de amortización proyectada vs. real
- Cuando detectes posibles patrones de manipulación (Benford, outliers, ratios anómalos)
- Cuando ajustes cifras históricas para comparabilidad (inflación, FX)

## Patrones forenses canónicos (con plantillas listas para llamar)

Ver `references/forensic-patterns.md` para el catálogo completo. Los más usados:

### 1. Valor futuro / costo de oportunidad

```wolfram
P = 600000; r = 0.1038; n = 8;
FV = P*(1 + r)^n;
{FV, FV - P}   (* {1322130.63, 722130.63} *)
```

### 2. Tabla de amortización (cuota fija)

```wolfram
P = 600000; r = 0.1038; n = 96;  (* 8 años x 12 meses *)
i = r/12;
cuota = P*i*(1+i)^n / ((1+i)^n - 1);
saldo[k_] := P*(1+i)^k - cuota*((1+i)^k - 1)/i;
Table[{k, N@cuota, N@saldo[k]}, {k, 0, n, 12}]
```

### 3. Ley de Benford sobre primer dígito de transacciones

```wolfram
data = {1234.56, 2345.67, ...};  (* lista de valores *)
firstDigit[x_] := IntegerPart[x/10^IntegerPart[Log10[Abs[x]]]];
freqs = Counts[firstDigit /@ Select[data, # != 0 &]];
expected = Table[Log10[1 + 1/d], {d, 1, 9}];
chiSq = ChiSquareTest[Values[KeySort[freqs]], Total[Values[freqs]]*expected];
```

### 4. Días entre dos fechas

```wolfram
DateDifference[DateObject["2017-06-01"], DateObject["2026-05-31"], "Day"]
```

### 5. Valor presente neto de un flujo de recuperación

```wolfram
flujo = {-600000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000};
r = 0.1038;
NPV = Total[flujo*Table[1/(1+r)^t, {t, 0, Length[flujo]-1}]]
```

### 6. Ratio de gastos financieros sobre utilidad operativa

```wolfram
gastosFin = 13_200_000;  (* placeholder *)
utilOp = 1_000_000;
ratio = gastosFin/utilOp;
N[ratio]  (* 13.2x — confirma la cifra del informe consolidado *)
```

### 7. Ajuste por inflación USD 2017 → USD 2026

Usa WolframAlpha en lenguaje natural:
```
inflation adjustment $600,000 from 2017 to 2026 USA
```

## Workflow recomendado para una verificación forense

1. **Capturar la afirmación** del informe o del Contador en una sola línea (cifra + fecha + concepto).
2. **Identificar las primitivas** que la sustentan (suma, multiplicación, FV, PV, ratio).
3. **Llamar a Wolfram** con las cifras exactas, sin redondear.
4. **Comparar** el resultado con la cifra publicada. Si difiere >0.5% → marcar como **discrepancia material** y abrir cédula.
5. **Persistir** la query y la respuesta en la cédula de cuadre (`reference + N@result`).

## Files del skill

- `scripts/queries.py` — biblioteca de funciones Python que envuelven las queries más usadas (FV, PV, amortización, Benford, fechas)
- `references/forensic-patterns.md` — catálogo completo de patrones por categoría auditora
- `references/epacem-queries.md` — queries específicas ya validadas para el caso EPACEM / Oro Juez
- `references/wolfram-tips.md` — buenas prácticas con el kernel stateless

## Buenas prácticas

| Práctica | Por qué |
|---|---|
| Usa `N[expr]` para forzar resultado decimal | Wolfram devuelve enteros/racionales por defecto |
| Encierra cifras grandes con `_` (`600_000`) o sin separador | Coma o punto se interpretan como decimal según contexto |
| Para fechas usa `DateObject["YYYY-MM-DD"]` | ISO-8601 evita ambigüedades MM/DD vs DD/MM |
| Para moneda usa `Quantity[600000, "USDollars"]` cuando vayas a convertir | Quantity preserva unidades en operaciones |
| Documenta la query EXACTA en la cédula | Reproducibilidad ante el Directorio |
| Si WolframAlpha devuelve "No Results Found" | Reformula como Wolfram Language en `WolframLanguageEvaluator` |

## Conexión con el resto del expediente EPACEM

Este skill es el **motor de cifras** del informe forense que se está construyendo en el cuaderno EPACEM de NotebookLM (ver skill `notebooklm-reorganize`). Cada cifra del Resumen Ejecutivo y de las Cédulas de Cuadre debe pasar por aquí antes de publicarse. Las queries específicas del caso están en `references/epacem-queries.md`.
