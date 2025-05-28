import streamlit as st
import os
import shutil
import subprocess

st.set_page_config(page_title="StudyTrack 学习报告助手", layout="centered")
st.title("StudyTrack 学习报告生成器")

# 上传 Word 文档
uploaded_files = st.file_uploader("上传 Word 学习文档（支持多个）", type=["docx"], accept_multiple_files=True)

# 功能选择
report_type = st.selectbox("选择生成报告类型", ["学习周报", "课程分类总结", "期末总结报告"])

# 生成按钮
if st.button("生成报告"):
    if not uploaded_files:
        st.warning("请先上传 Word 文档！")
    else:
        # 清空并保存 docs 目录
        if os.path.exists("docs"):
            shutil.rmtree("docs")
        os.makedirs("docs")

        for file in uploaded_files:
            file_path = os.path.join("docs", file.name)
            st.write(f"保存文件：{file_path}")
            with open(file_path, "wb") as f:
                f.write(file.read())
            # 写入当前 docs 目录内容到日志，便于确认是否上传成功
            with open("upload_debug.txt", "w", encoding="utf-8") as logf:
                logf.write("当前 docs 目录文件列表：\n")
                logf.write("\n".join(os.listdir("docs")))

        script_map = {
            "学习周报": ("main_weekly.py", "weekly_report"),
            "课程分类总结": ("course_stats.py", "summary_30d"),
            "期末总结报告": ("generate_final_report.py", "final_report"),
        }

        script, output_name = script_map[report_type]

        python_path = os.path.join(".venv", "Scripts", "python.exe")
        subprocess.run([python_path, script])

        st.success("✅ 报告生成成功！请选择下载格式：")
        for ext in ["md", "docx", "pdf", "html"]:
            file_path = os.path.join("output", f"{output_name}.{ext}")
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    st.download_button(f"下载 {ext.upper()}", f, file_name=os.path.basename(file_path))
                    st.write("当前 output 目录内容：", os.listdir("output"))