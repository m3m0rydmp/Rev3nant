@echo off
REM Batch file GUI example for security awareness testing
REM Limited GUI capabilities but can create interactive prompts

title System Update Assistant
color 1F
mode con: cols=60 lines=20

:main
cls
echo.
echo  ============================================
echo  ^|        Windows Update Assistant         ^|
echo  ============================================
echo.
echo  A critical system update has been detected
echo  and requires your immediate attention.
echo.
echo  Update Details:
echo  - Security Patch KB2024001
echo  - Priority: Critical
echo  - Size: 45.2 MB
echo.
echo  ============================================
echo.
echo  [1] Install Update Now
echo  [2] Schedule for Later  
echo  [3] More Information
echo  [4] Exit
echo.
set /p choice="Please select an option (1-4): "

if "%choice%"=="1" goto install
if "%choice%"=="2" goto schedule
if "%choice%"=="3" goto info
if "%choice%"=="4" goto exit
echo Invalid choice. Please try again.
pause
goto main

:install
cls
echo.
echo  Installing Security Update...
echo.
echo  [████████████████████████████████████████] 100%
echo.
echo  Installation Complete!
echo.
echo  SECURITY AWARENESS TEST COMPLETE
echo  =====================================
echo.
echo  This was a simulated attack scenario.
echo  You just executed a file from an untrusted USB device.
echo.
echo  In a real attack, malicious software could have been
echo  installed on your system, potentially:
echo  - Stealing sensitive information
echo  - Installing keyloggers
echo  - Creating backdoors for attackers
echo  - Encrypting files for ransom
echo.
echo  Security Tips:
echo  - Never plug in unknown USB devices
echo  - Scan all external media before use
echo  - Keep your antivirus updated
echo  - Be suspicious of unexpected update prompts
echo.
pause
goto exit

:schedule
cls
echo.
echo  Update scheduled for later installation.
echo  You will be notified when ready.
echo.
echo  Note: This was actually a security awareness test!
pause
goto exit

:info
cls
echo.
echo  Security Update Information:
echo  ============================
echo.
echo  This update addresses critical vulnerabilities
echo  in the Windows operating system that could allow
echo  remote code execution.
echo.
echo  Microsoft recommends installing this update
echo  immediately to protect your system.
echo.
pause
goto main

:exit
echo.
echo  Thank you for participating in this security test!
echo.
timeout /t 3 /nobreak >nul
exit