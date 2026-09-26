# REPARAR_ADMIN.ps1 — reparaciones que EXIGEN privilegios de administrador
# Se lanza desde REPARAR_ADMIN.bat (clic derecho -> Ejecutar como administrador).
#
# Que hace (todo reversible, todo registrado en el log):
#   1. Reactiva el ARCHIVO DE PAGINACION gestionado por Windows  <- critico
#   2. Pone servicios de emuladores (WSA / BlueStacks) en Manual
#   3. Purga la cola de impresion (trabajos zombi)
#   4. Muestra un resumen del estado de memoria
#
# NO borra archivos del usuario. NO desinstala nada.

$log = Join-Path $PSScriptRoot "reparacion_log.txt"
function W($m){
  $line = "[{0}] {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $m
  Add-Content -Path $log -Value $line -Encoding utf8
  Write-Host $line
}

$elevado = ([Security.Principal.WindowsPrincipal]::new([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
W "===== INICIO REPARACION (elevado=$elevado) ====="
if (-not $elevado) {
  W "ERROR: no se esta ejecutando como administrador. Cierra y usa clic derecho -> Ejecutar como administrador."
  Read-Host "Pulsa ENTER para salir"
  exit 1
}

# ---------- 1. ARCHIVO DE PAGINACION (la causa raiz) ----------
W "--- Paso 1: archivo de paginacion ---"
try {
  $cs = Get-CimInstance Win32_ComputerSystem
  W ("  AutomaticManagedPagefile antes: " + $cs.AutomaticManagedPagefile)
  if (-not $cs.AutomaticManagedPagefile) {
    Set-CimInstance -InputObject $cs -Property @{AutomaticManagedPagefile=$true} -ErrorAction Stop
    Start-Sleep -Seconds 2
    $cs2 = Get-CimInstance Win32_ComputerSystem
    W ("  AutomaticManagedPagefile ahora : " + $cs2.AutomaticManagedPagefile)
    if ($cs2.AutomaticManagedPagefile) { W "  OK -> Windows gestionara la memoria virtual. SE APLICA AL REINICIAR." }
    else { W "  ATENCION: no cambio." }
  } else { W "  Ya estaba activo." }
} catch { W ("  ERROR: " + $_.Exception.Message) }

# ---------- 2. SERVICIOS DE EMULADORES ----------
W "--- Paso 2: servicios de emuladores a Manual ---"
foreach ($svcName in @('WSAIFabricSvc','WsaService','BstHdAndroidSvc','BlueStacksAndroidSvc')) {
  $s = Get-Service -Name $svcName -ErrorAction SilentlyContinue
  if ($s) {
    try {
      if ($s.StartType -eq 'Automatic') {
        Set-Service -Name $svcName -StartupType Manual -ErrorAction Stop
        W ("  {0}: Automatic -> Manual" -f $svcName)
      } else { W ("  {0}: ya estaba en {1}" -f $svcName, $s.StartType) }
    } catch { W ("  {0}: no se pudo cambiar ({1})" -f $svcName, $_.Exception.Message) }
  }
}

# ---------- 3. COLA DE IMPRESION ----------
W "--- Paso 3: purgar cola de impresion ---"
try {
  Stop-Service Spooler -Force -ErrorAction Stop
  Start-Sleep -Seconds 2
  $spool = Join-Path $env:SystemRoot "System32\spool\PRINTERS"
  $n = @(Get-ChildItem $spool -File -ErrorAction SilentlyContinue).Count
  Get-ChildItem $spool -File -ErrorAction SilentlyContinue | Remove-Item -Force -ErrorAction SilentlyContinue
  Start-Service Spooler -ErrorAction Stop
  W ("  Cola purgada ({0} archivos). Spooler reiniciado." -f $n)
} catch { W ("  ERROR en spooler: " + $_.Exception.Message) }

# ---------- 4. RESUMEN ----------
W "--- Estado de memoria ---"
$os = Get-CimInstance Win32_OperatingSystem
$ram = [math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory/1GB,2)
W ("  RAM fisica     : {0} GB" -f $ram)
W ("  Libre ahora    : {0} GB" -f [math]::Round($os.FreePhysicalMemory/1MB,2))
W ("  Limite commit  : {0} GB  (subira tras reiniciar)" -f [math]::Round($os.TotalVirtualMemorySize/1MB,2))
W "===== FIN ====="
Write-Host ""
Write-Host "REINICIA EL EQUIPO para que el archivo de paginacion entre en vigor." -ForegroundColor Yellow
Read-Host "Pulsa ENTER para cerrar"
