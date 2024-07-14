# func_convert_seconds_to_hms.py
def func_convert_seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

print(func_convert_seconds_to_hms(3661))
