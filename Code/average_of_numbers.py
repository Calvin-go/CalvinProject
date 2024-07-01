# average_of_numbers.py
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    numbers = list(map(float, input("Enter numbers separated by space: ").split()))
    average = calculate_average(numbers)
    print(f"The average of the numbers is: {average:.2f}")
