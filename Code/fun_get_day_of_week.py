# fun_get_day_of_week.py
import datetime

def fun_get_day_of_week():
    return datetime.datetime.now().strftime("%A")

print(fun_get_day_of_week())
