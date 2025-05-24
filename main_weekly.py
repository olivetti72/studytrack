import os
from processors.extractor_weekly import extract_study_docs
from processors.formatter_weekly import extract_study_info
from processors.writer_weekly import generate_weekly_markdown
from processors.exporter_weekly import export_to_word, export_to_pdf_html

# 1. 设置路径
input_dir = "docs"
output_dir = "output"
template_path = "template/weekly_template.md"
md_output_path = os.path.join(output_dir, "weekly_report.md")
docx_output_path = os.path.join(output_dir, "weekly_report.docx")
name_base = "weekly_report"

# 2. 提取 Word 学习文档数据
parsed_docs = extract_study_docs(input_dir,days=7)

# 3. 清洗 + 标准化格式
items = extract_study_info(parsed_docs)

# 4. 生成 Markdown 报告
generate_weekly_markdown(items, template_path, md_output_path)

# 5. 导出为 Word / PDF / HTML
export_to_word(md_output_path, docx_output_path)
export_to_pdf_html(md_output_path, output_dir, name_base)