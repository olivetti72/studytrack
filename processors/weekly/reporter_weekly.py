from pathlib import Path
from datetime import date
from processors.weekly.extractor_weekly import extract_study_docs
from processors.weekly.formatter_weekly import extract_study_info,convert_fields
from processors.shared.exporter_common import export_docx_and_pdf

def generate_weekly_markdown(items: list[dict]) -> list[str]:
    """
    生成 Markdown 格式的学习周报内容（返回字符串列表）
    """
    lines = [f"# 学习周报（{date.today().strftime('%Y年%m月%d日')}）", ""]

    for item in items:
        data = convert_fields(item)
        lines.append(f"## {data['course']}")
        lines.append("")
        lines.append(f"- **学习内容：** {', '.join(data['学习内容'])}")
        lines.append(f"- **遇到的问题：** {', '.join(data['遇到的问题'])}")
        lines.append(f"- **解决方案：** {', '.join(data['解决方案'])}")
        lines.append(f"- **学习心得：** {', '.join(data['学习心得'])}")
        lines.append("")

    return lines

def run_weekly_report(input_dir: Path, output_dir: Path, days: int = 7):
    """
    学习周报生成主流程
    """
    print(f"📂 提取目录：{input_dir.resolve()}")
    parsed_docs = extract_study_docs(input_dir, days=days)
    items = extract_study_info(parsed_docs)

    # 生成 Markdown 报告内容
    md_lines = generate_weekly_markdown(items)

    # 保存文件
    output_dir.mkdir(parents=True, exist_ok=True)
    date_str = date.today().strftime("%Y-%m-%d")
    base_name = f"weekly_{date_str}"
    md_path = output_dir / f"{base_name}.md"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"✅ 周报 Markdown 已生成：{md_path}")

    # 导出 Word / PDF
    export_docx_and_pdf(md_path, output_dir, base_name)

if __name__ == "__main__":
    from config import INPUT_DIR, OUTPUT_DIR, WEEKLY_TEMPLATE_PATH, WEEKLY_CUTOFF_DAYS

    print("🧪 [测试] 直接运行 reporter_weekly 模块")
    run_weekly_report(
        input_dir=INPUT_DIR,
        output_dir=OUTPUT_DIR,
        template_path=WEEKLY_TEMPLATE_PATH,
        cutoff_days=WEEKLY_CUTOFF_DAYS
    )