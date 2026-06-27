"""Biblioteca de queries forenses para Wolfram Language.

Cada funcion devuelve el STRING de codigo Wolfram listo para pasar al tool
`mcp__...__WolframLanguageEvaluator`. El llamador es responsable de invocar
el MCP — esta libreria solo genera el codigo correcto y compacto.

Diseño: kernel stateless, autocontenido, sin dependencias entre llamadas.
"""
from typing import Iterable


# === Valor del dinero en el tiempo ===

def future_value(principal: float, rate_annual: float, years: float) -> str:
    """FV con capitalizacion anual."""
    return (
        f"P = {principal}; r = {rate_annual}; n = {years};\n"
        f"FV = P*(1 + r)^n;\n"
        f"{{\"Principal\" -> P, \"Rate\" -> r, \"Years\" -> n, "
        f"\"FutureValue\" -> N@FV, \"OpportunityCost\" -> N@(FV - P)}}"
    )


def present_value(future_amount: float, rate_annual: float, years: float) -> str:
    return (
        f"F = {future_amount}; r = {rate_annual}; n = {years};\n"
        f"PV = F / (1 + r)^n;\n"
        f"{{\"FutureAmount\" -> F, \"PresentValue\" -> N@PV}}"
    )


def npv(cashflows: Iterable[float], rate_annual: float) -> str:
    """Net Present Value. cashflows[0] suele ser negativo (inversion)."""
    flows = ", ".join(str(c) for c in cashflows)
    return (
        f"flujo = {{{flows}}}; r = {rate_annual};\n"
        f"NPV = Total[flujo * Table[1/(1+r)^t, {{t, 0, Length[flujo]-1}}]];\n"
        f"{{\"CashFlows\" -> flujo, \"NPV\" -> N@NPV}}"
    )


def irr(cashflows: Iterable[float]) -> str:
    """Internal Rate of Return."""
    flows = ", ".join(str(c) for c in cashflows)
    return (
        f"flujo = {{{flows}}};\n"
        f"sol = FindRoot[Total[flujo*Table[1/(1+r)^t, {{t,0,Length[flujo]-1}}]] == 0, {{r, 0.1}}];\n"
        f"{{\"CashFlows\" -> flujo, \"IRR\" -> N@(r /. sol)}}"
    )


# === Amortizacion ===

def amortization_schedule(principal: float, annual_rate: float, months: int,
                          yearly_snapshot: bool = True) -> str:
    """Tabla de amortizacion con cuota fija mensual."""
    step = 12 if yearly_snapshot else 1
    return (
        f"P = {principal}; r = {annual_rate}; n = {months};\n"
        f"i = r/12;\n"
        f"cuota = P*i*(1+i)^n / ((1+i)^n - 1);\n"
        f"saldo[k_] := P*(1+i)^k - cuota*((1+i)^k - 1)/i;\n"
        f"intAcum[k_] := cuota*k - (P - saldo[k]);\n"
        f"Prepend[\n"
        f"  Table[{{k, N@cuota, N@saldo[k], N@intAcum[k]}}, {{k, {step}, n, {step}}}],\n"
        f"  {{\"mes\", \"cuota\", \"saldo\", \"interes_acumulado\"}}\n"
        f"]"
    )


def remaining_balance(principal: float, annual_rate: float,
                      total_months: int, months_paid: int) -> str:
    return (
        f"P = {principal}; r = {annual_rate}; n = {total_months}; k = {months_paid};\n"
        f"i = r/12;\n"
        f"cuota = P*i*(1+i)^n / ((1+i)^n - 1);\n"
        f"saldo = P*(1+i)^k - cuota*((1+i)^k - 1)/i;\n"
        f"{{\"Cuota\" -> N@cuota, \"SaldoVigente\" -> N@saldo}}"
    )


# === Anomalia y deteccion ===

def benford_first_digit(values: Iterable[float]) -> str:
    """Test de Benford sobre el primer digito de una lista de transacciones."""
    vals = ", ".join(str(v) for v in values)
    return (
        f"data = {{{vals}}};\n"
        f"firstDigit[x_] := IntegerPart[Abs[x]/10^IntegerPart[Log10[Abs[x]]]];\n"
        f"valid = Select[data, # != 0 &];\n"
        f"freqs = KeySort[Counts[firstDigit /@ valid]];\n"
        f"observed = Lookup[freqs, Range[1,9], 0];\n"
        f"expected = Total[observed]*Table[Log10[1 + 1/d], {{d, 1, 9}}];\n"
        f"chiSq = Total[(observed - expected)^2/expected];\n"
        f"{{\"N\" -> Total[observed], \"Observed\" -> observed, "
        f"\"Expected\" -> N@expected, \"ChiSquared\" -> N@chiSq, "
        f"\"Conforms\" -> N@chiSq < 15.51 (* alpha=0.05, df=8 *)}}"
    )


def outliers_zscore(values: Iterable[float], threshold: float = 3.0) -> str:
    vals = ", ".join(str(v) for v in values)
    return (
        f"data = {{{vals}}};\n"
        f"mu = Mean[data]; sigma = StandardDeviation[data];\n"
        f"z = (data - mu)/sigma;\n"
        f"outliers = Select[Transpose[{{Range[Length[data]], data, z}}], Abs[#[[3]]] > {threshold} &];\n"
        f"{{\"Mean\" -> N@mu, \"SD\" -> N@sigma, \"OutlierThreshold\" -> {threshold}, "
        f"\"Outliers\" -> N@outliers}}"
    )


