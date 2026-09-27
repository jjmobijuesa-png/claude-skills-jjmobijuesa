# Auditoría del libro «FLUJO DE CAJA MOBIJUESA - ACTUALIZADO AL 07-09-2026.xlsx»

_Espejo nube, 2026-09-26. Solo lectura: el libro NO se modificó. Cifras recalculadas con openpyxl._

## Estructura
- Visibles: `FLUJO SEMANAL (2)` (hoja viva, SEM 37-2026 → SEM 16-2027, 32 semanas), `GANTT OBRAS`, `Estadística (2)`.
- Ocultas: PORTADA, INSTRUCTIVO CPA, PARAMETROS, `FLUJO SEMANAL` (versión anterior), Estadística, RESUMEN Y ALERTA.

## Lo que dice el flujo actual
- Caja nunca baja de 0; mínimo 19.064,64 en SEM 13-2027 (bajo la caja mínima de 24.885,54 en SEM 13-14).
- Obra programada SEM 37→16: 323.660 (≈10.114/sem). Sin programar: 161.200 (adoquinado 120.657,
  Compatty Flores 35.445, 14 tubos 6.500, Tapia bodega 150 m² 4.370).
- Agroaéreo: 3 aportes de 30.000 (SEM 41, SEM 49, SEM 5-2027).

## Hallazgos (por gravedad)
1. 🔴 **Egresos fijos subestimados ~94 mil.** El flujo carga 28.260 en 32 semanas (≈883/sem), pero
   PARAMETROS fija 3.818,26/sem (16.590/mes). Mantenimiento de bodegas, impuestos/prediales,
   estudios y retiros de socios están en 0 casi todas las semanas; gasto administrativo 1.755/mes vs 3.268.
   **Con los fijos de PARAMETROS la caja se vuelve negativa en SEM 48 (nov-2026) y cierra SEM 16 en −66.751**
   (24 de 32 semanas bajo la caja mínima). Hay que decidir cuál de los dos valores es el real.
2. 🔴 **RESUMEN Y ALERTA apunta a la hoja vieja** (`'FLUJO SEMANAL'!D61`, oculta): anuncia déficit de
   40.530 y 13 semanas de fondeo, mientras la hoja (2) muestra todo 🟢. Dos mensajes contradictorios.
3. 🟠 **Septiembre con ingreso 2,4× el promedio**: SEM 37-39 = 62.478 vs 26.459/mes. Si fuera un mes
   normal, −41.310 de caja. Confirmar si son cobros reales (extracto Pichincha) o proyectados.
4. 🟠 **Ingreso operativo tecleado, no vinculado**: fila 8 tiene los valores de PARAMETROS!E15:H15 como
   constantes; cambiar el ingreso en PARAMETROS no mueve el flujo (rompe el «sistema vivo»).
5. 🟠 **Fila 56 (Flores enblocado paso vial)**: en T56/U56 (SEM 1-2 de 2027) quedaron fórmulas de control
   `=SUM(D56:S56)` y `=B56-T56` que se suman como egreso → 3.450 de doble cuenta. Fila 57: `U57=B57-T57`
   programa 2.643,85 en SEM 2 quizá por accidente.
6. 🟡 **Sobre-ejecución vs presupuesto (AK negativo)**: puertas Tapia −2.000, Chinchi −2.480,
   Flores piso −1.198, pared metálica −817. Actualizar presupuesto o registrar el sobrecosto.
7. 🟡 **Columna C mezcla conceptos**: en filas 62-65 guarda $/m² (40; 113,43) y el TOTAL (AJ) la suma
   como si fuera dinero (~380 de error). GANTT D16 «programado» incluye lo ya ejecutado (col. C).
8. 🟡 Cadenas `=+N62`, `=+O64` saltan semanas a propósito (media semana), frágiles al insertar columnas.

## Acción propuesta (pendiente de aprobación del usuario / PC)
- Decidir la base de fijos (PARAMETROS vs lo cargado) y vincular filas 8 y 13-20 a PARAMETROS.
- Reapuntar RESUMEN Y ALERTA a `FLUJO SEMANAL (2)` y mostrarla.
- Limpiar T56/U56/U57 y pasar $/m² a otra columna.
- Recalcular fondeo Agroaéreo necesario con fijos reales → base para hoja ESCENARIOS (fase 2).
