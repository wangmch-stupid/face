@echo off
chcp 65001 >nul 2>&1
cd /d "D:\codex\face\voice_interview\web"
echo.
echo   === Summer Camp Mock Interview - Web ===
echo   Open: http://127.0.0.1:5000
echo   Ctrl+C to stop
echo.
"C:\Users\21364\AppData\Local\Python\bin\python.exe" app.py
pause
