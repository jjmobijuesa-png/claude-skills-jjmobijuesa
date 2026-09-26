# diagnostico.ps1 - Barrido forense de cuelgues y caidas en Windows.
#
# No repara nada: solo observa y ordena la evidencia. Cubre de una pasada las
# causas que en la practica explican casi todos los "se congela el Explorador"
# y "se cierra solo el programa".
#
#   .\diagnostico.ps1                    # barrido completo, 30 dias
#   .\diagnostico.ps1 -Dias 60           # ventana mas larga
#   .\diagnostico.ps1 -App EXCEL         # centrado en un programa
#
# No requiere administrador.

param(
    [int]$Dias = 30,
    [string]$App = ''
)

$ErrorActionPreference = 'SilentlyContinue'
$MB = 1048576
$GB = 1073741824
$desde = (Get-Date).AddDays(-$Dias)

function Titulo($t) {
    Write-Host ""
    Write-Host ("=== " + $t + " ") -NoNewline -ForegroundColor Cyan
    Write-Host ("=" * [Math]::Max(4, 66 - $t.Length)) -ForegroundColor Cyan
}
function Nota($t) { Write-Host ("    " + $t) -ForegroundColor DarkGray }
function Alerta($t) { Write-Host ("  >> " + $t) -ForegroundColor Yellow }

Write-Host ""
Write-Host ("BARRIDO FORENSE - " + (Get-Date -Format 'yyyy-MM-dd HH:mm') + " - ultimos $Dias dias") -ForegroundColor White

# ---------------------------------------------------------------------------
Titulo "1. CUELGUES (evento 1002) - el programa ESPERA algo"
# El campo P6 del informe WER nombra el proceso implicado en un cuelgue
# cross-process. Es la pista mas valiosa y casi nadie la mira.
$colgados = Get-WinEvent -FilterHashtable @{LogName='Application'; Id=1002; StartTime=$desde} -MaxEvents 100
if (-not $colgados) { Nota "ninguno" }
else {
    $colgados | ForEach-Object {
        $n = $_.Properties[0].Value
        [pscustomobject]@{ Fecha = $_.TimeCreated; Programa = $n }
    } | Group-Object Programa | Sort-Object Count -Descending |
      Select-Object Count, Name, @{n='Ultima';e={($_.Group | Sort-Object Fecha -Descending)[0].Fecha}} |
      Format-Table -AutoSize | Out-String -Width 110 | Write-Host

    Titulo "1b. FIRMAS WER DE LOS CUELGUES (P6 = proceso implicado)"
    Get-WinEvent -FilterHashtable @{LogName='Application'; Id=1001; StartTime=$desde} -MaxEvents 400 |
      Where-Object { $_.Message -match 'AppHang' } |
      Select-Object -First 8 | ForEach-Object {
        Write-Host ("    ---- " + $_.TimeCreated + " ----") -ForegroundColor DarkGray
        ($_.Message -split "`n") | Where-Object { $_ -match '^\s*P[0-9]' -and $_ -notmatch ':\s*$' } |
          ForEach-Object { Write-Host ("      " + $_.Trim()) }
      }
    Nota "P1 = programa colgado. P6 = el proceso al que estaba esperando."
}

# ---------------------------------------------------------------------------
Titulo "2. CAIDAS (evento 1000) - huella modulo + desplazamiento"
# Agrupar por modulo Y desplazamiento: si el offset se repite, es UN fallo
# reproducible, no corrupcion aleatoria de memoria.
$f = @{LogName='Application'; Id=1000; StartTime=$desde}
$caidas = Get-WinEvent -FilterHashtable $f -MaxEvents 500 | ForEach-Object {
    $p = $_.Properties
    [pscustomobject]@{
        Fecha=$_.TimeCreated; Programa=$p[0].Value; VerApp=$p[1].Value
        Modulo=$p[3].Value; VerMod=$p[4].Value; Excepcion=$p[6].Value; Offset=$p[7].Value
    }
}
if ($App) { $caidas = $caidas | Where-Object { $_.Programa -match $App } }
if (-not $caidas) { Nota "ninguna" }
else {
    $caidas | Group-Object Programa, Modulo, Excepcion, Offset | Sort-Object Count -Descending |
      Select-Object -First 15 Count, @{n='Programa / Modulo / Excepcion / Offset';e={$_.Name}},
        @{n='Ultima';e={($_.Group | Sort-Object Fecha -Descending)[0].Fecha}} |
      Format-Table -AutoSize | Out-String -Width 150 | Write-Host
    $rep = $caidas | Group-Object Modulo, Offset | Where-Object { $_.Count -ge 3 }
    foreach ($r in $rep) { Alerta ("Offset repetido " + $r.Count + " veces: " + $r.Name + "  -> fallo REPRODUCIBLE, mismo punto de codigo") }
}

# ---------------------------------------------------------------------------
Titulo "3. UNIDADES Y RUTAS DE RED (causa n.1 de Explorador congelado)"
Get-CimInstance Win32_LogicalDisk | ForEach-Object {
    [pscustomobject]@{
        Unidad=$_.DeviceID; Tipo=$_.DriveType; Nombre=$_.VolumeName
        Libre_GB = if ($_.FreeSpace) { [math]::Round($_.FreeSpace / $GB,1) } else { 'SIN RESPUESTA' }
    }
} | Format-Table -AutoSize | Out-String -Width 90 | Write-Host
Nota "Tipo: 2=extraible, 3=local, 4=RED, 5=CD"

