# diagnostico_impresora.ps1  (ASCII, PS 5.1 seguro)
# Diagnostico rapido de impresion: impresoras, predeterminada, estado,
# cola, trabajos zombi y spooler.
#   Uso:  powershell -ExecutionPolicy Bypass -File diagnostico_impresora.ps1

Write-Output "=== Impresoras + estado ==="
Get-CimInstance Win32_Printer |
  Select-Object Name, Default, WorkOffline,
    @{n='EstadoCod';e={$_.PrinterStatus}},
    @{n='ErrorCod';e={$_.DetectedErrorState}} |
  Format-Table -Auto -Wrap
Write-Output "  (EstadoCod: 3=Lista 4=Imprimiendo 7=Offline | ErrorCod: 0=sin error 2=sin papel 5=sin tinta 9=offline)"

Write-Output ""
Write-Output "=== Cola de impresion (todos). 'Error/Retained' = zombi ==="
$zombis = New-Object System.Collections.ArrayList
foreach ($pr in (Get-Printer)) {
  $p = $pr.Name
  $jobs = Get-PrintJob -PrinterName $p -ErrorAction SilentlyContinue
  foreach ($jb in $jobs) {
    [pscustomobject]@{ Impresora=$p; Id=$jb.Id; Doc=$jb.DocumentName; Estado=$jb.JobStatus }
    if ($jb.JobStatus -match 'Error|Retained') { [void]$zombis.Add("$p / Id $($jb.Id)") }
  }
}
Write-Output ""
Write-Output "=== Servicio Spooler ==="
Get-Service Spooler | Select-Object Name, Status, StartType | Format-Table -Auto

if ($zombis.Count -gt 0) {
  Write-Output ""
  Write-Output "*** TRABAJOS ZOMBI DETECTADOS: ***"
  foreach ($z in $zombis) { Write-Output "    $z" }
  Write-Output "    Purga con ADMIN: ver el comando de 3 pasos en el SKILL.md de esta skill."
}
