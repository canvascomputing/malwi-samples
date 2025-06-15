# Importing NumPy as "np"


class Multiplication:

    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, number):
        # Using NumPy .dot() to multiply the numbers
        return number * self.multiplier
