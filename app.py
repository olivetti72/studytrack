import streamlit as st
from pathlib import Path
from datetime import date
from config import WEEKLY_CUTOFF_DAYS, COURSE_CUTOFF_DAYS, FINAL_CUTOFF_DAYS

from processors.weekly.reporter_weekly import run_weekly_report
from processors.course.reporter_course import run_course_report
from processors.final.reporter_final import run_final_report

st.set_page_config(page_title="📘 StudyTrack 学习报告生成器", layout="centered")
st.title("📘 StudyTrack 学习报告生成器")

# --- 📂 输入路径选择区 ---
st.sidebar.header("📁 输入设置")
def_path = Path("docs")
input_dir = st.sidebar.text_input("输入学习文档目录：", value=str(def_path.resolve()))
input_path = Path(input_dir)
if not input_path.exists():
    st.sidebar.error("❌ 目录不存在，请检查路径")

# --- 📄 报告类型选择区 ---
st.sidebar.header("📄 报告类型")
report_type = st.sidebar.radio("请选择要生成的报告：", ["学习周报", "课程总结", "期末总结"])

# --- 📤 主内容区域 ---
st.markdown("---")
st.sidebar.info("📂 当前默认从 docs/ 目录中提取文档。\n请将学习文档放入该目录再点击生成。")

output_dir = Path("output")
today_str = date.today().strftime("%Y-%m-%d")

if report_type == "学习周报":
    st.subheader("📅 学习周报")
    st.markdown("提取过去 7 天的学习内容，生成 Markdown、Word 和 PDF 报告。")

    if st.button("▶️ 生成学习周报"):
        try:
            run_weekly_report(
                input_dir=input_path,
                output_dir=output_dir,
                days=WEEKLY_CUTOFF_DAYS
            )
            st.success("✅ 学习周报生成成功！")
            md_file = output_dir / f"weekly_{today_str}.md"
            pdf_file = output_dir / f"weekly_{today_str}.pdf"

            if md_file.exists():
                with open(md_file, "r", encoding="utf-8") as f:
                    st.markdown("### 📝 报告预览")
                    st.code(f.read(), language="markdown")

            if pdf_file.exists():
                with open(pdf_file, "rb") as f:
                    st.download_button("📥 下载 PDF 文件", f, file_name=pdf_file.name)

        except Exception as e:
            st.error(f"❌ 周报生成失败：{e}")

elif report_type == "课程总结":
    st.subheader("📚 分类课程总结")
    st.markdown("统计每门课程的学习次数、问题与反思，适合阶段性复盘学习。")

    if st.button("▶️ 生成课程总结报告"):
        try:
            run_course_report(
                input_dir=input_path,
                output_dir=output_dir,
                days=COURSE_CUTOFF_DAYS
            )
            st.success("✅ 课程总结生成成功！")
            md_file = output_dir / f"course_{today_str}.md"
            pdf_file = output_dir / f"course_{today_str}.pdf"

            if md_file.exists():
                with open(md_file, "r", encoding="utf-8") as f:
                    st.markdown("### 📝 报告预览")
                    st.code(f.read(), language="markdown")

            if pdf_file.exists():
                with open(pdf_file, "rb") as f:
                    st.download_button("📥 下载 PDF 文件", f, file_name=pdf_file.name)

        except Exception as e:
            st.error(f"❌ 课程总结失败：{e}")

elif report_type == "期末总结":
    st.subheader("📈 分类期末总结")
    st.markdown("期末阶段总结每门课程内容，生成复习导图式表格报告。")

    if st.button("▶️ 生成期末总结报告"):
        try:
            run_final_report(
                input_dir=input_path,
                output_dir=output_dir,
                days=FINAL_CUTOFF_DAYS
            )
            st.success("✅ 期末总结报告生成成功！")
            md_file = output_dir / f"final_report.md"
            pdf_file = output_dir / f"final_report.pdf"

            if md_file.exists():
                with open(md_file, "r", encoding="utf-8") as f:
                    st.markdown("### 📝 报告预览")
                    st.code(f.read(), language="markdown")

            if pdf_file.exists():
                with open(pdf_file, "rb") as f:
                    st.download_button("📥 下载 PDF 文件", f, file_name=pdf_file.name)

        except Exception as e:
            st.error(f"❌ 期末总结失败：{e}")


