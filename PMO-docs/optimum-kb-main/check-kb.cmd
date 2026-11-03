@echo off
rem Double-click to check this computer is set up for the team KB (changes nothing).
rem Runs tools\kb-doctor.sh with the bash that ships with Git for Windows. Lives at the repo root.
cd /d "%~dp0"
"%ProgramFiles%\Git\bin\bash.exe" tools/kb-doctor.sh
echo.
pause
