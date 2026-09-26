# imagen_a_pdf.ps1 - arma un PDF a partir de una o varias imagenes JPEG,
# escribiendo el PDF a mano. Sin Word, sin Acrobat, sin nada instalado.
#
# La clave: un JPEG se puede incrustar en un PDF TAL CUAL, sin recomprimir,
# declarandolo como XObject con /Filter /DCTDecode. El PDF pesa practicamente
# lo mismo que el JPEG y no pierde calidad.
#
#   .\imagen_a_pdf.ps1 -Imagenes a.jpg,b.jpg -Salida doc.pdf -Dpi 300
#
# Limitacion: los JPEG deben ser de linea base (baseline). Los progresivos no
# los admite DCTDecode. System.Drawing genera baseline por omision.

param(
    [Parameter(Mandatory=$true)][string[]]$Imagenes,
    [Parameter(Mandatory=$true)][string]$Salida,
    [double]$Dpi = 300,
    [string]$Titulo = ''
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$fs = [System.IO.File]::Create($Salida)
$enc = [System.Text.Encoding]::ASCII
$offsets = @{}

function W([string]$s) { $b = $enc.GetBytes($s); $fs.Write($b, 0, $b.Length) }
function WB([byte[]]$b) { $fs.Write($b, 0, $b.Length) }
function Obj([int]$n) { $offsets[$n] = $fs.Position; W("$n 0 obj`n") }

W("%PDF-1.4`n")
WB([byte[]](0x25, 0xE2, 0xE3, 0xCF, 0xD3, 0x0A))   # marca de binario

# --- recopilar datos de cada imagen ----------------------------------------
$paginas = @()
foreach ($ruta in $Imagenes) {
    if (-not (Test-Path $ruta)) { throw "No existe la imagen: $ruta" }
    $bytes = [System.IO.File]::ReadAllBytes($ruta)
    $img = [System.Drawing.Image]::FromFile($ruta)
    $w = $img.Width; $h = $img.Height
    $gris = $img.PixelFormat -match 'Format8bppIndexed|Format16bppGrayScale'
    $img.Dispose()
    $paginas += [pscustomobject]@{ Bytes=$bytes; W=$w; H=$h; Gris=$gris }
}
$n = $paginas.Count

# Numeracion: 1 catalogo, 2 arbol de paginas, luego 3 objetos por pagina.
$idPagina    = New-Object int[] $n
$idImagen    = New-Object int[] $n
$idContenido = New-Object int[] $n
for ($i = 0; $i -lt $n; $i++) {
    $idPagina[$i]    = 3 + $i * 3
    $idImagen[$i]    = 4 + $i * 3
    $idContenido[$i] = 5 + $i * 3
}

# --- 1. catalogo ------------------------------------------------------------
Obj 1
W("<< /Type /Catalog /Pages 2 0 R >>`nendobj`n")

# --- 2. arbol de paginas ----------------------------------------------------
Obj 2
$kids = ($idPagina | ForEach-Object { "$_ 0 R" }) -join ' '
W("<< /Type /Pages /Kids [$kids] /Count $n >>`nendobj`n")

# --- objetos por pagina -----------------------------------------------------
for ($i = 0; $i -lt $n; $i++) {
    $p = $paginas[$i]
    $anchoPt = [math]::Round(($p.W / $Dpi) * 72, 2)
    $altoPt  = [math]::Round(($p.H / $Dpi) * 72, 2)
    $espacio = if ($p.Gris) { '/DeviceGray' } else { '/DeviceRGB' }

    Obj $idPagina[$i]
    W("<< /Type /Page /Parent 2 0 R /MediaBox [0 0 $anchoPt $altoPt]")
    W(" /Resources << /XObject << /Im0 $($idImagen[$i]) 0 R >> >>")
    W(" /Contents $($idContenido[$i]) 0 R >>`nendobj`n")

    Obj $idImagen[$i]
    W("<< /Type /XObject /Subtype /Image /Width $($p.W) /Height $($p.H)")
    W(" /ColorSpace $espacio /BitsPerComponent 8 /Filter /DCTDecode")
    W(" /Length $($p.Bytes.Length) >>`nstream`n")
    WB $p.Bytes
    W("`nendstream`nendobj`n")

    # La matriz cm estira la imagen (que mide 1x1 en su espacio) al tamano
    # completo de la pagina. q ... Q aisla el estado grafico.
    $flujo = "q`n$anchoPt 0 0 $altoPt 0 0 cm`n/Im0 Do`nQ`n"
    Obj $idContenido[$i]
    W("<< /Length $($flujo.Length) >>`nstream`n")
    W($flujo)
    W("endstream`nendobj`n")
}

# --- tabla de referencias cruzadas -----------------------------------------
$total = 2 + $n * 3
$inicioXref = $fs.Position
W("xref`n0 $($total + 1)`n")
W("0000000000 65535 f `n")
for ($k = 1; $k -le $total; $k++) {
    W(("{0:D10} 00000 n `n" -f $offsets[$k]))
}
W("trailer`n<< /Size $($total + 1) /Root 1 0 R")
if ($Titulo) { W(" /Info << /Title ($Titulo) >>") }
W(" >>`nstartxref`n$inicioXref`n%%EOF`n")

$fs.Close()

$f = Get-Item $Salida
Write-Host ("PDF: " + $f.FullName)
Write-Host ("  {0} pagina(s), {1:N2} MB" -f $n, ($f.Length / 1MB))
foreach ($p in $paginas) {
    Write-Host ("  {0} x {1} px a {2} dpi  =  {3:N1} x {4:N1} cm" -f $p.W, $p.H, $Dpi, (($p.W / $Dpi) * 2.54), (($p.H / $Dpi) * 2.54))
}
