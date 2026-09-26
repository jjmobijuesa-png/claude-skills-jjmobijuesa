---
name: saneamiento-complementos-office
description: |
  Repara Excel, Word o PowerPoint cuando SE CIERRAN SOLOS, atacando las dos
  causas que explican la mayoría de los casos: los COMPLEMENTOS de terceros
  que cargan al arrancar (Adobe PDFMaker, Dropbox, Acrobat en Outlook) y la
  COLA DE TELEMETRÍA corrupta, que hace reventar a Office siempre en el
  mismo punto de `MsoAria.dll`.

  Trae `scripts/sanear_office.ps1`: inventaría, respalda, desactiva y
  revierte. Todo en HKCU, sin administrador, y sin borrar nada del trabajo
  del usuario.

  Se usa DESPUÉS de [[forense-cuelgues-y-caidas-windows]], que es quien
  identifica el módulo culpable y decide si el problema es de Office.

trigger_phrases:
  - "excel se cierra solo"
  - "word se cierra sin avisar"
  - "office se bloquea al abrir"
  - "MsoAria.dll"
  - "desactiva los complementos de office"
  - "excel pierde el trabajo"

idioma_de_salida: español
nivel: aplicada
dominio: Office / estabilidad de aplicaciones
metadata:
  version: 1.0
  fecha: 2026-08-30
  scripts:
    - scripts/sanear_office.ps1
  relacionada:
    - forense-cuelgues-y-caidas-windows
    - excel-macro-vba-embebido-gui
---

# Skill `saneamiento-complementos-office`

## Doctrina

Office rara vez se cae por sí mismo. Se cae por **lo que otros le meten
dentro**: complementos COM de terceros que se cargan en su mismo proceso.
Un complemento que corrompe el montón de memoria hace reventar a Office en
**cualquier otro sitio** — y muy a menudo ese sitio es la biblioteca de
telemetría, porque es la que corre después.

Por eso `MsoAria.dll` aparece tanto en los informes y por eso **culparla es
el error**: es la víctima que estaba en el lugar equivocado, no el asesino.

## Cómo leer la huella

`MsoAria.dll` = telemetría de Office (SDK Aria). Excepción `c0000005` =
violación de acceso. Lo que decide el diagnóstico es el **desplazamiento**:

- **Se repite** → un fallo reproducible. Hay una causa concreta.
- **Persiste entre versiones de Office** → actualizar **no** lo arregla; el
  disparador está en el entorno, no en el binario.
- `ntdll.dll` en la mezcla, siempre en el mismo desplazamiento → suele ser
  la ruta de **detección de corrupción del montón**: confirma que alguien
  está corrompiendo memoria antes.

## Las dos causas, en orden

### 1 · Complementos que cargan al inicio

`LoadBehavior` en la clave del complemento manda:

| Valor | Significado |
|---|---|
| **2** | No se carga ← el que se quiere poner |
| **3** | **Carga al inicio** ← el que causa problemas |
| 9 / 16 | A demanda |

Viven en tres ramas, y **solo `HKCU` se puede tocar sin administrador**:

```
HKCU:\SOFTWARE\Microsoft\Office\<App>\Addins                 <- editable
HKLM:\SOFTWARE\Microsoft\Office\<App>\Addins                 <- necesita admin
HKLM:\SOFTWARE\WOW6432Node\Microsoft\Office\<App>\Addins     <- necesita admin
```

⚠️ **`HKCU` gana sobre `HKLM`.** Es habitual encontrar un complemento con
`2` a nivel de máquina y `3` a nivel de usuario: se carga igual. Revisar
siempre las tres ramas antes de concluir que está desactivado.

Sospechosos habituales: **`PDFMaker.OfficeAddin`** (Acrobat),
**`Dropbox.OfficeAddIn`**, `AdobeAcroOutlook.SendAsLink`, `UCAddin.LyncAddin`.

### 2 · Cola de telemetría corrupta

