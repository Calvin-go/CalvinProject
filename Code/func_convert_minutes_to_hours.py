# func_convert_minutes_to_hours.py
def func_convert_minutes_to_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours} hours and {remaining_minutes} minutes"

print(func_convert_minutes_to_hours(125))
