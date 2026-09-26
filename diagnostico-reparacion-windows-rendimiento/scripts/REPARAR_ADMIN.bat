@echo off
REM ============================================================
REM  REPARACION DEL SISTEMA  -  CLIC DERECHO -> EJECUTAR COMO ADMINISTRADOR
REM  Reactiva el archivo de paginacion (causa raiz de las caidas),
REM  pone los emuladores en Manual y purga la cola de impresion.
REM ============================================================
net session >nul 2>&1
if %errorlevel% neq 0 (
  echo.
  echo  *** NO se esta ejecutando como ADMINISTRADOR ***
  echo  Cierra esta ventana, haz CLIC DERECHO sobre REPARAR_ADMIN.bat
  echo  y elige "Ejecutar como administrador".
  echo.
  pause
  exit /b 1
)
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0REPARAR_ADMIN.ps1"
