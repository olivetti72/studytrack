import os
from docx import Document
from datetime import datetime, timedelta

def parse_docx_as_dict(path):
    fields_list = parse_docx(path)
    return fields_list[0] if fields_list else {}
def parse_docx(path):
    doc = Document(path)

    text_map = {
        "course": "",
        "teacher": "",
        "content": "",
        "problem": "",
        "solution": "",
        "reflection": ""
    }

    label_map = {
        "课程名称": "course",
        "老师": "teacher",
        "本周学习内容": "content",
        "遇到的问题": "problem",
        "解决方案": "solution",
        "学习心得": "reflection"
    }

    current = None

    for para in doc.paragraphs:
        line = para.text.strip()
        for label, key in label_map.items():
            if line.startswith(label):
                value = line[len(label):].lstrip(":：").strip()
                if value:
                    text_map[key] += value + "\n"
                current = key
                break
        else:
            if current:
                text_map[current] += line + "\n"

    # 最终返回一个“课程内容列表”，每个元素是一个 dict
    return [text_map] if any(text_map.values()) else []

def all_docx_files(folder):
    docx_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".docx"):
                docx_files.append(os.path.join(root, file))
    return docx_files

def extract_study_docs(folder, days=7):
    parsed_items = []
    cutoff = datetime.now() - timedelta(days=days)

    for filepath in all_docx_files(folder):
        modified_time = datetime.fromtimestamp(os.path.getmtime(filepath))
        if modified_time >= cutoff:
            parsed = parse_docx_as_dict(filepath)
            if parsed:
                parsed_items.append(parsed)
            else:
                print(f"[!] 未能解析文档：{filepath}")

    return parsed_items

def extract_study_info(parsed_docs):
    results = []

    for block in parsed_docs:
        course = block.get("course", "").strip()
        if not course:
            continue
        results.append({
            "course": course,
            "学习内容": [line.strip() for line in block.get("content", "").splitlines() if line.strip()],
            "遇到的问题": [line.strip() for line in block.get("problem", "").splitlines() if line.strip()],
            "解决方案": [line.strip() for line in block.get("solution", "").splitlines() if line.strip()],
            "学习心得": [line.strip() for line in block.get("reflection", "").splitlines() if line.strip()],
        })

    return results