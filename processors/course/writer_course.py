# processors/course/writer_course.py

from pathlib import Path
from processors.course.formatter_course import format_course_summary_to_markdown
from processors.course.extractor_course import CourseSummary


def write_course_report(
    summary: CourseSummary,
    output_dir: Path,
    basename: str = "summary_course"
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. 生成 Markdown 内容
    markdown = format_course_summary_to_markdown(summary)

    # 2. 保存为 .md 文件
    md_path = output_dir / f"{basename}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown))  # ✅ 将 list[str] 合成 str

    print(f"✅ Markdown 报告已保存至：{md_path}")


# ✅ 测试入口（可单独运行）
if __name__ == "__main__":
    from processors.course.extractor_course import extract_course_summary
    from pprint import pprint

    # 获取根目录下的 docs 路径
    docs_dir = Path(__file__).resolve().parents[2] / "docs"
    output_dir = Path(__file__).resolve().parents[2] / "output"

    print(f"🔍 提取 {docs_dir.resolve()} 中的课程总结...")
    summary = extract_course_summary(docs_dir, cutoff_days=3650)

    print("📊 报告内容预览：")
    pprint(summary)

    write_course_report(summary, output_dir)
    print(f"✅ Markdown 报告已保存至：{output_dir / 'summary_course.md'}")


