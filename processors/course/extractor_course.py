# processors/course/extractor_course.py

import os
from collections import defaultdict
from typing import Dict, List, TypedDict
from pathlib import Path
from processors.weekly.extractor_study_legacy import parse_docx_as_dict
from datetime import datetime, timedelta
# --- 类型定义 ---
class CourseContent(TypedDict, total=False):
    count: int
    content: List[str]
    problem: List[str]
    solution: List[str]
    reflection: List[str]

CourseSummary = Dict[str, CourseContent]

# --- 提取函数实现 ---
def extract_course_summary(folder: Path, cutoff_days: int = 30) -> CourseSummary:
    cutoff_date = datetime.now() - timedelta(days=cutoff_days)

    stats = defaultdict(int)
    content_map = defaultdict(lambda: {
        "content": [],
        "problem": [],
        "solution": [],
        "reflection": []
    })

    def extract_date_from_filename(name: str) -> datetime | None:
        try:
            parts = name.rstrip(".docx").split("_")
            date_str = parts[-1].replace("年", "-").replace("月", "-").replace("日", "")
            return datetime.strptime(date_str, "%Y-%m-%d")
        except Exception:
            return None

    for name in os.listdir(folder):
        if not name.endswith(".docx") or name.startswith("~$"):
            continue
        doc_date = extract_date_from_filename(name)
        if not doc_date or doc_date < cutoff_date:
            continue

        fields = parse_docx_as_dict(folder / name)
        if not fields:
            continue

        course = fields.get("course", "").strip()
        if not course:
            continue

        stats[course] += 1
        for field in ["content", "problem", "solution", "reflection"]:
            lines = [line.strip("- ").strip() for line in fields.get(field, "").split("\n") if line.strip()]
            content_map[course][field].extend(lines)

    # 合并 count 字段
    for course in stats:
        content_map[course]["count"] = stats[course]

    return content_map
from pathlib import Path
from pprint import pprint
from datetime import datetime
from processors.course.extractor_course import extract_course_summary

if __name__ == "__main__":
    from pathlib import Path
    from pprint import pprint

    docs_dir = Path(r"D:\alex_code\studytrack\docs")  # ✅ 用绝对路径先测通
    print(f"🔍 从目录 {docs_dir.resolve()} 提取课程总结...")

    summary = extract_course_summary(docs_dir, cutoff_days=3650)

    print("\n📊 提取结果如下：\n")
    pprint(summary)




