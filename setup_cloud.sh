#!/bin/bash
# 模拟面试 — PythonAnywhere 一键部署脚本
# 在 PythonAnywhere Bash 终端中运行此脚本即可

set -e

echo "=== Camp Interview - Auto Deploy ==="
echo ""

# 1. 克隆代码
if [ -d "face" ]; then
    echo "[1/4] Updating existing code..."
    cd face && git pull && cd ..
else
    echo "[1/4] Downloading code..."
    git clone https://github.com/wangmch-stupid/face.git
fi

# 2. 安装依赖
echo "[2/4] Installing Flask..."
pip install --user flask -q

# 3. 配置 Web App
echo "[3/4] Configuring web app..."
USERNAME=$(whoami)
WSGI_FILE="/var/www/${USERNAME}_pythonanywhere_com_wsgi.py"

cat > "$WSGI_FILE" << 'WEOF'
import sys
import os

# 项目路径
project_home = os.path.expanduser('~/face/voice_interview/web')
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application
WEOF

# 4. 重载 Web App
echo "[4/4] Reloading web app..."
pythonanywhere reload 2>/dev/null || echo "Please reload manually: Web tab -> Reload button"

echo ""
echo "=== Done! ==="
echo "Your URL: https://${USERNAME}.pythonanywhere.com"
echo ""
echo "If the site doesn't load, go to the Web tab and click the green Reload button."
echo ""
