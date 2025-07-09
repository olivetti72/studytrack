from pathlib import Path
from processors.final.extractor_final import extract_final_summary
from processors.final.formatter_final import format_final_summary_to_markdown
from processors.final.writer_final import write_final_report
from processors.final.exporter_final import export_final_report
from config import FINAL_CUTOFF_DAYS
def main():
    days = 90
    base_dir = Path(__file__).resolve().parent  # 📌 脚本目录为基准
    docs_dir = base_dir / "docs"
    output_dir = base_dir / "output"
    basename = "final_report"

    print(f"\n📚 生成分类期末总结报告（近 {days} 天）")
    print(f"📂 读取目录：{docs_dir.resolve()}\n")

    # 1. 提取数据
    summary = extract_final_summary(docs_dir, days=FINAL_CUTOFF_DAYS)

    # 2. 生成 markdown 内容
    markdown_lines = format_final_summary_to_markdown(summary, days=days)

    # 3. 保存 markdown 文件
    md_path = write_final_report(markdown_lines, output_dir, basename=basename)

    # 4. 导出为 Word / PDF / HTML
    export_final_report(md_path, output_dir, basename=basename)

if __name__ == "__main__":
    main()

