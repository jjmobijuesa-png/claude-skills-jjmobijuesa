---
name: analisis-variaciones-cascada
description: |
  Convierte «vendimos menos que el presupuesto» en una CAUSA RAÍZ accionable,
  descomponiendo la diferencia entre real y presupuesto en sus efectos separables
  —precio, volumen, mezcla, tipo de cambio, tiempo— y entregándola como gráfico
  de cascada (waterfall) donde cada barra es una decisión, no un número.

  Es la técnica que le falta al cierre mensual de esta casa: hoy el cierre dice
  CUÁNTO se desvió; esta skill dice POR QUÉ y QUIÉN puede corregirlo. Regla dura:
  las variaciones deben sumar exactamente la diferencia total; si no cuadran al
  centavo, el análisis está mal y no se presenta.

trigger_phrases:
  - "por qué se desvió el presupuesto"
  - "análisis de variaciones"
  - "variance analysis"
  - "gráfico de cascada / waterfall"
  - "descompón la diferencia entre real y presupuesto"
  - "causa raíz de la desviación del mes"
idioma_de_salida: español
nivel_madurez: aplicada
dominio: finanzas / control de gestión
metadata:
  version: 1.0
  fecha: 2026-09-05
  origen: destilada el 2026-09-05 a partir del ítem 7 del post de Nicolas Boucher «4 years of finance college in 10 YouTube videos» (lnkd.in/p/eYTCmUEW). 🚦 El video prometido NO EXISTE en su canal (92 videos verificados con yt-dlp); la técnica se reconstruyó desde contabilidad de gestión estándar y se ancló en OpenStax Financial Accounting (CC BY, verificado).
  relacionada: cfo-mensual-con-claude, control-financiero-semanal-qvp, conciliacion-multicuenta-fdc, bancabilidad-matriz-cuatro-bloques, entrega-visual-html-vs-texto
---

# Skill `analisis-variaciones-cascada`

## Doctrina

Un cierre que informa «el margen cayó 12 %» no sirve para decidir: nadie puede corregir un
porcentaje. Un cierre que informa «el margen cayó 12 %: **−8 puntos son precio**, −6 son volumen y
+2 los recuperó la mezcla» pone la conversación donde debe estar, porque cada efecto tiene un dueño
distinto —el precio es del comercial, el volumen del mercado, la mezcla de la decisión de qué
empujar—. **La descomposición es lo que convierte un informe en una orden de trabajo.**

La regla que separa el análisis serio del adorno: **los efectos deben sumar exactamente la
diferencia total**. Si queda un residuo sin nombre, no se presenta hasta bautizarlo.

## Las cuatro variaciones canónicas

Sea `P` precio, `Q` cantidad; `r` real y `p` presupuesto.

| Efecto | Fórmula | Pregunta que responde | Dueño |
|---|---|---|---|
| **Precio** | `(Pr − Pp) × Qr` | ¿Vendimos más caro o más barato? | Comercial |
| **Volumen** | `(Qr − Qp) × Pp` | ¿Vendimos más o menos unidades? | Mercado y comercial |
| **Mezcla** | `Σ (participación_r − participación_p) × margen_p` | ¿Cambió qué producto pesa más? | Decisión de portafolio |
| **Cambio / plazo** | diferencia por tipo de cambio o por corrimiento de fecha | ¿Es real o es calendario? | Tesorería |

Orden de cálculo: **precio primero, volumen después, con el precio presupuestado**. Invertir el orden
mueve dinero entre las dos barras y hace que dos analistas honestos obtengan números distintos.

## Protocolo

> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

1. **Fijar el par que se compara.** Real contra presupuesto, o real contra el mismo mes del año
   anterior, o real contra el último forecast. **Nunca mezclar los tres en el mismo gráfico.**
2. **Bajar al nivel donde el efecto es separable**: producto, proyecto o centro de costo. A nivel
   consolidado todos los efectos se cancelan y el análisis no dice nada.
3. **Calcular las variaciones** en el orden de arriba.
4. **Verificar el cuadre:** la suma de efectos debe igualar la diferencia total al centavo.
   Si no cuadra, hay un efecto sin identificar; buscarlo antes de seguir.
5. **Nombrar cada barra con una causa, no con una categoría contable.** «Precio: −$4.200 por el
   descuento de cierre de trimestre» vale; «Variación de precio: −$4.200» no.
6. **Entregar como cascada** (barras que parten del presupuesto y aterrizan en el real), con las
   barras negativas en un color y las positivas en otro. Ver [[entrega-visual-html-vs-texto]].
7. **Cerrar con las tres acciones** que se derivan, cada una con dueño y fecha. Un análisis de
   variaciones sin acciones es contabilidad, no control.

## Aplicación en esta casa

- **Cierre mensual** ([[cfo-mensual-con-claude]]): sustituir el relato del mes por la cascada.
  El DSCR se explica mejor por sus efectos que por su nivel.
- **Belén y San Sebastián**: descomponer la desviación del costo por m² en precio de material,
  rendimiento de mano de obra y avance físico.
- **QVP y palma**: la desviación de ingreso casi siempre es precio internacional más rendimiento
  por hectárea; separarlos evita culpar al equipo por el mercado.
- **Bodegas**: ocupación contra tarifa. Son dos negocios distintos dentro de la misma línea.

## Compuertas 🚦

- **No presentar variaciones que no cuadran.** El residuo sin nombre destruye la credibilidad de
  todo el informe.
- **No usar porcentajes solos.** Un −12 % sobre base pequeña no es comparable con un −3 % sobre base
  grande: la cascada va en dinero, y el porcentaje acompaña.
- **No consolidar antes de descomponer.** Es el error más común y anula el ejercicio.
- **No convertirlo en juicio de personas.** El análisis nombra efectos; la conversación sobre
  responsabilidad viene después y es otra reunión.

## Fuente y honestidad de origen

La técnica es estándar de contabilidad de gestión; el disparador fue un post de LinkedIn que
prometía un video sobre el tema. **Ese video no existe en el canal del autor** (92 videos
verificados). Base documental utilizable y verificada: **OpenStax Financial Accounting** (CC BY,
`openstax.org`) y **MIT 15.401** para la parte de valor. Ver
`E:\vars\var 5\Universidad-Abierta\notas\2026-09-05_destilacion-post-boucher.md`.

## Relacionado

- Microciclo 5 del [[programa-estudio-profundo-mit]] (Estados financieros y variaciones)
- [[cfo-virtual-44-agentes]] · [[control-financiero-semanal-qvp]] · [[modelo-tres-estados-integrado]]
