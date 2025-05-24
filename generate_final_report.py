# studytrack/generate_final_report.py

import os
import datetime
from processors.extractor_study_legacy import extract_study_docs, extract_study_info
from processors.exporter_final import (
    export_final_report_to_word,
    export_final_report_to_pdf,
    export_final_report_to_html,
)

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_final_report(days=90):
    print(f"📚 分类期末总结报告（近 {days} 天）\n")

    folder = "docs"
    all_docs = extract_study_docs(folder)
    all_info = extract_study_info(all_docs)

    # 聚合数据
    course_summary = {}

    def normalize(value):
        if isinstance(value, list):
            lines = []
            for v in value:
                if not v:
                    continue
                v = str(v).strip()
                while v.startswith(("-", "—", "·", "–")):
                    v = v.lstrip("-—·–").strip()
                lines.append(v)
            return lines
        elif isinstance(value, str):
            v = value.strip()
            while v.startswith(("-", "—", "·", "–")):
                v = v.lstrip("-—·–").strip()
            return [v] if v else []
        return []

    print("结构化后数据示例：")
    from pprint import pprint
    pprint(all_info[:2])

    for item in all_info:
        course = item.get("course", "").strip()
        if not course:
            continue
        if course not in course_summary:
            course_summary[course] = {
                "学习内容": [],
                "遇到的问题": [],
                "解决方案": [],
                "学习心得": [],
                "count": 0
            }

        course_summary[course]["学习内容"].extend(normalize(item.get("学习内容", "")))
        course_summary[course]["遇到的问题"].extend(normalize(item.get("遇到的问题", "")))
        course_summary[course]["解决方案"].extend(normalize(item.get("解决方案", "")))
        course_summary[course]["学习心得"].extend(normalize(item.get("学习心得", "")))
        course_summary[course]["count"] += 1

    # 写入 Markdown
    report_lines = []
    report_lines.append(f"# 分类期末总结报告（近 {days} 天）\n")
    report_lines.append(f"生成时间：{datetime.date.today()}\n")

    for course, data in course_summary.items():
        report_lines.append(f"## {course}（共 {data['count']} 条学习记录）\n")

        # 写入 Markdown
        report_lines = []
        report_lines.append(f"# 分类期末总结报告（近 {days} 天）\n")
        report_lines.append(f"生成时间：{datetime.date.today()}\n")

        for course, data in course_summary.items():
            report_lines.append(f"## {course}（共 {data['count']} 条学习记录）\n")
            report_lines.append("| 分类 | 内容 |")
            report_lines.append("|:----:|:-----|")

            MIN_LINES_PER_SECTION = 3

            for section in ["学习内容", "遇到的问题", "解决方案", "学习心得"]:
                lines = list(filter(None, data[section]))

                # 如果内容太少就自动补“暂无记录”或空白撑高度
                if len(lines) < MIN_LINES_PER_SECTION:
                    while len(lines) < MIN_LINES_PER_SECTION:
                        lines.append("暂无记录")

                content = "<br>".join(
                    f"- {line.strip().lstrip('•-–—·o').strip()}"
                    for line in lines
                )

                report_lines.append(f"| {section} | {content} |")

            report_lines.append("\n---\n")
    # 保存文件
    output_name = "final_report"
    md_path = os.path.join(OUTPUT_DIR, output_name + ".md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
    print(f"✅ Markdown 文件已保存至：{md_path}")
    return md_path, output_name

# 主执行入口
if __name__ == "__main__":
    md_path, output_name = generate_final_report(days=90)
    export_final_report_to_word(md_path, os.path.join(OUTPUT_DIR, output_name + ".docx"))
    export_final_report_to_pdf(md_path, os.path.join(OUTPUT_DIR, output_name + ".pdf"))
    export_final_report_to_html(md_path, os.path.join(OUTPUT_DIR, output_name + ".html"))