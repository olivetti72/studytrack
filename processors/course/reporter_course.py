# processors/course/reporter_course.py

from pathlib import Path
from datetime import date
from processors.course.extractor_course import extract_course_summary
from processors.course.formatter_course import format_course_summary_to_markdown
from processors.shared.exporter_common import export_docx_and_pdf

def run_course_report(input_dir: Path, output_dir: Path, days: int = 30):
    print(f"📂 提取目录：{input_dir.resolve()}（近 {days} 天）")
    summary = extract_course_summary(input_dir, days=days)

    md_lines = format_course_summary_to_markdown(summary, days)
    date_str = date.today().strftime("%Y-%m-%d")
    base_name = f"course_{date_str}"

    output_dir.mkdir(parents=True, exist_ok=True)
    md_path = output_dir / f"{base_name}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"✅ Markdown 报告已保存至：{md_path}")
    export_docx_and_pdf(md_path, output_dir, base_name)
    print("🎉 课程总结报告生成完成！")

if __name__ == "__main__":
    from config import INPUT_DIR, OUTPUT_DIR, COURSE_CUTOFF_DAYS
    run_course_report(INPUT_DIR, OUTPUT_DIR, COURSE_CUTOFF_DAYS)