`%LOCALAPPDATA%\Microsoft\Office\OTele` guarda una base SQLite por
aplicación (`excel.exe.db` con su `-wal` y su `-shm`). Si una queda
corrupta, Office la reproduce **en cada arranque** y revienta siempre en el
mismo punto. Encaja con el patrón de racimos: cae, se reabre, vuelve a caer
a los tres minutos.

Vaciarla es seguro: **es una cola de envío, no datos del usuario**. Office
la recrea. Algunos archivos quedarán retenidos por procesos vivos
(`sdxhelper`, `OfficeClickToRun`); es normal y no importa.

## Uso

```powershell
$S = "$env:USERPROFILE\.claude\skills\saneamiento-complementos-office\scripts"

# 1. Ver qué hay, sin tocar nada
& powershell -ExecutionPolicy Bypass -File "$S\sanear_office.ps1"

# 2. Desactivar los de terceros (Office debe estar CERRADO)
& powershell -ExecutionPolicy Bypass -File "$S\sanear_office.ps1" -Aplicar

# 3. Además, vaciar la cola de telemetría
& powershell -ExecutionPolicy Bypass -File "$S\sanear_office.ps1" -Aplicar -Telemetria

# 4. Deshacer
& powershell -ExecutionPolicy Bypass -File "$S\sanear_office.ps1" -Revertir
```

Para incluir Outlook u otra lista hay que usar **`-Command`**, no `-File`
(con `-File` el arreglo llega como una sola cadena y no encuentra nada):

```powershell
& powershell -ExecutionPolicy Bypass -Command "& '$S\sanear_office.ps1' -Apps Excel,Word,PowerPoint,Outlook"
```

El script aborta si detecta Office abierto, respalda a `.reg` antes de tocar
y conserva por omisión los complementos de Microsoft (Power Pivot, Power
View, Data Streamer, OneNote).

## Qué NO hacer

- **No borrar `Resiliency\DocumentRecovery`.** Cada entrada es un documento
  que Office recuperó y el usuario aún no ha rescatado. Contarlas sirve de
  medida del daño; borrarlas destruye trabajo.
- **No culpar a `MsoAria.dll`** ni salir a buscar cómo «reparar esa DLL».
- **No desactivar los complementos de Outlook a la ligera:** ahí suele vivir
  la integración corporativa (Lync, importadores). Inventariarlos, avisar, y
  que decida el usuario.

## Si aún así persiste

Escalar en este orden: **Reparación en línea** de Office (Panel de control →
Programas → Microsoft Office → Cambiar → Reparación en línea) y, si Office
es de **32 bits** con libros muy grandes, considerar la migración a 64 bits
por el límite de 2 GB de espacio de direcciones.

## Caso de referencia — 2026-08-30

Excel con **23 caídas en 30 días**, todas `c0000005` en `MsoAria.dll`, con
los desplazamientos repitiéndose (8× `00060636`, 8× `00060c76`) a través de
**cinco actualizaciones de Office**. `PDFMaker.OfficeAddin` y
`Dropbox.OfficeAddIn` cargaban al inicio en Excel, Word y PowerPoint —
PDFMaker con `2` en máquina y `3` en usuario. Desactivados los seis, y
vaciada la cola `OTele` (`excel.exe.db-wal` escrito **un minuto antes** de
una de las caídas). Detalle en [[project_diagnostico_explorador_windows]].

## Vecindad en la red

Racimo de mantenimiento de la máquina. Actúa DESPUÉS del forense, y sobre las mismas aplicaciones de Office que usan las skills de Excel y Word.

- [[forense-cuelgues-y-caidas-windows]]
- [[diagnostico-reparacion-windows-rendimiento]]
- [[excel-macro-vba-embebido-gui]]
- [[excel-pagina-a4-optima]]

> Puente tendido el 9-sep-2026: este racimo estaba conectado entre sí pero desprendido del cuerpo principal ([[regla-del-primer-tropiezo]] §10).
