# fibonacci_sequence.py
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

num_terms = 10
fibonacci_sequence = fibonacci(num_terms)
print(f"First {num_terms} terms of the Fibonacci sequence: {fibonacci_sequence}")
