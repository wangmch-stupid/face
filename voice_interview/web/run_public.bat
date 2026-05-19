@echo off
chcp 65001 >nul 2>&1
cd /d "D:\codex\face\voice_interview\web"

echo.
echo   === Summer Camp Mock Interview - Public ===
echo.
echo   Starting Flask server...
start "Flask" "C:\Users\21364\AppData\Local\Python\bin\python.exe" app.py

echo   Starting Cloudflare Tunnel...
echo   Public URL will appear below. Keep this window open.
echo   Press Ctrl+C to stop.
echo.
"D:\ngrok\cloudflared.exe" tunnel --url http://localhost:5000
pause
