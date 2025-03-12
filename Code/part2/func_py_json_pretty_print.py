# func_py_json_pretty_print.py
import json

def func_py_json_pretty_print(json_str):
    parsed_json = json.loads(json_str)
    return json.dumps(parsed_json, indent=4, sort_keys=True)

json_data = '{"name": "Alice", "age": 25, "city": "New York"}'
print(func_py_json_pretty_print(json_data))
