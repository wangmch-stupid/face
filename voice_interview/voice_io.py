"""
语音输入输出模块 — TTS 语音合成 + STT 语音识别
"""

import asyncio
import tempfile
import os
import sys
import time

# ============================================================
# TTS — 使用 edge-tts（微软免费 TTS，中文效果好）
# ============================================================

# 按面试风格定制的 TTS 音色预设
# (voice, rate, pitch)
STYLE_VOICE_PRESETS = {
    "stress": {
        "zh": ("zh-CN-YunxiNeural", "+35%", "-20Hz"),   # 男声，极快语速，低沉压迫
        "en": ("en-US-GuyNeural", "+25%", "-15Hz"),      # 男声英文，快且低沉
    },
    "structured": {
        "zh": ("zh-CN-YunjianNeural", "+5%", "+0Hz"),    # 男声，成熟稳重，中性
        "en": ("en-US-GuyNeural", "+0%", "+0Hz"),
    },
    "gentle": {
        "zh": ("zh-CN-XiaoxiaoNeural", "-5%", "+3Hz"),   # 女声，慢语速，略高音 → 温暖
        "en": ("en-US-JennyNeural", "-5%", "+3Hz"),
    },
}

# 可选的中文声音（命令行 --tts-voice 用）
VOICES = {
    "xiaoxiao": "zh-CN-XiaoxiaoNeural",
    "yunxi": "zh-CN-YunxiNeural",
    "xiaoyi": "zh-CN-XiaoyiNeural",
    "yunjian": "zh-CN-YunjianNeural",
}

DEFAULT_VOICE = "zh-CN-XiaoxiaoNeural"
DEFAULT_EN_VOICE = "en-US-JennyNeural"

# 当前激活的 TTS 预设
_current_style = "structured"


def set_tts_style(style: str):
    """切换 TTS 风格预设"""
    global _current_style
    if style in STYLE_VOICE_PRESETS:
        _current_style = style


async def _speak_edge_tts(text: str, voice: str = None, rate: str = "+0%",
                          pitch: str = "+0Hz", is_english: bool = False):
    """使用 edge-tts 生成语音并播放"""
    if voice is None:
        preset = STYLE_VOICE_PRESETS.get(_current_style, STYLE_VOICE_PRESETS["structured"])
        lang = "en" if is_english else "zh"
        voice, rate, pitch = preset[lang]

    try:
        import edge_tts
    except ImportError:
        print("[错误] 请先安装 edge-tts: pip install edge-tts")
        return

    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)

    # 保存到临时文件（带 30 秒超时）
    tmp_path = os.path.join(tempfile.gettempdir(), f"interview_tts_{os.getpid()}.mp3")
    try:
        await asyncio.wait_for(communicate.save(tmp_path), timeout=30)
    except asyncio.TimeoutError:
        print(f"[TTS 超时] 网络请求超过 30 秒，跳过语音")
        return
    except Exception as e:
        print(f"[TTS 生成失败] {e}")
        return

    # 校验文件有效
    if os.path.getsize(tmp_path) < 100:
        print(f"[TTS 生成失败] 音频数据为空或过短")
        try:
            os.remove(tmp_path)
        except Exception:
            pass
        return

    # 播放音频
    _play_audio(tmp_path)

    # 清理
    try:
        os.remove(tmp_path)
    except Exception:
        pass


def _play_audio(file_path: str):
    """跨平台播放音频 — 优先使用系统内置方案"""
    if sys.platform == "win32":
        _play_win32_mci(file_path)
        return

    # Linux/Mac 回退方案
    try:
        import subprocess
        subprocess.run(
            ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", file_path],
            timeout=120
        )
        return
    except Exception:
        pass
    try:
        import subprocess
        subprocess.run(["mpv", "--no-terminal", file_path], timeout=120)
        return
    except Exception:
        pass
    os.system(f'xdg-open "{file_path}" 2>/dev/null &')
    time.sleep(5)


