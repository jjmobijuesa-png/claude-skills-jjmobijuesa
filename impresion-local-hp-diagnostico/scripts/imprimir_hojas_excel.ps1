# imprimir_hojas_excel.ps1
# Imprime un rango de HOJAS (pestañas) de un .xlsx a la impresora indicada
# (o a la predeterminada), ajustando cada hoja a 1 página, vía Excel COM.
#
# Uso:
#   powershell -File imprimir_hojas_excel.ps1 -Path "<ruta.xlsx>" -Desde 1 -Hasta 4 [-Impresora "<nombre>"]
#
# Notas:
#   - Abre el libro en SOLO LECTURA y NO lo guarda (los cambios de PageSetup
#     son en memoria). No altera el archivo original.
#   - Si -Impresora se omite, usa la predeterminada de Windows.
#   - Devuelve el/los trabajo(s) enviados al spooler para poder monitorear.

param(
  [Parameter(Mandatory=$true)][string]$Path,
  [int]$Desde = 1,
  [int]$Hasta = 4,
  [string]$Impresora = ""
)

if (-not (Test-Path $Path)) { Write-Output "ERROR: no existe $Path"; exit 1 }

$xl = $null; $wb = $null
try {
  $xl = New-Object -ComObject Excel.Application
  $xl.Visible = $false; $xl.DisplayAlerts = $false; $xl.ScreenUpdating = $false
  $wb = $xl.Workbooks.Open($Path, 0, $true)   # ReadOnly
  $total = $wb.Worksheets.Count
  if ($Hasta -gt $total) { $Hasta = $total }
  Write-Output "Libro: $([System.IO.Path]::GetFileName($Path)) ($total hojas). Imprimiendo hojas $Desde..$Hasta."
  for ($i=$Desde; $i -le $Hasta; $i++) {
    $ws = $wb.Worksheets.Item($i)
    $ps = $ws.PageSetup
    $ps.Zoom = $false; $ps.FitToPagesWide = 1; $ps.FitToPagesTall = 1
    $ps.CenterHorizontally = $true
    Write-Output ("  [{0}] {1}" -f $i, $ws.Name)
  }
  $wb.Worksheets.Item($Desde).Select($true)
  for ($i=$Desde+1; $i -le $Hasta; $i++) { $wb.Worksheets.Item($i).Select($false) }
  if ($Impresora -ne "") { $xl.ActivePrinter = $Impresora }  # opcional; si falla, usa la predeterminada
  $xl.ActiveWindow.SelectedSheets.PrintOut()
  Write-Output "PrintOut enviado."
}
catch { Write-Output "ERROR COM: $($_.Exception.Message)" }
finally {
  if ($wb) { $wb.Close($false) }
  if ($xl) { $xl.Quit() }
  try { [System.Runtime.InteropServices.Marshal]::ReleaseComObject($xl) | Out-Null } catch {}
}

Start-Sleep -Seconds 3
$target = if ($Impresora -ne "") { $Impresora } else { (Get-CimInstance Win32_Printer -Filter 'Default=True').Name }
Write-Output ""
Write-Output "=== Cola de '$target' tras enviar ==="
$j = Get-PrintJob -PrinterName $target -ErrorAction SilentlyContinue
if ($j) { $j | Select-Object Id, DocumentName, JobStatus, @{n='Pgs';e={$_.TotalPages}} | Format-Table -Auto -Wrap }
else { Write-Output "  (sin trabajos: o imprimio muy rapido o no entro; revisar la impresora)" }
