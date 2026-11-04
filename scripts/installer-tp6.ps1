param()
$ErrorActionPreference = 'Stop'
$racineTp6 = Split-Path -Parent $PSScriptRoot
Push-Location $racineTp6
try {
    if (-not (Test-Path '.venv311/Scripts/python.exe')) {
        py -3.11 -m venv .venv311
        if ($LASTEXITCODE -ne 0) { throw 'Python 3.11 est requis.' }
    }
    & ./.venv311/Scripts/python.exe -m pip install -r requirements-tp6.txt -r requirements-dev.txt
    if ($LASTEXITCODE -ne 0) { throw 'Installation des dépendances échouée.' }
    & ./.venv311/Scripts/python.exe -m pip install -e '.[ui]'
    if ($LASTEXITCODE -ne 0) { throw 'Installation du paquet échouée.' }
    & ./.venv311/Scripts/python.exe src/make_demo.py
    if ($LASTEXITCODE -ne 0) { throw 'Génération des données échouée.' }
    & ./.venv311/Scripts/python.exe src/train.py
    if ($LASTEXITCODE -ne 0) { throw 'Entraînement échoué.' }
    Write-Host 'Prêt. Activez : .\.venv311\Scripts\Activate.ps1'
} finally {
    Pop-Location
}
