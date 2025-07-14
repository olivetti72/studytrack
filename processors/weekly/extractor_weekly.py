import os
import re
from datetime import datetime, timedelta
from docx import Document

def parse_docx(path):
    doc = Document(path)

    label_map = {
        "课程名称": "course",
        "老师": "teacher",
        "本周学习内容": "content",
        "遇到的问题": "problem",
        "解决方案": "solution",
        "学习心得": "reflection"
    }

    data = {k: "" for k in label_map.values()}
    current = None

    for para in doc.paragraphs:
        line = para.text.strip()
        for label, key in label_map.items():
            if line.startswith(label):
                value = line[len(label):].lstrip(":：").strip()
                if value:
                    data[key] += value + "\n"
                current = key
                break
        else:
            if current:
                data[current] += line + "\n"

    return data if any(data.values()) else None

def extract_date_from_filename(filename):
    match = re.search(r"(\d{4})-(\d{1,2})-(\d{1,2})", filename)
    if match:
        try:
            return datetime(*map(int, match.groups())).date()
        except ValueError:
            return None
    return None

def extract_study_docs(input_dir, days=None, start_date=None, end_date=None):
    today = datetime.today().date()
    if days:
        start_date = today - timedelta(days=days)
        end_date = today

    docs = []
    for filename in os.listdir(input_dir):
        if filename.endswith(".docx"):
            date = extract_date_from_filename(filename)
            if date and (not start_date or start_date <= date <= end_date):
                path = os.path.join(input_dir, filename)
                parsed = parse_docx(path)
                if parsed:
                    parsed["date"] = date  # ✅ 添加这一行
                    docs.append(parsed)

    print(f"[i] 提取到 {len(docs)} 篇学习记录")
    return docs

