---
name: diagnostico-reparacion-windows-rendimiento
description: |
  Diagnostica y repara CAÍDAS DE APLICACIONES y LENTITUD en este
  Windows 11 (Dell, i7-1255U, 32 GB RAM). Ordena el diagnóstico de modo
  que primero DESCARTA hardware, luego mide MEMORIA VIRTUAL, y solo
  después culpa al software — al revés de como suele hacerse.

  Hallazgo fundacional (2026-07-27): el equipo tenía el **ARCHIVO DE
  PAGINACIÓN COMPLETAMENTE DESACTIVADO** (`pagefile.sys` inexistente,
  `AutomaticManagedPagefile=False`, límite de confirmación idéntico a la
  RAM física = margen 0). Con 0 de margen, cualquier pico de memoria no
  se pagina: **falla la reserva y la aplicación MUERE en el acto**.
  Firma inconfundible: `msedge.exe` con excepción **`e0000008`** (en
  Chromium = «sin memoria») mientras el Administrador de tareas todavía
  muestra RAM libre, y **cero** pantallazos azules.

  Incluye `diagnostico_sistema.ps1` (sin elevación) y
  `REPARAR_ADMIN.bat` (un clic, elevado) que reactiva la paginación,
  pone los emuladores en Manual y purga la cola de impresión.

trigger_phrases:
  - "el computador está lento / se cae todo"
  - "se cierra solo Edge / Claude / NotebookLM / YouTube"
  - "no se cargan los archivos en pantalla"
  - "parece que no alcanza la memoria"
  - "diagnostica el sistema / revisa la computadora"
  - "unknown software exception"

idioma_de_salida: español
nivel: aplicada
dominio: operaciones / rendimiento de Windows
metadata:
  version: 1.0
  fecha: 2026-07-27
  equipo: Dell · i7-1255U (10 núcleos / 12 hilos) · 31,7 GB RAM · Iris Xe · C: 930 GB
  scripts:
    - scripts/diagnostico_sistema.ps1
    - scripts/REPARAR_ADMIN.bat (+ .ps1)
  relacionada:
    - agente-gui-autoaprobado-windows
    - impresion-local-hp-diagnostico
    - ui-tars-desktop-control-local
---

# Skill `diagnostico-reparacion-windows-rendimiento`

## Resultado verificado del caso fundacional (2026-07-27)

| Indicador | Antes | Después |
|---|---|---|
| Archivo de paginación | **inexistente** | `C:\pagefile.sys` activo, gestionado |
| Límite de confirmación | 31,69 GB | **33,69 GB** |
| **Margen virtual** | **0 GB** | **2 GB (y crece bajo demanda)** |
| **Memory Compression** | **702 MB** | **0 MB** |
| RAM libre (recién arrancado) | 11 GB | **20,6 GB** |
| Entradas de arranque (HKCU) | 12 | **0** |
| Servicios WSA | Automático | Manual (detenidos) |

La caída de *Memory Compression* de 702 MB a **0** es la prueba más
limpia: Windows ya no necesita comprimir RAM a la desesperada porque
por fin tiene dónde paginar.

## Doctrina: el orden del diagnóstico

Ante «todo se cae y está lento», el instinto es culpar a la RAM o al
disco. **El orden correcto es otro**, porque separa causas que se
parecen mucho:

1. **¿Cae el NÚCLEO o caen las APLICACIONES?**
   `Kernel-Power 41` (apagón inesperado) y `BugCheck` (pantallazo azul).
   - **Ambos en 0** → el hardware y los drivers están bien. Deja de
     buscar RAM defectuosa: el problema es de software o de memoria
     virtual. *(Este fue el caso.)*
   - Alguno > 0 → sí hay sospecha de hardware: `mdsched` (memoria),
     temperatura, drivers.
2. **¿Hay MARGEN de memoria virtual?**
   `Límite de confirmación − RAM física`. Si da **0**, no hay archivo de
   paginación y el sistema está a un pico de distancia del fallo.
