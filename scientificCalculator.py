from sympy import symbols, diff, integrate, sin, cos, tan, log
import math
import statistics

def main():
    while True:
        print("\nAdvanced Scientific Calculator")
        print("1. Derivative")
        print("2. Integration")
        print("3. Statistics")
        print("4. Decimal to Binary")
        print("5. Binary to Decimal")
        print("6. Logarithm")
        print("7. Trigonometry")
        print("8. Exit")

        choice = input("Enter a choice (1-8): ")

        if choice == "1":
            handleDerivative()
        elif choice == "2":
            handleIntegration()
        elif choice == "3":
            handleStatistics()
        elif choice == "4":
            handleDecToBin()
        elif choice == "5":
            handleBinToDec()
        elif choice == "6":
            handleLogarithm()
        elif choice == "7":
            handleTrigonometry()
        elif choice == "8":
            print("Thank you for using our calculator! Goodbye!")
            break
        else:
            print("You need to pick a valid operation")

def handleDerivative():
    try:
        function = input("Enter your function (use x as variable): ")
        x = symbols('x')
        derivative = diff(function, x)
        print(f"Derivative: {derivative}")
    except Exception as e:
        print(f"Error calculating derivative: {e}")

def handleIntegration():
    try:
        function = input("Enter your function (use x as variable): ")
        x = symbols('x')
        integration = integrate(function, x)
        print(f"Integration: {integration}")
    except Exception as e:
        print(f"Error calculating integration: {e}")

def handleStatistics():
    try:
        numbers = input("Enter numbers separated by spaces: ").split()
        numbers = [float(num) for num in numbers]
        print(f"Mean: {statistics.mean(numbers)}")
        print(f"Median: {statistics.median(numbers)}")
        print(f"Standard Deviation: {statistics.stdev(numbers)}")
    except Exception as e:
        print(f"Error calculating statistics: {e}")

def handleDecToBin():
    try:
        decimal = int(input("Enter a decimal number: "))
        binary = bin(decimal)[2:]  # remove '0b' prefix
        print(f"Binary: {binary}")
    except Exception as e:
        print(f"Error converting to binary: {e}")

def handleBinToDec():
    try:
        binary = input("Enter a binary number: ")
        decimal = int(binary, 2)
        print(f"Decimal: {decimal}")
    except Exception as e:
        print(f"Error converting to decimal: {e}")

def handleLogarithm():
    try:
        number = float(input("Enter a number: "))
        base = input("Enter the base (default is e): ")
        if base == "" or base.lower() == "e":
            result = math.log(number)
        else:
            result = math.log(number, float(base))
        print(f"Logarithm: {result}")
    except Exception as e:
        print(f"Error calculating logarithm: {e}")

def handleTrigonometry():
    try:
        angle = float(input("Enter angle in degrees: "))
        radians = math.radians(angle)
        print(f"Sine: {math.sin(radians)}")
        print(f"Cosine: {math.cos(radians)}")
        print(f"Tangent: {math.tan(radians)}")
        print(f"Secant: {1 / math.cos(radians)}")
        print(f"Cosecant: {1 / math.sin(radians)}")
        print(f"Cotangent: {1 / math.tan(radians)}")
    except Exception as e:
        print(f"Error calculating trigonometry: {e}")

if __name__ == "__main__":
    main()

    
