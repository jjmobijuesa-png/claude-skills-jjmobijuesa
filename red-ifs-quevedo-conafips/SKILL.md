---
name: red-ifs-quevedo-conafips
description: |
  Fuente permanente sobre la RED DE INSTITUCIONES FINANCIERAS (IFs) de Quevedo
  y su entorno (bancos, mutualistas y COACs), las líneas con fondos CONAFIPS
  para crédito hipotecario, el mecanismo de CONAFIPS como banca de segundo piso
  y la ESTRATEGIA DE MARKETING INMOBILIARIO orientada a esas IFs (playbook +
  plantilla de carta). Úsala como fuente para financiar o colocar proyectos de
  vivienda (Belén, San Sebastián, Ciudad del Río, Mobijuesa) ante IFs/COACs,
  para preparar acercamientos a cooperativas/bancos y para analizar tasas de
  referencia de la plaza. ANCLA la oferta VIGENTE 2026 (MIT · BIESS · BDE ·
  CONAFIPS) remitiendo a [[bonos-vivienda-ecuador-2026]], y conserva el mapa
  histórico de la plaza de Quevedo (tasas abr-2024, documentos sep-2024) como
  antecedente. VERIFICAR vigencia antes de citar cualquier tasa como actual.
trigger_phrases:
  - "red de bancos de quevedo"
  - "instituciones financieras quevedo"
  - "ifs con fondos conafips"
  - "tasas de las coac de quevedo"
  - "a qué banco o cooperativa llevamos el proyecto"
  - "carta a un banco para financiar el proyecto"
  - "estrategia de marketing para las ifs"
idioma_de_salida: español
nivel: aplicada
dominio: finanzas inmobiliarias / colocación de crédito
metadata:
  version: 1.0
  fecha: 2026-10-03
  corte_datos: "tasas abr-2024; documentos sep-2024 (hace ~2 años, verificar vigencia)"
  fuente: "E:\\vars\\var 8\\0  Mobijuesa SA\\IFs  +  E:\\vars\\var 8\\3 Ciudad del Río\\Marketing Ciud Rio"
  relacionada: bonos-vivienda-ecuador-2026, auditoria-corrida-financiera-inmobiliaria, estratega-ventas-inmobiliario-vista-al-rio, modelo-tres-estados-integrado, memoria-financiera-inteligenciada, project_financiero_san_sebastian
---

# Skill `red-ifs-quevedo-conafips`

## Qué resuelve (mecanismo, no síntoma)
Cuando hay que **financiar o colocar** un proyecto de vivienda (Belén, San Sebastián,
Ciudad del Río, Mobijuesa) ante una institución financiera, la pregunta real no es
«¿a quién llamo?» sino **«qué IF de la plaza presta para vivienda, con qué fondo,
a qué tasa de referencia, y cómo se le presenta el proyecto»**. Esta skill es la
**fuente** de esos cuatro datos y del playbook para acercarse. No reemplaza la
calificación VIS ([[bonos-vivienda-ecuador-2026]]) ni la corrida ([[auditoria-corrida-financiera-inmobiliaria]]);
las **alimenta** con el mapa de la banca local.

> ⚠️ **DOS CAPAS, NO CONFUNDIR.** (a) El **marco VIGENTE 2026** (§0) es lo que se ofrece
> HOY y vive verificado en [[bonos-vivienda-ecuador-2026]]. (b) El **mapa de la plaza**
> (§1–§3) es **histórico**: tasas **abr-2024**, documentos **sep-2024** (hace ~2 años) —
> sirve para saber quién opera en Quevedo, no para citar una tasa como actual. Nunca llevar
> una tasa de 2024 a un tercero sin revalidar con la IF, la SEPS o el BCE. Marcar 🚦 la cifra.

## 0 · Marco VIGENTE 2026 — ancla actual (MIT · BIESS · BDE · CONAFIPS)
> Esta sección **resume y remite**, no duplica. La autoridad viva es
> **[[bonos-vivienda-ecuador-2026]]** (corte 10-sep-2026, fuente normativa primaria:
> Acuerdo MIT-MIT-26-42-ACU). Ante un tercero, citar esa skill, no la tabla de §2.

