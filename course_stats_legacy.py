import os
import datetime
from collections import defaultdict
from processors.extractor_study_legacy import parse_docx_as_dict
from processors.exporter_final import (
    export_final_report_to_word,
    export_final_report_to_pdf,
    export_final_report_to_html,
)

# 设置参数
FOLDER = "./docs"
OUTPUT_DIR = "./output"
DAYS = 30
now = datetime.datetime.now()
cutoff_date = now - datetime.timedelta(days=DAYS)

# 初始化
stats = defaultdict(int)
content_map = defaultdict(lambda: {
    "content": [],
    "problem": [],
    "solution": [],
    "reflection": []
})
report_lines = []

def extract_date_from_filename(name):
    try:
        parts = name.rstrip(".docx").split("_")
        date_str = parts[-1].replace("年", "-").replace("月", "-").replace("日", "")
        return datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except Exception:
        return None

# 处理文档
for name in os.listdir(FOLDER):
    if not name.endswith(".docx") or name.startswith("~$"):
        continue
    doc_date = extract_date_from_filename(name)
    if not doc_date or doc_date < cutoff_date:
        continue

    path = os.path.join(FOLDER, name)
    fields = parse_docx_as_dict(path)
    if not fields:
        continue
    course = fields.get("course", "").strip()
    if not course:
        continue

    stats[course] += 1
    for field in ["content", "problem", "solution", "reflection"]:
        lines = [line.strip("- ").strip() for line in fields.get(field, "").split("\n") if line.strip()]
        content_map[course][field].extend(lines)

# 构建 Markdown 内容
report_lines.append(f"# 分类时间段总结报告（近 {DAYS} 天）\n")
report_lines.append(f"生成时间：{datetime.date.today()}\n")

sorted_courses = sorted(stats.items(), key=lambda x: x[1], reverse=True)
for course, count in sorted_courses:
    report_lines.append(f"## {course}（共 {count} 次）\n")

    for field_label, field_key in [
        ("学习内容", "content"),
        ("遇到的问题", "problem"),
        ("解决方案", "solution"),
        ("学习心得", "reflection")
    ]:
        items = list(set(content_map[course][field_key]))  # 去重
        if not items:
            continue
        report_lines.append(f"**{field_label}：**\n")
        for item in items:
            report_lines.append(f"- {item}")
            #report_lines.append("")
        report_lines.append("")

    report_lines.append("---\n")

# 设置统一导出文件名前缀
output_name = "summary_30d"

# 保存 Markdown 文件
md_path = os.path.join(OUTPUT_DIR, output_name + ".md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print(f"✅ Markdown 文件已保存至：{md_path}")

# 同步生成其它格式，输出路径统一为 summary_30d.xxx
export_final_report_to_word(md_path, os.path.join(OUTPUT_DIR, output_name + ".docx"))
export_final_report_to_pdf(md_path, os.path.join(OUTPUT_DIR, output_name + ".pdf"))
export_final_report_to_html(md_path, os.path.join(OUTPUT_DIR, output_name + ".html"))