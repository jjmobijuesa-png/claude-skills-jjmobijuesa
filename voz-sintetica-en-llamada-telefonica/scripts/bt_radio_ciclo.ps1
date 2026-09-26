# bt_radio.ps1  -  apaga y enciende la radio Bluetooth por WinRT (sin admin)
param([string]$Modo = 'ciclo')

Add-Type -AssemblyName System.Runtime.WindowsRuntime

$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() |
    Where-Object { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and
                   $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]

function Await($op, $tipo) {
    $m = $asTaskGeneric.MakeGenericMethod($tipo)
    $t = $m.Invoke($null, @($op))
    $t.Wait(-1) | Out-Null
    $t.Result
}

$null = [Windows.Devices.Radios.Radio, Windows.System.Devices, ContentType=WindowsRuntime]
$null = [Windows.Devices.Radios.RadioAccessStatus, Windows.System.Devices, ContentType=WindowsRuntime]
$null = [Windows.Devices.Radios.RadioState, Windows.System.Devices, ContentType=WindowsRuntime]

$acceso = Await ([Windows.Devices.Radios.Radio]::RequestAccessAsync()) ([Windows.Devices.Radios.RadioAccessStatus])
Write-Host "Acceso a radios: $acceso"
if ("$acceso" -ne 'Allowed') { Write-Host "SIN PERMISO para controlar radios."; exit 1 }

$radios = Await ([Windows.Devices.Radios.Radio]::GetRadiosAsync()) ([System.Collections.Generic.IReadOnlyList[Windows.Devices.Radios.Radio]])
$bt = $radios | Where-Object { "$($_.Kind)" -eq 'Bluetooth' }
if (-not $bt) { Write-Host "No se encontro radio Bluetooth."; exit 1 }

foreach ($r in $bt) {
    Write-Host "Radio: $($r.Name)  estado actual: $($r.State)"
    if ($Modo -eq 'ciclo' -or $Modo -eq 'off') {
        $res = Await ($r.SetStateAsync([Windows.Devices.Radios.RadioState]::Off)) ([Windows.Devices.Radios.RadioAccessStatus])
        Write-Host "  -> apagar: $res"
    }
}

if ($Modo -eq 'ciclo') {
    Start-Sleep -Seconds 6
    $radios = Await ([Windows.Devices.Radios.Radio]::GetRadiosAsync()) ([System.Collections.Generic.IReadOnlyList[Windows.Devices.Radios.Radio]])
    foreach ($r in ($radios | Where-Object { "$($_.Kind)" -eq 'Bluetooth' })) {
        $res = Await ($r.SetStateAsync([Windows.Devices.Radios.RadioState]::On)) ([Windows.Devices.Radios.RadioAccessStatus])
        Write-Host "  -> encender: $res"
    }
    Start-Sleep -Seconds 8
    $radios = Await ([Windows.Devices.Radios.Radio]::GetRadiosAsync()) ([System.Collections.Generic.IReadOnlyList[Windows.Devices.Radios.Radio]])
    foreach ($r in ($radios | Where-Object { "$($_.Kind)" -eq 'Bluetooth' })) {
        Write-Host "Estado final: $($r.Name) = $($r.State)"
    }
}
