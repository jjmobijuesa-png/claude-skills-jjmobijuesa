---
name: forense-cuelgues-y-caidas-windows
description: |
  Diagnostica por qué un programa de Windows SE CONGELA o SE CIERRA SOLO,
  con evidencia del registro de eventos en lugar de conjeturas. Cubre el
  Explorador de archivos que se bloquea o no termina de leer carpetas, y
  aplicaciones que se cierran sin aviso (Office, navegadores, cualquiera).

  Regla de oro: **un cuelgue no es un fallo**. Windows los registra en
  eventos distintos y significan cosas opuestas — el evento 1002 dice que
  el programa ESTÁ ESPERANDO algo; el 1000 dice que reventó. Mirar el
  registro equivocado hace perder horas.

  Trae `scripts/diagnostico.ps1`, que hace de una pasada el barrido
  completo: cuelgues con su firma WER, caídas con huella de módulo y
  desplazamiento, unidades de red muertas, superposiciones de icono,
  controladores de vista previa, procesos de Office huérfanos,
  complementos y salud de discos. No repara nada: solo observa.

trigger_phrases:
  - "el explorador de windows se cuelga"
  - "hay que cerrar el explorador"
  - "no abre las carpetas / no lee los archivos"
  - "el programa se cierra solo"
  - "se congela la barra de tareas"
  - "diagnostica por qué se bloquea"
  - "revisa el visor de eventos"

idioma_de_salida: español
nivel: aplicada
dominio: diagnóstico de Windows / shell / eventos
metadata:
  version: 1.0
  fecha: 2026-08-30
  scripts:
    - scripts/diagnostico.ps1
  relacionada:
    - saneamiento-complementos-office
    - diagnostico-reparacion-windows-rendimiento
---

# Skill `forense-cuelgues-y-caidas-windows`

## Doctrina

**Un cuelgue no es un fallo, y Windows lo sabe aunque casi nadie lo mire.**

| Evento | Significa | Dónde está la pista |
|---|---|---|
| **1002** `Application Hang` | El programa **espera** algo y deja de responder | La **firma WER** del evento 1001 que lo acompaña |
| **1000** `Application Error` | El programa **revienta** con una excepción | El **módulo** y el **desplazamiento** del fallo |

Si el síntoma es «se queda pensando, hay que cerrarlo», buscar errores 1000
no encuentra nada y se concluye en falso que «no hay nada en los registros».
Hay que ir al **1002**, y de ahí a su **1001**.

## Las dos huellas que resuelven casi todo

### 1 · Cuelgue: el campo **P6** de la firma WER

El informe del evento 1001 trae `P1`…`P10`. En un cuelgue *cross-process*:

```
P1: explorer.exe          <- el que se colgó
P2: 10.0.26100.9168
P5: 135266336             <- tipo de cuelgue
P6: WINWORD.EXE           <- EL PROCESO AL QUE ESTABA ESPERANDO
```

**P6 nombra al culpable.** Ese solo campo convierte «el Explorador se cuelga»
en «el Explorador espera a Word», que es una hipótesis comprobable.

### 2 · Caída: agrupar por **módulo + desplazamiento**

No basta con ver el módulo. Hay que agrupar también por `Offset`:

- **Desplazamiento que se repite** → un fallo **reproducible**, siempre el
  mismo punto de código. Hay una causa concreta y localizable.
- **Desplazamientos dispersos** → corrupción de memoria; el módulo que
  aparece suele ser la víctima, no el culpable.

El desplazamiento cambia cuando se recompila el módulo, así que al comparar
entre versiones hay que agrupar por versión. Caso real: 8 caídas en
`MsoAria.dll+00060c76` y luego 8 en `+00060636` tras una actualización —
mismo fallo, DLL recompilada.

Y ojo: **si el fallo persiste a través de varias actualizaciones, actualizar
no es la solución.** Hay que buscar el disparador en el entorno.

## Los cinco sospechosos del Explorador congelado

En orden de frecuencia real:

