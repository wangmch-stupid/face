@echo off
chcp 65001 >nul 2>&1
cd /d "D:\codex\face\voice_interview\web"

echo.
echo   === 夏令营模拟面试 - 公网版 ===
echo.
echo   启动 Flask 服务器...
start "Flask面试服务器" "C:\Users\21364\AppData\Local\Python\bin\python.exe" app.py

echo   启动公网隧道 (serveo)...
echo   公网链接将在下方显示，按 Ctrl+C 停止
echo.
ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=30 -R 80:localhost:5000 serveo.net
pause
