from logger import Logger
from calculator import Calculator


class Assistant:
    def __init__(self, age) -> None:
        self.age = age

    def handle_employee(self) -> None:
        (Logger()).log()
        (Calculator(37)).calculate()
