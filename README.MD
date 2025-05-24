# StudyTrack 学习报告生成器

**StudyTrack** 是一个用于生成学生学习总结的辅助工具，支持上传 Word 学习文档，自动生成学习周报、课程分类总结及期末总结报告，并可导出为 Markdown、Word、PDF 和 HTML 等格式。

---

## 功能特点

- 支持上传多个 `.docx` 格式学习记录
- 支持三类学习报告生成：
  - **学习周报**
  - **课程分类总结**（默认近 30 天）
  - **期末总结报告**
- 支持导出为以下格式：
  - `.md`（Markdown）
  - `.docx`（Word）
  - `.pdf`（PDF）
  - `.html`（网页）
- 提供简洁直观的 Streamlit 可视化界面

---

## 使用方式

### 1. 安装依赖

确保已激活虚拟环境（如 `.venv`）后，执行：

```bash
pip install -r requirements.txt
```

### 2. 启动 Streamlit 界面应用

```bash
streamlit run app.py
```

### 3. 操作步骤

1. 上传 `.docx` 学习记录文件（支持多个）
2. 选择报告类型：
   - 学习周报
   - 课程分类总结
   - 期末总结报告
3. 点击 **生成报告**
4. 下载所需格式的报告文件（`.md` / `.docx` / `.pdf` / `.html`）

---

## 项目结构说明

```
studytrack/
├── app.py                   # Streamlit 可视化入口
├── main_weekly.py           # 学习周报生成脚本
├── course_stats.py          # 课程分类总结脚本
├── generate_final_report.py # 期末总结生成脚本
├── processors/              # 文档提取与处理模块
├── templates/               # 报告模板文件（Markdown）
├── docs/                    # 用户上传文档的临时目录
├── output/                  # 报告生成输出目录
├── requirements.txt         # 依赖安装列表
└── README.md                # 项目说明文档
```

---

## 示例截图（可选）

若你准备了操作界面截图，可按如下方式插入：

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
