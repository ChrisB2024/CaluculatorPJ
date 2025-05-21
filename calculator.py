x = int(input("Enter a number: " ))
y = int(input("Enter another number: "))
user_input = input("Enter an operation: ")
addition = x + y
substraction = x - y
multiplication = x * y
exponentiation = x ** y
if user_input == "+":
    print(addition)
elif user_input == "-":
    print(substraction)
elif user_input == "*":
    print(multiplication)
elif user_input == "/":
        try:
            division =  x / y
            print(division)
        except ZeroDivisionError:
            print("Error: Division by zero")
elif user_input == "**":
    print(exponentiation)
elif user_input == "//":
        try:
            floor_division = x // y
            print(floor_division)
        except ZeroDivisionError:
            print("Error: Division by zero")
elif user_input == "%":
    try:
        modulus = x % y
        print(modulus)
    except ZeroDivisionError:
        print("Error: Division by zero")
else:
    print("Invalid operation")
