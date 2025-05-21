try:
    x = int(input("Enter a number: " ))
    y = int(input("Enter another number: "))
    user_input = input("Enter an operation: ")
    if user_input == "+":
         print(x + y)
    elif user_input == "-":
         print(x - y)
    elif user_input == "*":
         print(x * y)
    elif user_input == "/":
         print(x/y)
    elif user_input == "**":
         print(x ** y)
    elif user_input == "//":
         print(x // y)
    elif user_input == "%":
         print(x % y)
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid input")
