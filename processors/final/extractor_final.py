# processors/final/extractor_final.py

from typing import List, Dict
from collections import defaultdict
from pathlib import Path
from datetime import datetime, timedelta
from processors.weekly.extractor_study_legacy import extract_study_docs, extract_study_info

# 类型定义
CourseFinalSummary = Dict[str, Dict[str, List[str] | int]]

def normalize(value) -> List[str]:
    """清洗字段，统一为列表格式"""
    if isinstance(value, list):
        lines = []
        for v in value:
            if not v:
                continue
            v = str(v).strip()
            while v.startswith(("-", "—", "·", "–")):
                v = v.lstrip("-—·–").strip()
            lines.append(v)
        return lines
    elif isinstance(value, str):
        v = value.strip()
        while v.startswith(("-", "—", "·", "–")):
            v = v.lstrip("-—·–").strip()
        return [v] if v else []
    return []

def extract_final_summary(folder: Path, days: int = 90) -> CourseFinalSummary:
    docs = extract_study_docs(folder, days=days)  # ✅ 显式传入
    cutoff = datetime.now() - timedelta(days=days)
    info_list = extract_study_info(docs)

    summary = defaultdict(lambda: {
        "学习内容": [],
        "遇到的问题": [],
        "解决方案": [],
        "学习心得": [],
        "count": 0
    })

    for item in info_list:
        course = item.get("course", "").strip()
        date = item.get("date")  # 如果有时间字段

        # 如果有时间字段，可以按需过滤
        # if date and isinstance(date, datetime) and date < cutoff:
        #     continue

        if not course:
            continue

        summary[course]["学习内容"].extend(normalize(item.get("学习内容", "")))
        summary[course]["遇到的问题"].extend(normalize(item.get("遇到的问题", "")))
        summary[course]["解决方案"].extend(normalize(item.get("解决方案", "")))
        summary[course]["学习心得"].extend(normalize(item.get("学习心得", "")))
        summary[course]["count"] += 1

    return summary

# ✅ 测试入口（可单独运行）
if __name__ == "__main__":
    from pprint import pprint

    docs_dir = Path(__file__).resolve().parents[2] / "docs"
    print(f"🔍 提取 {docs_dir} 的期末总结数据...\n")

    result = extract_final_summary(docs_dir, days=3650)

    pprint(result)

