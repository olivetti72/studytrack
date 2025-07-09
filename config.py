from pathlib import Path
from datetime import date

# 报告时间筛选范围（单位：天）
WEEKLY_CUTOFF_DAYS = 7       # 周报提取近 7 天
COURSE_CUTOFF_DAYS = 30      # 课程总结提取近 30 天
FINAL_CUTOFF_DAYS = 90       # 分类期末总结提取近 90 天

# 根路径
BASE_DIR = Path(__file__).resolve().parent

# 输入 / 输出路径
INPUT_DIR = BASE_DIR / "docs"
OUTPUT_DIR = BASE_DIR / "output"

# 模板路径
WEEKLY_TEMPLATE_PATH = BASE_DIR / "template" / "weekly_template.md"

# 默认报告文件名
REPORT_NAME = f"学习周报_{date.today().strftime('%Y年%m月%d日')}"

# 创建必要的目录
INPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
