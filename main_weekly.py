# main_weekly.py

from pathlib import Path
from processors.weekly.extractor_weekly import extract_study_docs
from processors.weekly.formatter_weekly import extract_study_info
from processors.weekly.writer_weekly import generate_weekly_markdown
from processors.weekly.exporter_weekly import export_to_word, export_to_pdf_html
from config import WEEKLY_CUTOFF_DAYS

def main():
    # 1. 设置路径（统一使用脚本所在目录为基准）
    base_dir = Path(__file__).resolve().parent

    input_dir = base_dir / "docs"
    output_dir = base_dir / "output"
    template_path = base_dir / "template" / "weekly_template.md"
    md_output_path = output_dir / "weekly_report.md"
    docx_output_path = output_dir / "weekly_report.docx"
    name_base = "weekly_report"

    output_dir.mkdir(parents=True, exist_ok=True)

    # 2. 提取 Word 学习文档数据
    parsed_docs = extract_study_docs(input_dir, days=WEEKLY_CUTOFF_DAYS)

    # 3. 清洗 + 标准化格式
    items = extract_study_info(parsed_docs)

    # 4. 生成 Markdown 报告
    generate_weekly_markdown(items, template_path, md_output_path)

    # 5. 导出为 Word / PDF / HTML
    export_to_word(md_output_path, docx_output_path)
    export_to_pdf_html(md_output_path, output_dir, name_base)

    print("✅ 学习周报已生成")

# ✅ 测试运行入口
if __name__ == "__main__":
    main()
