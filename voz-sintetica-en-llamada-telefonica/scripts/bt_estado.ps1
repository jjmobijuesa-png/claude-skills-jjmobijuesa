# bt_conectar.ps1 - lista dispositivos Bluetooth conectados/recordados y, opcionalmente,
# activa el perfil Manos libres del Infinix usando BluetoothSetServiceState (Win32).
param([switch]$Conectar)

$src = @"
using System;
using System.Runtime.InteropServices;

public static class Bt {
    [StructLayout(LayoutKind.Sequential)]
    public struct SYSTEMTIME { public ushort wYear, wMonth, wDayOfWeek, wDay, wHour, wMinute, wSecond, wMilliseconds; }

    [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
    public struct BLUETOOTH_DEVICE_INFO {
        public uint dwSize;
        public ulong Address;
        public uint ulClassofDevice;
        [MarshalAs(UnmanagedType.Bool)] public bool fConnected;
        [MarshalAs(UnmanagedType.Bool)] public bool fRemembered;
        [MarshalAs(UnmanagedType.Bool)] public bool fAuthenticated;
        public SYSTEMTIME stLastSeen;
        public SYSTEMTIME stLastUsed;
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 248)] public string szName;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct BLUETOOTH_DEVICE_SEARCH_PARAMS {
        public uint dwSize;
        [MarshalAs(UnmanagedType.Bool)] public bool fReturnAuthenticated;
        [MarshalAs(UnmanagedType.Bool)] public bool fReturnRemembered;
        [MarshalAs(UnmanagedType.Bool)] public bool fReturnUnknown;
        [MarshalAs(UnmanagedType.Bool)] public bool fReturnConnected;
        [MarshalAs(UnmanagedType.Bool)] public bool fIssueInquiry;
        public byte cTimeoutMultiplier;
        public IntPtr hRadio;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct BLUETOOTH_FIND_RADIO_PARAMS { public uint dwSize; }

    [DllImport("bthprops.cpl", SetLastError = true)]
    public static extern IntPtr BluetoothFindFirstRadio(ref BLUETOOTH_FIND_RADIO_PARAMS p, out IntPtr hRadio);
    [DllImport("bthprops.cpl", SetLastError = true)]
    public static extern bool BluetoothFindRadioClose(IntPtr hFind);
    [DllImport("bthprops.cpl", SetLastError = true)]
    public static extern IntPtr BluetoothFindFirstDevice(ref BLUETOOTH_DEVICE_SEARCH_PARAMS p, ref BLUETOOTH_DEVICE_INFO i);
    [DllImport("bthprops.cpl", SetLastError = true)]
    public static extern bool BluetoothFindNextDevice(IntPtr hFind, ref BLUETOOTH_DEVICE_INFO i);
    [DllImport("bthprops.cpl", SetLastError = true)]
    public static extern bool BluetoothFindDeviceClose(IntPtr hFind);
    [DllImport("bthprops.cpl", SetLastError = true)]
    public static extern uint BluetoothSetServiceState(IntPtr hRadio, ref BLUETOOTH_DEVICE_INFO i, ref Guid g, uint flags);
}
"@
Add-Type -TypeDefinition $src -ErrorAction Stop

$rp = New-Object Bt+BLUETOOTH_FIND_RADIO_PARAMS
$rp.dwSize = [System.Runtime.InteropServices.Marshal]::SizeOf($rp)
$hRadio = [IntPtr]::Zero
$hFindRadio = [Bt]::BluetoothFindFirstRadio([ref]$rp, [ref]$hRadio)
if ($hFindRadio -eq [IntPtr]::Zero) { Write-Host "No hay radio Bluetooth."; exit 1 }

$sp = New-Object Bt+BLUETOOTH_DEVICE_SEARCH_PARAMS
$sp.dwSize = [System.Runtime.InteropServices.Marshal]::SizeOf($sp)
$sp.fReturnAuthenticated = $true
$sp.fReturnRemembered    = $true
$sp.fReturnUnknown       = $false
$sp.fReturnConnected     = $true
$sp.fIssueInquiry        = $false
$sp.cTimeoutMultiplier   = 2
$sp.hRadio               = $hRadio

$di = New-Object Bt+BLUETOOTH_DEVICE_INFO
$di.dwSize = [System.Runtime.InteropServices.Marshal]::SizeOf($di)

$hFind = [Bt]::BluetoothFindFirstDevice([ref]$sp, [ref]$di)
if ($hFind -eq [IntPtr]::Zero) { Write-Host "Sin dispositivos emparejados."; exit 1 }

$lista = @()
do {
    $lista += [pscustomobject]@{
        Nombre      = $di.szName
        Conectado   = $di.fConnected
        Recordado   = $di.fRemembered
        Autenticado = $di.fAuthenticated
        VistoUlt    = ("{0:d4}-{1:d2}-{2:d2} {3:d2}:{4:d2}" -f $di.stLastSeen.wYear,$di.stLastSeen.wMonth,$di.stLastSeen.wDay,$di.stLastSeen.wHour,$di.stLastSeen.wMinute)
        UsadoUlt    = ("{0:d4}-{1:d2}-{2:d2} {3:d2}:{4:d2}" -f $di.stLastUsed.wYear,$di.stLastUsed.wMonth,$di.stLastUsed.wDay,$di.stLastUsed.wHour,$di.stLastUsed.wMinute)
        Info        = $di
    }
    $di = New-Object Bt+BLUETOOTH_DEVICE_INFO
    $di.dwSize = [System.Runtime.InteropServices.Marshal]::SizeOf($di)
} while ([Bt]::BluetoothFindNextDevice($hFind, [ref]$di))
[void][Bt]::BluetoothFindDeviceClose($hFind)

$lista | Select-Object Nombre, Conectado, Recordado, Autenticado, VistoUlt, UsadoUlt |
    Format-Table -AutoSize | Out-String -Width 160 | Write-Host

if ($Conectar) {
    $infinix = $lista | Where-Object { $_.Nombre -match 'Infinix' } | Select-Object -First 1
    if (-not $infinix) { Write-Host "Infinix no aparece en la lista."; exit 1 }
    $svc = @{
        'Manos libres (HFP)' = [Guid]'0000111e-0000-1000-8000-00805f9b34fb'
        'Audio A2DP sink'    = [Guid]'0000110b-0000-1000-8000-00805f9b34fb'
        'PAN / red'          = [Guid]'00001115-0000-1000-8000-00805f9b34fb'
    }
    $obj = $infinix.Info
    foreach ($k in $svc.Keys) {
        $g = $svc[$k]
        $r = [Bt]::BluetoothSetServiceState($hRadio, [ref]$obj, [ref]$g, 1)
        if ($r -eq 0) { Write-Host "  $k -> ACTIVADO (0)" }
        else { Write-Host ("  {0} -> error {1} : {2}" -f $k, $r, ([ComponentModel.Win32Exception]$r).Message) }
    }
}

[void][Bt]::BluetoothFindRadioClose($hFindRadio)
