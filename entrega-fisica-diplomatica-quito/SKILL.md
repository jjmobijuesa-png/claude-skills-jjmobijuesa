---
name: entrega-fisica-diplomatica-quito
description: |
  Planifica y opera la entrega física personal de paquetes diplomáticos /
  oficios institucionales en la ciudad de Quito (Ecuador). Resuelve el
  problema completo desde el momento en que el usuario llega en su auto
  hasta el regreso al parqueadero: estacionamiento estratégico, ruta
  óptima con Metro de Quito + Uber, ventanillas y horarios de cada
  institución, protocolo de mesa de partes con acuse de recibo, y
  presupuesto controlado.

  El destinatario habitual del paquete son las cinco instituciones del
  «cinturón institucional» quiteño:
    - Asamblea Nacional del Ecuador (Comisiones Especializadas, CAL)
    - Ministerio de Telecomunicaciones (MINTEL)
    - Presidencia de la República (Palacio de Carondelet)
    - Ministerios sectoriales con sede en Av. 6 de Diciembre
    - Cancillería (Av. 10 de Agosto)

  La doctrina central es: **una sola parada de auto + Metro Línea 1 como
  columna vertebral + Uber como contingencia**. El Metro de Quito atraviesa
  la ciudad de norte a sur y conecta directamente los dos polos donde se
  concentran los destinatarios: La Pradera/Iñaquito (norte, sector Asamblea
  y Ministerios) y San Francisco (sur, Centro Histórico, Carondelet).

trigger_phrases:
  - "organizar entrega física en Quito"
  - "planificar ruta diplomática Quito"
  - "itinerario entrega de oficios Quito"
  - "aplica la skill entrega-fisica-diplomatica-quito"

idioma_de_salida: español neutro institucional

---

# Entrega Física Diplomática — Quito

## Filosofía

Un paquete diplomático bien redactado y firmado **pierde 50 % de su
peso si la entrega física falla**: oficio recibido sin sello, ventanilla
cerrada, recepción genérica sin canalizar al asesor de mesa, o entrega
en horario de cambio de turno. La logística de entrega es continuación
del acto institucional, no apéndice administrativo.

Esta skill resuelve la operación con tres principios:

1. **Una sola parada de auto** — estacionar cerca de una estación
   estratégica de la Línea 1 del Metro, y de ahí movilizarse 100 % a pie,
   Metro o Uber. Evita el caos vehicular del Centro Histórico y de la Av.
   6 de Diciembre en hora pico.
2. **Metro como columna vertebral** — la Línea 1 (Quitumbe-Labrador, 15
   estaciones, 22.5 km) cubre el 90 % de los traslados institucionales
   en menos de 15 minutos por tramo.
3. **Acuse de recibo SIEMPRE** — ninguna entrega se cierra sin sello con
   número de oficio + nombre del receptor + hora. Foto de cada sello al
   firmante (Sr. Presidente FBSE) en el momento.

## Paso 0 — Confirmación de variables clave

Antes de armar el itinerario, confirmar con el solicitante:

> 1. **¿Quién entrega físicamente?**
>    - Usuario mismo (titular o equipo FBSE)
>    - Presidente / firmante en persona
>    - Mensajero institucional
>    - Comitiva de dos
>
> 2. **¿Nivel de entrega buscado?**
>    - Recepción formal con acuse de recibo (estándar)
>    - Audiencia con asesor técnico (requiere agendar)
>    - Mixto
>
> 3. **¿Día previsto?** (martes/miércoles/jueves son óptimos)
>
> 4. **¿Destinatarios?** (lista cerrada — ver Anexo 1)
>
> 5. **¿Viene desde fuera de Quito en su auto?** (define la estrategia
>    de parqueo)

## Paso 1 — Geografía operativa de Quito

### Eje Norte (sector Asamblea / Ministerios)

