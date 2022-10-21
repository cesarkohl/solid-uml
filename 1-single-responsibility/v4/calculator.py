class Calculator:
    retirement_age: int = 65
    age: int

    def __init__(self, age):
        self.age = age

    def calculate(self):
        print(self.retirement_age - self.age)
