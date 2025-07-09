# app.py

import streamlit as st
from datetime import date
from pathlib import Path
import shutil
import os

# 导入主逻辑函数
from main_final import main as generate_final_report
from main_course import main as generate_course_report
from main_weekly import main as generate_weekly_report

# 根目录
BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"
OUTPUT_DIR = BASE_DIR / "output"

st.set_page_config(page_title="StudyTrack 学习报告生成器", layout="centered")

st.title("📘 StudyTrack 学习报告生成器")

# --------------------------------------------
# ⏱️ 时间范围 & 📓 学期名称输入
# --------------------------------------------

st.subheader("🛠️ 参数设置")

with st.form("params_form"):
    days = st.slider("选择统计时间范围（单位：天）", min_value=7, max_value=365, value=90, step=7)
    semester = st.text_input("输入学期名称（用于报告标题）", value="2025春季学期")
    submitted = st.form_submit_button("✅ 应用设置")

# --------------------------------------------
# 📤 上传 Word 文档
# --------------------------------------------

st.subheader("📄 上传学习总结文档（Word）")

uploaded_files = st.file_uploader("上传一个或多个 .docx 文件", type=["docx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        save_path = DOCS_DIR / file.name
        with open(save_path, "wb") as f:
            f.write(file.read())
    st.success(f"已成功上传 {len(uploaded_files)} 个文档。")

# --------------------------------------------
# 📊 生成按钮区域
# --------------------------------------------

st.subheader("📈 生成学习报告")

col1, col2, col3 = st.columns(3)

if col1.button("📘 生成期末总结报告"):
    generate_final_report()
    st.success("✅ 期末总结报告已生成")

if col2.button("📚 生成课程总结报告"):
    generate_course_report()
    st.success("✅ 课程总结报告已生成")

if col3.button("📝 生成学习周报"):
    generate_weekly_report()
    st.success("✅ 学习周报已生成")

# --------------------------------------------
# 📂 查看输出文件
# --------------------------------------------

st.subheader("📁 查看已生成报告")

output_files = sorted(OUTPUT_DIR.glob("*.*"))

if output_files:
    for f in output_files:
        st.markdown(f"📄 [{f.name}](./output/{f.name})")
else:
    st.info("尚未生成任何报告。")

