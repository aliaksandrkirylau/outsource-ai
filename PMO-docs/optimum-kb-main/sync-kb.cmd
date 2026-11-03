@echo off
rem Double-click to sync the team KB, for people without an AI agent.
rem Runs tools\kb-sync.sh with the bash that ships with Git for Windows. Lives at the repo root.
cd /d "%~dp0"
"%ProgramFiles%\Git\bin\bash.exe" tools/kb-sync.sh
echo.
pause
