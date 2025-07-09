# processors/course/exporter_course.py

from pathlib import Path
from processors.exporter_final import (
    export_final_report_to_word,
    export_final_report_to_pdf,
    export_final_report_to_html,
)

def export_course_report(md_path: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    export_final_report_to_word(md_path, output_dir / "course_summary.docx")
    export_final_report_to_pdf(md_path, output_dir / "course_summary.pdf")
    export_final_report_to_html(md_path, output_dir / "course_summary.html")

    print(f"📄 Word 报告已生成：{output_dir / 'course_summary.docx'}")
    print(f"📄 PDF 报告已生成：{output_dir / 'course_summary.pdf'}")
    print(f"📄 HTML 报告已生成：{output_dir / 'course_summary.html'}")
