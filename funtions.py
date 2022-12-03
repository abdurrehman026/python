def addition():
    a = int(input("Enter any two numbers"))
    b = int(input())
    sum = a + b
    print("The Answer of the entered numbers is: ", sum)
def subtraction():
    a = int(input("Enter any two numbers"))
    b = int(input())
    sub = a - b
    print("The Answer of the entered numbers is: ", sub)
def multiplication():
    a = int(input("Enter any two numbers"))
    b = int(input())
    product = a * b
    print("The Answer of the entered numbers is: ", product)
def division():
    a = int(input("Enter any two numbers"))
    b = int(input())
    div = a / b
    print("The Answer of the entered numbers is: ",div)
def condition():
    print("Enter '0' to continue")
    zero = int(input())

    if zero != 0:
            print("Failed to detect '0, re-enter")
    else:
            print("You May proceed")


print("BASIC CALCULATION")
condition()
print("For Addition")
addition()
print("For Subtraction")
subtraction()
print("For Multiplication")
multiplication()
print("For Division")
division()


# zero = int(input())
# if zero == 0:
#     print("You may Proceed")
# else:
#     print("Failed to detect '0', re-enter")