3. **¿QUÉ módulo falla exactamente?**
   Evento 1000 del registro Aplicación: da app + DLL culpable + código
   de excepción. Ahí se distingue «sin memoria» de «bug de un plugin».
4. **¿Qué carga permanente hay?** Arranque automático, emuladores, VMs.

## Tabla de códigos de excepción (lo que realmente significan)

| Código | Significado | Qué hacer |
|---|---|---|
| **`e0000008`** | **Sin memoria** (lo lanza Chromium/Edge al fallar una reserva) | Revisar paginación y commit. **No** es «Edge dañado» |
| `c0000005` | Violación de acceso | Bug del módulo nombrado (plugin, complemento, driver) |
| `c0000409` | Desborde de búfer de pila | Bug de la app; actualizarla |
| `c00001ad` | Sin recursos de gráficos/compositor (`dwm.exe`) | Presión de memoria o driver de video |

## 🚦 El error clásico que esta skill evita

> **«Hay RAM libre, así que no es memoria.»** FALSO.
> Windows no limita por RAM libre sino por el **límite de confirmación**
> (commit). Sin archivo de paginación, ese límite es la RAM física y
> **no hay válvula de escape**: cuando una app pide un bloque grande y
> el commit está cerca del tope, la reserva falla y el proceso muere —
> aunque el Administrador de tareas muestre gigas «libres».
> Señal de apoyo: el proceso **«Memory Compression»** crecido (Windows
> comprimiendo RAM porque no tiene disco donde paginar).

## Por qué NO se debe desactivar el archivo de paginación
Circula el consejo de «desactivar la paginación si tienes mucha RAM
para que vaya más rápido». Es **falso y dañino**:
- Windows usa el commit como contabilidad, no solo como respaldo.
- Sin él no se pueden generar volcados de fallo.
- Aplicaciones modernas (navegadores, Electron, Office, IA local)
  **reservan** mucha más memoria de la que tocan; sin paginación esas
  reservas fallan.
Lo correcto es **gestionado por el sistema** (Windows lo dimensiona y
solo ocupa disco cuando hace falta).

## Protocolo

> **Tómate tu tiempo. Calidad antes que velocidad.**

### 1. Diagnosticar (sin elevación)
```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\datos\.claude\skills\diagnostico-reparacion-windows-rendimiento\scripts\diagnostico_sistema.ps1"
```
Da los 5 bloques: memoria/commit · descarte de hardware · quién se cae y
por qué · carga permanente · disco.

### 2. Reparar (un clic, elevado)
`scripts\REPARAR_ADMIN.bat` → **clic derecho → Ejecutar como
administrador**. Reactiva la paginación gestionada, pone WSA/BlueStacks
en Manual y purga la cola de impresión. Deja `reparacion_log.txt`.
**Reiniciar** para que la paginación entre en vigor.

### 3. Aligerar el arranque (sin elevación)
Quitar de `HKCU:\...\CurrentVersion\Run` lo que no se use a diario
(emuladores, actualizadores). Guardar respaldo del valor antes.

## 🚦 Límite real: el UAC en escritorio seguro
En este equipo `PromptOnSecureDesktop=1`. **El escritorio seguro del UAC
NO es automatizable** — ni por computer-use, ni por UI-TARS, ni por
tarea programada (registrarla también exige elevación). No es una
limitación del agente: es una frontera de seguridad de Windows y
**no debe intentar sortearse**. Por eso las reparaciones elevadas se
empaquetan en **un solo .bat** para que el usuario dé **un único clic**.
Ver [[agente-gui-autoaprobado-windows]] (que sí cubre todo lo demás).

## Cómo depurar si falla
- **El .bat dice «no eres administrador»**: se abrió con doble clic;
  hay que usar clic derecho → Ejecutar como administrador.
- **Tras reiniciar el margen sigue en 0**: una directiva de grupo o una
  «app optimizadora» está desactivando la paginación de nuevo; revisar
  software de «limpieza/tuning» instalado.
- **Sigue cayéndose una app concreta**: mirar su módulo en el paso 3; si
  es un complemento (p. ej. `MsoAria.dll` de Office), actualizar o
  desactivar ese complemento — eso es un bug aparte, no memoria.

