# processors/exporter_final.py

import subprocess

def export_final_report_to_word(markdown_path: str, output_file: str):
    cmd = [
        "pandoc",
        markdown_path,
        "-f", "markdown+raw_html",
        "-o", output_file,
        "--resource-path=.",
        "-V", "mainfont=SimSun",
        "-V", "geometry:margin=2cm",       # 控制页边距
        "-V", "documentclass=ctexart"
    ]
    subprocess.run(cmd, check=True)
    print(f"✅ Word 文件已导出至：{output_file}")

def export_final_report_to_pdf(markdown_path: str, output_file: str):
    cmd = [
        "pandoc",
        markdown_path,
        "-f", "markdown+raw_html",
        "-o", output_file,
        "--resource-path=.",
        "-V", "mainfont=SimSun",
        "-V", "geometry:margin=2cm",
        "-V", "documentclass=ctexart"
    ]
    subprocess.run(cmd, check=True)
    print(f"✅ PDF 文件已导出至：{output_file}")
def export_final_report_to_html(markdown_path: str, output_file: str):
    cmd = [
        "pandoc",
        markdown_path,
        "-o", output_file
    ]
    subprocess.run(cmd, check=True)
    print(f"✅ HTML 文件已导出至：{output_file}")