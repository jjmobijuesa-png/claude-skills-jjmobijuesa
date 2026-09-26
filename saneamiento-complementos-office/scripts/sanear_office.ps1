# sanear_office.ps1 - Desactiva los complementos de Office que cargan al inicio
# y vacia la cola de telemetria, que son las dos causas mas frecuentes de que
# Excel, Word o PowerPoint se cierren solos.
#
#   .\sanear_office.ps1                       # ver que hay, sin tocar nada
#   .\sanear_office.ps1 -Aplicar              # desactivar complementos de terceros
#   .\sanear_office.ps1 -Aplicar -Telemetria  # ademas, vaciar la cola OTele
#   .\sanear_office.ps1 -Revertir             # deshacer
#
# Reversible: exporta un .reg antes de tocar nada. No requiere administrador
# (todo vive en HKCU).

param(
    [switch]$Aplicar,
    [switch]$Telemetria,
    [switch]$Revertir,
    [string[]]$Apps = @('Excel','Word','PowerPoint'),
    # Complementos de Microsoft que NO se tocan aunque carguen al inicio.
    [string[]]$Conservar = @('MicrosoftDataStreamer','PowerPivot','AdHocReporting','OneNote')
)

$ErrorActionPreference = 'Stop'
$bk = Join-Path $env:USERPROFILE 'Downloads\respaldo_addins_office'
New-Item -ItemType Directory -Path $bk -Force | Out-Null

function Nombre-Carga($lb) {
    switch ($lb) {
        0 {'0 descargado'} 1 {'1 cargado, no al inicio'} 2 {'2 NO se carga'}
        3 {'3 CARGA AL INICIO'} 8 {'8 descargado'} 9 {'9 a demanda'}
        16 {'16 carga al inicio'} default {"$lb"}
    }
}

# ---------------------------------------------------------------- REVERTIR --
if ($Revertir) {
    $regs = Get-ChildItem $bk -Filter '*.reg' | Sort-Object LastWriteTime -Descending
    if (-not $regs) { Write-Host "  No hay respaldos en $bk" -ForegroundColor Red; exit 1 }
    $sello = ($regs[0].BaseName -split '_')[-2..-1] -join '_'
    foreach ($r in ($regs | Where-Object { $_.Name -match [regex]::Escape($sello) })) {
        Write-Host ("  Restaurando " + $r.Name) -ForegroundColor Yellow
        reg import $r.FullName
    }
    Write-Host "  Restaurado. Cierra y vuelve a abrir Office." -ForegroundColor Green
    exit 0
}

# --------------------------------------------------------- OFFICE ABIERTO? --
$vivos = Get-Process EXCEL, WINWORD, POWERPNT, OUTLOOK, MSACCESS -ErrorAction SilentlyContinue
if ($vivos -and ($Aplicar -or $Telemetria)) {
    Write-Host "  HAY OFFICE ABIERTO. Cierralo antes de aplicar cambios:" -ForegroundColor Red
    $vivos | Select-Object Name, Id, MainWindowTitle | Format-Table -AutoSize | Out-String -Width 120 | Write-Host
    exit 1
}