$map = Get-SmbMapping
if ($map) {
    $map | Format-Table -AutoSize | Out-String -Width 120 | Write-Host
    foreach ($m in $map) {
        if ($m.Status -ne 'OK') {
            Alerta ("Unidad " + $m.LocalPath + " -> " + $m.RemotePath + " en estado " + $m.Status)
            Alerta "  Una unidad de red muerta congela el Explorador en CADA enumeracion"
            Alerta "  de unidades: 'Este equipo', panel de navegacion, dialogos de archivo."
            $srv = ($m.RemotePath -split '\\')[2]
            $c = New-Object System.Net.Sockets.TcpClient
            $ar = $c.BeginConnect($srv, 445, $null, $null)
            $ok = $ar.AsyncWaitHandle.WaitOne(4000, $false)
            if ($ok -and $c.Connected) { Nota ("  SMB 445 en " + $srv + ": abierto") }
            else { Alerta ("  SMB 445 en " + $srv + ": NO responde") }
            $c.Close()
        }
    }
    Nota "Se quita con:  Remove-SmbMapping -LocalPath 'X:' -Force -UpdateProfile"
    Nota "y borrando HKCU:\Network\X para que no vuelva al reiniciar."
} else { Nota "sin unidades de red mapeadas" }

$ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -notlike '127.*' -and $_.IPAddress -notlike '169.254.*' }).IPAddress
Nota ("IP actual del equipo: " + ($ip -join ', ') + "   <- comparar la subred con la del servidor")

# ---------------------------------------------------------------------------
Titulo "4. SUPERPOSICIONES DE ICONO (Windows solo procesa 15)"
$ov = Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers' | Sort-Object PSChildName
$i = 0
foreach ($o in $ov) {
    $i++
    $clsid = (Get-ItemProperty $o.PSPath).'(default)'
    $dll = (Get-ItemProperty ('HKLM:\SOFTWARE\Classes\CLSID\' + $clsid + '\InprocServer32')).'(default)'
    $marca = if ($i -le 15) { '        ' } else { 'IGNORADA' }
    Write-Host ("    {0,2}. {1,-42} {2}  {3}" -f $i, $o.PSChildName.Trim(), $marca, $dll)
}
if ($i -gt 15) { Alerta ("Hay $i registradas y el limite duro son 15. Se consultan de forma") ; Alerta "  SINCRONA por cada archivo mostrado: cada sincronizador extra pesa." }

# ---------------------------------------------------------------------------
Titulo "5. CONTROLADORES DE VISTA PREVIA"
$ph = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\PreviewHandlers'
$ph.PSObject.Properties | Where-Object { $_.Name -like '{*' } | ForEach-Object {
    $dll = (Get-ItemProperty ('HKLM:\SOFTWARE\Classes\CLSID\' + $_.Name + '\InprocServer32')).'(default)'
    $sos = if ($_.Value -match 'Adobe') { '  <-- causa clasica de cuelgues' } else { '' }
    Write-Host ("    {0,-38} {1}{2}" -f $_.Value, $dll, $sos)
}

# ---------------------------------------------------------------------------
Titulo "6. PROCESOS DE OFFICE HUERFANOS (-Embedding, sin ventana)"
# Un WINWORD/EXCEL -Embedding lanzado por svchost es ACTIVACION COM: alguien
# pidio a Windows arrancar Office fuera de proceso. Tipicamente el controlador
# de vista previa o de miniatura del Explorador. Si se queda colgado, bloquea.
$emb = Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE' OR Name='EXCEL.EXE' OR Name='POWERPNT.EXE'"
$hay = $false
foreach ($e in $emb) {
    $pr = Get-Process -Id $e.ProcessId
    if ($e.CommandLine -match 'Embedding' -and $pr.MainWindowTitle -eq '') {
        $hay = $true
        $padre = (Get-CimInstance Win32_Process -Filter ("ProcessId=" + $e.ParentProcessId)).Name
        Alerta ($e.Name + " PID " + $e.ProcessId + " -Embedding, sin ventana, padre " + $padre + ", desde " + $e.CreationDate)
    }
}
if (-not $hay) { Nota "ninguno" }

# ---------------------------------------------------------------------------
Titulo "7. COMPLEMENTOS DE OFFICE QUE CARGAN AL INICIO"
foreach ($app in @('Excel','Word','PowerPoint','Outlook')) {
    foreach ($raiz in @('HKCU:\SOFTWARE\Microsoft\Office\', 'HKLM:\SOFTWARE\Microsoft\Office\', 'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Office\')) {
        $p = $raiz + $app + '\Addins'
        foreach ($a in (Get-ChildItem $p)) {
            $lb = (Get-ItemProperty $a.PSPath).LoadBehavior
            if ($lb -eq 3 -or $lb -eq 16) {
                Write-Host ("    {0,-12} {1,-58} carga al inicio" -f $app, $a.PSChildName)
            }
        }
    }
}
Nota "Para desactivar uno: LoadBehavior = 2 en su clave (reversible, sin admin)."

# ---------------------------------------------------------------------------
Titulo "8. SALUD FISICA DE LOS DISCOS"
Get-PhysicalDisk | Select-Object DeviceId, FriendlyName, MediaType, HealthStatus, OperationalStatus |
    Format-Table -AutoSize | Out-String -Width 120 | Write-Host
$err = Get-WinEvent -FilterHashtable @{LogName='System'; StartTime=$desde} -MaxEvents 2000 |
       Where-Object { $_.ProviderName -match 'disk|Ntfs|volmgr|storahci' -and $_.LevelDisplayName -match 'Error' }
if ($err) { Alerta ("Hay " + $err.Count + " errores de disco o NTFS en el registro del sistema") }
else { Nota "sin errores de disco ni de NTFS" }

Write-Host ""
Write-Host "Barrido terminado." -ForegroundColor White
Write-Host ""
exit 0
