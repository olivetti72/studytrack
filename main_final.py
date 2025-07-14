# main_final.py（可选保留）
from processors.final.reporter_final import run_final_report
from config import INPUT_DIR, OUTPUT_DIR

if __name__ == "__main__":
    run_final_report(INPUT_DIR, OUTPUT_DIR)