# ------------------------------------------------------------- INVENTARIO --
Write-Host ""
Write-Host "=== Complementos que cargan al iniciar Office ===" -ForegroundColor Cyan
Write-Host ""
# Los complementos viven en tres ramas. Solo HKCU se puede modificar sin
# administrador; las de HKLM se inventarian y se avisa.
$raices = @(
    @{ Ruta='HKCU:\SOFTWARE\Microsoft\Office\';                  Etq='usuario';   Editable=$true  },
    @{ Ruta='HKLM:\SOFTWARE\Microsoft\Office\';                  Etq='maquina64'; Editable=$false },
    @{ Ruta='HKLM:\SOFTWARE\WOW6432Node\Microsoft\Office\';      Etq='maquina32'; Editable=$false }
)
$objetivo  = @()
$requieren = @()
foreach ($app in $Apps) {
    foreach ($r in $raices) {
        $base = $r.Ruta + $app + '\Addins'
        if (-not (Test-Path $base)) { continue }
        foreach ($a in (Get-ChildItem $base)) {
            $lb = (Get-ItemProperty $a.PSPath).LoadBehavior
            if ($lb -ne 3 -and $lb -ne 16) { continue }
            $salvado = $false
            foreach ($c in $Conservar) { if ($a.PSChildName -match $c) { $salvado = $true } }
            $marca = if ($salvado) { 'se conserva (Microsoft)' }
                     elseif (-not $r.Editable) { 'NECESITA ADMINISTRADOR' }
                     else { 'candidato a desactivar' }
            Write-Host ("   {0,-11} {1,-9} {2,-52} {3,-20} {4}" -f $app, $r.Etq, $a.PSChildName, (Nombre-Carga $lb), $marca)
            if ($salvado) { continue }
            if ($r.Editable) { $objetivo  += [pscustomobject]@{ App=$app; Nombre=$a.PSChildName; Ruta=$a.PSPath } }
            else             { $requieren += [pscustomobject]@{ App=$app; Nombre=$a.PSChildName; Ruta=$a.PSPath } }
        }
    }
}
if (-not $objetivo -and -not $requieren) { Write-Host "   Ninguno de terceros carga al inicio." -ForegroundColor Green }
if ($requieren) {
    Write-Host ""
    Write-Host ("   " + $requieren.Count + " complemento(s) estan en HKLM: este script no los toca.") -ForegroundColor Yellow
    Write-Host "   Se desactivan desde la propia aplicacion: Archivo > Opciones > Complementos" -ForegroundColor Yellow
    Write-Host "   > Complementos COM > Ir, y quitar la casilla." -ForegroundColor Yellow
}

if (-not ($Aplicar -or $Telemetria)) {
    Write-Host ""
    Write-Host "   (solo inventario; usa -Aplicar para desactivarlos)" -ForegroundColor DarkGray
    Write-Host ""
    exit 0
}

# ---------------------------------------------------------------- APLICAR --
$sello = Get-Date -Format 'yyyyMMdd_HHmmss'

if ($Aplicar -and $objetivo) {
    Write-Host ""
    Write-Host "=== Desactivando ===" -ForegroundColor Cyan
    foreach ($app in ($objetivo.App | Sort-Object -Unique)) {
        $dest = Join-Path $bk ($app + '_addins_' + $sello + '.reg')
        reg export ('HKCU\SOFTWARE\Microsoft\Office\' + $app + '\Addins') $dest /y | Out-Null
        Write-Host ("   respaldo -> " + $dest) -ForegroundColor DarkGray
    }
    foreach ($o in $objetivo) {
        $antes = (Get-ItemProperty $o.Ruta).LoadBehavior
        Set-ItemProperty -Path $o.Ruta -Name 'LoadBehavior' -Value 2 -Type DWord
        $desp = (Get-ItemProperty $o.Ruta).LoadBehavior
        Write-Host ("   {0,-12} {1,-50} {2} -> {3}" -f $o.App, $o.Nombre, $antes, $desp) -ForegroundColor Green
    }
}

# ------------------------------------------------------------- TELEMETRIA --
if ($Telemetria) {
    Write-Host ""
    Write-Host "=== Cola de telemetria (OTele) ===" -ForegroundColor Cyan
    # Cada .db es una base SQLite por aplicacion, con su -wal y su -shm. Si uno
    # queda corrupto, Office lo reproduce en cada arranque y revienta siempre en
    # el mismo punto de MsoAria.dll. Vaciarla es seguro: es cola, no datos.
    $otele = Join-Path $env:LOCALAPPDATA 'Microsoft\Office\OTele'
    if (-not (Test-Path $otele)) { Write-Host "   no existe la carpeta OTele" -ForegroundColor DarkGray }
    else {
        $destino = Join-Path $env:USERPROFILE ('Downloads\respaldo_otele_' + $sello)
        Copy-Item -Path $otele -Destination $destino -Recurse -Force
        Write-Host ("   respaldo -> " + $destino) -ForegroundColor DarkGray
        $n = 0; $bloq = 0
        foreach ($f in (Get-ChildItem $otele -File)) {
            try { Remove-Item -LiteralPath $f.FullName -Force; $n++ } catch { $bloq++ }
        }
        Write-Host ("   vaciados $n archivos" + $(if ($bloq) { ", $bloq retenidos por procesos vivos (normal)" } else { "" })) -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "  LISTO. Abre Office y comprueba." -ForegroundColor Cyan
Write-Host "  Si algo se echa en falta:  .\sanear_office.ps1 -Revertir"
Write-Host ""
exit 0
