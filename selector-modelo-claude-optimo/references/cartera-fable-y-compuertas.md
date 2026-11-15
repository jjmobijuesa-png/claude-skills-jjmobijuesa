# Guía de uso de Fable 5.2 — cartera completa

**Francisco Duque · 14-nov-2026 · ventana hasta el 16-nov-2026, techo 50 % del plan**

> Esta guía no es sobre Fable. Es sobre **qué trabajo suyo merece el techo de
> capacidad**, una pregunta que sobrevive a esta ventana. Lo que caduca el 16 de
> noviembre es la disponibilidad, no el criterio.
>
> Doctrina madre: [[selector-modelo-claude-optimo]]. Cifras y IDs vivos:
> [[reference_familia_fable_y_generacion_55]]. El quitar andamiaje viene de
> [[prompting-opus-5-doctrina]]. La compuerta 2 la gobierna
> [[gobernanza-datos-financieros-ia]].

---

## 1. Las tres compuertas: pasan las tres o no pasa

No basta que una tarea sea difícil. Tiene que pasar **las tres**, en este orden.

| # | Compuerta | La pregunta | Si falla |
|---|---|---|---|
| **1** | **Dificultad** | ¿Excede de verdad a Opus 5.5? | Queda en Opus 5.5. Fable solo duplicaría la factura |
| **2** | **Retención** | ¿El material puede quedar retenido 30 días? | **Prohibido.** Fable no funciona con retención cero |
| **3** | **Ventana** | ¿Están los insumos HOY? | No entra. No hay tiempo de conseguirlos |

La compuerta 2 es la que más gente olvida y la única que no admite negociación:
es su propia regla permanente, no una preferencia, y vive en
[[gobernanza-datos-financieros-ia]].

### La compuerta 2, explícita

**Nunca a Fable**, porque exige retención de 30 días:

- Cédulas y nombres de personas naturales.
- Escrituras y certificados del expediente hipotecario COAC.
- Deuda personal, DSCR, cierres de cuenta, conciliación de las cinco cuentas.
- Modelos financieros de Belén y San Sebastián con cifras reales.
- El Excel real de flujo de caja de Mobijuesa.

**Sí a Fable**, porque no son datos sensibles:

- Metodología, doctrina, arquitectura de agentes, la red de skills.
- Legislación pública y textos normativos sin nombres de particulares.
- Material académico del Aula.
- Modelos **anonimizados**: la estructura sin las cifras reales ni los nombres.

🚦 **El truco que sí sirve:** cuando el trabajo es difícil pero el dato es
sensible, no se renuncia a Fable — se le da **la estructura sin el dato**.
Fable diseña el modelo, el método o el dictamen en abstracto; Opus 5.5 lo
rellena después con las cifras reales en esta máquina.

---

## 2. Su cartera, hilo por hilo

Siete hilos con relevo activo, más los proyectos grandes. Veredicto por cada uno.

### Verde — entra en la ventana

| Hilo o proyecto | Qué parte es de Fable | Por qué |
|---|---|---|
| **Red de skills** (`agente-ia-local-autoreflexivo`) | Recomposición: qué fusionar, qué partir, dónde falta arista, qué hub está mal puesto, sobre 199 skills y 897 aristas | Proyecto entero de una pasada · cero dato sensible · es lo único que abarata todo lo demás |
| **JRPFM / matriz legislativa** | La matriz artículo por artículo contra el informe de primer debate | Razonamiento largo sobre corpus grande, atascado desde el 5-oct · legislación pública |
| **IBPP / EcuaLedger** | La arquitectura jurídico-técnica completa: dos capas, dos generaciones, zona franca, en un solo documento coherente | Diseño de sistema, no ejecución · sin nombres de particulares |
| **Ingeniería de prompts** | El marco entero, que lleva sin volcado desde septiembre | Metaproblema atascado · es doctrina, no dato |
| **Kleper** (libro) | Una pasada de coherencia narrativa sobre el manuscrito completo | Obra entera de una vez · contenido propio |

### Ámbar — solo si lo anonimiza primero

| Hilo | Qué sí, qué no |
|---|---|
| **CFO virtual 44 agentes** ([[cfo-virtual-44-agentes]]) | **Sí** la arquitectura de los 9 pilares y los criterios de activación. **No** las cifras de QVP ni de Mobijuesa |
| **San Sebastián / financial-report** | **Sí** el diseño del motor de financiamiento como método. **No** el modelo con las cifras reales |
| **Bancabilidad / red de IFs** | **Sí** la matriz de crédito como instrumento. **No** su DSCR ni su deuda |

### Rojo — no entra, y conviene decir por qué