| Institución | Dirección exacta | Estación Metro |
|---|---|---|
| **Asamblea Nacional** | Piedrahíta N°212 y Av. 6 de Diciembre | **La Pradera** (1-7 min a pie) |
| **MINTEL** | Av. 6 de Diciembre N25-75 y Av. Colón | **La Pradera** (5 min a pie) |
| Cancillería | Av. 10 de Agosto y Carrión | La Alameda (10 min) |
| MEF | Av. 10 de Agosto y Jorge Washington | La Alameda (8 min) |

### Eje Sur (sector Centro Histórico)

| Institución | Dirección exacta | Estación Metro |
|---|---|---|
| **Palacio de Carondelet** (Presidencia) | García Moreno y Chile, Plaza Grande | **San Francisco** (5 min a pie) |
| Corte Constitucional | Av. 12 de Octubre y Pasaje Nicolás Jiménez | Alameda (15 min) o Uber |
| Asamblea (acceso público) | Av. 6 de Diciembre y Piedrahíta | La Pradera |

### Conectividad Metro Línea 1

```
Quitumbe → Morán Valverde → Solanda → Cardenal de la Torre → El Recreo →
La Magdalena → SAN FRANCISCO ⬅️ Centro Histórico
                    ↓
La Alameda → El Ejido → Universidad Central → LA PRADERA ⬅️ Asamblea/MINTEL
                                                    ↓
                                          IÑAQUITO ⬅️ Parqueo Carolina 3
                                                    ↓
                                          Jipijapa → EL LABRADOR
```

**Tramo crítico**: La Pradera ↔ San Francisco = ~6 estaciones, ~12 min
de viaje. Es el corredor diplomático completo en una sola línea.

## Paso 2 — Estacionamiento estratégico

| Parqueo | Junto a estación | Plazas | Tarifa | Cuándo usar |
|---|---|---|---|---|
| **Carolina 3** | Iñaquito (1 al norte de La Pradera) | 94 | $0.50/hr | Estándar — equidistante eje norte/sur, parque La Carolina entrega seguridad y referencia |
| **Bicentenario B** | El Labrador | 100 | $0.50/hr | Si viene del aeropuerto/norte |
| **Quitumbe (Terminal)** | Quitumbe | 200+ | $0.50/hr | Si viene desde la costa por la Panamericana Sur |

**Recomendación por defecto**: **Carolina 3** — calle Japón y Av.
Amazonas. Frente al parque La Carolina, una cuadra al sur de la estación
Iñaquito, conexión directa al Metro.

## Paso 3 — Itinerario tipo (5 entregas, eje norte + eje sur)

Diseñado para un día hábil con jornada de 4 horas en Quito centro.

| Hora | Acción | Duración |
|---|---|---|
| **08:30** | Llegar a parqueadero **Carolina 3**, parquear | 5 min |
| **08:35** | Caminar a estación Iñaquito | 5 min |
| **08:40** | Metro Iñaquito → **La Pradera** (1 estación sur) | 3 min |
| **08:43** | Caminar de La Pradera a **Asamblea Nacional** | 7 min |
| **08:50** | Entregar B-011 + B-012 + B-013 en Gestión Documental | 30-40 min |
| **09:30** | Caminar de Asamblea a **MINTEL** (5 cuadras por Av 6 Dic) | 8 min |
| **09:40** | Entregar B-014 en MINTEL Gestión Documental | 20 min |
| **10:00** | Caminar a estación **La Pradera** | 5 min |
| **10:05** | Metro La Pradera → **San Francisco** (6 estaciones sur) | 12 min |
| **10:20** | Caminar a **Palacio de Carondelet** (Plaza Grande) | 5 min |
| **10:30** | Entregar B-015 en Secretaría General de Presidencia | 30 min |
| **11:00** | Caminar a estación San Francisco | 5 min |
| **11:10** | Metro San Francisco → **Iñaquito** (7 estaciones norte) | 14 min |
| **11:25** | Caminar a parqueadero Carolina 3 | 5 min |
| **11:30** | Retirar auto. **Listo**. | — |

