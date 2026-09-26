# diagnostico_sistema.ps1 (ASCII, PS 5.1 seguro, SIN elevacion)
# Diagnostico de caidas de aplicaciones y lentitud en Windows.
# Orden deliberado: primero descarta HARDWARE, luego mide MEMORIA VIRTUAL,
# luego identifica el MODULO culpable de cada caida.
#   Uso: powershell -ExecutionPolicy Bypass -File diagnostico_sistema.ps1

Write-Output "=========== 1. MEMORIA Y COMMIT ==========="
$os = Get-CimInstance Win32_OperatingSystem
$cs = Get-CimInstance Win32_ComputerSystem
$ram = [math]::Round($cs.TotalPhysicalMemory/1GB,2)
$commit = [math]::Round($os.TotalVirtualMemorySize/1MB,2)
Write-Output ("  RAM fisica    : {0} GB" -f $ram)
Write-Output ("  Libre         : {0} GB" -f [math]::Round($os.FreePhysicalMemory/1MB,2))
Write-Output ("  Limite commit : {0} GB" -f $commit)
Write-Output ("  Margen virtual: {0} GB" -f [math]::Round($commit-$ram,2))
Write-Output ("  Pagefile auto : {0}" -f $cs.AutomaticManagedPagefile)
$pf = Get-CimInstance Win32_PageFileUsage -ErrorAction SilentlyContinue
if (-not $pf) { Write-Output "  *** ALERTA: NO HAY ARCHIVO DE PAGINACION -> los picos de memoria MATAN aplicaciones ***" }
else { $pf | Select-Object Name, AllocatedBaseSize, CurrentUsage, PeakUsage | Format-Table -Auto }

Write-Output ""
Write-Output "=========== 2. DESCARTAR HARDWARE ==========="
$k41 = @(Get-WinEvent -FilterHashtable @{LogName='System'; Id=41; StartTime=(Get-Date).AddDays(-30)} -ErrorAction SilentlyContinue).Count
$bc  = @(Get-WinEvent -FilterHashtable @{LogName='System'; Id=1001; ProviderName='Microsoft-Windows-WER-SystemErrorReporting'; StartTime=(Get-Date).AddDays(-30)} -ErrorAction SilentlyContinue).Count
$tdr = @(Get-WinEvent -FilterHashtable @{LogName='System'; Id=4101; StartTime=(Get-Date).AddDays(-14)} -ErrorAction SilentlyContinue).Count
Write-Output ("  Apagones inesperados (Kernel-Power 41): {0}" -f $k41)
Write-Output ("  Pantallazos azules (BugCheck)         : {0}" -f $bc)
Write-Output ("  Driver de video colgado (TDR 4101)    : {0}" -f $tdr)
if ($k41 -eq 0 -and $bc -eq 0) { Write-Output "  -> El NUCLEO no cae. El problema esta en aplicaciones / memoria virtual." }
else { Write-Output "  -> Hay caidas de nucleo: revisar RAM (mdsched), temperatura y drivers." }

Write-Output ""
Write-Output "=========== 3. QUIEN SE CAE Y POR QUE (7 dias) ==========="
$ev = Get-WinEvent -FilterHashtable @{LogName='Application'; Id=1000; StartTime=(Get-Date).AddDays(-7)} -ErrorAction SilentlyContinue
Write-Output ("  Total de caidas de aplicacion: {0}" -f @($ev).Count)
$ev | ForEach-Object {
  $p=$_.Properties
  [pscustomobject]@{
    App    = $(if($p[0].Value){$p[0].Value}else{'(vacio)'})
    Modulo = $(if($p.Count -gt 3 -and $p[3].Value){$p[3].Value}else{'?'})
    Exc    = $(if($p.Count -gt 6){$p[6].Value}else{'?'})
  }
} | Group-Object App,Modulo,Exc | Sort-Object Count -Descending | Select-Object -First 12 Count,Name | Format-Table -Auto -Wrap
Write-Output "  Codigos utiles: e0000008 = SIN MEMORIA (Chromium/Edge) | c0000005 = violacion de acceso | c0000409 = desborde de pila"

Write-Output ""
Write-Output "=========== 4. CARGA PERMANENTE ==========="
Write-Output "  -- Top 10 procesos por RAM --"
Get-Process | Sort-Object WS -Descending | Select-Object -First 10 @{n='Proceso';e={$_.ProcessName}}, @{n='RAM_MB';e={[math]::Round($_.WS/1MB,0)}} | Format-Table -Auto
Write-Output "  -- Arranque automatico (HKCU) --"
$run='HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
if (Test-Path $run) { (Get-ItemProperty $run).PSObject.Properties | Where-Object {$_.Name -notmatch '^PS'} | ForEach-Object { Write-Output ("     {0}" -f $_.Name) } }
Write-Output "  -- Emuladores / VMs corriendo --"
$h = Get-Process -ErrorAction SilentlyContinue | Where-Object { $_.ProcessName -match 'ollama|HD-Player|Bst|BlueStacks|vmmem|Wsa|docker|VBox' }
if ($h) { $h | Select-Object ProcessName, @{n='RAM_MB';e={[math]::Round($_.WS/1MB,0)}} | Format-Table -Auto } else { Write-Output "     ninguno (bien)" }

Write-Output ""
Write-Output "=========== 5. DISCO ==========="
Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" | Select-Object DeviceID, @{n='TotalGB';e={[math]::Round($_.Size/1GB,1)}}, @{n='LibreGB';e={[math]::Round($_.FreeSpace/1GB,1)}}, @{n='Libre_pct';e={[math]::Round($_.FreeSpace/$_.Size*100,1)}} | Format-Table -Auto
Write-Output ""
Write-Output "Si el paso 1 marca ALERTA -> ejecuta REPARAR_ADMIN.bat como administrador y REINICIA."
