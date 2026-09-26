---
name: bce-datos-frescos-bimestral
description: >-
  Refresca cada dos meses los indicadores macro del Banco Central del Ecuador
  (BCEData) y actualiza la memoria compartida, para que toda sesión analice con
  datos vigentes. Invocar al abrir un análisis financiero, preparar una mesa
  bancaria, o cuando se pregunte por tasas, riesgo país, PIB, WTI o remesas.
trigger_phrases:
  - "datos del BCE"
  - "actualizar indicadores macro"
  - "riesgo país / tasa referencial / WTI"
  - "cómo está la economía del Ecuador"
  - "contexto macro para el informe"
  - "refresco bimestral BCE"
idioma_de_salida: español
nivel_de_madurez: aplicada
dominio: finanzas / contexto macro Ecuador
fuente:
  - 'Portal BCEData del Banco Central del Ecuador: https://contenido.bce.fin.ec/'
  - 'Snapshots locales en E:/vars/var 5/BCE-datos/ (bce_ultimo.json, bce_ultimo.md)'
  - 'Referencia en memoria: reference_bce_indicadores.md'
---

## Acerca de mí (cargar al arrancar)
Leer `...\memory\user_role.md` + `MEMORY.md`. Alimenta a
[[memoria-financiera-inteligenciada]], [[control-financiero-semanal-qvp]],
[[cfo-mensual-con-claude]], [[negociacion-bancaria-reperfilamiento]] y
[[desapalancamiento-empresa-familiar]].

## Doctrina central
> Un análisis financiero con macro vieja es un análisis equivocado con buena
> presentación. **El costo de la deuda, el riesgo país y el precio del crudo se
> mueven; las conclusiones deben moverse con ellos.**

Cada **dos meses** se refresca el tablero macro y se actualiza la memoria
compartida, de modo que cualquier sesión futura arranque con datos vigentes sin
volver a navegar el sitio.

## 🚦 El hallazgo que hace posible esta skill (no perderlo)
- **`www.bce.fin.ec` NO sirve**: exige **aceptar una política de privacidad**
  (banner bloqueante, Resolución JPRFM-2026-010-A) antes de mostrar contenido.
  🚦 **Nunca aceptar términos en nombre del usuario**: aceptar acuerdos requiere
  su autorización explícita. Por eso **no se usa ese dominio**.
- **`contenido.bce.fin.ec` SÍ sirve**: es el portal **BCEData — Series
  Estadísticas y Datos**, publica los indicadores **sin muro** (solo un aviso de
  analítica no bloqueante) y es la fuente oficial del mismo banco.
- Las URLs antiguas (`IEMensual.jsp`, `EstMacro.htm`, `home1/estadisticas/…`)
  **devuelven 404**: el BCE migró su portal. No reintentarlas.

## Qué NO hacer / compuertas 🚦
- 🚦 **No aceptar banners de privacidad ni cookies** para conseguir el dato. Si
  alguna vez el portal BCEData también los exige, **detenerse y pedir permiso**.
- 🚦 **No inventar ni interpolar cifras.** Si un indicador no se extrae, se
  reporta faltante. Cada dato lleva **su fecha de referencia**, que puede ser
  varios meses anterior a la fecha de extracción.
- 🚦 **Distinguir fecha del dato de fecha de extracción.** «PIB 2025 (prel)»
  significa preliminar: sujeto a revisión por el propio BCE.
- 🚦 **No usar la tasa referencial como si fuera la tasa que te cobran.** Es un
  promedio del sistema; la tasa efectiva de la empresa suele ser mayor.
- 🚦 **No convertir esto en pronóstico.** La skill informa el estado, no predice.
- 🚦 LIBOR aparece congelada (30-sep-2024): **está descontinuada**; usar **SOFR**.