**Tiempo total operativo**: ~3 horas. Margen de seguridad: 1 hora.

## Paso 4 — Protocolo de entrega en mesa de partes

### Asamblea Nacional

- Ventanilla: **Gestión Documental** (planta baja del edificio principal)
- Horario: **lunes a viernes 8:00 – 16:30**
- Procedimiento:
  1. Presentar cédula del entregador
  2. Entregar oficio físico (un ejemplar) + sobre con copia
  3. Solicitar sello con número de ingreso + folio + hora
  4. Pedir copia foliada para constancia
- Para 3 oficios distintos (B-011, B-012, B-013): UN solo trámite,
  tres números de ingreso correlativos.
- Tel: (02) 399-1000 / Secretaría General 399-1397

### MINTEL

- Ventanilla: **Documentación y Archivo** (planta baja Edificio MINTEL)
- Dirección: Av. 6 de Diciembre N25-75 y Av. Colón
- Horario: **lunes a viernes 8:00 – 17:00**
- Tel: (02) 220-0200
- Procedimiento idéntico a Asamblea

### Palacio de Carondelet

- Acceso: **Secretaría General de la Presidencia**
- Dirección: García Moreno N10-43 y Chile (Plaza Grande)
- Horario: **lunes a viernes 8:00 – 17:00**
- Procedimiento especial:
  1. Identificarse en garita (cédula + motivo de visita)
  2. Solicitar ingreso a Secretaría General (NO al museo)
  3. Entregar oficio en ventanilla de correspondencia presidencial
  4. Pedir sello + número + nombre del receptor
- Email para coordinación previa: agenda@presidencia.gob.ec
- Tip: para Carondelet **se recomienda coordinación previa por email**
  para que la garita tenga registrado el ingreso del entregador.

## Paso 5 — Checklist físico

Materiales obligatorios:

```
[ ] Carpeta tipo A4 organizadora con 5 secciones rotuladas
[ ] Cada oficio impreso en alta calidad (1 original + 1 copia c/u)
[ ] Sobres oficiales con membrete FBSE rotulados al destinatario
[ ] Carta de presentación firmada por Presidente FBSE
[ ] USB con PDFs (opcional, por si solicitan versión digital)
[ ] Cédula del entregador (original + copia)
[ ] Tarjeta Ciudad del Metro de Quito ($0.45/pasaje, primera tarjeta
    gratis en estaciones; alternativa: pago por código QR vía
    Cuenta Ciudad app)
[ ] Bolígrafo azul
[ ] Cuaderno de campo para anotar nombre receptor + hora + N° ingreso
[ ] Cargador de celular + power bank
[ ] Efectivo USD: $20 para contingencias + $6 estacionamiento
[ ] Tarjeta crédito/débito (Uber)
[ ] Botella de agua + snack ligero
[ ] Paraguas plegable (Quito clima cambiante)
```

## Paso 6 — Presupuesto

| Concepto | Costo USD |
|---|---|
| Estacionamiento Carolina 3 (4-5 hr × $0.50) | $2.50 |
| Pasajes Metro (4 viajes × $0.45) | $1.80 |
| Contingencia Uber (2 viajes promedio) | $8.00 |
| Almuerzo Quito | $10.00 |
| **Operativo en Quito** | **$22.30** |
| Combustible Quevedo–Quito ida/vuelta (~700 km × $0.08) | $56.00 |
| Peajes (Quevedo-Quito) | $4.00 |
| **TOTAL incluyendo viaje desde Quevedo** | **~$82.30** |

Si pernocta una noche en Quito: +$45 hostal/hotel modesto en sector
La Mariscal.

## Paso 7 — Contingencias

