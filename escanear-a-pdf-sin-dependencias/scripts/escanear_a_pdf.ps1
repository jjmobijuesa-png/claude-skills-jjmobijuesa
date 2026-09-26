# escanear_a_pdf.ps1 - flujo completo: escanear -> PDF -> validar.
#
#   .\escanear_a_pdf.ps1 -Destino "E:\ruta"
#   .\escanear_a_pdf.ps1 -Destino "E:\ruta" -Nombre "Contrato" -Dpi 200 -Modo Gris
#   .\escanear_a_pdf.ps1 -Destino "E:\ruta" -Alimentador     # lote multipagina
#
# Encadena los tres scripts de la skill. Sin Word, sin Acrobat, sin nada
# instalado: solo WIA, System.Drawing y un escritor de PDF propio.

param(
    [Parameter(Mandatory=$true)][string]$Destino,
    [string]$Nombre = '',
    [int]$Dpi = 300,
    [ValidateSet('Color','Gris','ByN')][string]$Modo = 'Color',
    [int]$Calidad = 85,
    [string]$Dispositivo = '',
    [switch]$Alimentador,
    [int]$MaxPaginas = 25,
    [switch]$ConservarImagenes
)

$ErrorActionPreference = 'Stop'
$aqui = $PSScriptRoot
if (-not (Test-Path $Destino)) { throw "La ruta de destino no existe: $Destino" }
if (-not $Nombre) { $Nombre = 'Escaneo_' + (Get-Date -Format 'yyyy-MM-dd_HHmm') }

$tmp = Join-Path $env:TEMP ('escaneo_' + [guid]::NewGuid().ToString('N').Substring(0,8))
New-Item -ItemType Directory -Path $tmp -Force | Out-Null

try {
    # --- 1. capturar --------------------------------------------------------
    $args = @{ Carpeta = $tmp; Dpi = $Dpi; Modo = $Modo; Calidad = $Calidad; MaxPaginas = $MaxPaginas }
    if ($Dispositivo) { $args['Dispositivo'] = $Dispositivo }
    if ($Alimentador) { $args['Alimentador'] = $true }
    $imgs = & (Join-Path $aqui 'escanear.ps1') @args
    $imgs = @($imgs | Where-Object { $_ -is [string] -and (Test-Path $_) })
    if (-not $imgs) { throw "El escaneo no produjo ninguna imagen." }

    # --- 2. armar el PDF, sin pisar uno existente ---------------------------
    $pdf = Join-Path $Destino ($Nombre + '.pdf')
    $i = 1
    while (Test-Path $pdf) { $pdf = Join-Path $Destino ($Nombre + "_$i.pdf"); $i++ }

    Write-Host ""
    & (Join-Path $aqui 'imagen_a_pdf.ps1') -Imagenes $imgs -Salida $pdf -Dpi $Dpi -Titulo $Nombre

    # --- 3. validar ---------------------------------------------------------
    Write-Host ""
    & (Join-Path $aqui 'validar_pdf.ps1') -Ruta $pdf

    if ($ConservarImagenes) {
        foreach ($f in $imgs) { Copy-Item -LiteralPath $f -Destination $Destino -Force }
        Write-Host ("  imagenes conservadas en " + $Destino) -ForegroundColor DarkGray
    }
    Write-Host ""
    Write-Host ("LISTO: " + $pdf) -ForegroundColor Green
}
finally {
    if (Test-Path $tmp) { Remove-Item -LiteralPath $tmp -Recurse -Force -ErrorAction SilentlyContinue }
}
