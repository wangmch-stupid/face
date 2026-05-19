"""
论文图片生成器 — 生成学术期刊风格的文献截图
用于夏令营面试的英文文献翻译环节（模拟真实论文阅读体验）
"""
import os
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import MAJOR_PAPER_ABSTRACTS

from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "static", "papers")

# 字体路径（按优先级尝试）
_FONT_PATHS = [
    "C:/Windows/Fonts/times.ttf",
    "C:/Windows/Fonts/timesi.ttf",
    "C:/Windows/Fonts/georgia.ttf",
    "C:/Windows/Fonts/georgiai.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
]


def _find_font(size: int) -> ImageFont.FreeTypeFont:
    for fp in _FONT_PATHS:
        if os.path.exists(fp):
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()


def generate_paper_image(major: str, width: int = 1200, height: int = 1000) -> str:
    """为指定学科生成论文图片，返回图片路径"""
    data = MAJOR_PAPER_ABSTRACTS.get(major)
    if not data:
        return ""

    # 解析标题行和正文
    lines = data.strip().split("\n")
    title_line = ""
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith("[From"):
            title_line = line.strip("[] ")
            body_start = i + 1
            break

    # 正文部分（跳过最后一行 Key terms）
    body_lines = [l for l in lines[body_start:] if l.strip() and not l.startswith("Key terms")]
    body_text = " ".join(body_lines)

    # 创建画布
    img = Image.new("RGB", (width, height), color=(253, 252, 248))  # 米白底
    draw = ImageDraw.Draw(img)

    # 字体
    font_title = _find_font(22)
    font_meta = _find_font(14)
    font_body = _find_font(15)
    font_journal = _find_font(13)

    # 顶部期刊标识
    draw.text((60, 40), "RESEARCH ARTICLE", fill=(80, 80, 80), font=font_journal)

    # 线条
    draw.line([(60, 65), (width - 60, 65)], fill=(180, 180, 175), width=2)

    # 标题（自动换行）
    y = 80
    title_wrapped = _wrap_text(title_line, font_title, width - 120)
    for tw in title_wrapped:
        draw.text((60, y), tw, fill=(20, 20, 20), font=font_title)
        y += 30

    # 分割线
    y += 10
    draw.line([(60, y), (width - 60, y)], fill=(200, 200, 195), width=1)
    y += 20

    # 正文 — 双栏布局
    body_wrapped = _wrap_text(body_text, font_body, (width - 140) // 2)

    mid_x = width // 2
    col_width = (width - 140) // 2
    left_y = y
    right_y = y

    lines_per_col = len(body_wrapped) // 2 + len(body_wrapped) % 2

    # 左栏
    for line in body_wrapped[:lines_per_col]:
        if left_y > height - 60:
            break
        draw.text((60, left_y), line, fill=(30, 30, 30), font=font_body)
        left_y += 20

    # 右栏
    for line in body_wrapped[lines_per_col:]:
        if right_y > height - 60:
            break
        draw.text((mid_x + 10, right_y), line, fill=(30, 30, 30), font=font_body)
        right_y += 20

    # 底部
    draw.line([(60, height - 50), (width - 60, height - 50)], fill=(200, 200, 195), width=1)
    draw.text((60, height - 40), f"Major: {major}  |  Summer Camp Mock Interview — English Translation Exercise",
              fill=(150, 150, 150), font=font_meta)

    # 保存
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"paper_{major.replace(' ', '_')}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)
    img.save(filepath, "PNG")
    return filepath


def _wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list:
    """按像素宽度自动换行"""
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + (" " if current_line else "") + word
        bbox = font.getbbox(test_line)
        if bbox[2] - bbox[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines


def generate_all():
    """为所有学科生成论文图片"""
    for major in MAJOR_PAPER_ABSTRACTS:
        path = generate_paper_image(major)
        if path:
            print(f"  {major}: {path}")


if __name__ == "__main__":
    generate_all()
    print("Done.")