## Portabilidad (revisar el 20%)
Las rutas, el nombre de los servicios de emulador y los umbrales. La
doctrina (orden del diagnóstico, commit vs RAM libre, tabla de códigos)
es estable y aplica a cualquier Windows 10/11.

## Relacionado
- [[agente-gui-autoaprobado-windows]] — qué sí puedo automatizar por GUI.
- [[impresion-local-hp-diagnostico]] — la purga del spooler también vive aquí.
- [[selector-modelo-claude-optimo]] · [[eficiencia-generacion-respuestas]].

## Vecindad en la red

Skills de mantenimiento que dependen de esta y que antes no la citaban de vuelta:

- [[forense-cuelgues-y-caidas-windows]]
- [[saneamiento-complementos-office]]
- [[escanear-a-pdf-sin-dependencias]]

> Puente tendido el 9-sep-2026: este racimo estaba conectado entre sí pero desprendido del cuerpo principal ([[regla-del-primer-tropiezo]] §10).

## Política de actualizaciones: seguridad SÍ, drivers NO (27-sep-2026)

**La pregunta no es «¿actualizo o no?». Es «¿qué tipo de actualización?»** —
Windows las mezcla a propósito y tienen riesgos opuestos.

| Tipo | Qué hacer | Por qué |
|---|---|---|
| **Seguridad** (`KB` + «Security Update») | **Siempre, sin excepción** | Tapan agujeros que ya se explotan. Desactivarlas no ahorra latencia: abre la puerta |
| **Drivers por Windows Update** | **Excluir** | Microsoft sirve versiones genéricas, a veces MÁS VIEJAS que las instaladas, y pisan lo que ya funciona |
| **Funciones** (saltos de versión anuales) | **Diferir semanas**, no rechazar | Los fallos gordos salen los primeros días |

### La prueba de que los drivers de WU son un retroceso
En este Dell Inspiron 15 3520, Windows Update ofrecía un driver del monitor LG
cuyo propio detalle decía **«released in March, 2016»** — diez años de atraso
sobre el genérico que ya funcionaba. Junto a él, un Intel Display de 525 MB que
tocaría justo el monitor principal (ver `feedback_monitor_primario_apagado`).

### El ajuste quirúrgico
`scripts/` no lo lleva; el script vive en el scratchpad de la sesión
(`drivers_fuera_de_wu.ps1`, con `-Revertir` y respaldo en JSON). Son dos valores,
ambos en HKLM y ambos con administrador:

| Llave | Valor | Efecto |
|---|---|---|
| `…\Policies\Microsoft\Windows\WindowsUpdate` → `ExcludeWUDriversInQualityUpdate` | `1` | Los drivers no viajan en las actualizaciones de calidad |
| `…\CurrentVersion\DriverSearching` → `SearchOrderConfig` | `0` | No buscar drivers en Windows Update |

🚦 **`ExcludeWUDriversInQualityUpdate` es directiva de Windows Update for
Business y esta máquina es Windows 11 HOME, que a veces las ignora.** La que sí
funciona con seguridad en Home es `SearchOrderConfig = 0`. No dar por hecho el
efecto de la primera: la prueba es de comportamiento, con el tiempo.

### Cómo comprobar el estado sin instalar nada
La búsqueda por COM es de solo lectura y separa los dos canales:

```powershell
$sr = (New-Object -ComObject Microsoft.Update.Session).CreateUpdateSearcher()
$sr.Search("IsInstalled=0 and IsHidden=0 and Type='Software'").Updates.Count  # seguridad
$sr.Search("IsInstalled=0 and IsHidden=0 and Type='Driver'").Updates.Count    # drivers
```

Mirar además `AutoSelectOnWebSites` e `IsMandatory` de cada uno: si ambos son
`False`, ese driver **es opcional** y Windows no lo iba a instalar solo. El
riesgo real entonces no es Windows, es pulsar «instalar todo» en la ventana.

### Contrapartida que hay que decirle al usuario
Al cortar esta vía, **revisar Dell SupportAssist o Intel DSA una o dos veces al
año pasa a ser tarea suya**. El olvido es el riesgo de esta opción, y hay que
nombrarlo al recomendarla.

