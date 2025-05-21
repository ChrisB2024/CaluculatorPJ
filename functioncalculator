def calculator(num1 , num2):
         try: 
             user_input = input("Enter an operation(+, -, /, //, *, **, %): ")
             if user_input == "+":
                return num1 + num2
             elif user_input == "*":
                return num1 * num2
             elif user_input == "-":
                return num1 - num2
             elif user_input == "/":
                return num1 / num2
             elif user_input == "//":
                return num1 // num2
             elif user_input == "**":
                return num1 ** num2
             elif user_input == "%":
                return num1 % num2
             else:
                print("Invalid operation.")
         except ZeroDivisionError:
            print("Error: we can't divide by zero.")
try:
   x = int(input("Enter a number: "))
   y = int(input("Enter another number: "))
   result = calculator(x, y)
   if result is not None:
     print("Result:", result)
except ValueError:
   print("Error: enter a good number.")
