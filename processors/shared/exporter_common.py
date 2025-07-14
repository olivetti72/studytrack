import subprocess
from pathlib import Path

def export_docx_and_pdf(md_path: Path, output_dir: Path, name: str = "report"):
    """
    通用导出：将 Markdown 转换为 Word 和 PDF（适配中文 / 表格 / 段落）
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    docx_path = output_dir / f"{name}.docx"
    pdf_path = output_dir / f"{name}.pdf"

    common_args = [
        "-V", "mainfont=Microsoft YaHei",
        "-V", "CJKmainfont=SimSun",
        "-V", "geometry:margin=2cm",
        "-V", "documentclass=ctexart"
    ]

    try:
        subprocess.run([
            "pandoc", str(md_path), "-o", str(docx_path),
            *common_args
        ], check=True)
        print(f"✅ 已导出 Word：{docx_path}")
    except Exception as e:
        print(f"❌ Word 导出失败：{e}")

    try:
        subprocess.run([
            "pandoc", str(md_path), "-o", str(pdf_path),
            "--pdf-engine=xelatex",
            *common_args
        ], check=True)
        print(f"✅ 已导出 PDF：{pdf_path}")
    except Exception as e:
        print(f"❌ PDF 导出失败：{e}")