Relacionado: [[forense-cuelgues-y-caidas-windows]] ·
`feedback_monitor_primario_apagado` · `feedback_camara_bloqueada_es_camara_virtual`.

## Geometría de pantallas: la trampa del DPI (15-oct-2026)

🚦 **Antes de «corregir» la posición de un monitor, comprobar en qué unidades se
está midiendo.** Medir mal aquí inventa problemas que no existen.

En esta máquina el panel interno va al **125%**: mide 1920 × 1080 físicos pero
un proceso **no consciente del DPI** lo lee como **1536 × 864**. En cambio la
posición del segundo monitor (`X=1920`) viene en píxeles **físicos**. Comparar
ambas cifras produjo un «hueco de 384 píxeles» **que no existía**: las dos
pantallas estaban pegadas.

### La vía que sí mide bien
No hace falta marshalar `DEVMODE` ni `QueryDisplayConfig` — ambos fallaron aquí
(salida vacía, nombres en blanco, `outputTechnology` absurdo). Basta **hacer el
proceso consciente del DPI** y releer `Screen.AllScreens`:

```powershell
Add-Type -TypeDefinition @"
using System; using System.Runtime.InteropServices;
public class Dpi { [DllImport("user32.dll")]
  public static extern bool SetProcessDpiAwarenessContext(IntPtr v); }
"@ -Language CSharp
[Dpi]::SetProcessDpiAwarenessContext([IntPtr](-4))   # PER_MONITOR_AWARE_V2
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Screen]::AllScreens | ForEach-Object { $_.DeviceName; $_.Bounds }
```

**Compuerta barata:** si el panel interno vuelve con su resolución nativa
(1920 × 1080 aquí, no 1536 × 864), la conciencia de DPI funcionó y las cifras ya
son comparables. Si no, no sirve seguir.

### Hueco, solapamiento y desfase
Con las cifras físicas: `hueco = X(derecha) − (X(izquierda) + ancho(izquierda))`.
Cero = pegadas. Y alinear por arriba (`Y=0` en ambas) con pantallas de distinta
altura deja un **borde invisible en el tercio inferior** de la más alta; para
centrar, `Y = (alto_mayor − alto_menor) / 2`.

### Brillo
Solo el **panel interno** expone `WmiMonitorBrightnessMethods`. Los externos
necesitan sus botones o DDC/CI. Fijarlo:

```powershell
$m = Get-CimInstance -Namespace 'root\wmi' -ClassName WmiMonitorBrightnessMethods
Invoke-CimMethod -InputObject $m -MethodName WmiSetBrightness -Arguments @{Timeout=0; Brightness=[byte]30}
```

Relacionado: `feedback_monitor_primario_apagado` — 🚦 esa nota dice que el LG era
la principal desde julio; **al 15-oct-2026 la principal es el panel interno**.

## Latencia de arranque: cuente las entradas de `Run` ANTES de culparlas (07-nov-2026)

🚦 **Si las entradas de arranque son dos y las aplicaciones que se abren son treinta,
el problema no está en las entradas: está en UN interruptor.**

### El caso
Francisco pidió corregir la latencia de arranque. `HKCU\…\Run` tenía **2 valores**
(Claude y Edge). El tren real de inicio de sesión, reconstruido desde los procesos
vivos, traía **unas 30 aplicaciones a lo largo de 5 min 43 s**: Fathom, Read AI,
BlueStacks, Claude, WhatsApp, Chrome, LinkedIn, Copilot, ChatGPT, Codex, Photoshop
Express, Edge con su sesión… Buscar treinta configuraciones habría sido el error.

**El culpable es `RestartApps`:** «Reiniciar automáticamente las aplicaciones
reiniciables al volver a iniciar sesión». **Cuando el valor NO existe, Windows 11
reabre igual** — el valor ausente no significa apagado. Un solo DWORD:

```powershell
Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced' `
  -Name RestartApps -Value 0 -Type DWord