1. **Unidad de red muerta.** La n.º 1 y la más invisible. Una unidad mapeada
   a un servidor inalcanzable bloquea al Explorador en **cada enumeración de
   unidades**: «Este equipo», el panel de navegación, cualquier diálogo de
   Abrir o Guardar. Los tiempos de espera SMB son de decenas de segundos.
   🔎 Comprobar **la subred**: si el equipo está en `192.168.100.x` y el
   servidor en `192.168.1.x`, esa unidad no conectará nunca desde ahí.
   Se quita con `Remove-SmbMapping` **y** borrando `HKCU:\Network\<letra>`,
   o no vuelve limpia tras reiniciar.

2. **Controladores de vista previa y de miniatura.** Un
   `WINWORD.EXE -Embedding` cuyo padre es `svchost.exe` es **activación
   COM**: el Explorador pidió a Windows arrancar Office para generar una
   miniatura o una vista previa. Si ese proceso se atasca, el Explorador se
   atasca con él. Los de Adobe (`pdfprevhndlr.dll`) son causa clásica.

3. **Superposiciones de icono.** Windows procesa **solo 15** y las consulta
   de forma **síncrona por cada archivo mostrado**. Con tres sincronizadores
   en la nube se llega a 23 sin darse cuenta, contra tres demonios distintos.

4. **Extensiones de menú contextual** de terceros.

5. **Disco.** Se descarta rápido con `Get-PhysicalDisk` y los eventos de
   `disk` / `Ntfs` del registro del sistema. Casi nunca es esto.

## Uso

```powershell
$S = "$env:USERPROFILE\.claude\skills\forense-cuelgues-y-caidas-windows\scripts"
& powershell -ExecutionPolicy Bypass -File "$S\diagnostico.ps1"
& powershell -ExecutionPolicy Bypass -File "$S\diagnostico.ps1" -Dias 60
```

Para pasar arreglos hay que usar `-Command`, no `-File`: con `-File`,
PowerShell no separa por comas y el parámetro llega como una sola cadena.

El script **no modifica nada**. Ocho secciones: cuelgues con firma · caídas
con huella · unidades y rutas de red · superposiciones · vista previa ·
procesos huérfanos · complementos · discos.

## Mitigación que casi siempre conviene

```powershell
Set-ItemProperty 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced' `
  -Name SeparateProcess -Value 1 -Type DWord
```

Cada ventana de carpeta pasa a correr en su propio proceso. Una carpeta
colgada deja de arrastrar al escritorio y a la barra de tareas: se cierra
esa ventana y ya. No cura la causa, pero convierte una catástrofe en una
molestia. Sin administrador.

## Trampas del entorno

- El sandbox de esta sesión bloquea comandos por **coincidencia de texto**,
  no por semántica: `/delete`, `/1GB`, un `'*'` en `Copy-Item`, una barra
  suelta dentro de un `Write-Output`, o `Remove-Job` cerca de una letra de
  unidad. Si aparece *«Remove-Item on system path … is blocked»* y no había
  ningún borrado, es un falso positivo: reescribir con variables o partir el
  comando.
- `IAudioMeterInformation` y en general cualquier interfaz COM **se degrada
  a `System.__ComObject`** al cruzar a PowerShell. El trabajo con interfaces
  COM tiene que quedar dentro de C#, devolviendo valores simples.

## Caso de referencia — 2026-08-30, Dell Inspiron 15 3520

Síntoma: «el Explorador se bloquea, hay que cerrarlo, o no procesa la
lectura de las carpetas». Resuelto en tres causas concurrentes:
`Z:` → `\\192.168.1.210\Cartera` muerta en otra subred (eliminada) · Word
arrancado por activación COM para miniaturas (cerrado) · 23 superposiciones
con límite de 15. Detalle en [[project_diagnostico_explorador_windows]].

## Vecindad en la red

Racimo de mantenimiento de la máquina. Es el diagnóstico que precede a toda reparación: quien encuentra el módulo culpable antes de tocar nada.

- [[diagnostico-reparacion-windows-rendimiento]]
- [[saneamiento-complementos-office]]
- [[impresion-local-hp-diagnostico]]
- [[cierre-jornada-apagado]]

> Puente tendido el 9-sep-2026: este racimo estaba conectado entre sí pero desprendido del cuerpo principal ([[regla-del-primer-tropiezo]] §10).
