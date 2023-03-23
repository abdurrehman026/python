import math

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Negative numbers do not have real square roots.")
    return math.sqrt(number)

while True:
    user_input = input("Enter a number (or type 'quit' to exit): ")
    if user_input.lower() == "quit":
        break
    try:
        number = float(user_input)
        result = calculate_square_root(number)
        print(f"The square root of {number} is {result:.2f}")
    except ValueError as error:
        print(error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
