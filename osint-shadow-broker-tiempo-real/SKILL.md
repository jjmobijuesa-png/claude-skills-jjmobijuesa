---
name: osint-shadow-broker-tiempo-real
description: |
  Doctrina de monitoreo OSINT en tiempo real destilada del tutorial
  «Shadow Broker / El Velocirraptor» del usuario jjmobijuesa
  (YouTube ID `gkfjDDcfwDc`). Plataforma open-source que consolida
  capas de datos públicos en tiempo real — aeronaves militares,
  tráfico marítimo, eventos satelitales, infraestructuras críticas,
  señales — sobre un mapa interactivo. Útil para due diligence
  geopolítico, investigación forense de movimientos sospechosos y
  análisis de exposición de infraestructura del Ecuador en redes
  abiertas.

  Esta NO es una skill de instalación: es la doctrina de qué
  herramientas usar, qué capas activar y cómo combinarlas con el
  expediente EcuaLedger Soberana (CNT, infraestructura crítica,
  oleoducto, etc.).

trigger_phrases:
  - "OSINT en tiempo real"
  - "monitoreo Shadow Broker"
  - "rastreo aeronaves militares"
  - "tráfico marítimo en vivo"
  - "infraestructura expuesta Ecuador"

idioma_de_salida: español neutro técnico-investigativo
nivel_madurez: aplicada
fuente: video YouTube gkfjDDcfwDc — transcripción local en `E:\vars\var 5\YouTube-jjmobijuesa\transcripciones\_manuales\gkfjDDcfwDc__gkfjDDcfwDc.md`
---

# OSINT en tiempo real — Shadow Broker

## Doctrina

> "Todo lo que ocurre en el mundo puede ser rastreado. Aviones,
> satélites, barcos, cámaras… Señales que están siendo transmitidas en
> este momento. No estoy hablando de hackear: hablamos de datos
> expuestos, recolectados, analizados constantemente en tiempo real."

La intuición operativa: la información ya está disponible en abierto.
La ventaja del analista no está en obtenerla, sino en consolidarla y
contextualizarla. Shadow Broker (también referido como «El
Velocirraptor») es una plataforma open-source que agrega capas y las
proyecta sobre un mapa.

## Capas de datos disponibles

El sistema se organiza por capas activables independientes:

| Capa | Tipo de dato | Uso típico |
|---|---|---|
| **Aeronaves militares** | ADS-B + transponders de tipo militar | Detectar movimientos inusuales sobre Ecuador o sus vecinos |
| **Tráfico marítimo** | AIS de buques comerciales y militares | Monitoreo de exportaciones agrícolas, contenedores, narcotráfico |
| **Espacios (satélites)** | Tracking de pasadas de satélites | Saber cuándo hay observación sobre un punto |
| **Eventos / amenazas globales** | Feed agregado de incidentes | Contextualización geográfica rápida |
| **Riesgos** | Capa derivada (zonas de conflicto, sanciones) | Due diligence de socios comerciales |
| **Infraestructuras críticas** | Energía, telecom, oleoductos | Análisis de exposición de Ecuador (CNT, OCP, SOTE) |
| **Señales / análisis de red** | Espectro radio + huella de red | OSINT avanzado |

## Cuándo invocarla

Cuando el expediente del usuario toque:

1. **EcuaLedger Soberana / CNT / infraestructura digital pública** —
   revisar exposición de los nodos validadores propuestos
   ([[project_alfalab_uteq]]).
2. **Quevepalma / exportaciones agrícolas** — monitoreo marítimo de
   contenedores de palma africana y oleoquímica
   ([[control-financiero-semanal-qvp]]).
3. **EPACEM / Oro Juez** — verificar movimientos marítimos asociables
   al caso forense ([[project_caso_epacem_orojuez]]).
4. **Análisis geopolítico Ecuador** — combinarlo con la curación X.com
   ([[intereses-geopolitica-latam]]).

## Flujo de trabajo sugerido

1. **Definir hipótesis** — qué se busca confirmar o refutar.
2. **Activar 2-3 capas máximo** — saturación visual mata el análisis.
3. **Acotar geografía** — Ecuador + vecinos (Colombia, Perú) o ruta
   marítima (Guayaquil → puerto destino).
4. **Capturar evidencia** — screenshot URL + timestamp. Usar la
   extensión Edge `Screenshot with URL - Full Page Screenshot` (ver
   [[inventario-extensiones-edge-jjmobijuesa]]).
5. **Cruzar con corpus interno** — bookmarks X
   ([[consulta-bookmarks-fdc-ec]]), NotebookLM, prensa.
6. **Persistir hallazgo** — `E:\vars\var 5\OSINT-hallazgos\YYYY-MM-DD_<asunto>.md`
   con captura + interpretación + fuentes cruzadas.

## Compuertas 🚦

1. **No publicar OSINT crudo** sobre terceros sin filtro jurídico.
2. **No interferir con activos militares** ni infraestructuras
   críticas ajenas — el monitoreo es lectura, no acción.
3. **Verificar fuentes** — ADS-B puede ser spoofeable; AIS también.
   Una sola capa no es evidencia.
4. **No vincular movimientos a personas naturales** en documentos
   externos del programa EcuaLedger (regla de inteligencia política
   velada de [[estrategia-implementacion-juridica]]).
5. **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**

## Cómo depurar si falla

- La plataforma requiere conexión a internet permanente.
- El video referencia repositorio en la descripción — buscar GitHub
  del proyecto antes de instalar.
- Si una capa no responde: el feed público puede haber sido cerrado o
  geo-restringido.

## Anclaje a la transcripción local

Transcripción íntegra en
`E:\vars\var 5\YouTube-jjmobijuesa\transcripciones\_manuales\gkfjDDcfwDc__gkfjDDcfwDc.md`
(235 líneas, español).

## Relacionado

- [[youtube-corpus-jjmobijuesa]] — fuente.
- [[wolfram-forensic-engine]] — verificación cuantitativa.
- [[intereses-geopolitica-soberania]] — cruce con curación X.com.
- [[project_caso_epacem_orojuez]] — aplicación forense local.
