# main_weekly.py

from pathlib import Path
from config import INPUT_DIR, OUTPUT_DIR, WEEKLY_CUTOFF_DAYS
from processors.weekly.reporter_weekly import run_weekly_report

def main():
    print("📊 开始生成学习周报...")
    run_weekly_report(
        input_dir=INPUT_DIR,
        output_dir=OUTPUT_DIR,
        cutoff_days=WEEKLY_CUTOFF_DAYS
    )
    print("🎉 学习周报生成完成！")

if __name__ == "__main__":
    main()
