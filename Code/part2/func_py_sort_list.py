# func_py_sort_list.py
def sort_list(items, reverse=False):
    """
    Sort a list of items in ascending or descending order.
    """
    if not items:
        raise ValueError("Input list cannot be empty.")
    
    return sorted(items, reverse=reverse)

# Example usage
if __name__ == "__main__":
    items = [5, 2, 9, 1, 5, 6]
    sorted_items = sort_list(items, reverse=True)
    print(f"Sorted List: {sorted_items}")