def _play_win32_mci(file_path: str):
    """Windows MCI (Media Control Interface) 播放 — 纯内置，零依赖"""
    import ctypes
    from ctypes import wintypes

    # 必须是绝对路径，反斜杠转义
    abs_path = os.path.abspath(file_path).replace("\\", "\\\\")

    # 打开
    cmd_open = f'open "{abs_path}" type mpegvideo alias interview_audio'
    r = ctypes.windll.winmm.mciSendStringW(cmd_open, None, 0, None)
    if r != 0:
        # mpegvideo 别名可能不支持，尝试自动检测
        cmd_open2 = f'open "{abs_path}" alias interview_audio'
        r2 = ctypes.windll.winmm.mciSendStringW(cmd_open2, None, 0, None)
        if r2 != 0:
            # MCI 失败，回退到 startfile + 估算时长
            duration = _get_mp3_duration(file_path)
            os.startfile(file_path)
            time.sleep(max(duration, 2))
            return

    # 获取音频时长
    buf = ctypes.create_unicode_buffer(128)
    ctypes.windll.winmm.mciSendStringW(
        "status interview_audio length", buf, 128, None
    )
    try:
        length_ms = int(buf.value)
    except (ValueError, TypeError):
        length_ms = 5000

    # 播放
    ctypes.windll.winmm.mciSendStringW(
        "play interview_audio", None, 0, None
    )

    # 等待播放完成
    elapsed = 0
    while elapsed < length_ms + 500:
        time.sleep(0.2)
        elapsed += 200
        buf2 = ctypes.create_unicode_buffer(128)
        ctypes.windll.winmm.mciSendStringW(
            "status interview_audio mode", buf2, 128, None
        )
        if buf2.value in ("stopped", ""):
            break

    # 关闭
    ctypes.windll.winmm.mciSendStringW(
        "close interview_audio", None, 0, None
    )


def _get_mp3_duration(file_path: str) -> float:
    """估算MP3文件时长（秒）"""
    try:
        # 使用 edge-tts 生成的 mp3 基本是固定比特率约 48kbps
        size = os.path.getsize(file_path)
        # 中文TTS约 4-6 KB/s，取 5KB/s 估算
        return size / 5000
    except Exception:
        return 0


async def speak(text: str, voice: str = None, rate: str = None, pitch: str = None):
    """TTS 朗读中文（自动使用当前风格预设）"""
    await _speak_edge_tts(text, voice=voice, rate=rate or "+0%",
                          pitch=pitch or "+0Hz", is_english=False)


async def speak_en(text: str):
    """TTS 朗读英文（自动使用当前风格预设）"""
    await _speak_edge_tts(text, is_english=True)


# ============================================================
# STT — 语音识别（麦克风 → 文本）
# ============================================================

# ============================================================
# Whisper 模型（已从魔搭下载到本地）
# ============================================================
_whisper_model = None
_MODEL_PATH = os.path.join(
    tempfile.gettempdir(),
    "whisper_models",
    "keepitsimple",
    "faster-whisper-large-v3"
)
_MODEL_READY = os.path.isdir(_MODEL_PATH) and os.listdir(_MODEL_PATH)


def _get_whisper_model():
    """加载本地 faster-whisper 模型（已通过魔搭下载）"""
    global _whisper_model
    if _whisper_model is not None:
        return _whisper_model
    if not _MODEL_READY:
        return None
    try:
        from faster_whisper import WhisperModel
        print("  ⏳ 加载 Whisper 模型...", end=" ", flush=True)
        model = WhisperModel(_MODEL_PATH, device="cpu", compute_type="int8",
                             local_files_only=True)
        _whisper_model = model
        print("✓")
        return model
    except ImportError:
        return None
    except Exception as e:
        print(f"失败: {e}")
        return None


def check_stt_available() -> bool:
    """检测 STT 模块是否可用，返回 True/False"""
    try:
        import sounddevice as sd
        import numpy as np
        test = sd.rec(int(16000 * 0.1), samplerate=16000, channels=1,
                      dtype='int16', blocking=True)
        sd.wait()
        return True
    except Exception as e:
        print(f"  ⚠️  麦克风不可用: {e}")
        print("  💡 请选择文字回答模式")
        return False


