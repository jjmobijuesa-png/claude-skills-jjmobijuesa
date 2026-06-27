---
name: presentacion-prezi-qvp
description: |
  Convierte el análisis financiero y la estrategia de Quevepalma (memoria financiera transversal,
  tablero de cumplimiento, mapa Estrategia 2.0) en una PRESENTACIÓN tipo Prezi, generando el
  PROMPT estructurado listo para pegar en Prezi AI y el guion de láminas. Pensada para el comité,
  la Gerencia (Ing. Sebastián Juez) y la Presidencia (Don Omar Juez).
  Triggers: "presentación prezi QVP", "prezi de la estrategia", "presentación del análisis
  financiero", "láminas para el comité", "prompt para Prezi IA", "presentación War Room".
user-invocable: true
metadata:
  version: 1.0
  fecha: 2026-06-13
  cuenta_prezi: jjmobijuesa@gmail.com
  relacionada: memoria-financiera-inteligenciada, control-financiero-semanal-qvp
---

# Skill `presentacion-prezi-qvp`

## Propósito
Producir el **insumo de contenido** para una presentación Prezi a partir del análisis ya hecho:
no diseña pixeles, **genera el prompt estructurado + el guion de láminas** que Prezi AI convierte
en presentación.

## Realidad de acceso (importante)
- La **extensión Claude-in-Chrome bloquea `prezi.com`** (igual que perplexity/x/linkedin); y Edge
  por computer-use es **solo-lectura**. Por eso **no se puede operar el dashboard de Prezi
  automáticamente** desde aquí.
- Vías válidas: (a) el usuario abre `https://prezi.com/dashboard/next/#/presentations` con
  `jjmobijuesa@gmail.com`, crea una presentación con **Prezi AI** y pega el prompt que genera esta
  skill; (b) usar la app de escritorio **Prezi**; (c) habilitar el dominio en la extensión si se
  desea automatizar a futuro.
- Precedente en Drive: doc "Prompt para Prezi IA: Presentación Didáctica" (formato probado).

## Fuentes de contenido (ya producidas)
- `Analisis\analisis-transversal-2009-2025.md` (serie 17 años, hallazgos).
- `Tableros\GRAFICOS TRANSVERSAL 2009-2025 QVP.png` (4 gráficos para insertar como imagen).
- `Tableros\TABLERO_CUMPLIMIENTO_QVP.html` (diagnóstico 2025 + bancabilidad).
- `Plan de Negocios 2-0\ESQUEMA ESTRATEGICO QUEVEPALMA 2.0.md` (mapa 0→10).
- `Analisis\integracion-informes-financieros-2025-2026.md` (margen mínimo / costo máximo).

## Estructura de láminas recomendada (guion)
1. Portada — "Quevepalma 2.0: de commodity de margen fino a valor agregado controlado".
2. El problema en un número — pérdida 2025 (−1,3 M); margen 2,2 % vs. equilibrio 3,6 %.
3. 17 años en una imagen — gráfico transversal (ventas, margen, utilidad, deuda).
4. Tres verdades — caja > utilidad; margen siempre fino; deuda quebró en 2019.
5. Dónde está el margen — refinados 1,66 % vs. valor agregado ~11 %.
6. La respuesta: Estrategia 2.0 — el mapa 0→10 (núcleo, integración, control, diversificación).
7. El control que lo sostiene — el War Room y la plantilla (margen mínimo, caja, bancabilidad).
8. Bancabilidad — qué corregir antes de pedir crédito (Deuda/EBITDA, cobertura, estructura).
9. Hoja de ruta — las 6 líneas de valor agregado (alimentos, desinfectantes, mantecas, envasados).
10. Cierre — "utilidad = rentabilidad; caja = supervivencia".

## Prompt listo para Prezi AI (plantilla)
> Crea una presentación ejecutiva y didáctica titulada **"QUEVEPALMA 2.0 — Memoria financiera y
> nueva estrategia"** para el comité directivo de una industria oleoquímica. Tono: profesional,
> sobrio, basado en datos. Estructura en 10 secciones: (1) portada; (2) el problema: en 2025 la
> empresa perdió USD 1,3 M con margen bruto de 2,2 %, cuando necesita 3,6 % para no perder;
> (3) trayectoria 2009–2025: creció 6× en ventas (18M→114M pico→94M) pero el margen fue siempre
> fino (~5 %); (4) tres verdades: la caja decide la supervivencia, no la utilidad; el margen nunca
> superó ~6 %; la deuda se disparó en 2019 (gastos financieros de 0,1–0,5 M a 1,2–2,0 M);
> (5) dónde está el margen: los refinados a granel dejan 1,66 % y los productos envasados/
> manufacturados ~11 %; (6) la estrategia 2.0 en un mapa: núcleo extractora-refinería, integración
> de palmistería y transporte, nuevo control financiero, y un nuevo plan de negocios que diversifica
> hacia valor agregado; (7) el control semanal (War Room) que sostiene el margen mínimo y la caja;
> (8) bancabilidad: corregir Deuda/EBITDA, cobertura de intereses y concentración de deuda corto
> plazo antes de pedir crédito; (9) las seis nuevas líneas: alimentos (animal/humano/aditivos),
> desinfectantes, mantecas y margarinas, y dos líneas de envasados; (10) cierre con la frase
> "utilidad = rentabilidad; caja = supervivencia". Usa gráficos de barras y líneas, paleta azul
> corporativa, y una lámina por sección.

## Flujo
1. Generar/actualizar el prompt y el guion con los números vigentes del análisis.
2. Exportar los gráficos PNG para insertarlos manualmente si Prezi AI no los genera.
3. El usuario pega el prompt en Prezi AI (cuenta jjmobijuesa) y ajusta el diseño.
