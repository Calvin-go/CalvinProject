# func_py_leap_year_checker.py
def func_py_leap_year_checker(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(func_py_leap_year_checker(2024))
print(func_py_leap_year_checker(2023))
