---
name: glosario-ecualedger-corrector
description: |
  Glosario canónico del programa EcuaLedger Soberana del Ecuador con
  capacidad de detección y depuración de errores tipográficos
  específicos del dominio:

    1. Términos del corpus mal escritos (Soberama → Soberana,
       Ecualeder → EcuaLedger, Soberanaa → Soberana, etc.).
    2. Palabras pegadas o concatenadas (FundaciFundacion, SoberSoberana,
       LOFPDLOFPD, etc.).
    3. Letras repetidas indebidamente en una palabra (LLLOFPD, EEEcuaLedger,
       Soberannnna).
    4. Acrónimos institucionales corruptos (FBBSE, BCEE, MINTELT, JJPRFM).
    5. Nombres de leyes mal formateados (Ley 68822/21, Ley 7572-25).

  La skill mantiene un glosario maestro con ~120 términos canónicos del
  corpus (entidades, leyes, conceptos jurídicos, acrónimos, paraguayos,
  ecuatorianos) y aplica:

    - Normalización Levenshtein contra el glosario.
    - Detección regex de palabra-duplicada-concatenada.
    - Detección regex de letra-repetida-excesiva.
    - Validación de acrónimos contra catálogo cerrado.

  Reutilizable para cualquier corpus EcuaLedger (memos, leyes,
  reglamentos, informes, presentaciones).

trigger_phrases:
  - "depurar glosario EcuaLedger"
  - "corregir palabras pegadas EcuaLedger"
  - "validar acrónimos institucionales"
  - "aplica la skill glosario-ecualedger-corrector"

idioma_de_salida: español neutro institucional-jurídico

---

# Glosario EcuaLedger Soberana — Corrector de dominio

## Filosofía

Un documento institucional sobre EcuaLedger Soberana puede tener
ortografía RAE perfecta y aún así contener errores que el lector
experto detectará de inmediato: un acrónimo invertido, un nombre
propio mal escrito, una ley citada con número errado, una palabra
concatenada por descuido.

Esta skill maneja un **glosario maestro de dominio** y depura el
texto contra él. Es el complemento esencial de
`correccion-ortografica-rae-espanol`: la RAE valida el español, este
glosario valida el corpus EcuaLedger.

## Las cuatro clases de error que este glosario depura

| Clase | Ejemplo encontrado | Corrección |
|-------|---------------------|------------|
| **Término canónico mal escrito** | Soberama, Sobeerana, Soberanaa | Soberana |
| **Palabra concatenada (sin espacio)** | FundaciFundacion, SoberSoberana | Fundación, Soberana |
| **Letra repetida excesiva** | LLLOFPD, EEEcuaLedger, Soberannnna | LOFPD, EcuaLedger, Soberana |
| **Acrónimo / cita corrupta** | FBBSE, JJPRFM, Ley 68822/21 | FBSE, JPRFM, Ley 6822/21 |

## El glosario maestro

### 1. Entidades del programa (acrónimos canónicos)

| Acrónimo | Significado |
|----------|-------------|
| **FBSE** | Fundación Blockchain Soberana del Ecuador |
| **IBPP** | Infraestructura Blockchain Pública Permisionada |
| **DTE** | Documento Transmisible Electrónico |
| **EPE** | Emisor de Pago Electrónico |
| **VNE** | Valor Negociable Endosable |
| **FFD** | Fideicomiso Financiero Digital |
| **SECAS** | Sociedades Emisoras de Capital Abierto Simplificadas |
| **MIPYMEs** | Micro, Pequeñas y Medianas Empresas |
| **EPS** | Economía Popular y Solidaria |
| **HSM** | Hardware Security Module |
| **PoA** | Proof of Authority |
| **DLT** | Distributed Ledger Technology |
| **PSAV** | Proveedor de Servicios de Activos Virtuales |
| **PII** | Personal Identifiable Information |
| **RWA** | Real World Assets |
| **DvP** | Delivery versus Payment |
| **LBTR** | Liquidación Bruta en Tiempo Real |

### 2. Leyes y reglamentos

| Cita canónica | Significado |
|---------------|-------------|
| **LOFPD** | Ley Orgánica de la Fe Pública Digital (Ecuador) |
| **COMYF** | Código Orgánico Monetario y Financiero |
| **LMV** | Ley de Mercado de Valores |
| **COPLAFIP** | Código Orgánico de Planificación y Finanzas Públicas |
| **LOPDP** | Ley Orgánica de Protección de Datos Personales |
| **COIP** | Código Orgánico Integral Penal |
| **COGEP** | Código Orgánico General de Procesos |
| **Ley 6822/21** | Servicios de Confianza (Paraguay) |
| **Ley 7572/25** | Mercado de Valores y Productos (Paraguay) |
| **CRE** | Constitución de la República del Ecuador |

### 3. Órganos del Estado

JPRFM, BCE, SCVS, SB, COSEDE, UAFE, SRI, MINTEL, MEF, SENESCYT,
ARCOTEL, CONCLAFT, CAL, CNT EP, CPYB, LegalLedger.

### 4. Conceptos doctrinales