def ratio_variance(numerator_series: Iterable[float],
                   denominator_series: Iterable[float],
                   labels: Iterable[str] = None) -> str:
    """Evoluciona un ratio (ej. GastoFin/UtilOp) por periodo."""
    num = ", ".join(str(n) for n in numerator_series)
    den = ", ".join(str(d) for d in denominator_series)
    if labels:
        lab = ", ".join(f'"{l}"' for l in labels)
        return (
            f"num = {{{num}}}; den = {{{den}}}; lab = {{{lab}}};\n"
            f"ratios = N[num/den];\n"
            f"Transpose[{{lab, num, den, ratios}}]"
        )
    return (
        f"num = {{{num}}}; den = {{{den}}};\n"
        f"ratios = N[num/den];\n"
        f"{{\"Numerator\" -> num, \"Denominator\" -> den, \"Ratios\" -> ratios}}"
    )


# === Fechas ===

def days_between(date1_iso: str, date2_iso: str) -> str:
    return (
        f'DateDifference[DateObject["{date1_iso}"], DateObject["{date2_iso}"], "Day"]'
    )


def business_days_between(date1_iso: str, date2_iso: str) -> str:
    return (
        f'DayCount[DateObject["{date1_iso}"], DateObject["{date2_iso}"], "BusinessDays"]'
    )


def age_of_debt(disbursement_iso: str, today_iso: str = None) -> str:
    today = f'DateObject["{today_iso}"]' if today_iso else "Today"
    return (
        f'DateDifference[DateObject["{disbursement_iso}"], {today}, '
        f'{{"Year", "Month", "Day"}}]'
    )


# === Auditoria estadistica ===

def sample_size_attribute(population: int, expected_deviation_rate: float,
                          tolerable_deviation_rate: float,
                          risk_of_overreliance: float = 0.05) -> str:
    """Tamano de muestra para pruebas de cumplimiento (atributos), aproximacion ISA 530."""
    return (
        f"N = {population}; pExp = {expected_deviation_rate}; "
        f"pTol = {tolerable_deviation_rate}; alpha = {risk_of_overreliance};\n"
        f"z = Quantile[NormalDistribution[0,1], 1 - alpha];\n"
        f"n0 = (z^2 * pExp*(1-pExp)) / (pTol - pExp)^2;\n"
        f"n = Ceiling[n0 / (1 + n0/N)];\n"
        f"{{\"Population\" -> N, \"ExpectedRate\" -> pExp, \"TolerableRate\" -> pTol, "
        f"\"Risk\" -> alpha, \"SampleSize\" -> n}}"
    )


# === Conversion de moneda / inflacion (delegada a WolframAlpha NL) ===

def inflation_adjustment_nl(amount: float, currency: str, year_from: int, year_to: int,
                             country: str = "USA") -> str:
    """Devuelve un string para WolframAlpha (no para Evaluator)."""
    return (
        f"inflation adjustment {currency.upper()} {amount:,} from {year_from} to {year_to} {country}"
    )


def fx_historic_nl(amount: float, currency_from: str, currency_to: str, date_iso: str) -> str:
    return (
        f"convert {amount} {currency_from} to {currency_to} on {date_iso}"
    )


# === Suma y cuadre rapido ===

def total_and_check(values: Iterable[float], expected_total: float, tolerance_pct: float = 0.5) -> str:
    vals = ", ".join(str(v) for v in values)
    return (
        f"data = {{{vals}}}; exp = {expected_total}; tol = {tolerance_pct}/100;\n"
        f"observed = Total[data];\n"
        f"diff = observed - exp;\n"
        f"pctDiff = If[exp != 0, 100*diff/exp, Infinity];\n"
        f"{{\"Observed\" -> N@observed, \"Expected\" -> exp, "
        f"\"Diff\" -> N@diff, \"PctDiff\" -> N@pctDiff, "
        f"\"WithinTolerance\" -> Abs[N@pctDiff] <= 100*tol}}"
    )


# === Punto de equilibrio (auditoria operacional) ===

def maquila_reasonability(tons: float, tariff_per_ton: float, observed_revenue: float,
                          tolerance_pct: float = 5.0) -> str:
    """Prueba de razonabilidad: ton * tarifa vs ingreso registrado."""
    return (
        f"tons = {tons}; tariff = {tariff_per_ton}; obs = {observed_revenue}; tol = {tolerance_pct}/100;\n"
        f"expected = tons * tariff;\n"
        f"diff = obs - expected;\n"
        f"pct = If[expected != 0, 100*diff/expected, Infinity];\n"
        f"{{\"Tons\" -> tons, \"Tariff\" -> tariff, \"ExpectedRevenue\" -> N@expected, "
        f"\"ObservedRevenue\" -> obs, \"Diff\" -> N@diff, \"PctDiff\" -> N@pct, "
        f"\"Reasonable\" -> Abs[N@pct] <= 100*tol}}"
    )