- **MIT = Ministerio de Infraestructura y Tecnología** (no «Transporte» ni MIDUVI; su brazo
  es el Viceministerio de Desarrollo Urbano Sostenible y Vivienda; plataforma SIIDUVI/MIDUVI).
  Norma vigente: **Acuerdo MIT-MIT-26-42-ACU (24-ago-2026)**. **SBU 2026 = $482.**
  - **Bono «Yapa Pa Tu Casa»** (2.º segmento VIS, tope vivienda 135 SBU = $65.070): subsidio
    parcial **tiered hasta 21 SBU = $10.122** por ingreso (≤1,5 SBU → $10.122; ≤2,5 → $9.158;
    ≤3,5 → $8.194). **Se combina con la tasa preferencial** y reduce el capital financiado.
  - **«Tu Casa Miti-Miti»** (3.er segmento / VIP): tasa **4,99 %** (4,87–4,99 % según banco),
    sostenida por el **Fideicomiso de Subsidio a la Tasa** (MEF+MIT, gestión CFN) — por eso
    aguanta 25 años sin asignación discrecional año a año.
  - Requisitos duros: **cuota ≤ 40 % del ingreso bruto** del hogar · **costo ≤ 2,49 SBU/m²**
    ($1.200,18/m²) · registro del promotor en SIIDUVI.
- **BIESS — «Credicasa / Vivienda Premier»:** tasa **2,99 % a 4,99 %**, hasta 30 años, hasta
  100 % de financiamiento; exige **afiliación IESS** (36 aportaciones, 13 últimas continuas).
  🚦 **Excluye empleadores de zafra y del Seguro Social Campesino** — crítico para nóminas
  agrícolas (Agro Aéreo, palma, banano): verificar el régimen antes de ofrecer el 2,99 %.
  Credicasa financia **hasta $65.000**, avalúo ≤ $71.504,70, ingreso ≤ 3,17 SBU ($1.527,94).
- **CONAFIPS (2.º piso):** fondea **COACs/Mutualistas** calificadas; no entrega bono directo al
  comprador. Es el canal natural de la banca cooperativa. Mecanismo histórico documentado en §3.
- **BDE — Banco de Desarrollo del Ecuador: crédito DIRECTO al PROMOTOR** de vivienda VIS/VIP
  (financia la **construcción**, no la hipoteca del comprador — complementa a la IF que financia
  al comprador). **Destilado y verificado** por el hilo `financial-report-mobijuesa` (San Sebastián,
  29-ago-2026):
  - Tasa **«primer piso» (crédito directo) 6,55 %** nominal (dashboard `consulta.bde.fin.ec`,
    corte 03-ago-2026). 🚦 No confundir con **«segundo piso» 2,68 %**, que es el fondeo del BDE a
    bancos/coops intermediarios, no la tasa directa al promotor.
  - Financia **hasta 80 % de costos directos**; aporte propio 20 % (puede ser el terreno). Monto
    máx. **hasta 200 % del patrimonio** del sujeto de crédito. **Los fideicomisos mercantiles son
    sujeto de crédito elegible** (respalda estructurar vía fideicomiso).
  - Elegibilidad: ventas anuales **≥ $300.000**, sin pérdidas el último año fiscal, **≥ 3 años** de
    experiencia como promotor. Precalificación (correo Ana Baquero, 22-sep-2026): RUC · EEFF
    auditados 2023-2025 · plantilla Excel de datos financieros · declaración IR 2023-2025.
  - Contactos BDE: Mgs. **Ana Baquero** (Ana.Baquero@bde.fin.ec · 098-443-0940) · Arq. **Jorge
    Andrade**, Dir. de Negocios Inmobiliarios (099-260-0232) · Rodrigo Avilés.
  - 🚦 Sin verificar (confirmar con el BDE): plazo 48 m, gracia 24 m, 10 % de preventas, mezcla
    51/49 VIS/VIP. Detalle: [[project_financiero_san_sebastian]] + `bde_linea_financiamiento_VERIFICADO.md`.