```

### Cómo reconstruir el tren de arranque sin ser administrador
El registro `Diagnostics-Performance` (eventos 100 y 101-110, lo que lee el
Administrador de tareas para su columna «Impacto de inicio») **exige elevación**:
sin ella da `UnauthorizedAccessException` y `wevtutil` responde «Acceso denegado».
La vía sin elevación: **los procesos vivos conservan su hora de creación**.

```powershell
$boot = (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
$logon = (Get-CimInstance Win32_Process -Filter "Name='explorer.exe'" |
          Sort-Object CreationDate | Select-Object -First 1).CreationDate
Get-CimInstance Win32_Process | Where-Object { $_.CreationDate -ge $logon -and $_.CreationDate -le $logon.AddMinutes(6) } |
  Sort-Object CreationDate | ForEach-Object {
    "+{0,4}s {1,5} MB  {2}" -f [int](($_.CreationDate-$logon).TotalSeconds), [int]($_.WorkingSetSize/1MB), $_.Name }
```

🚦 **Separe arranque de inicio de sesión.** Medir desde `LastBootUpTime` solo da el
tramo del núcleo; si el usuario inició sesión horas después, el tren que él *siente*
cuelga de `explorer.exe`, no del arranque. Aquí `explorer.exe` arrancó **+167 352 s**
tras el arranque: dos tramos distintos que no deben mezclarse.

### Las apps de la Tienda no están en `Run`
Catorce de ellas tenían **tarea de inicio propia**, invisible a `Win32_StartupCommand`:

```powershell
reg query "HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppModel\SystemAppData" /s /v State
```

Mapa de `State` **verificado por comportamiento** en esta máquina (no por documentación,
que circula contradictoria): **`0` = no arranca · `1` = activada por el usuario ·
`2` = activada por omisión**. La comprobación barata: `YourPhone=1` y `CrossDevice=1`
sí arrancaron; `Todos=0`, `WindowsTerminal=0` y `Xbox=0` no. Poner `0` apaga, y si el
mapa estuviera mal el peor caso es que siga arrancando: nada se rompe.

🚦 **`Win32_StartupCommand` miente por exceso:** listó 12 entradas en el hive del
usuario donde `reg query` mostraba 2. Arrastra residuos de `StartupApproved`. La
lectura autorizada es `reg query` sobre la clave `Run`.

### Lo que de verdad pesa en el arranque del equipo
A los **+107 s** entraron de golpe **14 procesos de Dell** (TechHub, Optimizer,
Instrumentation, Analytics, DataManager, CoreServices, UCA, Titan, Customer Connect…)
sumando **1,2 GB** y una tormenta de disco. Son telemetría y actualización: a **Manual**
se siguen pudiendo abrir a mano. Mismo tratamiento para McAfee WebAdvisor, Adobe ARM,
Autodesk, FlexNet, Wondershare, HP Print Scan Doctor, EShare y Prezi.

### Lo que NO se toca, y por qué
| Pieza | Razón |
|---|---|
| **Waves MaxxAudio** (`WavesSysSvc64`, 230 MB) | Es el APO de audio del Dell. El audio ya costó una sesión entera (`feedback_audio_dispositivos_predeterminados`) |
| Intel, Realtek | Mismo riesgo sobre audio y vídeo |
| Defender | Seguridad |
| `Office Automatic Updates 2.0` | Lleva los parches; se apagan solo sus hermanas de *logon* |
| Servicio **AnyDesk** | Acceso remoto desde el iPad. Se retira solo el acceso directo del Inicio; el servicio queda |
| **KMSpico** | Apagarlo puede desactivar Windows u Office. Se **informa**, no se decide |

### Guion y reversión
`C:\Users\datos\Downloads\ARRANQUE_filo_de_navaja_USUARIO.ps1` (sin elevación, con
`-Revertir`) y `ARRANQUE_filo_de_navaja_ADMIN.bat` + `REVERTIR_ARRANQUE_ADMIN.bat`
(un clic, respaldo en JSON, `-SoloInforme` para medir sin cambiar nada).

Relacionado: [[forense-cuelgues-y-caidas-windows]] · `feedback_audio_dispositivos_predeterminados`.

## «Se agotó el tiempo de espera del semáforo»: mire la energía, no el disco (07-nov-2026)

El Explorador falló al abrir `E:\vars\var 8\1 Urb San Sebastian\Legal SS` con
**«Ubicación no disponible — Se agotó el tiempo de espera del semáforo»**.
Ese texto es `ERROR_SEM_TIMEOUT` (121): **una petición de E/S al dispositivo
venció**. No dice «disco dañado»; dice «el dispositivo no contestó a tiempo».

### El mecanismo que transfiere

**Un disco mecánico USB que Windows apaga cada 30 segundos se desconecta del
bus al despertar.** El puente USB-SATA no aguanta el arranque del motor dentro
del plazo de E/S, devuelve timeout y Windows lo retira. Vuelve solo en segundos.

La prueba más limpia de que era eso y no avería: **`Get-Disk` lo vio una vez y
no la siguiente, con un minuto entre consultas.** Ante esta sospecha, consulte
`Get-Disk` dos veces separadas; un disco que aparece y desaparece no está roto,
está durmiendo.

### Los tres ajustes que se acumulan

| Ajuste | Valor hallado | Default de Windows | Qué aporta al desastre |
|---|---|---|---|
| `SUB_DISK / DISKIDLE` | **30 s** (CA y CC) | 1200 s (20 min) | **La causa.** El motor para y rearranca sin parar |
| Suspensión selectiva USB | Habilitado | Habilitado | El puerto también duerme; refuerza la anterior |
| `UserWriteCacheSetting` | **1** (activada) | 0 en discos externos | Convierte la desconexión en **pérdida de datos** |

Los dos primeros se corrigen **sin elevación**; el tercero y los concentradores
exigen administrador.

```powershell
$g=[regex]::Match((powercfg /getactivescheme|Out-String),'([0-9a-fA-F-]{36})').Value
powercfg /setacvalueindex $g SUB_DISK DISKIDLE 0
powercfg /setdcvalueindex $g SUB_DISK DISKIDLE 0
powercfg /setacvalueindex $g 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0
powercfg /setdcvalueindex $g 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0
powercfg /setactive SCHEME_CURRENT
```

🚦 **El GUID de la suspensión selectiva que circula en la red está mal.** No
use `48e6b7a6-50f5-4782-9c41-9a4e3f5ad3cf`: `powercfg` responde «Parámetros no
válidos». Léalo de la máquina con
`powercfg /query $g 2a737441-1930-4402-8d77-b2bebba308a3`.

### Cómo leer el daño

`Ntfs` **evento 50** = «Error en la escritura demorada». Aquí salieron **56, todos
en el mismo segundo**: una sola caída vaciando la caché sucia. Agrupe por marca
de tiempo — muchos eventos en un instante son **una** desconexión, no 56 fallos.

Lo decisivo es **qué NO aparece**: cero eventos de `disk` (Id 7 bloque dañado,
Id 11 error de controladora) y cero de `storahci`. Un disco que muere los
produce. Su ausencia descarta la avería de medio y deja la energía.

```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; StartTime=(Get-Date).AddHours(-12)} |
  Where-Object { $_.ProviderName -match 'disk|Ntfs|storahci|USBSTOR|volmgr|Kernel-PnP|usbhub' }
