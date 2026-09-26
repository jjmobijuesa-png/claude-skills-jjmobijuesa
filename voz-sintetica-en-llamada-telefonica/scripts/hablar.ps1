# hablar.ps1 - sintetiza voz con una voz OneCore (p.ej. Raul, masculina es-MX)
# y la reproduce por el dispositivo de audio predeterminado.
param(
    [Parameter(Mandatory=$true)][string]$Texto,
    [string]$Voz = 'Raul',
    [string]$GuardarEn = '',
    [switch]$NoReproducir
)

Add-Type -AssemblyName System.Runtime.WindowsRuntime

$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() |
    Where-Object { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and
                   $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]

function Await($op, $tipo) {
    $m = $asTaskGeneric.MakeGenericMethod($tipo)
    $t = $m.Invoke($null, @($op))
    $t.Wait(-1) | Out-Null
    $t.Result
}

$null = [Windows.Media.SpeechSynthesis.SpeechSynthesizer, Windows.Media, ContentType=WindowsRuntime]
$null = [Windows.Storage.Streams.DataReader, Windows.Storage.Streams, ContentType=WindowsRuntime]

$synth = New-Object Windows.Media.SpeechSynthesis.SpeechSynthesizer

$elegida = [Windows.Media.SpeechSynthesis.SpeechSynthesizer]::AllVoices |
    Where-Object { $_.DisplayName -match $Voz } | Select-Object -First 1
if (-not $elegida) {
    Write-Host "Voz '$Voz' no encontrada. Disponibles:"
    [Windows.Media.SpeechSynthesis.SpeechSynthesizer]::AllVoices |
        ForEach-Object { Write-Host ("  {0}  [{1}]  {2}" -f $_.DisplayName, $_.Gender, $_.Language) }
    exit 1
}
$synth.Voice = $elegida
Write-Host ("Voz: {0}  [{1}]  {2}" -f $elegida.DisplayName, $elegida.Gender, $elegida.Language)

$stream = Await ($synth.SynthesizeTextToStreamAsync($Texto)) ([Windows.Media.SpeechSynthesis.SpeechSynthesisStream])

$size   = [uint32]$stream.Size
$reader = New-Object Windows.Storage.Streams.DataReader($stream.GetInputStreamAt(0))
$null   = Await ($reader.LoadAsync($size)) ([uint32])
$bytes  = New-Object byte[] $size
$reader.ReadBytes($bytes)
$reader.Dispose()

if (-not $GuardarEn) {
    $GuardarEn = Join-Path $env:TEMP ("tts_" + [guid]::NewGuid().ToString('N').Substring(0,8) + ".wav")
}
[System.IO.File]::WriteAllBytes($GuardarEn, $bytes)
Write-Host ("WAV: {0}  ({1:N0} bytes)" -f $GuardarEn, $bytes.Length)

if (-not $NoReproducir) {
    $p = New-Object System.Media.SoundPlayer $GuardarEn
    $p.PlaySync()
    Write-Host "Reproducido."
}
