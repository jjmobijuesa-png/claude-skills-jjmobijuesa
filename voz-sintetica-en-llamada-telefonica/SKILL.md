---
name: voz-sintetica-en-llamada-telefonica
description: |
  Hace HABLAR a la computadora DENTRO de una llamada telefónica real.
  Claude no emite audio, pero sí puede: (1) sintetizar voz con el motor de
  Windows, incluida una voz MASCULINA en español que el sintetizador clásico
  de .NET no ve; (2) inyectarla en la llamada por un CABLE DE AUDIO VIRTUAL,
  sin eco y sin instalar nada; y (3) marcar el número desde Enlace Móvil
  (Phone Link) sobre el teléfono Infinix vinculado.

  El usuario dicta el texto; Claude marca, transfiere el audio al equipo y
  lo pronuncia. También sirve para cualquier app que tome micrófono (Meet,
  Teams, Zoom, WhatsApp Web): basta apuntar su micrófono al cable virtual.

  Incluye el conmutador de dispositivo de audio predeterminado POR ROL, que
  Windows no expone por línea de comandos.

trigger_phrases:
  - "haz que la computadora hable en la llamada"
  - "llama a X y dile ..."
  - "transmite este texto por teléfono"
  - "quiero que hables tú en la llamada"
  - "cambia el micrófono / el parlante predeterminado"
  - "pon voz masculina en español"
  - "devuélveme mi voz en la llamada"

idioma_de_salida: español
nivel: aplicada
dominio: audio de Windows / telefonía / síntesis de voz
metadata:
  version: 1.0
  fecha: 2026-08-30
  scripts:
    - scripts/audio_ruta.ps1
    - scripts/hablar.ps1
    - scripts/probar_cable.ps1
  relacionada:
    - diagnostico-reparacion-windows-rendimiento
    - percibir-y-hablarle-al-humano
    - voz-y-tono-usuario
---

# Skill `voz-sintetica-en-llamada-telefonica`

## Doctrina

Claude **no emite audio**. Pero el computador sí tiene voz, y Claude manda
sobre el computador. La frase correcta no es «no puedo hablar» sino
**«puedo hacer hablar a la máquina»** — con el texto que el usuario dicte,
la voz que elija y el momento que decida.

El problema nunca es generar la voz. Es la **cañería**: cómo se mete ese
audio dentro de la llamada. Hay dos vías y una es claramente superior:

| Vía | Nivel captado | Veredicto |
|---|---|---|
| Acústica (parlantes → micrófono real) | **4 / 100** | Sirve para una demostración; para una llamada real, no. La cancelación de eco de Windows está diseñada justamente para borrar del micrófono lo que suena en los parlantes, así que pelea en contra. |
| **Cable de audio virtual** | **88 / 100** | 22 veces más señal, sin eco. Es la vía. |

## Hallazgos verificados en este equipo (Dell Inspiron 15 3520)

### 1. Ya existe un cable de audio virtual instalado

No hace falta descargar VB-CABLE ni nada. La app **Palabra** dejó dos pares
de dispositivos virtuales, y uno de ellos es un cable limpio:

| Ruta | Nivel |
|---|---|
| `Speakers (PalabraMicrophone)` → `Microphone Array (PalabraMicrophone)` | **88 / 100** ✅ |
| `Speakers (PalabraSpeaker)` → `Microphone Array (PalabraSpeaker)` | 38 / 100 ✅ |
| Cruzado (Palabra Mic → Palabra Speaker) | 0 — son cables independientes |
| `EShare Audio` → `EShare Audio` | 0 — no es cable |

**Usar siempre el par `PalabraMicrophone`.**

### 2. La voz masculina en español está escondida

`System.Speech` (SAPI clásico) solo ve tres voces, y la única en español es
**Sabina**, femenina. La masculina —**Microsoft Raul, es-MX**— vive en la
rama **OneCore** del registro, invisible para SAPI.

Se alcanza con **WinRT** (`Windows.Media.SpeechSynthesis`), que es lo que
hace `hablar.ps1`. No hace falta tocar el registro ni ser administrador.

### 3. Enlace Móvil: dos trampas que cuestan media hora

- **La llamada se dispara con `Enter`, no con el botón verde.** Se puede
  hacer clic en el botón verde todas las veces que se quiera —incluso con
  estado de hover confirmado— y no pasa absolutamente nada. Se escribe el
  número en el teclado numérico y se pulsa `Enter`.
- **El audio arranca en el teléfono.** Tras marcar, el panel dice
  *«Llamada en un dispositivo móvil»*. Hay que pulsar **«Transferir al
  equipo»**. Cuando el panel pase a decir *«Llamar desde la PC»* y aparezca
  un cronómetro, la llamada está contestada y el audio está en la PC.
- El campo «Búsqueda de contactos» **no toma el foco del teclado**: todo lo
  que se escribe cae en el teclado numérico (escribir «Diana» produce
  `342-62`). Marcar por número, no por nombre.

### 4. Los roles de audio son tres, y ahí está la elegancia

Windows tiene tres roles independientes: **Console**, **Multimedia** y
**Communications**. Eso permite el reparto que hace funcionar todo:

| Rol | Apunta a | Para qué |
|---|---|---|
| Salida Console + Multimedia | `Speakers (PalabraMicrophone)` | Por ahí sale **la voz sintética**, hacia el cable |
| Salida Communications | parlantes reales | Por ahí **el usuario oye al interlocutor** |
| Entrada (los tres roles) | `Microphone Array (PalabraMicrophone)` | La llamada **escucha el cable** |

