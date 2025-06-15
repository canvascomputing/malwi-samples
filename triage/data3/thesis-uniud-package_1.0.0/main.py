import random

def random_calculations():
    # Generate two random numbers
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # Perform some basic calculations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "undefined"

    # Print the results
    print(f"Random numbers: {num1}, {num2}")
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")

if __name__ == "__main__":
    random_calculations()
