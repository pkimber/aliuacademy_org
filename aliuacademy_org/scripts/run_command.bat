@echo off

rem determine the script directory (could be in scripts, could be in root folder)
set "SCRIPT_DIR=%~dp0"
if exist "%SCRIPT_DIR%\academy" (
    set "KALITE_DIR=%SCRIPT_DIR%\academy"
) else (
    set "SCRIPT_DIR=%SCRIPT_DIR%\scripts"
    set "KALITE_DIR=%SCRIPT_DIR%\..\academy"
)

rem This file will run an arbitrary management command, within the confines of our "sandbox" script
start /b python.exe "%KALITE_DIR%\manage.py" run_sandboxed_command %*
