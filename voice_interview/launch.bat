@echo off
set PYTHON=C:\Users\21364\AppData\Local\Python\bin\python.exe
cd /d D:\codex\face\voice_interview
start "夏令营面试" powershell -NoExit -Command "& '%PYTHON%' main.py --style %1"
