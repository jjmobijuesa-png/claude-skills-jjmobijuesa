# escanear.ps1 - captura desde el escaner por WIA y entrega uno o varios JPEG.
#
#   .\escanear.ps1 -Carpeta C:\temp
#   .\escanear.ps1 -Carpeta C:\temp -Dpi 200 -Modo Gris
#   .\escanear.ps1 -Carpeta C:\temp -Alimentador -MaxPaginas 20
#
# Devuelve por la tuberia las rutas de los JPEG generados.
# No requiere administrador ni software del fabricante.

param(
    [Parameter(Mandatory=$true)][string]$Carpeta,
    [int]$Dpi = 300,
    [ValidateSet('Color','Gris','ByN')][string]$Modo = 'Color',
    [int]$Calidad = 85,
    [string]$Dispositivo = '',
    [switch]$Alimentador,
    [int]$MaxPaginas = 25
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
if (-not (Test-Path $Carpeta)) { New-Item -ItemType Directory -Path $Carpeta -Force | Out-Null }

# Formatos de transferencia WIA. BMP es el unico que TODO driver admite; pedir
# JPEG directamente falla en muchos escaneres, asi que se captura BMP y se
# comprime despues con System.Drawing.
$WIA_BMP = '{B96B3CAB-0728-11D3-9D7B-0000F81EF32E}'

# Capacidades y estado del manejo de documentos (WIA_DPS_DOCUMENT_HANDLING_*)
$CAP_ALIMENTADOR = 0x001
$EST_TAPA_ABIERTA = 0x08
$EST_ATASCO       = 0x20

# --- 1. Elegir escaner ------------------------------------------------------
$dm = New-Object -ComObject WIA.DeviceManager
$dev = $null; $nombreDisp = ''
for ($i = 1; $i -le $dm.DeviceInfos.Count; $i++) {
    $info = $dm.DeviceInfos.Item($i)
    $nom = $info.Properties.Item('Name').Value
    if ($Dispositivo) { if ($nom -notmatch [regex]::Escape($Dispositivo)) { continue } }
    elseif ($info.Type -ne 1) { continue }     # 1 = escaner
    try { $dev = $info.Connect(); $nombreDisp = $nom; break } catch { }
}
if (-not $dev) { throw "No se pudo conectar con ningun escaner WIA. Comprueba que este encendido y en la misma red." }
Write-Host ("Escaner: " + $nombreDisp) -ForegroundColor Cyan

# --- 2. Estado del aparato --------------------------------------------------
$prop = { param($n) ($dev.Properties | Where-Object { $_.Name -eq $n }).Value }
$est = & $prop 'Document Handling Status'
$cap = & $prop 'Document Handling Capabilities'
if ($est -band $EST_ATASCO) { throw "Hay un atasco de papel en el escaner." }
if ($est -band $EST_TAPA_ABIERTA) { Write-Host "  AVISO: la tapa esta levantada." -ForegroundColor Yellow }

$tieneAlim = ($cap -band $CAP_ALIMENTADOR) -ne 0
if ($Alimentador -and -not $tieneAlim) {
    Write-Host "  Este escaner NO tiene alimentador; se usara el cristal." -ForegroundColor Yellow
    $Alimentador = $false
}
Write-Host ("  alimentador: " + $(if ($tieneAlim) { 'si' } else { 'no (solo cristal)' }))

# --- 3. Configurar la captura -----------------------------------------------
$item = $dev.Items.Item(1)
$tipoDato = switch ($Modo) { 'Color' {3} 'Gris' {2} 'ByN' {0} }
function Fijar($n, $v) {
    $p = $item.Properties | Where-Object { $_.Name -eq $n }
    if ($p) { try { $p.Value = $v } catch { Write-Host ("  no admite '$n' = $v") -ForegroundColor DarkYellow } }
}
Fijar 'Horizontal Resolution' $Dpi
Fijar 'Vertical Resolution'   $Dpi
Fijar 'Data Type'             $tipoDato
$xr = ($item.Properties | Where-Object { $_.Name -eq 'Horizontal Resolution' }).Value
$xe = ($item.Properties | Where-Object { $_.Name -eq 'Horizontal Extent' }).Value
$ye = ($item.Properties | Where-Object { $_.Name -eq 'Vertical Extent' }).Value
Write-Host ("  {0} dpi, {1}, area {2} x {3} px" -f $xr, $Modo, $xe, $ye)

# --- 4. Capturar ------------------------------------------------------------
$cod = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$par = New-Object System.Drawing.Imaging.EncoderParameters(1)
$par.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [int]$Calidad)

$sello = Get-Date -Format 'yyyyMMdd_HHmmss'
$salidas = @()
$pag = 0
$limite = if ($Alimentador) { $MaxPaginas } else { 1 }

while ($pag -lt $limite) {
    $pag++
    Write-Host ("  capturando pagina $pag...") -ForegroundColor Cyan
    try { $img = $item.Transfer($WIA_BMP) }
    catch {
        # Con alimentador, quedarse sin papel es la senal normal de fin.
        if ($Alimentador -and $pag -gt 1) { Write-Host "  fin del lote (sin mas hojas)."; break }
        throw
    }
    $bmp = Join-Path $Carpeta ("scan_" + $sello + "_" + ('{0:D2}' -f $pag) + ".bmp")
    $img.SaveFile($bmp)
    [void][Runtime.InteropServices.Marshal]::ReleaseComObject($img)

    $jpg = [IO.Path]::ChangeExtension($bmp, '.jpg')
    $bm = [System.Drawing.Image]::FromFile($bmp)
    $bm.Save($jpg, $cod, $par)
    $w = $bm.Width; $h = $bm.Height
    $bm.Dispose()
    Remove-Item -LiteralPath $bmp -Force

    $mb = (Get-Item $jpg).Length / 1MB
    Write-Host ("    -> {0}  ({1} x {2} px, {3:N2} MB)" -f (Split-Path $jpg -Leaf), $w, $h, $mb) -ForegroundColor Green
    $salidas += $jpg

    if (-not $Alimentador) { break }
    $est = & $prop 'Document Handling Status'
    if (-not ($est -band 0x01)) { Write-Host "  el alimentador ya no tiene hojas."; break }
}

Write-Host ("Paginas capturadas: " + $salidas.Count)
$salidas