⚠️ Con ese reparto, **si el usuario habla, el interlocutor NO lo oye**: el
micrófono de la llamada es el cable. Hay que avisárselo siempre, y tener a
mano el comando para devolverle su voz.

## Procedimiento completo

```powershell
$S = "$env:USERPROFILE\.claude\skills\voz-sintetica-en-llamada-telefonica\scripts"
```

**1 · Comprobar que el teléfono está enlazado por Bluetooth.**
Las llamadas viajan por Bluetooth, no por Wi-Fi. Enlace Móvil puede decir
«Conectado» (Wi-Fi) y aun así no poder llamar. Verificar con el listado de
dispositivos: el Infinix debe salir `Conectado: True`. Si el aparato lleva
días sin aparecer, su Bluetooth está apagado — eso solo lo arregla el
usuario en el teléfono.

**2 · Liberar el canal de voz.** Un parlante Bluetooth conectado bloquea la
llamada (*«No se admiten llamadas con auriculares Bluetooth»*). Reiniciar la
radio por WinRT lo suelta sin administrador. Ojo: los parlantes se
reconectan solos y vuelven a apoderarse de la salida predeterminada —
reverificar el enrutamiento justo antes de marcar.

**3 · Enrutar el audio.**

```powershell
& powershell -File "$S\audio_ruta.ps1" -Fijar "Speakers (PalabraMicrophone)"        -Flujo Render  -Rol Console
& powershell -File "$S\audio_ruta.ps1" -Fijar "Speakers (PalabraMicrophone)"        -Flujo Render  -Rol Multimedia
& powershell -File "$S\audio_ruta.ps1" -Fijar "Speakers (Cirrus Logic"              -Flujo Render  -Rol Communications
& powershell -File "$S\audio_ruta.ps1" -Fijar "Microphone Array (PalabraMicrophone)" -Flujo Capture -Rol Todos
```

**4 · Preparar la voz.**

```powershell
& "$S\hablar.ps1" -Voz "Raul" -GuardarEn "$env:TEMP\mensaje.wav" -NoReproducir -Texto "..."
```

**5 · Marcar.** Enlace Móvil → pestaña Llamadas → clic en el título para dar
foco → escribir el número → **`Enter`** → **«Transferir al equipo»** →
esperar el cronómetro.

**6 · Transmitir**, ya con la llamada contestada:

```powershell
(New-Object System.Media.SoundPlayer "$env:TEMP\mensaje.wav").PlaySync()
```

**7 · Devolver la voz al usuario** cuando lo pida:

```powershell
& powershell -File "$S\audio_ruta.ps1" -Fijar "Digital Microphone" -Flujo Capture -Rol Todos
```

**8 · Restaurar al colgar.** Dejar salida y entrada en el hardware real.
No devolver ciegamente los valores previos si apuntaban a dispositivos
virtuales: eso es restituir una avería, no un estado.

## Las tres herramientas

| Script | Qué resuelve |
|---|---|
| **`audio_ruta.ps1`** | Lista y cambia el dispositivo predeterminado **por rol**, contra la interfaz COM `IPolicyConfig`. Windows no trae comando para esto, y aquí no hay `AudioDeviceCmdlets`, ni `nircmd`, ni `SoundVolumeView`. |
| **`hablar.ps1`** | Sintetiza con las voces **OneCore** vía WinRT (incluida **Raul**, masculina es-MX). Guarda WAV y reproduce. |
| **`probar_cable.ps1`** | Verifica si una salida virtual alimenta a una entrada, **abriendo una sesión de captura real**. |

## Tres trampas técnicas que costaron tiempo

1. **`IAudioMeterInformation` sobre una entrada devuelve 0** mientras no
   exista una sesión de captura activa. Un medidor así da falsos negativos
   en todos los cables. La solución es abrir una captura real —
   `SpeechRecognitionEngine.AudioLevel` sirve, y el idioma del reconocedor
   da igual porque solo se lee el nivel. **Siempre correr un control
   conocido** (parlantes reales → micrófono real) antes de creerle a un
   medidor.
2. **Toda interfaz COM que cruce el límite a PowerShell se degrada a
   `System.__ComObject`** y pierde sus métodos. Buscar el dispositivo,
   activar el medidor y hacer el bucle de medición tienen que vivir
   **dentro de C#**, devolviendo solo un valor simple.
3. **Dos scripts que declaren la misma CLSID colisionan** en una misma
   sesión de PowerShell: el segundo recibe el tipo del primero. Invocar
   `audio_ruta.ps1` como **proceso aparte**, nunca con `&` en la misma
   sesión que otro script con interop COM.

## Límite ético

La voz dirá lo que el usuario dicte, y es su llamada. Pero cuando el texto
afirme identidad ante un tercero, decirlo una vez, sin sermón, y seguir:
el interlocutor oye claramente que es una voz sintética. No inventar
contenido en boca del usuario; si hay silencio en la línea y no hay texto
dictado, transmitir a lo sumo un puente neutro («un momento, por favor»)
y pedir el texto.

## Vecindad en la red

Racimo de comunicación con humanos. Es el canal de voz de la casa; comparte doctrina de tono con la oratoria y con la lectura del interlocutor.

- [[percibir-y-hablarle-al-humano]]
- [[voz-y-tono-usuario]]
- [[neuro-oratoria-presentacion-persuasiva]]
- [[whatsapp-web-cdp-lectura-envio]]

> Enganchada a la red el 9-sep-2026, vuelta 1 de la espiral de [[regla-del-primer-tropiezo]] §10. Antes era huérfana: existía y la red no la alcanzaba.
