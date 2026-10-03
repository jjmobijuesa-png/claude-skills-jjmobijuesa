# RELEVO — Flujo de caja y proyección Mobijuesa

| Campo | Valor |
|---|---|
| **TURNO** | NUBE |
| Principal | Sesión local "Flujo de caja y proyección Mobijuesa" (PC) |
| Espejo | Sesión nube "Espejo — Flujo de caja y proyección Mobijuesa" |
| Último checkpoint | 2026-09-26 01:05 (Guayaquil) — espejo: Excel v2 con correcciones + hoja ESCENARIOS |
| Motivo del último relevo | toma automática: PC detenida |

## 🚦 Excepción de datos (aprobada por Francisco, 2026-09-28 — nota del coordinador)
Este hilo **sí puede** guardar el Excel real de flujo de caja de Mobijuesa en `archivos/`
(repo privado). No borrarlo ni poner candado aquí sin nueva decisión de Francisco.
La excepción cubre solo ese modelo: nada de cédulas, escrituras, expediente COAC ni datos
de Belén o San Sebastián. Ver `MEMORIA.md` › Regla de datos y excepciones.

## Tema / objetivo del hilo
Flujo de caja **CORPORATIVO de Inmobiliaria Juez & Juez «MOBIJUESA» S.A.** (Banco Pichincha),
enfocado en financiar la construcción de bodegas nuevas sin ahogar la caja ni recurrir al banco.
Objetivo de este hilo: aplicar la directriz «IA como sistema, no chat» (4 pilares) para volver el
flujo de caja un sistema vivo que se controla y actualiza cada semana.

## ⚠️ Corrección de alcance (para el espejo)
Este modelo es el **corporativo de Mobijuesa sobre BANCO PICHINCHA**, NO el flujo personal de
Francisco (ese corre en Produbanco). Por tanto:
- S2/S7 del espejo mencionan Produbanco y "cuota Mobijuesa 942": pertenecen al **modelo PERSONAL**,
  no a este. No aplicarlos aquí.
- La conciliación de caja aquí es contra el extracto de **Banco Pichincha** (una sola cuenta operativa).

## Razonamiento en curso (estado real del modelo)
Archivo principal: `archivos/FLUJO DE CAJA MOBIJUESA - ACTUALIZADO AL 07-09-2026.xlsx` (92,7 KB).
Ya evolucionó a **9 hojas**: PORTADA · INSTRUCTIVO CPA · PARAMETROS · FLUJO SEMANAL · Estadística ·
RESUMEN Y ALERTA · FLUJO SEMANAL (2) · GANTT OBRAS · Estadística (2). Horizonte SEM 37→52.

Cifras del corte 07-sep-2026 (Banco Pichincha):
- Saldo real de caja: **[cifra en local]**
- Ingreso operativo semanal estimado: [cifra en local] (concentrado en semanas 2-3 del mes)
- Egresos fijos semanales: [cifra en local]
- Generación operativa NETA semanal: **[cifra en local]**
- Caja mínima de seguridad (1,5× gasto fijo mensual): **[cifra en local]**  ← esto resuelve S5
- **Colchón HOY: [cifra en local] (la caja está POR DEBAJO del mínimo)**
- Ritmo histórico de gasto en obra: [cifra en local]/semana (4× la generación)

Contexto de obra ya modelado en hilos previos: dos frentes en paralelo — **bodega 22** (patio 1,
contratista D, parte 2 con descuento = [cifra en local] sin IVA / [cifra en local] con IVA) y **bodegas 16-21** (patio 2, [cifra en local] m²; total consolidado [cifra en local], unitario [cifra en local]/m²; acabado real [cifra en local]). Regla de caja:
material a crédito, mano de obra desde la operación, pagos fuertes en semanas 2-3.
Ingreso programado: capitalización del préstamo del gerente (~[cifra en local]) en septiembre.

## Directriz destilada y hoja de ruta
Ya redactadas por el espejo en `archivos/directriz-hoja-de-ruta-flujo-caja.md` (6 fases 0-5) y
`archivos/marco-aplicacion-skills-financieras.md`. La PC confirma que convergen con la hoja de
ruta entregada al usuario en el chat (4 pilares → artefactos → ritual semanal con error medido).
**Mapeo contra el modelo real (dónde estamos):**
- Contexto (fase 0): 🟡 parcial → PARAMETROS existe; falta `CONTEXTO-mobijuesa.md` formal.
- Instrucciones (fase 1): 🟡 parcial → INSTRUCTIVO CPA existe; falta que las validaciones sean automáticas.
- Formato (fase 2): 🟢 avanzado → RESUMEN Y ALERTA + Estadística + GANTT OBRAS. Falta hoja ESCENARIOS.
- Drivers (fase 3): 🟡 parcial → ingreso con curva semanal; falta articular 3 estados a 12-36 meses.
- Escenarios (fase 4): 🔴 pendiente.
- Repetición (fase 5): 🔴 el salto clave → que la contadora (CPA) sea la dueña del ritual semanal con error medido.

