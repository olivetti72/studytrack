
# StudyTrack 项目版本规划文档

## 🔖 v1.0.0：初始版本（稳定可用）

### ✅ 功能目标
- 实现学习周报、课程分类总结、期末总结报告的基本生成功能。
- 支持 `.docx` 学习文档上传与解析。
- Streamlit Web 界面，允许多文档上传、类型选择与格式下载。
- 成功打包上传 GitHub，并具备可运行说明。

### ✅ 关键任务
- [x] `main_weekly.py`, `course_stats.py`, `generate_final_report.py` 实现初步功能。
- [x] `processors/` 模块包含 extractor、writer、exporter 等基本模块。
- [x] Streamlit 界面实现上传和格式选择。
- [x] GitHub 项目上传，添加 README 与依赖说明。

---

## 🔖 v1.1.0：结构标准化与模块统一

### ✅ 功能目标
- 将 `course_stats.py`, `generate_final_report.py` 按照“周报模块化逻辑”改写为统一结构：`extractor` + `formatter` + `writer` + `exporter`。
- 保持接口一致性，方便维护和拓展。
- 引入依赖清单（如 requirements.txt）与推荐启动方式（如启动脚本或 `Makefile`）。

### ✅ 模块任务拆分
- [ ] 重构 `course_stats` 为模块化结构：
  - `extractor_course.py`
  - `formatter_course.py`
  - `writer_course.py`
  - `exporter_course.py`
- [ ] 重构 `generate_final_report` 为模块化结构：
  - `extractor_final.py`
  - `formatter_final.py`
  - `writer_final.py`
  - `exporter_final.py`
- [ ] 完善项目结构与依赖文件：
  - 添加 `requirements.txt`
  - 添加 `README.md` 中运行说明
  - 添加 `.streamlit/config.toml` 模板设置（如默认端口）

---

## 🔖 v1.2.0：输入多样性与报告呈现优化

### ✅ 用户反馈功能拓展
- [ ] 增加对平板类笔记输入支持：
  - 支持 PDF 笔记、OneNote、Notability 导出格式解析。
- [ ] 增加 OCR 图片拍照输入能力（选用 `pytesseract` 等 OCR 工具）。
- [ ] 改进报告表格渲染逻辑，使其稳定美观，支持自动缩放与分页。
- [ ] 增加导出选项（如：Markdown with TOC、Web 页形式等）

---

## 🔖 后续计划展望（可独立分支开发）

- [ ] 将项目封装为桌面端应用（PyInstaller / Electron + PyWebView）
- [ ] 或部署为微信小程序（采用后端接口服务如 FastAPI）
- [ ] 增加用户管理和笔记分类历史功能（持久化）
- [ ] 数据安全与隐私合规性机制设计

---

## 💡 技术建议与能力补强

| 问题 | 建议 |
|------|------|
| Streamlit 启动环境与虚拟环境不一致 | 熟悉 `where python`/`which python` 与 PyCharm 配置，掌握虚拟环境绑定方式 |
| 成员无法运行克隆代码 | 加入 `.venv` 配置说明 + `requirements.txt` + 启动文档（或 Makefile） |
| 模块划分逐渐混乱 | 严格执行模块化结构（extractor/formatter/writer/exporter） |
| 多输入格式兼容性不足 | 学习 `pdfplumber`, `pytesseract`, `PaddleOCR` 等工具使用 |

---

> 更新时间：2025-05-28
