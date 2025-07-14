# processors/final/reporter_final.py

from pathlib import Path
from processors.final.extractor_final import extract_final_summary
from processors.final.formatter_final import format_final_summary_to_markdown
from processors.shared.exporter_common import export_docx_and_pdf
from config import FINAL_CUTOFF_DAYS

def write_final_report(
    markdown_lines: list[str],
    output_dir: Path,
    basename: str = "final_report"
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)

    md_path = output_dir / f"{basename}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_lines))

    print(f"✅ Markdown 报告已保存至：{md_path}")
    return md_path

def run_final_report(input_dir: Path, output_dir: Path, days: int = FINAL_CUTOFF_DAYS):
    print(f"\n📚 生成分类期末总结报告（近 {days} 天）")
    print(f"📂 读取目录：{input_dir.resolve()}\n")

    # 1. 提取数据
    summary = extract_final_summary(input_dir, days=days)

    # 2. 生成 Markdown 内容
    md_lines = format_final_summary_to_markdown(summary, days=days)

    # 3. 保存 Markdown 文件
    basename = "final_report"
    md_path = write_final_report(md_lines, output_dir, basename=basename)

    # 4. 导出 Word / PDF
    export_docx_and_pdf(md_path, output_dir, name=basename)

# ✅ 测试入口（可选保留）
if __name__ == "__main__":
    from config import INPUT_DIR, OUTPUT_DIR
    run_final_report(INPUT_DIR, OUTPUT_DIR)
