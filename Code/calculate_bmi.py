# calculate_bmi.py
class Person:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

if __name__ == "__main__":
    person = Person("John Doe", 70, 1.75)
    bmi = person.calculate_bmi()
    print(f"{person.name}'s BMI: {bmi:.2f}")