```

### La comprobación barata que cierra el caso

Si vuelve a caerse **con el apagado del disco ya desactivado**, entonces sí es
hardware: cable, puerto o caja. Esa es la línea divisoria, y se formula antes
de tocar nada.

### Herramientas dejadas

- `C:\Users\datos\Downloads\REPARAR_DISCO_USB_ADMIN.bat` — caché de escritura a
  «extracción rápida», concentradores USB sin apagado automático y `chkdsk /scan`
  de solo lectura en D: y E:. Revertir: `REVERTIR_DISCO_USB_ADMIN.bat`.
- Respaldos: `respaldo_energia_disco_usb.json` (usuario) y
  `respaldo_disco_usb_sistema.json` (sistema).

## Un divisor HDMI NUNCA extiende (15-oct-2026)

🚦 **Si dos monitores externos muestran lo mismo y no hay forma de extenderlos,
mirar el CABLE antes que la configuración.** Aquí se perdió tiempo buscando un
ajuste de Windows para un problema que era físico.

**El caso:** Francisco tenía un `HDTV SPLITTER 1x4 3D 4Kx2K` entre el portátil y
dos monitores. Un divisor toma **una** señal y la **copia** a varias salidas: es
su función, no un defecto. Windows veía dos pantallas (portátil + «un externo»)
aunque físicamente hubiera tres.

### Los tres delatores, en orden de coste
1. **Varios EDID con la MISMA instancia.** Decisivo y barato:
   ```powershell
   Get-ChildItem 'HKLM:\SYSTEM\CurrentControlSet\Enum\DISPLAY' | ForEach-Object {
     $e=$_.PSChildName; Get-ChildItem $_.PSPath | ForEach-Object { "$e  $($_.PSChildName)" } }
   ```
   Aquí `GSM5ACD`, `LRX2281` y `MAC0101` compartían `4&3b88f39d&0&UID4145`:
   **tres monitores recordados en UNA sola salida**.
2. **`DisplaySwitch.exe /extend` y volver a contar.** Si siguen siendo las
   mismas pantallas, Windows ya extendía y el problema no es suyo.
3. **La foto del escritorio.** Dos pantallas con contenido idéntico y la tercera
   distinta = la pareja cuelga del divisor.

### Qué SÍ crea una segunda salida
- **Adaptador DisplayLink** (USB-A 3.0 a HDMI) + su software. La vía fiable
  cuando solo hay un HDMI. Exigir la marca DisplayLink: los «USB a HDMI»
  genéricos suelen ser capturadoras. Comprime el vídeo: bien para ofimática,
  mal para vídeo a pantalla completa.
- **USB-C con DisplayPort alt mode** + cable directo. 🚦 **Que no haya
  Thunderbolt NO prueba que no haya vídeo** — son cosas distintas, y deducirlo
  así es un error. Se confirma por el logotipo DP junto al puerto, o probando.

### Vías que se comprobaron CERRADAS en esta máquina
`EShare` solo tiene componentes de audio y cámara, sin vídeo; no hay ningún
adaptador de pantalla virtual; y un único adaptador real (Intel Iris Xe).

### Capturadora ≠ adaptador de pantalla (26-oct-2026)

🚦 **Segundo tropiezo del mismo caso: se compró una CAPTURADORA USB-HDMI
creyendo que ampliaría la pantalla.** Van en sentidos opuestos y por fuera son
idénticas: un pincho con USB de un lado y HDMI del otro.

| | Capturadora | Adaptador DisplayLink |
|---|---|---|
| Dirección | HDMI **entra** al PC | PC **sale** al HDMI |
| Se registra como | **clase `Camera`** (`USB2 Video`) + `USB2 Digital Audio` | **adaptador de pantalla** nuevo |
| En la caja | *capture*, *grabber*, *OBS*, *streaming* | la palabra **`DisplayLink`** |
| Precio | 8 a 15 USD | 30 a 60 USD |
| Instalación | enchufar y listo (UVC) | **exige controlador** de displaylink.com |

**El diagnóstico en un comando:** si el aparato aparece bajo `-Class Camera` y
`Get-PnpDevice -Class Display` sigue mostrando un solo adaptador, es
capturadora.

```powershell
Get-PnpDevice -Class Camera -Status OK | Select-Object FriendlyName
Get-PnpDevice -Class Display | Select-Object Status, FriendlyName
```

**Al recomendar la compra, no basta con decir «adaptador USB a HDMI»:** hay que
exigir la palabra `DisplayLink` y avisar de que el precio bajo delata la
capturadora. Decirlo de pasada no evitó el error.

🚦 Efecto colateral que confundió más: al desenchufar el HDMI para probar la
capturadora, el recuento de pantallas bajó de 2 a 1. Antes de diagnosticar nada,
confirmar qué sigue conectado.
