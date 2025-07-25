def clean_text(text):
    return text.replace("\n", "").replace("\r", "").strip()

def format_as_list(text):
    # 如果已经带前缀 "-" 就不重复加
    return "\n".join(
        (line if line.strip().startswith("-") else f"- {line.strip()}") + "  "
        for line in text.splitlines() if line.strip()
    )

def extract_study_info(parsed_docs):
    results = []
    for block in parsed_docs:
        result = {
            "course": clean_text(block.get("course", "")),
            "teacher": clean_text(block.get("teacher", "")),
            "content": format_as_list(block.get("content", "")),
            "problem": format_as_list(block.get("problem", "")),
            "solution": format_as_list(block.get("solution", "")),
            "reflection": format_as_list(block.get("reflection", ""))
        }
        if result["course"]:
            results.append(result)
    return results
def convert_fields(item: dict) -> dict:
    return {
        "course": item.get("course", ""),
        "学习内容": item.get("content", "").strip().splitlines() or ["无"],
        "遇到的问题": item.get("problem", "").strip().splitlines() or ["无"],
        "解决方案": item.get("solution", "").strip().splitlines() or ["无"],
        "学习心得": item.get("reflection", "").strip().splitlines() or ["无"],
    }
