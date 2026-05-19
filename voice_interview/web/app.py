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

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()

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
    question = _next_with_dim(engine)

    return jsonify({
        "opening": opening,
        "current_dim": engine._current_dim,
        "dim_label": engine.state.DIMENSION_LABELS.get(engine._current_dim, ""),
        "dim_index": engine.state.dimension_index,
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

    question = _next_with_dim(engine)
    if question is None:
        report = engine.generate_report()
        engine.save_transcript()
        return jsonify({
            "finished": True,
            "report": report,
            "scores": engine.state.scores
        })

    # 获取上一维度的反馈
    feedback = engine.get_dimension_feedback(engine._current_dim)

    return jsonify({
        "finished": False,
        "current_dim": engine._current_dim,
        "dim_label": engine.state.DIMENSION_LABELS.get(engine._current_dim, ""),
        "dim_index": engine.state.dimension_index,
        "total_dims": len(engine.state.DIMENSIONS),
        "question": question,
        "feedback": feedback or ""
    })


def _next_with_dim(engine) -> str:
    """获取下一个问题（跳过过渡语中的空内容）"""
    # 跳过纯过渡语（qi=0），直接返回第一个真实问题
    q = engine.next_question()
    if q and engine.state.question_index == 1:
        # 这是过渡语，再取下一个
        q2 = engine.next_question()
        if q2:
            return q2
    return q


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
    print("\n  === 夏令营模拟面试 - Web 版 ===")
    print("  打开浏览器访问: http://127.0.0.1:5000")
    print("  按 Ctrl+C 停止服务器\n")
    app.run(host="127.0.0.1", port=5000, debug=True)
