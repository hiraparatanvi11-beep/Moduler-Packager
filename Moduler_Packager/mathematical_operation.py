# ----------------------------------------------------------
# 2. MATHEMATICAL OPERATIONS
# ----------------------------------------------------------
import math


def mathematical_operation():
    while True:
        print("\n----Mathematical Operations----")
        print("1.Calculate Factorial")
        print("2.Solve Compound Interest")
        print("3.Trigonometric Functions")
        print("4.Area of Geometric Shapes")
        print("5.Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter a number:"))
            print("Factorial:", math.factorial(n))

        elif choice == "2":
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter rate of interest(in %): "))
            years = float(input("Enter time(in years):"))

            amount = principal * ((1 + rate / 100) ** years)
            compound_interest = amount - principal

            print("Compound Interest:", round(compound_interest, 2))

        elif choice == "3":
            angle = float(input("Enter angle in degrees: "))

            radians = math.radians(angle)

            print("Sin:", round(math.sin(radians), 4))
            print("Cos:", round(math.cos(radians), 4))
            print("Tan:", round(math.tan(radians), 4))

        elif choice == "4":
            print("\n1.Circle")
            print("2.Rectangle")
            print("3.Triangle")

            shape = input("Enter your choice: ")

            if shape == "1":
                radius = float(input("Enter radius: "))
                area = math.pi * radius * radius
                print("Area of Circle:", round(area, 2))

            elif shape == "2":
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area = length * width
                print("Area of Rectangle:", round(area, 2))

            elif shape == "3":
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                area = 0.5 * base * height
                print("Area of Triangle:", round(area, 2))

            else:
                print("Invalid choice!")

        elif choice == "5":
            break

    else:    
     print("Invalid choice!")
