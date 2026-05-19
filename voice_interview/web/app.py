"""
夏令营模拟面试 — Web 版本
Flask REST API + 浏览器原生语音（SpeechRecognition / SpeechSynthesis）
"""
import os
import sys
import json
from pathlib import Path

# 确保能导入 engine 和 config
sys.path.insert(0, str(Path(__file__).parent.parent))
from engine import RuleBasedEngine
from config import MAJOR_BASICS

from flask import Flask, render_template, request, jsonify, session
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def _read_uploaded_file(filepath: str) -> str:
    """读取上传的文件（PDF/TXT），返回文本内容"""
    ext = os.path.splitext(filepath)[1].lower()

    if ext == '.pdf':
        # 尝试 pymupdf
        try:
            import fitz
            doc = fitz.open(filepath)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
            return text.strip() or "[PDF 内容为空]"
        except ImportError:
            pass
        except Exception:
            pass
        # 尝试 PyPDF2
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(filepath)
            text = ""
            for page in reader.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
            return text.strip() or "[PDF 内容为空]"
        except ImportError:
            return "[无法读取 PDF：服务器未安装 PDF 解析库]"
        except Exception as e:
            return f"[PDF 读取失败: {e}]"

    # 文本文件
    encodings = ['utf-8', 'gbk', 'gb2312', 'gb18030', 'latin-1']
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
        except Exception:
            break
    return "[文件编码无法识别]"

# 存储引擎实例（每个会话一个）
_engines = {}


def _get_engine():
    """获取当前会话的面试引擎"""
    sid = session.get("sid")
    return _engines.get(sid)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/interview")
def interview():
    return render_template("interview.html")


@app.route("/api/paper/<major>")
def get_paper_image(major):
    """返回论文图片的 URL"""
    filename = f"paper_{major}.png"
    filepath = os.path.join(app.static_folder, "papers", filename)
    if os.path.exists(filepath):
        return jsonify({"image_url": f"/static/papers/{filename}"})
    return jsonify({"image_url": ""}), 404


@app.route("/api/upload", methods=["POST"])
def upload_file():
    """上传简历文件，返回提取的文本"""
    if 'file' not in request.files:
        return jsonify({"error": "未选择文件"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "文件名为空"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        text = _read_uploaded_file(filepath)
        return jsonify({
            "filename": filename,
            "text": text,
            "length": len(text)
        })
    finally:
        try:
            os.remove(filepath)
        except Exception:
            pass


@app.route("/api/start", methods=["POST"])
def start_interview():
    """启动面试：接收风格、专业、简历，返回开场白和首个问题"""
    data = request.get_json()
    style = data.get("style", "structured")
    major = data.get("major", "计算机")
    resume = data.get("resume", "").strip()

    if not resume:
        resume = "(未提交简历)"

    # 验证风格
    if style not in ("stress", "structured", "gentle"):
        style = "structured"

    engine = RuleBasedEngine(style, resume, [], major)
    sid = os.urandom(8).hex()
    session["sid"] = sid
    _engines[sid] = engine

    opening = engine.start()
    question, dim_key, dim_label, dim_idx, total = _next_with_dim(engine)

    return jsonify({
        "opening": opening,
        "current_dim": dim_key,
        "dim_label": dim_label,
        "dim_index": dim_idx,
        "total_dims": total,
        "question": question,
        "finished": False
    })


@app.route("/api/answer", methods=["POST"])
def submit_answer():
    """提交回答，返回下一个问题或结束信号"""
    engine = _get_engine()
    if not engine:
        return jsonify({"error": "面试未启动"}), 400

    data = request.get_json()
    answer = data.get("answer", "").strip()

    if answer.lower() in ("/quit", "/exit"):
        engine.state.finished = True
        report = engine.generate_report()
        return jsonify({"finished": True, "report": report})

    if answer.lower() == "/skip":
        answer = "(候选人选择跳过此题)"

    if not answer:
        answer = "(候选人未作答)"

    engine.record_answer(answer)

    if engine.is_finished():
        report = engine.generate_report()
        engine.save_transcript()
        return jsonify({
            "finished": True,
            "report": report,
            "scores": engine.state.scores
        })

    question, dim_key, dim_label, dim_idx, total = _next_with_dim(engine)
    if question is None:
        report = engine.generate_report()
        engine.save_transcript()
        return jsonify({
            "finished": True,
            "report": report,
            "scores": engine.state.scores
        })

    # 获取上一维度的反馈
    feedback = engine.get_dimension_feedback(dim_key) if dim_key else ""

    return jsonify({
        "finished": False,
        "current_dim": dim_key,
        "dim_label": dim_label,
        "dim_index": dim_idx,
        "total_dims": total,
        "question": question,
        "feedback": feedback or ""
    })


def _next_with_dim(engine) -> tuple:
    """获取下一个有效问题，返回 (question, dim_key, dim_label, dim_index, total_dims)
    自动跳过过渡语和维度切换的 None"""
    total = len(engine.state.DIMENSIONS)
    while not engine.is_finished():
        q = engine.next_question()
        if q is None:
            if engine.is_finished():
                return None, "", "", 0, total
            continue
        # 保存 _current_dim（在 next_question 内部已锁定，不受 advance 影响）
        dim = engine._current_dim
        label = engine.state.DIMENSION_LABELS.get(dim, dim)
        dim_idx = engine.state.DIMENSIONS.index(dim) if dim in engine.state.DIMENSIONS else 0
        # 跳过纯过渡语（qi=0）
        if engine.state.question_index == 1:
            q2 = engine.next_question()
            if q2:
                dim2 = engine._current_dim
                label2 = engine.state.DIMENSION_LABELS.get(dim2, dim2)
                dim_idx2 = engine.state.DIMENSIONS.index(dim2) if dim2 in engine.state.DIMENSIONS else 0
                return q2, dim2, label2, dim_idx2, total
            continue
        return q, dim, label, dim_idx, total
    return None, "", "", 0, total


@app.route("/api/compare", methods=["GET"])
def compare_history():
    """获取历史对比数据"""
    import glob as gmod
    transcripts_dir = os.path.join(os.path.dirname(__file__), "..", "transcripts")
    if not os.path.isdir(transcripts_dir):
        return jsonify({"has_history": False})

    files = sorted(gmod.glob(os.path.join(transcripts_dir, "interview_*.json")),
                   reverse=True)
    if len(files) < 2:
        return jsonify({"has_history": False})

    try:
        with open(files[1], "r", encoding="utf-8") as f:
            prev = json.load(f)
    except Exception:
        return jsonify({"has_history": False})

    prev_scores = prev.get("scores", {})
    if not prev_scores:
        return jsonify({"has_history": False})

    prev_total = sum(prev_scores.values())
    prev_count = len(prev_scores)
    prev_avg = prev_total / prev_count if prev_count else 0

    return jsonify({
        "has_history": True,
        "date": os.path.basename(files[1]).replace("interview_", "").replace(".json", ""),
        "style": prev.get("style", ""),
        "avg_score": round(prev_avg, 1),
        "scores": prev_scores
    })


if __name__ == "__main__":
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print("\n  === 夏令营模拟面试 - Web 版 ===")
    print(f"  本机访问: http://127.0.0.1:5000")
    print(f"  局域网访问: http://{local_ip}:5000")
    print("  按 Ctrl+C 停止服务器\n")
    app.run(host="0.0.0.0", port=5000, debug=True)
