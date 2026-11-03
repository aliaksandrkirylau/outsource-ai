@echo off
rem Opens the OE prototype in the browser. Needs Python (py or python) for a small local web server.
cd /d "%~dp0"
where py >nul 2>nul && (set PY=py) || (set PY=python)
start "OE prototype server - close to stop" %PY% -m http.server 8000
timeout /t 2 >nul
start "" http://localhost:8000/Demo.dc.html
