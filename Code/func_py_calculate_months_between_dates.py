# func_py_calculate_months_between_dates.py
from datetime import datetime

def func_py_calculate_months_between_dates(date1, date2):
    return abs((date2.year - date1.year) * 12 + date2.month - date1.month)

date1 = datetime(2023, 1, 1)
date2 = datetime(2024, 12, 1)
print(func_py_calculate_months_between_dates(date1, date2))