- 🚦 **Vacíos a cerrar:** (a) parámetros BDE aún sin verificar (plazo/gracia/preventas); (b) confirmar
  que el canal del bono Yapa está operativo bajo el nuevo Acuerdo; (c) tasas Miti-Miti por banco al
  día. Al verificarse, actualizar la autoridad que corresponda — [[bonos-vivienda-ecuador-2026]] para
  MIT/BIESS, [[project_financiero_san_sebastian]] para BDE — y re-datar esta ancla.

## 1 · Roster de IFs de la plaza (Quevedo y entorno) — ANTECEDENTE histórico (2024)
20 instituciones mapeadas (base sin tasas/contactos rellenos; es el universo a trabajar):
Coac El Sagrario · Mutualista Pichincha · Coac 29 de Octubre · Consorcio del Pichincha ·
Banco Pichincha · CACPECO · **Coac JEP** · Coac Policía Nacional · Coac Mushuc Runa ·
Coac Chibuleo · VisionFund · Banco D-Miro · Banco Bolivariano · Banco Solidario ·
Banco de Machala · Banco del Pacífico · Banco Internacional · Banco Guayaquil ·
Produbanco · VisionFund Ecuador.
→ **JEP y El Sagrario** son las dos COAC con las que ya hay acercamiento activo para
Belén (gerentes Ing. Avelina Villanueva y Ing. Andrés Ávila); ver proyecto Belén.

## 2 · IFs con fondos CONAFIPS para crédito hipotecario — tasas de referencia (abr-2024 🚦)
Estas sí traían tasa. Es el subconjunto que **capta recursos de CONAFIPS** y los
coloca en vivienda (banca de 2.º piso → OSFPS → beneficiario):

| IF (OSFPS) | Tasa ref. abr-2024 🚦 | Producto |
|---|---|---|
| Coop **Chone** Ltda. | **7,49 %** | Crédito Vivienda |
| Coop Microempresarial **Sucre** | **7,50 %** | Crédito Hipotecario |
| Coop **Santa Ana** Ltda. | 9,00 % | Crédito y Microcrédito |
| Coop **ERCO** | 9,00 % | Credi-Hogar |
| Coop **Jardín Azuayo** | 9,00 % | Créditos |
| Coop **Calceta** | 9,25 % | Crédito Vivienda |
| Coop **El Sagrario** | 9,41 % | Crédito hipotecario |
| Coop **Futuro Lamanense** | 9,50 % | Crédito Inmobiliario |
| Coop **Chibuleo** | 9,50 % | Microcréditos |
| **Mutualista Pichincha** | **4,99 % a 9,93 %** | Portal Inmobiliario |

Lectura: **Mutualista Pichincha** (piso 4,99 %, vía su Portal Inmobiliario) y las
coops **Chone/Sucre (~7,5 %)** son las más competitivas de este corte; el grueso de
las COAC rondaba el **9 %**. (Una versión redondeada previa del mismo corte daba
Chone 7 %, Sucre 8 %, El Sagrario/Santa Ana/ERCO/Jardín Azuayo/Calceta 9 %,
Futuro Lamanense/Chibuleo 10 %; usar la tabla de decimales de arriba como canónica.)

## 3 · CONAFIPS como banca de SEGUNDO PISO (el mecanismo)
CONAFIPS **no presta al comprador**: coloca recursos en las **OSFPS** (coops del sector
financiero popular y solidario), y estas otorgan el crédito hipotecario al beneficiario.
El programa documentado es **«Proyecto AFD — Mi Casa Desarrollo / Vivienda Popular»**
(Agencia Francesa de Desarrollo), para afectados del **terremoto de abril 2016** en
**Manabí, Esmeraldas, Guayas, Santa Elena, Los Ríos y Santo Domingo** (Los Ríos, donde
está Quevedo, **sí** califica). 🚦 Programa ligado a 2016 — verificar si sigue abierto o
si CONAFIPS tiene hoy otra línea equivalente.
- **Tipologías:** (1) reconstrucción/ampliación/remodelación, (2) construcción en terreno
  propio, (3) adquisición.
- **Monto referencia:** hasta **$81.728,20**. **Plazo 1er piso: hasta 25 años**. Tasa:
  segmento inmobiliario del BCE.