| Hilo o proyecto | Motivo |
|---|---|
| **Expediente hipoteca COAC** | Compuerta 2: escrituras y nombres. Y además está bloqueado: faltan 10 planos |
| **Belén habitacional** | Compuerta 2 |
| **Conciliación de las cinco cuentas** | Compuerta 2, y es trabajo mecánico: es de **Haiku 5.5**. Ver [[ahorro-de-tokens]] |
| **Flujo de caja Mobijuesa** | Compuerta 2, con excepción A1 que lo ancla a su hilo |
| **ERP antirobo QVP** | Compuerta 3: falta el contrato del proveedor |
| **Corpus de X y LinkedIn** | Compuerta 1: no es difícil, está caducada la sesión. Es relogueo |
| **Aula: 48 clases** | Compuerta 1: es volumen, no dificultad. Opus 5.5 basta |

---

## 3. Cómo se le habla a Fable: se le QUITA andamiaje

Esta es la parte contraintuitiva, y es la que arruina más corridas.

**El prompt afinado para Opus le BAJA la calidad a Fable.** No es una opinión de
estilo: los prompts prescriptivos —«primero haz A, luego B, después valida C»—
degradan su salida. Fable rinde cuando recibe **la especificación completa del
resultado** y se lo deja correr.

| En lugar de… | Déle… |
|---|---|
| «Primero lee los 199 SKILL.md, luego extrae los wikilinks, después…» | «Quiero la red recompuesta: sin enlaces rotos, sin skills que nadie cite, sin duplicados, y con los hubs justificados. Aquí está el corpus. El entregable es un informe de cambios aplicados.» |
| «Analiza el artículo 1. Ahora el 2. Ahora el 3.» | «Quiero la matriz completa artículo por artículo, con la correspondencia a la LOFPD y al proyecto 7572/25, y la columna de riesgo. Aquí están los dos textos.» |
| «Hazlo en unos 500 palabras» omitido | **Diga el largo siempre.** En Fable el esfuerzo casi no cambia la extensión: el largo se pide en el prompt |

**Cuatro cosas más que cambian la operación:**

1. **Un turno puede durar muchos minutos.** No se colgó. No lo interrumpa.
2. **El esfuerzo arranca en `high`.** `xhigh` solo donde usted haya medido mejora;
   `max` únicamente para medir el techo.
3. **No tiene Priority Tier** (tampoco Opus 5.5, Sonnet 5.5 ni Haiku 5.5).
4. **Un solo trabajo grande rinde más que diez medianos.** El techo del 50 % del
   plan se consume de verdad, y a $8 de entrada y $40 de salida por millón se
   consume rápido.

---

## 4. El error que más probablemente va a cometer

**Reservar Fable.** Con una ventana de tres días, «lo guardo para cuando
aparezca algo realmente difícil» significa perderlo. No hay después.

El error simétrico es igual de caro: **usar Fable de lujo**, para redactar un
correo o maquetar un Excel. Eso es Sonnet 5.5, y a veces Haiku 5.5.

**La prueba de una línea antes de lanzar:** *«¿Qué tiene esta tarea que Opus 5.5
no pueda?»* Si no sabe contestarla en una frase, no es de Fable.

---

## 5. Orden recomendado para las próximas 48 horas

1. **Recomposición de la red de skills.** Primero, porque es lo único que hace
   más baratas todas las demás sesiones de aquí en adelante, y porque el corpus
   está limpio y medido desde hoy: 199 skills, 897 aristas, 10 enlaces rotos de
   los que solo 2 son defectos, 21 skills que nadie cita.
2. **La matriz JRPFM artículo por artículo**, si confirma que el corpus va sin
   nombres de personas naturales.
3. **El marco de ingeniería de prompts**, que lleva atascado desde septiembre y
   cabe entero en una corrida.

Lo demás se queda en Opus 5.5, que es el default de la casa y el default
documentado de Anthropic.

---

## 6. Después del 16 de noviembre

Esta guía **no caduca**: lo que caduca es la disponibilidad. Las tres compuertas
y el mapa de la cartera siguen sirviendo para el siguiente modelo de techo que
aparezca.

🚦 **Antes de volver a ofrecer Fable, compruebe `/model` en la aplicación.** La
prueba por CLI anidada (`claude --model fable ... -p`) responde «Not logged in»
porque no hereda la sesión de la app, y no sirve para verificar nada.

---

*Nodo padre: [[selector-modelo-claude-optimo]]. Vecinas:
[[prompting-opus-5-doctrina]], [[gobernanza-datos-financieros-ia]],
[[eficiencia-generacion-respuestas]], [[regla-del-primer-tropiezo]].
Cifras vivas: [[reference_familia_fable_y_generacion_55]].*
