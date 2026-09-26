# validar_pdf.ps1 - comprueba que un PDF este bien formado: cabecera, tabla de
# referencias cruzadas con desplazamientos que apuntan de verdad a sus objetos,
# trailer y marca final.
param([Parameter(Mandatory=$true)][string]$Ruta)

$ErrorActionPreference = 'Stop'
$b = [System.IO.File]::ReadAllBytes($Ruta)
$t = [System.Text.Encoding]::GetEncoding(28591).GetString($b)   # latin1: 1 byte = 1 char
$ok = $true
function Bien($m) { Write-Host ("  OK   " + $m) -ForegroundColor Green }
function Mal($m)  { Write-Host ("  MAL  " + $m) -ForegroundColor Red; $script:ok = $false }

Write-Host ("Validando: " + $Ruta)
Write-Host ("  tamano: {0:N0} bytes" -f $b.Length)

if ($t.StartsWith('%PDF-')) { Bien ("cabecera " + $t.Substring(0,8)) } else { Mal "no empieza por %PDF-" }
$fin = $t.TrimEnd()
if ($fin.EndsWith('%%EOF')) { Bien "termina en %%EOF" } else { Mal "no termina en %%EOF" }

$m = [regex]::Match($t, 'startxref\s+(\d+)\s*%%EOF\s*$')
if (-not $m.Success) { Mal "no se encuentra startxref"; exit 1 }
$inicio = [int]$m.Groups[1].Value
if ($inicio -ge $b.Length) { Mal "startxref apunta fuera del archivo"; exit 1 }
if ($t.Substring($inicio, 4) -eq 'xref') { Bien "startxref apunta a la tabla xref" } else { Mal "startxref no apunta a 'xref'" }

$xr = [regex]::Match($t.Substring($inicio), "xref\s+0\s+(\d+)\s+")
$total = [int]$xr.Groups[1].Value
Bien ("la tabla declara $total objetos (incluido el libre 0)")

$cuerpo = $t.Substring($inicio + $xr.Length)
$ent = [regex]::Matches($cuerpo, '(\d{10}) (\d{5}) ([nf])')
Write-Host ("  entradas encontradas: " + $ent.Count)
$fallos = 0
for ($i = 1; $i -lt [Math]::Min($ent.Count, $total); $i++) {
    if ($ent[$i].Groups[3].Value -ne 'n') { continue }
    $off = [int]$ent[$i].Groups[1].Value
    $esperado = "$i 0 obj"
    if ($off -lt 0 -or $off + $esperado.Length -gt $b.Length) { Mal "objeto $i : desplazamiento fuera del archivo"; $fallos++; continue }
    $real = $t.Substring($off, $esperado.Length)
    if ($real -ne $esperado) { Mal ("objeto $i : el desplazamiento $off apunta a '" + $real + "' y no a '" + $esperado + "'"); $fallos++ }
}
if ($fallos -eq 0) { Bien "todos los desplazamientos apuntan a su objeto" }

foreach ($clave in @('/Type /Catalog', '/Type /Pages', '/Type /Page ', '/Filter /DCTDecode')) {
    if ($t -match [regex]::Escape($clave)) { Bien ("presente: " + $clave) } else { Mal ("falta: " + $clave) }
}

$img = [regex]::Match($t, '/Filter /DCTDecode\s*/Length (\d+)')
if ($img.Success) {
    $len = [int]$img.Groups[1].Value
    $ini = $t.IndexOf("stream`n", $img.Index) + 7
    if ($b[$ini] -eq 0xFF -and $b[$ini+1] -eq 0xD8) { Bien "el flujo de imagen empieza con la marca JPEG FFD8" }
    else { Mal "el flujo de imagen no empieza con FFD8" }
    if ($b[$ini+$len-2] -eq 0xFF -and $b[$ini+$len-1] -eq 0xD9) { Bien ("el flujo de imagen termina con FFD9 tras {0:N0} bytes" -f $len) }
    else { Mal "el flujo de imagen no termina con FFD9" }
}

$mb = [regex]::Match($t, '/MediaBox \[0 0 ([\d.]+) ([\d.]+)\]')
if ($mb.Success) {
    $w = [double]$mb.Groups[1].Value; $h = [double]$mb.Groups[2].Value
    Bien ("MediaBox {0} x {1} pt  =  {2:N1} x {3:N1} cm" -f $w, $h, ($w / 72 * 2.54), ($h / 72 * 2.54))
}

Write-Host ""
if ($ok) { Write-Host "  PDF VALIDO" -ForegroundColor Green } else { Write-Host "  PDF CON PROBLEMAS" -ForegroundColor Red }