- **EcuaLedger Soberana** (no Soberama, no Ecualeder, no Ecuableder)
- **Equivalencia funcional plena**
- **Gobernanza multisectorial 25-25-25-25**
- **Bolsa Soberana de Productos**
- **Twin-chain** o **H2 Twinchain**
- **Cross-chain settlement**
- **Off-chaining del PII**
- **Crypto-shredding** (derecho al olvido)
- **Sandbox Regulatorio CPYB**
- **Monedero Ciudadano Soberano**

### 5. Modelo paraguayo de referencia

- Cámara Paraguaya de Blockchain (CPYB)
- Banco Central del Paraguay (BCP)
- Superintendencia de Valores del Paraguay (SUVAL)
- Resolución General DNIT N.° 47/2026

## Las cuatro reglas de detección

### Regla 1 — Términos canónicos del corpus

Tabla de reemplazos directos (extracto):
```
Soberama → Soberana
Sobeerana → Soberana
Soberannna → Soberana
Ecualeger → EcuaLedger
Ecualeder → EcuaLedger
Ecuableder → EcuaLedger
Ecuableger → EcuaLedger
EcuaLedger Soberama → EcuaLedger Soberana
LegalLeger → LegalLedger
LegalLedguer → LegalLedger
FBBSE → FBSE
BCEE → BCE
MINTELT → MINTEL
JJPRFM → JPRFM
```

### Regla 2 — Palabra duplicada concatenada

Regex: `\b(\w{4,})\1\b`

Detecta: FundaciFundacion, SoberSoberana, LOFPDLOFPD, ConstituciConstitucion, EcuaLedEcuaLed.

Resolución: tomar la primera ocurrencia y descartar la repetición.

### Regla 3 — Letra repetida excesiva

Regex: `([a-zA-ZáéíóúñÁÉÍÓÚÑ])\1{2,}`

Detecta: LLLOFPD (3 L), EEEcuaLedger, Soberannnna, FFFBSE.

Resolución contextual:
- Si la palabra completa coincide con un término canónico tras quitar
  letras repetidas, aplicar.
- Si no, advertir sin tocar (puede ser un caso legítimo: ej. "vacíoo"
  es error, pero "Hawaiian" tiene doble "i" legítima).

### Regla 4 — Acrónimo contra catálogo cerrado

Para cada acrónimo canónico (FBSE, IBPP, DTE, EPE, VNE, FFD, BCE,
SCVS, JPRFM, MINTEL, MEF, COSEDE, UAFE, CONCLAFT, CAL, LMV, COMYF,
COPLAFIP, LOFPD, LOPDP, COIP, COGEP, CRE, CPYB, SUVAL, BCP, DNIT):

- Buscar variantes corruptas (letra duplicada, letra faltante).
- Reemplazar por el canónico.

## Workflow de la skill

### Paso 0 — Diagnóstico

Para cada DOCX:
- Conteo de cada clase de error.
- Lista de palabras sospechosas detectadas (para revisión humana).

### Paso 1 — Aplicación de reglas

Aplicar en orden:
1. Reglas de términos canónicos (Regla 1).
2. Regex de palabra duplicada concatenada (Regla 2).
3. Regex de letra repetida excesiva (Regla 3) — solo para palabras
   que tras corrección coincidan con un término canónico.
4. Validación de acrónimos contra catálogo cerrado (Regla 4).

### Paso 2 — Verificación

Re-ejecutar el diagnóstico. El conteo debe ser 0 o cercano a 0.
Reportar residuales para revisión humana.

## Anti-falsos positivos

- **"hh"** legítimo: ninguno conocido en castellano. Detectar y
  corregir.
- **"ll"** legítimo: bastantes (lleno, llave, calle). NO eliminar.
- **"rr"** legítimo: muchos (carro, perro). NO eliminar.
- **"oo"** raro: zoológico, cooperativo, cooperación. **Mantener**.
- **"ee"** raro: leer, creer, proveer. **Mantener**.
- Tres o más letras repetidas: prácticamente siempre error.

## Casos resueltos

**Junio 2026 — Paquete EcuaLedger Soberana B-011 a B-015:**
- Detectados y corregidos: "Soberama" (×13 ocurrencias acumuladas),
  "ms" → "más", "dems" → "demás", "ano" contextual → "año".
- Acrónimos validados: FBSE, IBPP, JPRFM, MINTEL, BCE, SCVS, COSEDE,
  UAFE, CAL, COMYF, LMV, COPLAFIP, LOFPD — todos OK tras pasada.

## Reglas inviolables

- ✅ El glosario maestro es la fuente de verdad para términos del
  corpus.
- ✅ Las correcciones de letras repetidas solo aplican si el resultado
  coincide con un término canónico.
- ✅ Los acrónimos del catálogo cerrado no se modifican.
- ✅ Documentar cada corrección sustantiva en un log de auditoría.

## Antipatrones

- ❌ Eliminar todas las letras repetidas sin contexto.
- ❌ Aplicar Levenshtein con umbral alto (introduce falsos positivos).
- ❌ Modificar acrónimos sin validar contra el catálogo.
- ❌ Confundir typo con nombre propio extranjero.

## Skills hermanas

- `correccion-ortografica-rae-espanol` — pase RAE general antes de
  esta skill.
- `redaccion-humana-legislativa` — filtro post-corrección para
  léxico no jurídico.
- `memo-institucional-juridico-fbse` — generador del DOCX que pasa
  por esta skill.
- `aceptar-revisiones-docx-y-comentarios` — limpieza de TC antes.
