from processors.course.reporter_course import run_course_report
from config import INPUT_DIR, OUTPUT_DIR, COURSE_CUTOFF_DAYS

run_course_report(INPUT_DIR, OUTPUT_DIR, COURSE_CUTOFF_DAYS)
