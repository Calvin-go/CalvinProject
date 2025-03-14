# func_py_matrix_transpose.py

def func_py_matrix_transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def test_matrix_transpose():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original Matrix:")
    for row in matrix:
        print(row)

    transposed = func_py_matrix_transpose(matrix)
    print("\nTransposed Matrix:")
    for row in transposed:
        print(row)

if __name__ == "__main__":
    test_matrix_transpose()
