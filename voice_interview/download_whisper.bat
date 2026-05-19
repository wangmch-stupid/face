@echo off
chcp 65001 >nul
cd /d "D:\codex\face\voice_interview"

echo ==========================================
echo   下载 Whisper 离线语音模型（约1.5GB）
echo ==========================================
echo.
echo 第一步：安装 modelscope（阿里魔搭，国内镜像）
"C:\Users\21364\AppData\Local\Python\bin\python.exe" -m pip install modelscope -q
echo.

echo 第二步：从魔搭下载模型...
"C:\Users\21364\AppData\Local\Python\bin\python.exe" -c "
import os, sys, tempfile
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
model_dir = os.path.join(tempfile.gettempdir(), 'whisper_models')
print('模型存放目录:', model_dir)
print('开始下载（约1.5GB，请耐心等待）...')
try:
    from faster_whisper import WhisperModel
    m = WhisperModel('small', device='cpu', compute_type='int8', download_root=model_dir)
    print('下载完成！')
except Exception as e:
    print(f'直接下载失败: {e}')
    print()
    print('尝试使用 modelscope 下载...')
    from modelscope import snapshot_download
    # 从魔搭下载 faster-whisper 模型
    local = snapshot_download('keepitsimple/faster-whisper-large-v3',
                              cache_dir=model_dir)
    print(f'模型路径: {local}')
    print('下载完成！请将此路径配置到代码中。')
"
echo.
echo ==========================================
pause
