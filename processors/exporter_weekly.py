import subprocess
import os

def export_to_word(md_path, docx_path):
    """
    将 Markdown 转换为 Word（支持中文）
    """
    try:
        subprocess.run([
            "pandoc", md_path, "-o", docx_path,
            "-V", "mainfont=SimSun",
            "-V", "documentclass=ctexart"
        ], check=True)
        print(f"✅ 已导出 Word：{docx_path}")
    except Exception as e:
        print(f"❌ Word 导出失败：{e}")

def export_to_pdf_html(md_path, output_dir, name_base):
    """
    将 Markdown 转换为 PDF 和 HTML（支持中文 PDF）
    """
    pdf_path = os.path.join(output_dir, f"{name_base}.pdf")
    html_path = os.path.join(output_dir, f"{name_base}.html")

    try:
        subprocess.run([
            "pandoc", md_path, "-o", pdf_path,
            "-V", "mainfont=SimSun",
            "-V", "documentclass=ctexart"
        ], check=True)
        print(f"✅ 已导出 PDF：{pdf_path}")
    except Exception as e:
        print(f"❌ PDF 导出失败：{e}")

    try:
        subprocess.run(["pandoc", md_path, "-o", html_path], check=True)
        print(f"✅ 已导出 HTML：{html_path}")
    except Exception as e:
        print(f"❌ HTML 导出失败：{e}")