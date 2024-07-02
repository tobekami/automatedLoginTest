@echo off
:: Check for admin rights
openfiles >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrative privileges...
    powershell -command "Start-Process cmd -ArgumentList '/c %~s0 {automatedLoginTest.py}' -Verb RunAs"
    exit /b
)

:: Run the Python script
python %1