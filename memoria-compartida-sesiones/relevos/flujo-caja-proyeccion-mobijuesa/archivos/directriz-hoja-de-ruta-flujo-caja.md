# Directriz destilada y hoja de ruta: gestión del flujo de caja de Mobijuesa como sistema

_Espejo nube, 2026-09-26. Fuente: `linkedin-post-7508480383286452224.md`, contrastada con `marco-aplicacion-skills-financieras.md`._
_Estado: **el modelo actual todavía no está en `archivos/`**, así que el contraste se hace contra el esqueleto del marco (§2). Cuando la PC suba el Excel, cada fase se verifica contra él._

## 1. Directriz en una línea
Un proceso financiero se vuelve un **sistema** cuando tiene cuatro piezas fijas: contexto, instrucciones, formato y repetición. Ese sistema proyecta a partir del histórico y los drivers (las variables que mueven el negocio), arma los 3 estados y los 3 escenarios, y **se actualiza** cuando cambian los resultados. No se rehace desde cero.

## 2. Lectura crítica (qué se adopta y qué se corrige)
| Punto de la publicación | Veredicto | Ajuste para Mobijuesa |
|---|---|---|
| 4 pilares (contexto, instrucciones, formato, repetición) | Se adopta | Cada pilar se vuelve un archivo versionado (ver §4) |
| Histórico → drivers → hipótesis → 3 estados → escenarios → actualizar | Se adopta; coincide con R17 de `memoria-financiera-inteligenciada` y con `modelo-tres-estados-integrado` | Ya está en el esqueleto del marco (§2) |
| "~30 min de setup" | Se corrige: es texto de marketing | El setup real toma 2–4 semanas (supuesto S1) |
| No habla de calidad del dato | Vacío | Regla: saldo inicial = banco conciliado (S2) |
| La unidad es la proyección mensual | Insuficiente para gestionar la caja | Dos niveles: 13 semanas por método directo (gestión) + 12–36 meses con 3 estados (planificación) (S3) |
| "Mejora cada semana" sin métrica | Vacío | Medir el error del forecast por horizonte (S4) |

**¿Es nueva?** No como método: ya está cubierto por R17 y por `modelo-tres-estados-integrado`. Lo nuevo es la **disciplina operativa**: setup en capas y repetición medida. Se propone registrarla como **R32 «Sistema, no chat: contexto, instrucciones, formato y repetición medida»** en `memoria-financiera-inteligenciada`, cuando la PC lo apruebe.

## 3. Supuestos nuevos (documentados)
| Id | Supuesto | Fuente | Cómo se valida |
|---|---|---|---|
| S1 | El setup completo toma 2–4 semanas, no 30 min | Criterio del espejo; práctica de `control-financiero-semanal-qvp` | Comparar con el tiempo real de las fases 0–4 |
| S2 | El saldo inicial de cada semana es el saldo bancario conciliado, nunca un saldo contable sin conciliar | `cfo-mensual-con-claude` (W2) y `conciliacion-multicuenta-fdc` | Control: suma de movimientos = saldo final − saldo inicial → 0 |
| S3 | La gestión se hace a 13 semanas por método directo; la proyección a 12–36 meses es indirecta y con 3 estados | Marco §2 punto 3 | La caja de la semana 4 y la del mes 1 difieren menos de 5 % |
| S4 | Metas de precisión: error ≤ 5 % a 1 semana y ≤ 10 % a 4 semanas | Umbrales 3 %/5 % de `control-financiero-semanal-qvp`, ampliados según el horizonte | Hoja PLAN-VS-REAL, columna "error %" |
| S5 | Existe una política de caja mínima (semanas de cobertura de pagos fijos) | Pendiente del usuario, **sin valor asumido** | El usuario la fija; se sugieren 4 semanas como punto de partida |
| S6 | Cada escenario lleva una acción disparadora decidida de antemano | Pilar "Formato: plan de acción" de la publicación | Tabla ESCENARIOS con columna "acción si se activa" |
| S7 | La cuota de Mobijuesa (942) que no pasa por Produbanco se registra como flujo propio | Marco §1 (`cfo-mensual-con-claude`) | Pendiente: confirmar qué es Mobijuesa en el modelo (§5 del marco) |

## 4. Hoja de ruta (cada pilar se vuelve un artefacto)
| Fase | Plazo | Pilar | Entregable en el repo | Criterio de "hecho" |
|---|---|---|---|---|
| 0 | Días 1–3 | Contexto | `CONTEXTO-mobijuesa.md`: modelo de negocio, cuentas, top-10 clientes y proveedores con plazos reales, nómina, calendario SRI (IVA, retenciones, IR), deuda, caja mínima (S5), KPIs (cobertura, DSO/DPO/DIO, ciclo de conversión de caja, generación semanal) | La PC lo revisa; ningún dato inventado |
| 1 | Semana 1 | Instrucciones | Reglas en la skill del hilo: conciliar primero (S2); marcar cada cifra como real, comprometida o supuesto; alertas (saldo < mínimo, desvío > ±10 %, cliente fuera de plazo); si falta un dato, preguntar | Una corrida de prueba produce alertas correctas |
| 2 | Semana 2 | Formato | Excel sistema vivo: SUPUESTOS · CAJA-13S (directo) · PLAN-VS-REAL · TABLERO (semáforos) · CONCLUSIONES-ACCIÓN · CONTROLES | Controles = 0; prueba de vida con una palanca |
| 3 | Semanas 3–4 | Drivers | Cobros = ventas × curva de cobro por antigüedad; pagos = compras × plazo; nómina, SRI y deuda por calendario; mensual 12–36 meses con 3 estados articulados | Balance cuadra sin plug; caja del flujo = caja del balance |
| 4 | Semana 4 | Escenarios | Base, optimista y pesimista + estrés (cliente principal +30 días, ventas −20 %, sin renovación de línea), con acción disparadora (S6) | Celda selectora única; DSCR y cobertura por escenario |
| 5 | Desde el mes 2 | Repetición | Ritual del lunes: extractos → conciliar → real vs plan → avanzar la ventana → ajustar hipótesis → informe. Cierre mensual con `cfo-mensual-con-claude`. Revisión trimestral de supuestos | Error medido cada semana (S4); ritual < 45 min |

## 5. Correspondencia con la infografía
Creé proyecto = este hilo y su carpeta · Cargué contexto = fase 0 · Guardé instrucciones = fase 1 · Definí formato = fase 2 · Lo usé en un proceso real = fases 3–5 con cifras reales · **Sistema** = el ritual semanal con error medido.

## 6. Qué necesita el espejo para seguir (lo sube la PC o el usuario)
1. El modelo actual (Excel) y su ruta: es el archivo principal.
2. Extractos bancarios del último trimestre (se pueden anonimizar).
3. Antigüedad de cartera por cobrar y por pagar.
4. Valor de la caja mínima (S5) y respuesta a qué es Mobijuesa en el modelo (S7).
