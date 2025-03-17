# func_py_leap_year.py

def func_py_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def test_leap_year():
    years = [2000, 2024, 1900, 2023]
    for year in years:
        print(f"{year} is a leap year: {func_py_leap_year(year)}")

if __name__ == "__main__":
    test_leap_year()
