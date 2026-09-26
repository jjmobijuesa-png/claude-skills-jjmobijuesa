# ProbarCable2.ps1 - verifica si una SALIDA virtual alimenta a una ENTRADA virtual.
# Abre una sesion de captura real (SpeechRecognitionEngine) sobre la entrada
# predeterminada y mide su AudioLevel mientras reproduce un WAV en la salida.
# Un medidor IAudioMeterInformation NO sirve aqui: en un endpoint de captura
# devuelve 0 mientras no exista una sesion de captura activa.
param(
    [string]$Salida  = 'PalabraMicrophone',
    [string]$Entrada = 'PalabraMicrophone',
    [string]$Wav     = ''
)

if (-not $Wav) { $Wav = Join-Path $PSScriptRoot 'saludo_diana.wav' }
if (-not (Test-Path $Wav)) { Write-Host "No existe el WAV: $Wav" -ForegroundColor Red; exit 1 }

$ruta = Join-Path $PSScriptRoot 'audio_ruta.ps1'
Write-Host ("--- Salida  -> {0}" -f $Salida)
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File $ruta -Fijar $Salida  -Flujo Render  -Rol Todos | Out-Host
Write-Host ("--- Entrada -> {0}" -f $Entrada)
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File $ruta -Fijar $Entrada -Flujo Capture -Rol Todos | Out-Host

Add-Type -AssemblyName System.Speech
$eng = New-Object System.Speech.Recognition.SpeechRecognitionEngine
try {
    $eng.SetInputToDefaultAudioDevice()
} catch {
    Write-Host ("No se pudo abrir la entrada predeterminada: " + $_.Exception.Message) -ForegroundColor Red
    exit 1
}
$g = New-Object System.Speech.Recognition.DictationGrammar
$eng.LoadGrammar($g)
$eng.RecognizeAsync([System.Speech.Recognition.RecognizeMode]::Multiple)

Start-Sleep -Milliseconds 800   # que la sesion de captura arranque

$player = New-Object System.Media.SoundPlayer $Wav
$player.Load()
$player.Play()

$max = 0
$fin = (Get-Date).AddSeconds(10)
while ((Get-Date) -lt $fin) {
    $l = $eng.AudioLevel
    if ($l -gt $max) { $max = $l }
    Start-Sleep -Milliseconds 40
}
$player.Stop()
$eng.RecognizeAsyncStop()
$eng.Dispose()

Write-Host ""
Write-Host ("Nivel maximo captado en la entrada '{0}': {1} / 100" -f $Entrada, $max)
if ($max -gt 3) {
    Write-Host "==> CABLE VIRTUAL OPERATIVO: la voz llega a ese microfono." -ForegroundColor Green
} else {
    Write-Host "==> Sin senal en esa entrada." -ForegroundColor Yellow
}