| Riesgo | Mitigación |
|---|---|
| Ventanilla cerrada por feriado / paro | Llamar la víspera a verificar (Asamblea 399-1000) |
| Tráfico extremo en Av. 6 de Diciembre | Metro inmune al tráfico; mantenerse en Metro |
| Lluvia fuerte en Centro Histórico | Estación San Francisco subterránea; salir solo al cruzar a Plaza Grande |
| Demora prolongada en Carondelet | Llevar lectura o trabajo digital, no agendar nada después |
| Asaltos/inseguridad Centro Histórico | Mantenerse en arteria turística Plaza Grande / Calle García Moreno; no entrar a callejones |
| Auto inseguro en parqueo | Carolina 3 es vigilado 24/7; no dejar nada visible |

## Paso 8 — Cierre y reporte post-entrega

Al final de la jornada:

1. **Foto** de cada sello/acuse de recibo a alta resolución
2. **Subir** las 5 fotos a la carpeta institucional FBSE
3. **Email** al firmante (Sr. Presidente Francisco Duque) con:
   - 5 acuses en PDF
   - Tabla resumen: institución / número de ingreso / hora / receptor
4. **Anotar** en log de gestión institucional FBSE el cierre del trámite
5. **Calendarizar** seguimiento a +10 días hábiles si no hay respuesta

## Anexo 1 — Catálogo de destinatarios habituales

| Institución | Sector | Estación Metro óptima |
|---|---|---|
| Asamblea Nacional (Pleno + Comisiones + CAL) | Norte | La Pradera |
| MINTEL | Norte | La Pradera |
| Ministerio de Economía y Finanzas | Norte | Alameda |
| Cancillería | Norte | Alameda |
| SCVS (Superintendencia Compañías) | Norte | Universidad Central |
| BCE (Banco Central) | Norte | Alameda |
| Presidencia de la República | Centro Histórico | San Francisco |
| Vicepresidencia | Centro Histórico | San Francisco |
| Defensoría del Pueblo | Centro Histórico | Plaza del Teatro |
| Corte Constitucional | Norte alto | 12 de Octubre — Uber desde Universidad Central |
| Procuraduría General | Norte | Iñaquito |
| Junta Política y Regulación Financiera (JPRFM) | Norte | La Carolina |

## Antipatrones

- ❌ Intentar manejar el auto hasta cada institución (tráfico Quito
  destruye el cronograma)
- ❌ Estacionar en Centro Histórico (escaso, caro, inseguro)
- ❌ Entregar a recepción genérica sin solicitar Gestión Documental
- ❌ Salir de cada lugar sin acuse de recibo sellado
- ❌ Subestimar el tiempo en Carondelet (garita + protocolo de seguridad)
- ❌ Entregar viernes por la tarde (oficio queda dormido al lunes)
- ❌ Confiar en Uber al 100 % (puede tardar 20 min en hora pico Centro)

## Skills hermanas

- `memo-institucional-juridico-fbse` — genera los oficios que se entregan
- `inteligencia-politica-estrategica-multivectorial` — define a quién
  enviar y en qué orden
- `articulacion-inter-comision-legislativa` — coordina entrega múltiple
  a comisiones

## Reglas inviolables

- ✅ El acuse de recibo sellado es la única prueba válida de entrega
- ✅ No se entrega sin foto del sello enviada al firmante el mismo día
- ✅ Una sola parada de auto por jornada operativa
- ✅ Mesa de partes siempre, recepción genérica nunca
- ✅ Día óptimo: martes, miércoles o jueves (8:30–11:30 am)

## Casos resueltos

**Junio–julio 2026 — Paquete Diplomático EcuaLedger Soberana
(B-011 a B-015)**:
- 5 oficios firmados por Scolg. Francisco Duque, Mba., Presidente FBSE
- Destinatarios: Asamblea (×3), MINTEL, Carondelet
- Ruta operativa óptima: Carolina 3 → La Pradera → Asamblea → MINTEL
  → San Francisco → Carondelet → Iñaquito
- Tiempo total: 3 horas operativas + 1 hora margen
- Presupuesto operativo en Quito: $22 USD
