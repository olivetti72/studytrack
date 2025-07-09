# processors/final/formatter_final.py

from typing import List
from processors.final.extractor_final import CourseFinalSummary
from datetime import date

def format_final_summary_to_markdown(summary: CourseFinalSummary, days: int = 90) -> List[str]:
    lines = []
    lines.append(f"# 分类期末总结报告（近 {days} 天）\n")
    lines.append(f"生成时间：{date.today()}\n")

    MIN_LINES_PER_SECTION = 3

    for course, data in summary.items():
        lines.append(f"## {course}（共 {data['count']} 条学习记录）\n")
        lines.append("| 分类 | 内容 |")
        lines.append("|:----:|:-----|")

        for section in ["学习内容", "遇到的问题", "解决方案", "学习心得"]:
            entries = data.get(section, [])

            if len(entries) < MIN_LINES_PER_SECTION:
                entries += ["暂无记录"] * (MIN_LINES_PER_SECTION - len(entries))

            formatted = "<br>".join(f"- {line.strip()}" for line in entries)
            lines.append(f"| {section} | {formatted} |")

        lines.append("\n---\n")

    return lines

# ✅ 测试入口
if __name__ == "__main__":
    from extractor_final import extract_final_summary
    from pathlib import Path
    from pprint import pprint

    docs_dir = Path(__file__).resolve().parents[2] / "docs"
    summary = extract_final_summary(docs_dir, days=3650)

    markdown_lines = format_final_summary_to_markdown(summary)
    print("\n".join(markdown_lines))
