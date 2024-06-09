Set-Location $PSScriptRoot
Set-Location "../"

$envPath = $(pipenv --venv)
$env:PATH = "$envPath\Scripts;" + $env:PATH

$env:DJANGO_DEBUG = "False";
$env:DJANGO_SETTINGS_MODULE = "DjangoServer.settings"; uvicorn DjangoServer.asgi:application --host 0.0.0.0 --port 443
