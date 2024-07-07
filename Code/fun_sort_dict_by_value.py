# fun_sort_dict_by_value.py
def fun_sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

sample_dict = {'apple': 10, 'banana': 2, 'cherry': 5}
print(fun_sort_dict_by_value(sample_dict))
