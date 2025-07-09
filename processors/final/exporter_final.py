# processors/final/exporter_final.py

from pathlib import Path
from processors.exporter_final import (
    export_final_report_to_word,
    export_final_report_to_pdf,
    export_final_report_to_html,
)


def export_final_report(md_path: Path, output_dir: Path, basename: str = "final_report"):
    output_dir.mkdir(parents=True, exist_ok=True)

    word_path = output_dir / f"{basename}.docx"
    pdf_path = output_dir / f"{basename}.pdf"
    html_path = output_dir / f"{basename}.html"

    export_final_report_to_word(md_path, word_path)
    export_final_report_to_pdf(md_path, pdf_path)
    export_final_report_to_html(md_path, html_path)

    print(f"📄 导出完成：\n- {word_path}\n- {pdf_path}\n- {html_path}")


# ✅ 可单独运行测试
if __name__ == "__main__":
    output_dir = Path(__file__).resolve().parents[2] / "output"
    md_path = output_dir / "final_report.md"
    export_final_report(md_path, output_dir)