- **Exige certificación de sismo-resistencia** (consultora externa) + documentos técnicos:
  planos arquitectónicos con implantación, estudio de suelos, planos estructurales NEC-2015,
  memoria de cálculo, presupuesto y cronograma valorado, certificado de riesgos municipal.
- **Colocación:** dos modalidades — **Anticipo** (según plan de colocación de la OSFPS) y
  **Reembolso** (créditos otorgados desde 20-dic-2017). Desembolsos al **constructor** por
  avance de obra, supervisados mensualmente por la consultora externa.
- **Fases:** 1) Socialización · 2) Elegibilidad del proyecto · 3) Certificación de viviendas
  · 4) Colocación de recursos · 5) Ejecución de obra. El **promotor** emite carta de
  intención a la Gerencia General de CONAFIPS adjuntando los documentos técnicos.
→ Para el promotor, CONAFIPS es la **palanca que abarata y habilita** a la COAC aliada:
conviene presentar el proyecto a una OSFPS que ya capte fondos CONAFIPS (tabla §2).

## 4 · Estrategia de marketing inmobiliario orientado a IFs (el playbook)
De `ESTRATEGIA DE MÁRKETING INMOBILIAIO PARA IFs` (sep-2024). Objetivo: colocar el
proyecto **a través** de la IF, alineando tres intereses — IF (coloca su cartera),
promotor (vende) y comprador (accede al crédito).
1. **Mercado y posicionamiento:** segmentar (familias jóvenes, primera vivienda, sectores
   vulnerables, microempresarios); analizar la competencia de crédito; **oferta diferenciada**
   = resaltar los beneficios del crédito con fondos CONAFIPS (tasa preferente, menos requisitos,
   hasta 100 % de financiamiento en ciertos casos).
2. **Comercial y financiera:** (a) **alianzas con el promotor** — el proyecto se presenta
   directamente a la IF para que esta solicite los fondos a CONAFIPS; (b) **capacitar a la
   fuerza de ventas** en el crédito CONAFIPS y su documentación (banco + municipio); el
   vendedor es el intermediario clave; (c) **asesoría al comprador** para armar su perfil
   financiero y acelerar la aprobación.
3. **Publicitaria:** campañas digitales segmentadas (redes, Google Ads, medios locales) +
   stands de la IF dentro del proyecto + activaciones en ferias inmobiliarias.
4. **Seguimiento (KPIs):** volumen de créditos aprobados, tiempo promedio de aprobación,
   satisfacción, tasa de conversión de leads; retroalimentación continua IF↔promotor↔asesor.
5. **Contenidos:** guías del proceso de crédito, material para ventas, landing pages de
   captura de leads, manuales de documentación, talleres.
- **Proceso de ventas:** proceso estándar inmobiliario cruzado con **Jordan Belfort**
  (línea recta) y **Jürgen Klaric** (neuroventa) → enlaza con [[estratega-ventas-inmobiliario-vista-al-rio]].

## 5 · Plantilla de carta a una IF / banco (de la carta a Banco ProCredit, Mobijuesa)
Estructura que funcionó (Ciudad del Río → ProCredit, oct-2024): (1) presentar el proyecto
y su **visión** diferenciada (p. ej. «Ciudad de 15 minutos», malecón, sostenibilidad);
(2) **por qué esa IF es el socio ideal** (alinear con su propio enfoque: PYMEs, finanzas
verdes, ODS); (3) **beneficios mutuos** (volumen de colocación hipotecaria, cartera de
proyectos sostenibles, posicionamiento); (4) **solicitud concreta** (monto del
financiamiento estructurado) + esquema (tasas preferentes para los compradores);
(5) cierre + reunión; (6) **adjuntos**: corrida/pre-factibilidad, aprobación del proyecto,
análisis legal, diseños.
- **Firma/contacto Mobijuesa:** Sociólogo **Francisco Duque, MBA — Gerente General,
  Inmobiliaria Mobijuesa S.A.** · Edificio Xima piso 1 local 75, Guayaquil ·
  Telf. 05 2781927 / 0993819017. (Para Belén se firma como Francisco Emilio Duque Cedeño,
  promotor; usar el bloque que corresponda al proyecto.)

