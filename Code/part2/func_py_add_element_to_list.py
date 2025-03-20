# func_py_add_element_to_list.py

def func_py_add_element_to_list(lst, element):
    lst.append(element)
    return lst

def test_add_element_to_list():
    numbers = [1, 2, 3]
    print(f"List after addition: {func_py_add_element_to_list(numbers, 4)}")

if __name__ == "__main__":
    test_add_element_to_list()
