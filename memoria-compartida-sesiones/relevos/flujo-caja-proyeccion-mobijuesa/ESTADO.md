# RELEVO — Flujo de caja y proyección Mobijuesa

| Campo | Valor |
|---|---|
| **TURNO** | NUBE |
| Principal | Sesión local "Flujo de caja y proyección Mobijuesa" (PC) |
| Espejo | Sesión nube "Espejo — Flujo de caja y proyección Mobijuesa" |
| Último checkpoint | 2026-09-25 23:39 (Guayaquil) — espejo nube: toma de posta + marco de skills financieras |
| Motivo del último relevo | toma automática: PC detenida (sin volcado previo de la PC) |

## Tema / objetivo del hilo
Flujo de caja y proyección financiera de Mobijuesa. _(La PC completa el detalle en el primer checkpoint.)_

## Razonamiento en curso
_(La PC lo completa: supuestos del modelo, horizonte, escenarios, decisiones tomadas.)_

## Archivos centrales
_(La PC los copia a `archivos/`.)_
- `archivos/linkedin-post-7508480383286452224.md` — publicación guardada de LinkedIn (pendiente de extraer).

## Siguiente paso concreto
**Buscar, crear y aplicar el contenido y la directriz de la publicación guardada de LinkedIn**
(cuenta fedphd@gmail.com, sesión abierta en Edge):
https://www.linkedin.com/feed/update/urn:li:activity:7508480383286452224/

1. **PC** (la nube no tiene acceso a LinkedIn): abrir la publicación en Edge (skill
   `linkedin-guardados-fedphd`), extraer autor, fecha, texto completo, imágenes/carrusel
   descritos y enlaces, y guardarlo en `archivos/linkedin-post-7508480383286452224.md`.
   Copiar además el modelo actual de flujo de caja/proyección a `archivos/`.
2. **PC**: TURNO = NUBE, push a `main`.
3. **Espejo**: destilar la directriz de la publicación (qué propone, método, métricas),
   contrastarla con el modelo actual, y crear/aplicar los cambios al flujo de caja y a la
   proyección en `archivos/`, documentando cada supuesto nuevo.
4. **Espejo**: devolver la posta (TURNO = PC) con resumen de cambios.

## Bloqueantes
- 🔴 **Publicación LinkedIn 7508480383286452224**: solo la PC puede extraerla (sesión de
  fedphd@gmail.com en Edge). La nube **no tiene acceso a LinkedIn**. Hasta que la PC suba
  `archivos/linkedin-post-7508480383286452224.md`, el espejo no puede destilar su directriz.
- 🟠 **Modelo actual de flujo de caja/proyección**: aún no está en `archivos/` (lo sube la PC).

## Avance del espejo (nube)
- Tomó la posta sin volcado de la PC.
- Preparó `archivos/marco-aplicacion-skills-financieras.md`: qué aporta cada skill financiera
  del repo y una plantilla de cómo aplicar la directriz de la publicación al modelo.

## Pendientes / preguntas abiertas
- Identificar el archivo principal del modelo (¿Excel?).
- Skills relacionadas para consultar: `cfo-mensual-con-claude`, `memoria-financiera-inteligenciada`,
  `modelo-tres-estados-integrado`, `modelo-excel-sistema-vivo`, `control-financiero-semanal-qvp`.
