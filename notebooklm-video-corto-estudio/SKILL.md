---
name: notebooklm-video-corto-estudio
description: >
  Selecciona correctamente la opción de VIDEO CORTO en el Estudio de NotebookLM
  (KLM IA / Gemini Notebook), distinguiéndola de las opciones que se le parecen
  y con las que suele confundirse: el video "Explicación" (largo) y la
  "Presentación de diapositivas" (que NO es video). Cubre la vía CLI
  (notebooklm-py) —que es la confiable— y la vía GUI manual / UI-TARS cuando hay
  que hacerlo a mano sobre la pantalla. Regla del usuario (grabada en video
  2026-08-22): el video corto se alcanza por la opción de ARRIBA-IZQUIERDA del
  Estudio (Descripción general del vídeo) y luego el formato "Corto"; NO por la
  opción de ARRIBA-DERECHA ("Presentación de…", diapositivas). Invocar ante:
  "genera el video corto en notebooklm", "elige la opción Corto", "video corto y
  no explicación", "no confundas el video con la presentación", "usa UI-TARS para
  el video corto", "descripción general del vídeo corto".
metadata:
  type: reference
---

# NotebookLM — Selección de la opción de VIDEO CORTO en el Estudio

## 0. El problema (limitaciones primero)

En el panel **Estudio** de NotebookLM hay varias opciones con ícono parecido a
"video/pantalla" y es fácil equivocarse. Hay que distinguir TRES cosas:

| Se ve parecido | Qué es en realidad | ¿Es el video corto? |
|---|---|---|
| **Descripción general del vídeo → formato "Corto"** | Video breve (≈ visión general breve de las fuentes) | ✅ SÍ — esto es lo que se pide |
| **Descripción general del vídeo → formato "Explicación"** | Video largo, estructurado y completo | ❌ No (es el video LARGO) |
| **"Presentación de…" (BETA), arriba-derecha** | Diapositivas / slide deck, NO es video | ❌ No (es presentación, no video) |

Regla espacial del usuario (del video grabado 2026-08-22): **entra por la opción
de ARRIBA-IZQUIERDA** del Estudio (la del vídeo), **no por la de ARRIBA-DERECHA**
("Presentación de…"). Luego, dentro del diálogo, elige **"Corto"**.

> Referencias visuales en `referencias/`:
> - `estudio-cuadricula-opciones.png` — la cuadrícula del Estudio.
> - `formato-video-explicacion-vs-corto.png` — el diálogo con **Explicación (izq.)**
>   vs **Corto ¡Nuevo! (der., seleccionado ✓)**.

## 1. Regla de oro

**"Video corto" = Descripción general del vídeo, formato «Corto»** (¡Nuevo!),
descrito como *"Una visión general breve para ayudarte a captar rápidamente las
ideas clave de tus fuentes"*.

NO es "Explicación" (*"visión general estructurada y completa"*) ni la
"Presentación de diapositivas".

## 2. Vía CLI — la confiable (usar siempre que se pueda)

La CLI `notebooklm-py` elige el formato sin tocar la pantalla:

```bash
NLM="$HOME/.notebooklm-venv/Scripts/notebooklm.exe"
# VIDEO CORTO:
"$NLM" --profile "<perfil>" generate video "<instrucción>" --format brief --language es
# VIDEO LARGO (Explicación):
"$NLM" --profile "<perfil>" generate video "<instrucción>" --format explainer --language es
```

Mapa de equivalencias (UI ↔ CLI):

| UI (diálogo "Personalizar visión general del vídeo") | CLI `--format` |
|---|---|
| **Corto** (¡Nuevo!, visión breve) | `brief`  ← **video corto** |
| **Explicación** (estructurada y completa) | `explainer` |
| Presentación de diapositivas | *(no es video)* `generate slide-deck` |

Idioma: añadir `--language es` y, en la instrucción, exigir explícitamente
**"video en ESPAÑOL: voz y texto"**.

## 3. Vía GUI manual / UI-TARS (cuando hay que hacerlo sobre la pantalla)

Usar cuando el CLI no aplica (p. ej. verificación visual, o el usuario pide
hacerlo en la interfaz). Delegar el control del ratón/teclado a
[[ui-tars-desktop-control-local]] / [[agente-gui-autoaprobado-windows]] con esta
instrucción precisa:

1. En el cuaderno abierto, ir al panel **Estudio** (derecha).
2. Hacer clic en la opción de **ARRIBA-IZQUIERDA**: **"Descripción general del
   vídeo"** (ícono de pantalla con ▷). **NO** hacer clic en la de arriba-derecha
   **"Presentación de…"** (BETA) — esa es diapositivas.
3. Se abre el diálogo **"Personalizar visión general del vídeo"**.
4. En **Formato**, seleccionar la tarjeta **"Corto"** (la que dice *¡Nuevo!* y
   *"Una visión general breve…"*). Debe quedar con el ✓. **No** elegir
   "Explicación".
5. (Opcional) Definir **Fuentes**, el foco (*"¿En qué debería centrarse el
   vídeo?"*) y el **Tema personalizado** (pegar la indicación destilada, en
   español).
6. Clic en **"Generar"**.

Instrucción lista para UI-TARS (copiar/pegar):

> "En NotebookLM, panel Estudio: haz clic en la opción de arriba a la IZQUIERDA
> 'Descripción general del vídeo' (NO la de arriba a la derecha 'Presentación
> de…'). En el diálogo 'Personalizar visión general del vídeo', en Formato elige
> la tarjeta 'Corto' (¡Nuevo!, visión breve), verifica el ✓, y pulsa Generar."

## 4. Elegir "la una o la otra" según se solicite

- Piden **"video corto"** → formato **Corto** / CLI `--format brief`. *(caso por defecto actual)*
- Piden **"video explicativo / largo / completo"** → **Explicación** / `--format explainer`.
- Piden **"presentación / diapositivas"** → NO es video: `generate slide-deck`
  (o la tarjeta "Presentación de…").

Ante duda, preguntar; si no hay a quién preguntar, **por defecto: video corto**
(es lo que la FBSE usa para las publicaciones de LinkedIn).

## 5. Verificación

- CLI: la respuesta imprime `Started: <id>`; confirmar en `artifact list` que el
  artefacto es tipo **Video** y luego `--format brief` fue el usado.
- GUI: el título del diálogo debe decir **"…del vídeo"** y la tarjeta marcada
  debe ser **"Corto"**. Si dice "Explicación" o el diálogo es de diapositivas,
  está mal: cancelar y reintentar por la opción correcta.

## 6. Notas de contexto

- Cuota free de video: **por cuenta, ~5/día** (no por cuaderno). Para más videos
  el mismo día, usar otra cuenta (p. ej. jjmobijuesa vía captura CDP). Ver la
  memoria del proyecto EcuaLedger.
- Esta skill nació de un video de pantalla del usuario (2026-08-22) que mostró
  explícitamente cómo elegir "Corto" y evitar la opción de la derecha.
- Relacionadas: [[ui-tars-desktop-control-local]], [[agente-gui-autoaprobado-windows]],
  [[eficiencia-generacion-respuestas]].
