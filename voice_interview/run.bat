@echo off
cd /d "D:\codex\face\voice_interview"
"C:\Users\21364\AppData\Local\Python\bin\python.exe" main.py --style %1 --skip-setup --no-stt
pause
