@echo off

rem determine the script directory (could be in scripts, could be in root folder)
set "SCRIPT_DIR=%~dp0"
if not exist "%SCRIPT_DIR%\python.bat" (
    set "SCRIPT_DIR=%SCRIPT_DIR%\scripts"
)

rem (we won't be using cron call) "%SCRIPT_DIR%\cronstop.bat"
call "%SCRIPT_DIR%\serverstop.bat"

echo.
echo The KA Lite server was stopped.
