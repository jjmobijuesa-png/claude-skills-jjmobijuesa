# RELEVO — Flujo de caja y proyección Mobijuesa

| Campo | Valor |
|---|---|
| **TURNO** | NUBE |
| Principal | Sesión local "Flujo de caja y proyección Mobijuesa" (PC) |
| Espejo | Sesión nube "Espejo — Flujo de caja y proyección Mobijuesa" |
| Último checkpoint | 2026-09-26 — espejo nube: publicación guardada + directriz destilada + hoja de ruta (S1–S7) |
| Motivo del último relevo | toma automática: PC detenida (sin volcado previo de la PC) |

## Tema / objetivo del hilo
Flujo de caja y proyección financiera de Mobijuesa. _(La PC completa el detalle en el primer checkpoint.)_

## Razonamiento en curso
_(La PC lo completa: supuestos del modelo, horizonte, escenarios, decisiones tomadas.)_

## Archivos centrales
- `archivos/linkedin-post-7508480383286452224.md` — publicación completa (texto + infografía). ✅ La pegó el usuario en el chat espejo.
- `archivos/directriz-hoja-de-ruta-flujo-caja.md` — directriz, lectura crítica, supuestos S1–S7 y hoja de ruta en 6 fases. ✅
- `archivos/marco-aplicacion-skills-financieras.md` — §3 llenada. ✅
- **Archivo principal (Excel del modelo): aún no está** → lo sube la PC.

## Siguiente paso concreto
> **Checkpoint del espejo (2026-09-26):** paso 1 resuelto (el usuario pegó la publicación). Paso 3 hecho
> **contra el esqueleto del marco**, porque falta el Excel real. **Falta:** que la PC suba el modelo actual
> + los datos de §6 de la hoja de ruta. Con eso el espejo verifica la brecha real y arranca la fase 0 (CONTEXTO-mobijuesa.md).

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
- ✅ ~~Publicación LinkedIn~~: resuelto el 2026-09-26 (la pegó el usuario). Faltan autor y fecha; la PC puede completarlos.
- 🟠 **Modelo actual de flujo de caja/proyección**: aún no está en `archivos/` (lo sube la PC).
- 🟠 Datos para la fase 0: extractos del trimestre, antigüedad de cartera CxC/CxP, caja mínima (S5), qué es Mobijuesa en el modelo (S7).

## Avance del espejo (nube)
- Tomó la posta sin volcado de la PC.
- 2026-09-26: guardó la publicación y destiló la directriz: 4 pilares + método histórico → drivers → 3 estados → escenarios → actualizar.
  Lectura crítica: los "30 min" de setup se corrigen a 2–4 semanas; se agregan conciliación previa, 13 semanas por método directo y error medido.
  Se propone R32 «Sistema, no chat» para `memoria-financiera-inteligenciada` (pendiente de aprobación).
- Preparó `archivos/marco-aplicacion-skills-financieras.md`: qué aporta cada skill financiera
  del repo y una plantilla de cómo aplicar la directriz de la publicación al modelo.

## Pendientes / preguntas abiertas
- Identificar el archivo principal del modelo (¿Excel?).
- Skills relacionadas para consultar: `cfo-mensual-con-claude`, `memoria-financiera-inteligenciada`,
  `modelo-tres-estados-integrado`, `modelo-excel-sistema-vivo`, `control-financiero-semanal-qvp`.
