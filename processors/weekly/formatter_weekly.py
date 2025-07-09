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