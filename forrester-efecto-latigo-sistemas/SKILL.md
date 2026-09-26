---
name: forrester-efecto-latigo-sistemas
description: >-
  Diagnostica oscilaciones de inventario, producción y caja como EFECTO LÁTIGO
  (Jay Forrester, MIT — Beer Game): el problema es la estructura de retrasos e
  información, no las personas. Invocar ante brecha producción-ventas, inventario
  inmovilizado, crisis de caja recurrente o cuando el equipo busca un culpable.
trigger_phrases:
  - "efecto látigo"
  - "brecha entre producción y ventas"
  - "inventario inmovilizado"
  - "por qué se repite la crisis de caja"
  - "quién se equivocó en la compra"
  - "Beer Game"
idioma_de_salida: español
nivel_de_madurez: especializada
dominio: producción industrial / cadena de suministro
fuente:
  - "Jay W. Forrester (MIT Sloan), fundador de la Dinámica de Sistemas; «amplificación de la demanda» (1958, 1961) y el Beer Distribution Game (años 60)"
  - "Documentación pública: System Dynamics Society, beergame.org"
  - "Bookmark @fdc_ec: https://x.com/MentalidadFeroz/status/1876392112390090879"
  - "Material de estudio: E:\\vars\\var 5\\Clases-Magistrales-HTML\\05-forrester-beer-game-dinamica-sistemas.html"
---

## Acerca de mí (cargar al arrancar)
Leer `...\memory\user_role.md` + `MEMORY.md`. Se aplica sobre todo a
[[control-financiero-semanal-qvp]], [[comite-cuarto-guerra-qvp]] y
[[project_flujo_caja_bodegas_mobijuesa]].

## Doctrina central
> **La estructura genera el comportamiento.** Las oscilaciones de una cadena
> (inventario que sobra y luego falta, caja que se ahoga y luego respira) no
> vienen de la torpeza de nadie: vienen de **retrasos + bucles de
> retroalimentación + información local**.

El Beer Game lo demuestra: cuatro eslabones (minorista → mayorista → distribuidor
→ fábrica), prohibido comunicarse, objetivo minimizar el costo combinado de
inventario y quiebre de stock. Los jugadores **invariablemente** producen el
efecto látigo: la demanda del cliente final es casi plana y la fábrica ve
oscilaciones enormes. Forrester lo llamó **amplificación de la demanda**.

**Las 3 causas estructurales:** ① retrasos (de entrega **y de información**);
② bucles de retroalimentación; ③ cada eslabón ve solo el pedido del de abajo,
nunca la demanda real.

## Qué NO hacer / compuertas 🚦
- 🚦 **No buscar culpables.** «Compras se pasó», «ventas no avisó». Cambias a la
  persona y el patrón se repite idéntico. Es el error de diagnóstico más caro.
- 🚦 **No confundir el síntoma con la causa:** el inventario inmovilizado *es* el
  paso ⑤ del látigo, no una falla de criterio aislada.
- 🚦 **No prometer que desaparece:** el látigo se **amortigua**, no se elimina.
  Prometer estabilidad total es simular éxito.
- 🚦 **No aplicar a cadenas sin retraso ni realimentación** (servicios inmediatos
  sin inventario): ahí el modelo no explica nada.
- 🚦 Este marco explica **estructura**, no fraude ni robo. Si hay faltantes sin
  explicación estructural, es materia de [[project_erp_antirobo_qvp]], no de aquí.

## Protocolo de diagnóstico
> **Tómate tu tiempo. Calidad antes que velocidad. No saltes pasos.**
1. **Dibuja la cadena** con sus eslabones reales (QVP: compra de fruta →
   extractora → refinería → ventas). El dibujo *es* la representación que expone
   la restricción ([[winston-representacion-restricciones-ia]]).
2. **Mide el retraso** de cada tramo: días entre decisión y efecto, y —clave—
   **días entre el hecho y el dato**.
3. **Pregunta quién ve la demanda final.** Si solo ventas la ve, ya encontraste
   la causa ③.
4. **Grafica la oscilación** por eslabón. Si la amplitud crece aguas arriba,
   es látigo confirmado.
5. **Aplica las 4 contramedidas** (abajo) y vuelve a medir en semanas, no en meses.

## Las 4 contramedidas
| Causa | Contramedida |
|---|---|
| Nadie ve la demanda real | **Compartir la demanda del punto final** con toda la cadena (la más potente) |
| Retrasos largos | Acortar tiempos de entrega y **de información** |
| Pedidos en lote | Pedir **más seguido y en menor cantidad** |
| Pánico y sobre-pedido | **Reglas explícitas** de reposición (punto de pedido, stock de seguridad) |

## Cómo depurar si falla
Si tras compartir la demanda el patrón sigue, revisa el **retraso de información**
(a menudo el dato existe pero llega tarde al que decide) y el tamaño de lote.

## Portabilidad (revisar el 20% al reusar)
Cambian los eslabones y los tiempos por industria. El mecanismo es universal:
sirve igual para palma, cemento, inmobiliario o inventario de bodegas.

## Reuso (no empezar de cero)
[[control-financiero-semanal-qvp]] (medición semanal),
[[comite-cuarto-guerra-qvp]] (dónde se discute),
[[memoria-financiera-inteligenciada]] (efecto en caja),
[[winston-representacion-restricciones-ia]] (el diagrama como representación).

## Ejemplos de invocación
- «¿Por qué otra vez tenemos exceso de inventario y crisis de caja?»
- «El comité quiere culpar a compras: dame la lectura sistémica.»
- «Diagrama la cadena de QVP y dime dónde está el látigo.»
