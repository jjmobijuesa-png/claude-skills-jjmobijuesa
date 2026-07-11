@echo off
REM ============================================================
REM Lanza UI-TARS Desktop (control GUI del escritorio via VLM local).
REM Pre-requisito: Ollama corriendo con un modelo de vision
REM (qwen2.5vl:7b). Este .bat verifica Ollama y arranca la app.
REM ============================================================

echo [1/3] Verificando servidor Ollama en :11434 ...
powershell -NoProfile -Command "if (Test-NetConnection -ComputerName localhost -Port 11434 -InformationLevel Quiet) { exit 0 } else { exit 1 }"
if errorlevel 1 (
    echo   Ollama NO responde. Arrancando servicio...
    start "" "C:\Users\datos\AppData\Local\Programs\Ollama\ollama app.exe"
    timeout /t 8 /nobreak >nul
) else (
    echo   Ollama OK.
)

echo [2/3] Verificando modelo de vision qwen2.5vl:7b ...
"C:\Users\datos\AppData\Local\Programs\Ollama\ollama.exe" list | findstr /C:"qwen2.5vl" >nul
if errorlevel 1 (
    echo   Modelo NO instalado. Descargando (~6 GB, una sola vez)...
    "C:\Users\datos\AppData\Local\Programs\Ollama\ollama.exe" pull qwen2.5vl:7b
) else (
    echo   Modelo de vision OK.
)

echo [3/3] Arrancando UI-TARS Desktop ...
start "" "C:\Users\datos\AppData\Local\UiTars\UI-TARS.exe"
echo.
echo UI-TARS Desktop lanzado. Config: espanol + Ollama local + operador de escritorio.
echo En la ventana de la app, escribe la tarea de control GUI en espanol.
