# AudioRuta.ps1 - lista y cambia el dispositivo de audio predeterminado de Windows
# usando las interfaces COM IMMDeviceEnumerator e IPolicyConfig. Sin descargas,
# sin administrador.
#
#   .\AudioRuta.ps1 -Listar
#   .\AudioRuta.ps1 -Fijar "PalabraMicrophone" -Flujo Render -Rol Communications

param(
    [switch]$Listar,
    [string]$Fijar = '',
    [ValidateSet('Render','Capture')][string]$Flujo = 'Render',
    [ValidateSet('Console','Multimedia','Communications','Todos')][string]$Rol = 'Todos'
)

$cs = @"
using System;
using System.Runtime.InteropServices;

namespace AudioRuta {

  [StructLayout(LayoutKind.Sequential, Pack = 4)]
  public struct PropertyKey { public Guid fmtid; public int pid; }

  [StructLayout(LayoutKind.Explicit)]
  public struct PropVariant {
    [FieldOffset(0)] public ushort vt;
    [FieldOffset(8)] public IntPtr pwszVal;
  }

  [Guid("A95664D2-9614-4F35-A746-DE8DB63617E6"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
  public interface IMMDeviceEnumerator {
    int EnumAudioEndpoints(int dataFlow, int stateMask, out IMMDeviceCollection devices);
    int GetDefaultAudioEndpoint(int dataFlow, int role, out IMMDevice device);
    int GetDevice(string id, out IMMDevice device);
    int RegisterEndpointNotificationCallback(IntPtr cb);
    int UnregisterEndpointNotificationCallback(IntPtr cb);
  }

  [Guid("0BD7A1BE-7A1A-44DB-8397-CC5392387B5E"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
  public interface IMMDeviceCollection {
    int GetCount(out uint count);
    int Item(uint index, out IMMDevice device);
  }

  [Guid("D666063F-1587-4E43-81F1-B948E807363F"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
  public interface IMMDevice {
    int Activate(ref Guid iid, int clsCtx, IntPtr activationParams, [MarshalAs(UnmanagedType.IUnknown)] out object iface);
    int OpenPropertyStore(int stgmAccess, out IPropertyStore properties);
    int GetId([MarshalAs(UnmanagedType.LPWStr)] out string id);
    int GetState(out int state);
  }

  [Guid("886d8eeb-8cf2-4446-8d02-cdba1dbdcf99"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
  public interface IPropertyStore {
    int GetCount(out uint count);
    int GetAt(uint index, out PropertyKey key);
    int GetValue(ref PropertyKey key, out PropVariant value);
    int SetValue(ref PropertyKey key, ref PropVariant value);
    int Commit();
  }

  [Guid("F8679F50-850A-41CF-9C72-430F290290C8"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
  public interface IPolicyConfig {
    int GetMixFormat(string id, IntPtr f);
    int GetDeviceFormat(string id, bool def, IntPtr f);
    int ResetDeviceFormat(string id);
    int SetDeviceFormat(string id, IntPtr e, IntPtr m);
    int GetProcessingPeriod(string id, bool def, IntPtr d, IntPtr m);
    int SetProcessingPeriod(string id, IntPtr p);
    int GetShareMode(string id, IntPtr m);
    int SetShareMode(string id, IntPtr m);
    int GetPropertyValue(string id, bool store, ref PropertyKey key, out PropVariant v);
    int SetPropertyValue(string id, bool store, ref PropertyKey key, ref PropVariant v);
    int SetDefaultEndpoint(string id, int role);
    int SetEndpointVisibility(string id, bool visible);
  }

  [ComImport, Guid("BCDE0395-E52F-467C-8E3D-C4579291692E")] public class MMDeviceEnumerator { }
  [ComImport, Guid("870AF99C-171D-4F9E-AF0D-E63DF40C2BC9")] public class PolicyConfigClient { }

  public class Dispositivo {
    public string Id; public string Nombre; public string Flujo;
    public override string ToString() { return Flujo + " | " + Nombre; }
  }

  public static class Api {
    static PropertyKey PKEY_FriendlyName() {
      PropertyKey k = new PropertyKey();
      k.fmtid = new Guid("a45c254e-df1c-4efd-8020-67d146a850e0");
      k.pid = 14;
      return k;
    }

    public static Dispositivo[] Listar(int dataFlow) {
      var en = (IMMDeviceEnumerator)(new MMDeviceEnumerator());
      IMMDeviceCollection col;
      en.EnumAudioEndpoints(dataFlow, 1 /*ACTIVE*/, out col);
      uint n; col.GetCount(out n);
      var res = new System.Collections.Generic.List<Dispositivo>();
      for (uint i = 0; i < n; i++) {
        IMMDevice d; col.Item(i, out d);
        string id; d.GetId(out id);
        IPropertyStore ps; d.OpenPropertyStore(0 /*READ*/, out ps);
        PropertyKey k = PKEY_FriendlyName();
        PropVariant v; ps.GetValue(ref k, out v);
        string nombre = v.pwszVal != IntPtr.Zero ? Marshal.PtrToStringUni(v.pwszVal) : "(sin nombre)";
        var item = new Dispositivo();
        item.Id = id; item.Nombre = nombre;
        item.Flujo = (dataFlow == 0) ? "Salida" : "Entrada";
        res.Add(item);
      }
      return res.ToArray();
    }

    public static string PredeterminadoId(int dataFlow, int role) {
      var en = (IMMDeviceEnumerator)(new MMDeviceEnumerator());
      IMMDevice d;
      if (en.GetDefaultAudioEndpoint(dataFlow, role, out d) != 0 || d == null) return null;
      string id; d.GetId(out id); return id;
    }

    public static int Fijar(string id, int role) {
      var pc = (IPolicyConfig)(new PolicyConfigClient());
      return pc.SetDefaultEndpoint(id, role);
    }
  }
}
"@

Add-Type -TypeDefinition $cs -ErrorAction Stop

$flujoNum = if ($Flujo -eq 'Render') { 0 } else { 1 }
$roles = @{ 'Console' = 0; 'Multimedia' = 1; 'Communications' = 2 }

if ($Listar -or -not $Fijar) {
    foreach ($f in 0,1) {
        $etq = if ($f -eq 0) { 'SALIDA (reproduccion)' } else { 'ENTRADA (microfono)' }
        Write-Host ""
        Write-Host "=== $etq ===" -ForegroundColor Cyan
        $defC = [AudioRuta.Api]::PredeterminadoId($f, 0)
        $defM = [AudioRuta.Api]::PredeterminadoId($f, 2)
        foreach ($d in [AudioRuta.Api]::Listar($f)) {
            $marca = ''
            if ($d.Id -eq $defC) { $marca += ' [PREDET]' }
            if ($d.Id -eq $defM) { $marca += ' [COMUNICACIONES]' }
            Write-Host ("  {0}{1}" -f $d.Nombre, $marca)
        }
    }
    Write-Host ""
    return
}

$cands = [AudioRuta.Api]::Listar($flujoNum) | Where-Object { $_.Nombre -like "*$Fijar*" }
if (-not $cands) { Write-Host "No hay dispositivo '$Fijar' en $Flujo." -ForegroundColor Red; exit 1 }
if ($cands.Count -gt 1) {
    Write-Host "Coincidencias multiples; se toma la primera:" -ForegroundColor Yellow
    $cands | ForEach-Object { Write-Host ("   - " + $_.Nombre) }
}
$dev = @($cands)[0]

$aplicar = if ($Rol -eq 'Todos') { @(0,1,2) } else { @($roles[$Rol]) }
foreach ($r in $aplicar) {
    $hr = [AudioRuta.Api]::Fijar($dev.Id, $r)
    $nom = ($roles.GetEnumerator() | Where-Object { $_.Value -eq $r }).Key
    if ($hr -eq 0) { Write-Host ("OK  {0} -> rol {1}" -f $dev.Nombre, $nom) -ForegroundColor Green }
    else { Write-Host ("ERR {0} -> rol {1} (hr=0x{2:X8})" -f $dev.Nombre, $nom, $hr) -ForegroundColor Red }
}