## 6 · Fuentes vivas (rutas en disco) y uso posterior
- **Marco VIGENTE MIT/BDE (destilado por el hilo `financial-report-mobijuesa`, San Sebastián — solo citar, no editar):**
  — `G:\Mi unidad\Urbanización San Sebastian\02 Financiero\Bonos MIT\` (Acuerdo MIT-MIT-26-42-ACU,
    Oficio MIT-VDUSV-2026-0309-O, «Normativa MIT aplicada a San Sebastián», resumen y transcripciones
    de las reuniones MIDUVI 22-09-2026 y MIT Quito 25-09-2026).
  — `G:\Mi unidad\Urbanización San Sebastian\02 Financiero\Fondos BDE\` («Especificaciones BDE aplicadas
    a San Sebastián», «Vivienda BDE.pdf», plantilla de precalificación, correo Ana Baquero).
  — Belén: `…\1 Estructura Juridica\HTML - Marco Legal, Fiduciario y Bonos\Belen_Ruta_Aplicacion_MIT_Oficio_BDE.*`
    y `…\HTML - Gerencia, Financiero y BDE\`. Registro MIDUVI: `E:\vars\var 8\13 Reg MIDUVI\`.
- **IFs + CONAFIPS (plaza Quevedo, histórico):** `E:\vars\var 8\0  Mobijuesa SA\IFs\`
  — `Base IFs Quevedo Productos Financieros - CONAFIPS.xlsx` (roster, hoja «IFs - COACs»)
  — `Cred x IFs con fondos Conafips - v2.pdf` (tasas redondeadas abr-2024)
  — `DOC-Presentación CONAFIPS.pdf` (12 pág, Proyecto AFD Mi Casa Desarrollo)
  — `IMG-20240919-WA0061.jpg` (captura de hoja de refinanciamiento, sep-2022; valor marginal).
- **Estrategia + plantillas:** `E:\vars\var 8\3 Ciudad del Río\Marketing Ciud Rio\`
  — `ESTRATEGIA DE MÁRKETING INMOBILIAIO PARA IFs.pdf/.docx` (el playbook, antecedente)
  — `ESTRATEGIA DE MÁRKETING Y VENTAS INMOBILIARIAS.docx` (proceso de ventas Belfort/Klaric)
  — `Carta sobre Ciudad del Rio a Banco ProCredit*.pdf/.docx` (plantilla de carta)
  — `Ciudad del Rio PROJECT.xlsx` · `FOLLETO HARU A4 HORIZONTAL.pdf` · subcarpeta `IJSUD`.
- **Ciudad del Río como fuente posterior (todo el árbol):** `E:\vars\var 8\3 Ciudad del Río\`
  — proyección de factibilidad, Conafis Ciudad del Rio, diseños 3D, escrituras, planos,
    estudio de suelo, memoria descriptiva, malecón, modelos de vivienda, ventas.
  Proyecto de referencia: **1.000 viviendas, «Ciudad de 15 minutos», malecón de 1 km**.
  🚦 No mezclar sus cifras con Belén ni San Sebastián; es fuente de antecedente y de
  plantillas, no de números para otro proyecto.

## Cómo usar
- Para **qué se ofrece hoy** (bono, tasa, requisitos): **§0** y su autoridad
  [[bonos-vivienda-ecuador-2026]]. Para **quién opera en la plaza de Quevedo**: §1–§2 (histórico).
- Para un acercamiento a COAC/banco, **partir de la plantilla §5** y adjuntar la corrida
  auditada ([[auditoria-corrida-financiera-inmobiliaria]]) y el encaje VIS/bono
  ([[bonos-vivienda-ecuador-2026]]).
- Si la tasa/condición importa para una decisión, **revalidarla** (la de aquí es abr-2024).
- Si aparece una tasa, producto o contacto nuevo verificado, **actualizar esta skill**
  (y re-datar el corte) — [[llave-maestra-autoaprendizaje-ia]].

## Relacionadas
[[bonos-vivienda-ecuador-2026]] · [[auditoria-corrida-financiera-inmobiliaria]] ·
[[estratega-ventas-inmobiliario-vista-al-rio]] · [[modelo-tres-estados-integrado]] ·
[[memoria-financiera-inteligenciada]]
