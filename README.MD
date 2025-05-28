
# StudyTrack 学习报告生成器

**StudyTrack** 是一个学生学习总结辅助工具，支持上传 Word 学习文档，自动生成学习周报、课程分类总结和期末总结报告，并可导出为 Markdown、Word、PDF 和 HTML 格式，适合在 Web 页面中使用。

---

## 🔧 环境要求

- Python 3.10 及以上
- 推荐使用虚拟环境（如 `.venv`）

此外，请确保安装以下外部工具（用于格式转换）：

- [Pandoc](https://pandoc.org/installing.html)：支持 Markdown 转 Word/PDF/HTML
- [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)：如启用 HTML 转 PDF 功能

---

## ✨ 功能特点

- 支持上传多个 `.docx` 格式的学习记录
- 自动生成三类学习报告：
  - 📆 学习周报
  - 📚 课程分类总结（默认近 30 天）
  - 📝 期末总结报告
- 多格式导出：
  - `.md`（Markdown）
  - `.docx`（Word）
  - `.pdf`（PDF）
  - `.html`（网页）
- 提供简洁直观的 Web 界面（基于 Streamlit）

---

## 🚀 使用方式

### 1. 安装依赖

确保已激活虚拟环境后执行：

```bash
pip install -r requirements.txt
```

### 2. 启动 Streamlit 应用

```bash
streamlit run app.py
```

### 3. 使用步骤

1. 上传 `.docx` 学习记录文件（可多选）
2. 选择报告类型：
   - 学习周报
   - 课程分类总结
   - 期末总结报告
3. 点击 **生成报告**
4. 下载需要的报告格式（`.md` / `.docx` / `.pdf` / `.html`）

---

## 📁 项目结构说明

```
studytrack/
├── app.py                   # 主界面入口
├── main_weekly.py           # 周报生成脚本
├── course_stats.py          # 课程统计脚本
├── generate_final_report.py # 期末报告脚本
├── processors/              # 文档提取与处理模块
├── templates/               # 报告模板（Markdown）
├── docs/                    # 上传文档目录
├── output/                  # 报告输出目录
├── requirements.txt         # 项目依赖
└── README.md                # 使用说明
```

---

## 🖼 示例界面（可选）

若准备好截图，可如下插入：

```markdown
![界面示意图](docs/interface_screenshot.png)
```

---

## 开发者信息

- 项目作者：刘胤廷
- 联系方式：1827764696@qq.com

---

## License

本项目基于 BISTU License 开源，可自由使用、修改与分发。
