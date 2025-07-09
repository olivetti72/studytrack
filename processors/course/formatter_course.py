# processors/course/formatter_course.py

from typing import List
from datetime import date
from processors.course.extractor_course import extract_course_summary, CourseSummary

def format_course_summary_to_markdown(summary: CourseSummary, days: int = 30) -> List[str]:
    """
    将课程学习数据结构转为 Markdown 文本（以列表返回每一行，便于写入文件）
    """
    lines = []
    lines.append(f"# 分类时间段总结报告（近 {days} 天）\n")
    lines.append(f"生成时间：{date.today()}\n")

    # 按出现次数排序
    sorted_courses = sorted(summary.items(), key=lambda x: x[1].get("count", 0), reverse=True)

    for course, data in sorted_courses:
        lines.append(f"## {course}（共 {data.get('count', 0)} 次）\n")

        for label, key in [
            ("学习内容", "content"),
            ("遇到的问题", "problem"),
            ("解决方案", "solution"),
            ("学习心得", "reflection")
        ]:
            items = list(set(data.get(key, [])))  # 去重
            if not items:
                continue
            lines.append(f"**{label}：**\n")
            for item in items:
                lines.append(f"- {item}")
            lines.append("")  # 空行分段

        lines.append("---\n")  # 课程间分隔

    return lines
if __name__ == "__main__":
    from pathlib import Path
    from processors.course.extractor_course import extract_course_summary
    from processors.course.formatter_course import format_course_summary_to_markdown

    docs_dir = Path(r"D:\alex_code\studytrack\docs")  # ✅ 改为你实际路径
    summary = extract_course_summary(docs_dir)
    lines = format_course_summary_to_markdown(summary)
    print("\n".join(lines))