def listen(language: str = "zh-CN", timeout: int = 10) -> str:
    """
    从麦克风录音并转文字。
    优先使用 faster-whisper（本地离线），失败回退 Google STT。
    操作：按 Enter 开始 → 说话 → 按 Enter 结束（或超时自动停止）→ 自动转写
    timeout: 最长录音秒数，默认 60 秒
    """
    try:
        import sounddevice as sd
        import numpy as np
    except ImportError:
        return "[请安装: pip install sounddevice]"

    SAMPLE_RATE = 16000
    max_duration = timeout if timeout and timeout > 0 else 60

    print(f"\n  🎤 按 Enter 开始录音 (最长{max_duration}秒)...", end=" ", flush=True)
    input("")

    print(f"  🔴 录音中... (说完按 Enter 或 {max_duration}秒自动停止)", end=" ", flush=True)

    import threading
    recording_flag = [True]
    audio_chunks = []

    def _record_thread():
        try:
            with sd.InputStream(samplerate=SAMPLE_RATE, channels=1,
                                dtype='int16', blocksize=1600) as stream:
                while recording_flag[0]:
                    data, _ = stream.read(1600)
                    audio_chunks.append(data.copy())
        except Exception:
            pass

    rec_thread = threading.Thread(target=_record_thread, daemon=True)
    rec_thread.start()

    # 等待用户按 Enter 或超时
    start_time = time.time()
    user_stopped = [False]

    def _wait_enter():
        input("")
        user_stopped[0] = True

    wait_thread = threading.Thread(target=_wait_enter, daemon=True)
    wait_thread.start()
    wait_thread.join(timeout=max_duration)

    recording_flag[0] = False
    rec_thread.join(timeout=2)

    if not audio_chunks:
        print("\n  ⏰ 未检测到录音。")
        return ""

    audio_data = np.concatenate(audio_chunks, axis=0).flatten().astype(np.float32) / 32768.0
    duration = len(audio_data) / SAMPLE_RATE

    if duration < 0.5:
        print("  ⏰ 录音太短。")
        return ""
    actual_level = np.abs(audio_data).mean()
    if actual_level < 0.0003:
        print(f"  📢 音量过低 (电平: {actual_level:.5f})，请检查麦克风是否静音或离得太远。")
        return ""

    print(f"  {duration:.0f}秒，转写中...", end=" ", flush=True)

    # 转写（Whisper 离线优先 → Google 在线兜底）
    text = _transcribe(audio_data, SAMPLE_RATE, language)
    if text:
        return text

    print("失败。")
    return ""


def _transcribe(audio_data, sample_rate: int, language: str) -> str:
    """转写音频：Whisper 离线优先，Google 在线兜底，自动重试"""

    # --- Whisper 离线 ---
    model = _get_whisper_model()
    if model is not None:
        try:
            segments, _ = model.transcribe(
                audio_data, beam_size=5,
                language="zh" if language.startswith("zh") else None,
                vad_filter=True
            )
            text = " ".join(s.text for s in segments).strip()
            if text:
                print("✓ [离线]")
                return text
        except Exception:
            pass

    # --- Google 在线（重试3次）---
    for attempt in range(3):
        try:
            import speech_recognition as sr
            r = sr.Recognizer()
            int_audio = (audio_data * 32767).astype(np.int16)
            sr_audio = sr.AudioData(int_audio.tobytes(), sample_rate, 2)
            text = r.recognize_google(sr_audio, language=language)
            if text.strip():
                tag = "✓" if attempt == 0 else f"✓(重试{attempt+1})"
                print(tag)
                return text.strip()
        except sr.UnknownValueError:
            continue  # 听不清，重试
        except sr.RequestError:
            continue  # 网络波动，重试
        except Exception:
            continue

    return ""


