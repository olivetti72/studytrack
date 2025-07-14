import os
from datetime import datetime

VERSION_FILE = "VERSION.md"

def add_version(version: str, description: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    version_entry = f"- **{version}** | `{now}`  \n  {description}\n"

    if not os.path.exists(VERSION_FILE):
        with open(VERSION_FILE, "w", encoding="utf-8") as f:
            f.write("# 📦 本地版本记录\n\n")

    with open(VERSION_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if version in content:
        print(f"⚠️ 版本 {version} 已存在，跳过写入。")
        return

    with open(VERSION_FILE, "a", encoding="utf-8") as f:
        f.write(version_entry + "\n")

    print(f"✅ 版本 {version} 已记录至 {VERSION_FILE}")

if __name__ == "__main__":
    print("📌 生成版本记录")
    version = input("请输入版本号（如 v1.1.0-beta）：").strip()
    desc = input("请输入版本说明：").strip()
    add_version(version, desc)