## Siguiente paso concreto
> **ENTREGA DEL ESPEJO (2026-09-26 01:05) — para la PC:**
> Archivo nuevo: `archivos/FLUJO DE CAJA MOBIJUESA - 07-09-2026 v2 (correcciones espejo 26-09).xlsx`
> (el original queda intacto al lado). Cambios, cada uno con comentario «ESPEJO 26-09-2026» en la celda:
> 1. Fila 8 (SEM 40→16): ingreso vinculado a PARAMETROS!E15:H15 (29 celdas). SEM 37-39 sin tocar.
> 2. T56/U56: retiradas fórmulas de control que se sumaban como egreso (+[cifra en local] de caja). U57 = [cifra en local] fijo (confirmar semana).
> 3. AJ62:AJ65 ya no suman el $/m² de la columna C.
> 4. RESUMEN Y ALERTA B18/B19/B21 → 'FLUJO SEMANAL (2)' fila 76 (antes hoja vieja oculta).
> 5. PARAMETROS filas 51-54 (sección 8) + hoja nueva **ESCENARIOS** (A actual / B fijos PARAMETROS / C B+sept normal).
> Resultados verificados (motor Python `formulas`, 0 errores; LibreOffice no funciona en la nube):
> A: mín [cifra en local], final [cifra en local], fondeo extra [cifra en local] · B: final [cifra en local], 17 sem. negativas, fondeo extra [cifra en local] ·
> C: final [cifra en local], fondeo extra [cifra en local].
> **PC:** abrir en Excel (recalcula solo: fullCalcOnLoad), revisar formato y los 2 gráficos, guardar y subir a Drive
> reemplazando la versión vigente si el usuario lo aprueba. Luego copiar el PPTX del hilo a `archivos/`.

1. **PC (requiere Edge):** completar autor y fecha de la publicación en
   `archivos/linkedin-post-7508480383286452224.md` (el texto ya está; falta la cabecera del post).
   Skill `linkedin-guardados-fedphd`, solo lectura. — PENDIENTE, requiere confirmación del usuario.
2. **Fase 0 (arrancar):** crear `archivos/CONTEXTO-mobijuesa.md` con modelo de negocio, cuentas
   (Banco Pichincha), top clientes/proveedores con plazos, calendario SRI, deuda, caja mínima
   (ya = 1,5 meses / [cifra en local]) y KPIs (DSO/DPO/DIO, ciclo de caja, DSCR, generación semanal).
3. **Fase 2 (cerrar):** añadir hoja ESCENARIOS (base/optimista/pesimista + estrés) con acción disparadora.
4. Instalar los 4 hooks del relevo en `~/.claude/settings.json` — PENDIENTE de mostrar el JSON y confirmar.

## Bloqueantes
- 🟠 **PPTX del hilo**: el usuario pidió verlo, pero no está en el repo. La PC debe copiarlo a `archivos/`.
- 🔴 **Decisión del usuario**: fijos reales = [cifra en local]/sem (PARAMETROS) o ≈[cifra en local]/sem (cargado en el flujo).
  Con PARAMETROS la caja es negativa desde SEM 48 y cierra en [cifra en local] (ver auditoría).
- ✅ ~~Modelo actual en `archivos/`~~: RESUELTO 2026-09-26 (subido, 9 hojas).
- ✅ ~~Caja mínima (S5)~~: RESUELTO — el modelo ya la fija en 1,5 meses de gasto fijo = [cifra en local].
- 🟠 Autor/fecha de la publicación LinkedIn (requiere Edge; contenido ya pegado).
- 🟠 Fase 0 necesita: antigüedad de cartera CxC/CxP y calendario SRI reales (los aporta el usuario/contadora).
- 🟠 Hooks del relevo aún no instalados (cambio de configuración; requiere confirmación).

## Avance del espejo (nube) — conservado
- 2026-09-26: guardó la publicación, destiló la directriz (4 pilares + histórico→drivers→3 estados→
  escenarios→actualizar), lectura crítica (los "30 min" reales son 2-4 semanas; conciliación previa;
  13 semanas método directo; error medido). Propuso R32 «Sistema, no chat» para
  `memoria-financiera-inteligenciada` (pendiente de aprobación del usuario).

## Pendientes / preguntas abiertas
- Aprobar R32 en `memoria-financiera-inteligenciada`.
- Confirmar si se hace la extracción LinkedIn (autor/fecha) y la instalación de hooks.
- Skills a consultar: `cfo-mensual-con-claude`, `memoria-financiera-inteligenciada`,
  `modelo-tres-estados-integrado`, `modelo-excel-sistema-vivo`, `control-financiero-semanal-qvp`.
