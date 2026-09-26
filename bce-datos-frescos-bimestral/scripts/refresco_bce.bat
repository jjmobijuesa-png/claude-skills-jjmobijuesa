@echo off
REM ============================================================
REM  Refresco bimestral de indicadores del Banco Central del Ecuador
REM  Lo ejecuta la tarea programada de Windows "BCE_Refresco_Bimestral"
REM  (dia 17 de cada mes par, 09:07). No requiere que Claude este abierto.
REM  Skill: bce-datos-frescos-bimestral
REM ============================================================
setlocal
REM UTF-8 en la consola para que el log no salga con caracteres corruptos
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
set PY=%USERPROFILE%\.notebooklm-venv\Scripts\python.exe
set SCRIPT=%USERPROFILE%\.claude\skills\bce-datos-frescos-bimestral\scripts\extraer_bce.py
set DEST=E:\vars\var 5\BCE-datos
set LOG=%DEST%\refresco.log

if not exist "%DEST%" mkdir "%DEST%"

echo. >> "%LOG%"
echo ============================================================ >> "%LOG%"
echo Inicio: %date% %time% >> "%LOG%"

"%PY%" "%SCRIPT%" --comparar >> "%LOG%" 2>&1

if errorlevel 1 (
  echo RESULTADO: ERROR - revisar el log y correr el script a mano >> "%LOG%"
) else (
  echo RESULTADO: OK >> "%LOG%"
)
echo Fin: %date% %time% >> "%LOG%"
endlocal
