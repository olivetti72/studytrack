from string import Template

def generate_weekly_markdown(items, template_path, output_path):
    with open(template_path, encoding="utf-8") as f:
        template = Template(f.read())

    body = ""
    for item in items:
        for key in ["course", "teacher", "content", "problem", "solution", "reflection"]:
            item.setdefault(key, "")
        body += template.substitute(**item).strip() + "\n\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# 学习周报\n\n" + body.strip())
    print(f"✅ 已生成 Markdown：{output_path}")