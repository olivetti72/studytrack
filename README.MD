📄 README.md 推荐内容（适配 v2.0.0）
markdown
复制
编辑
# 📘 StudyTrack 学习报告生成器

一个面向学生的自动化学习总结工具，支持生成学习周报、课程总结、期末复习总结，并导出为 Markdown / Word / PDF 格式。

---

## ✨ 主要功能

- 🗓️ **学习周报**：从近 7 天文档中提取内容，生成结构化报告；
- 📚 **课程总结**：按课程分类提取内容，适用于阶段性复盘；
- 📈 **期末总结**：提取课程内容生成表格式复习报告；
- 🖨️ **支持导出**：可导出为 `.md` / `.docx` / `.pdf` 格式；
- 💻 **双模式使用**：
  - `CLI` 命令行运行（如 `python processors/weekly/reporter_weekly.py`）
  - `Streamlit` 图形界面运行：`streamlit run app.py`

---

## 📁 项目结构（v2.0.0）

studytrack/
├── app.py # Streamlit 图形界面入口
├── config.py # 全局配置项（路径、时间窗口等）
├── docs/ # ✅ 输入：原始学习文档目录
├── output/ # ✅ 输出：生成的报告文件
├── processors/
│ ├── weekly/ # 学习周报逻辑
│ │ └── reporter_weekly.py
│ ├── course/ # 课程总结逻辑
│ │ └── reporter_course.py
│ ├── final/ # 分类期末总结逻辑
│ │ └── reporter_final.py
│ ├── shared/ # 通用模块（如导出器）
│ └── exporter_common.py
└── requirements.txt

yaml
复制
编辑

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
你还需要安装 Pandoc 和 xelatex 以支持 Word/PDF 导出（推荐安装 TeX Live）。

2. 运行方式
🖥️ CLI 模式（命令行）
bash
复制
编辑
python processors/weekly/reporter_weekly.py     # 生成周报
python processors/course/reporter_course.py     # 生成课程总结
python processors/final/reporter_final.py       # 生成期末总结
🌐 Streamlit 图形界面
bash
复制
编辑
streamlit run app.py
✍️ 报告模板说明
输入目录默认为 docs/，输出目录为 output/

输入文件为 .docx，要求包含字段如课程名、学习内容、问题、心得等

输出包括 Markdown（结构清晰）、Word（便于排版）、PDF（便于提交）

📌 版本记录
v2.0.0（当前）：

重构模块结构为 reporter_xxx.py 系列

Streamlit 界面整合统一入口

支持 CLI 和 GUI 双模式