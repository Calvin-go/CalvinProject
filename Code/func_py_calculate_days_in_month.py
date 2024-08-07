# func_py_calculate_days_in_month.py
import calendar

def func_py_calculate_days_in_month(year, month):
    return calendar.monthrange(year, month)[1]

print(func_py_calculate_days_in_month(2024, 2))