## Protocolo (ejecución bimestral)
> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**
1. **Extraer y comparar:**
   ```
   python ~/.claude/skills/bce-datos-frescos-bimestral/scripts/extraer_bce.py --comparar
   ```
   Deja `bce_indicadores_YYYY-MM-DD.json`, `bce_ultimo.json` y `bce_ultimo.md`
   en `E:\vars\var 5\BCE-datos\`, e imprime **qué cambió** desde el refresco previo.
2. **Leer el delta**, no la tabla completa ([[eficiencia-generacion-respuestas]]).
3. **Actualizar la memoria compartida**: reescribir
   `...\memory\reference_bce_indicadores.md` con los valores nuevos, su fecha y
   los 3-5 movimientos relevantes. Mantener el índice `MEMORY.md` en una línea.
4. **Marcar implicaciones** para los expedientes vivos (ver tabla abajo).
5. **Fijar el próximo refresco**: +2 meses, anotado en el propio archivo de memoria.

## Qué mirar primero (los que mueven decisiones aquí)
| Indicador | Por qué importa en estos expedientes |
|---|---|
| **Tasa Activa Referencial** | Vara para juzgar si el crédito de QVP/Mobijuesa está caro. Insumo directo de [[negociacion-bancaria-reperfilamiento]]. |
| **Riesgo País** | Termómetro del costo de fondeo soberano y del apetito de banca de desarrollo (CAF/BID). |
| **Precio WTI** | Ecuador exporta crudo: mueve fisco, liquidez y crédito. Afecta a todo el sector real. |
| **Crecimiento del PIB / PIB nominal** | Denominador de casi todo ratio macro y contexto obligatorio de cualquier propuesta a fondos. |
| **Resultado global SPNF y deuda interna** | Si el fisco se aprieta, se retrasan pagos a proveedores del Estado. |
| **Remesas** | Sostienen consumo y demanda inmobiliaria (Vista al Río, Belén). |
| **Crédito al sector privado y captaciones** | Si el crédito se frena, la venta a crédito y la cartera se endurecen. |

## Cómo depurar si falla
- **`0 indicadores extraídos`** → el portal cambió de estructura: abrir
  `https://contenido.bce.fin.ec/` en el navegador, revisar el orden
  *nombre → valor → fecha → unidad-periodicidad* y ajustar los regex del script.
- **Timeout** → el sitio del BCE es lento; subir el `timeout` del `goto`.
- **Perfil Edge bloqueado** → cerrar Edge y reintentar (usa
  `browser_profile_edge`, ver [[feedback_solo_edge]]).

## ✅ Automatización YA ACTIVA (creada 2026-08-17 con OK del usuario)
**Tarea programada de Windows: `BCE_Refresco_Bimestral`**
- Ejecuta `scripts\refresco_bce.bat` → que llama a `extraer_bce.py --comparar`.
- **Día 17 de cada mes par, 09:07.** Próxima: **17-oct-2026**.
- Log acumulativo en `E:\vars\var 5\BCE-datos\refresco.log` (marca `RESULTADO: OK` o `ERROR`).
- **No necesita que Claude esté abierto**: el script corre solo y deja los archivos
  frescos; cualquier sesión posterior solo los lee.
- Probada de extremo a extremo el 2026-08-17: 39 indicadores, `RESULTADO: OK`.

Comandos útiles:
```
schtasks /Query /TN "BCE_Refresco_Bimestral" /FO LIST     # estado y próxima ejecución
schtasks /Run   /TN "BCE_Refresco_Bimestral"              # forzar un refresco ahora
schtasks /Delete /TN "BCE_Refresco_Bimestral" /F          # cancelar la programación
```

🚦 **Por qué NO se usó `CronCreate`:** sus trabajos viven **solo en la sesión** de
Claude y **auto-expiran a los 7 días** — un refresco bimestral nunca llegaría a
dispararse. Para periodicidades largas, la vía correcta es el Programador de
tareas de Windows.

**Qué hace la sesión cuando el dato ya está fresco:** leer `bce_ultimo.md`,
comparar contra `reference_bce_indicadores.md` y **actualizar esa ficha de memoria**
si cambiaron cifras relevantes (el script refresca los datos; la interpretación y
la memoria las actualiza Claude).

## Portabilidad (revisar el 20% al reusar)
Cambian: la ruta de destino (`E:\vars\var 5\BCE-datos\`) y el perfil de Edge.
El resto es estable mientras el BCE mantenga el portal BCEData.

## Reuso (no empezar de cero)
[[memoria-financiera-inteligenciada]] (interpretación) ·
[[negociacion-bancaria-reperfilamiento]] (usar la referencial como vara) ·
[[cfo-mensual-con-claude]] (bancabilidad) · [[control-financiero-semanal-qvp]] ·
[[cuantificar-antes-de-pedir]] (llevar el número ya hecho a la mesa).

## Ejemplos de invocación
- «Actualiza los datos del BCE antes de armar el informe.»
- «¿Cómo está el riesgo país y la tasa referencial hoy?»
- «¿La tasa que nos cobra el banco está por encima del mercado?»
