class Assistant:
    retirement_age: int = 65
    age: int

    def __init__(self, age) -> None:
        self.age = age

    def handle_employee(self) -> None:
        self.log()
        self.calculate()

    def log(self) -> None:
        print("Logging data...")

    def calculate(self):
        print(self.retirement_age - self.age)
