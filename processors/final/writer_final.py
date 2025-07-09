# processors/final/writer_final.py

from pathlib import Path
from processors.final.extractor_final import CourseFinalSummary
from processors.final.formatter_final import format_final_summary_to_markdown


def write_final_report(
    markdown_lines: list[str],
    output_dir: Path,
    basename: str = "final_report"
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)


    # 2. 保存为 .md 文件
    md_path = output_dir / f"{basename}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_lines))  # 使用 markdown_lines，而不是再格式化

    print(f"✅ Markdown 报告已保存至：{md_path}")
    return md_path


# ✅ 测试入口（可单独运行）
if __name__ == "__main__":
    from processors.final.extractor_final import extract_final_summary
    from pprint import pprint

    docs_dir = Path(__file__).resolve().parents[2] / "docs"
    output_dir = Path(__file__).resolve().parents[2] / "output"

    print(f"🔍 提取 {docs_dir} 的期末总结数据...")
    summary = extract_final_summary(docs_dir, days=3650)

    print("📊 提取数据预览：")
    pprint(summary)

    write_final_report(summary, output_dir)
