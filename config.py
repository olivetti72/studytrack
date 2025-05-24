import os
from datetime import date

# 根路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 输入 / 输出路径
INPUT_DIR = os.path.join(BASE_DIR, "docs")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# 模板路径
WEEKLY_TEMPLATE_PATH = os.path.join(BASE_DIR, "template", "weekly_template.md")

# 默认文件名
REPORT_NAME = f"学习周报_{date.today().strftime('%Y年%m月%d日')}"
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)