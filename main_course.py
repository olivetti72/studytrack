from pathlib import Path
from processors.course.extractor_course import extract_course_summary
from processors.course.writer_course import write_course_report
from processors.course.exporter_course import export_course_report
from config import COURSE_CUTOFF_DAYS
def main():
    base_dir = Path(__file__).resolve().parent  # ✅ 当前脚本目录

    docs_dir = base_dir / "docs"       # 学习文档目录
    output_dir = base_dir / "output"   # 生成报告目录

    print(f"🔍 从目录 {docs_dir.resolve()} 提取课程总结...")
    summary = extract_course_summary(docs_dir, cutoff_days=COURSE_CUTOFF_DAYS)

    print(f"📝 生成 Markdown 报告并保存...")
    write_course_report(summary, output_dir)

    md_path = output_dir / "summary_course.md"
    print(f"📄 导出 Word / PDF / HTML 报告...")
    export_course_report(md_path, output_dir)

    print("🎉 课程总结报告生成完毕！")

if __name__ == "__main__":
    main()
