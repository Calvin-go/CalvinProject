# func_py_calculate_weeks_and_days_between_dates.py
from datetime import datetime

def func_py_calculate_weeks_and_days_between_dates(date1, date2):
    delta = date2 - date1
    weeks = delta.days // 7
    days = delta.days % 7
    return weeks, days

date1 = datetime(2023, 1, 1)
date2 = datetime(2024, 1, 1)
print(func_py_calculate_weeks_and_days_between_dates(date1, date2))
