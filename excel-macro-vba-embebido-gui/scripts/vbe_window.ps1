# vbe_window.ps1 -- utilidades de ventana para manejar el editor VBA por GUI
#
#   .\vbe_window.ps1 list                 -> lista ventanas del proceso EXCEL (clase | visible | titulo)
#   .\vbe_window.ps1 find                 -> dice si el VBE esta abierto
#   .\vbe_window.ps1 focus  [clase]       -> trae la ventana al frente (default: VBE)
#   .\vbe_window.ps1 move   <x> <y> <w> <h> [clase]
#
# Clases utiles:  wndclass_desked_gsk = editor VBA   |   XLMAIN = ventana de Excel
#
# NOTA: ejecutar SIEMPRE fuera del sandbox (dangerouslyDisableSandbox) para que
# actue sobre el Excel real del usuario.

param(
  [Parameter(Position=0)][string]$Action = "list",
  [Parameter(Position=1)]$A1,
  [Parameter(Position=2)]$A2,
  [Parameter(Position=3)]$A3,
  [Parameter(Position=4)]$A4,
  [Parameter(Position=5)][string]$Cls = "wndclass_desked_gsk"
)

$sig = @'
using System;using System.Text;using System.Runtime.InteropServices;using System.Collections.Generic;
public class VW{
 [DllImport("user32.dll")] public static extern bool EnumWindows(EnumWindowsProc cb,IntPtr l);
 public delegate bool EnumWindowsProc(IntPtr h,IntPtr l);
 [DllImport("user32.dll")] public static extern int GetClassName(IntPtr h,StringBuilder s,int m);
 [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h,StringBuilder s,int m);
 [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
 [DllImport("user32.dll")] public static extern int GetWindowThreadProcessId(IntPtr h,out int p);
 [DllImport("user32.dll")] public static extern bool MoveWindow(IntPtr h,int x,int y,int w,int t,bool r);
 [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
 [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h,int c);
 [DllImport("user32.dll")] public static extern bool BringWindowToTop(IntPtr h);
 [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
 [DllImport("user32.dll")] public static extern bool AttachThreadInput(uint a,uint b,bool c);
 [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr h,IntPtr p);
 [DllImport("kernel32.dll")] public static extern uint GetCurrentThreadId();

 public static List<string> ListFor(int pid){var r=new List<string>();
  EnumWindows((h,l)=>{int p;GetWindowThreadProcessId(h,out p);if(p==pid){
   var c=new StringBuilder(256);GetClassName(h,c,256);
   var t=new StringBuilder(256);GetWindowText(h,t,256);
   r.Add(c.ToString()+" | vis="+IsWindowVisible(h)+" | "+t.ToString());}
   return true;},IntPtr.Zero);return r;}

 // Busca por clase. requireTitle=true evita las ventanas fantasma sin titulo (XLMAIN duplicada).
 public static IntPtr Find(string cls,bool requireTitle){IntPtr f=IntPtr.Zero;
  EnumWindows((h,l)=>{var c=new StringBuilder(256);GetClassName(h,c,256);
   if(c.ToString()==cls){
     if(requireTitle){var t=new StringBuilder(256);GetWindowText(h,t,256);
       if(t.Length==0) return true;}
     f=h;return false;}
   return true;},IntPtr.Zero);return f;}

 // Foco robusto: sin AttachThreadInput Windows suele IGNORAR SetForegroundWindow.
 public static void Force(IntPtr h){
  uint fg=GetWindowThreadProcessId(GetForegroundWindow(),IntPtr.Zero);
  uint me=GetCurrentThreadId();
  AttachThreadInput(fg,me,true);
  BringWindowToTop(h);SetForegroundWindow(h);
  AttachThreadInput(fg,me,false);}

 public static string FgClass(){var c=new StringBuilder(256);GetClassName(GetForegroundWindow(),c,256);return c.ToString();}
}
'@
Add-Type -TypeDefinition $sig

switch ($Action.ToLower()) {

  "list" {
    $p = Get-Process EXCEL -EA SilentlyContinue
    if (-not $p) { Write-Output "Excel no esta corriendo"; break }
    Write-Output "PID Excel: $($p.Id)"
    [VW]::ListFor($p.Id) | ForEach-Object { Write-Output "  $_" }
  }

  "find" {
    $h = [VW]::Find($Cls, $false)
    if ($h -eq [IntPtr]::Zero) { Write-Output "NO abierto: $Cls" }
    else { Write-Output "abierto: $Cls  handle=$h" }
  }

  "focus" {
    $c = if ($A1) { [string]$A1 } else { $Cls }
    $h = [VW]::Find($c, ($c -eq "XLMAIN"))
    if ($h -eq [IntPtr]::Zero) { Write-Output "no encontrada: $c"; break }
    [VW]::ShowWindow($h,9) | Out-Null      # 9 = SW_RESTORE
    [VW]::Force($h)
    Start-Sleep -Milliseconds 700
    Write-Output "al frente ahora: $([VW]::FgClass())   (esperado: $c)"
  }

  "move" {
    $h = [VW]::Find($Cls, ($Cls -eq "XLMAIN"))
    if ($h -eq [IntPtr]::Zero) { Write-Output "no encontrada: $Cls"; break }
    [VW]::ShowWindow($h,1) | Out-Null      # 1 = SW_NORMAL (hay que des-maximizar para mover)
    [VW]::MoveWindow($h,[int]$A1,[int]$A2,[int]$A3,[int]$A4,$true) | Out-Null
    [VW]::Force($h)
    Start-Sleep -Milliseconds 700
    Write-Output "movida a ($A1,$A2) $A3 x $A4 | al frente: $([VW]::FgClass())"
  }

  default { Write-Output "Accion no reconocida. Use: list | find | focus | move" }
}

# --- Referencia de monitores de ESTE equipo (2026-07-24) ---
#   \\.\DISPLAY2  Primary=True   0,0     1536x864   <- TIENE ESCALADO DPI: los clics se desvian
#   \\.\DISPLAY3  Primary=False  1920,0  1366x768   <- responde EXACTO, preferir para trabajo por clics
#
#   Ejemplo: llevar el editor VBA al monitor bueno
#     .\vbe_window.ps1 move 1930 10 1346 740
