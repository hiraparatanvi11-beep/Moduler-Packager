import datetime
import time
import math
import random
import uuid
import string
import importlib

from Moduler_Packager.file_operation import file_operation
from Moduler_Packager.mathematical_operation import mathematical_operation
# ----------------------------------------------------------
# 1. DATETIME AND TIME OPERATIONS
# ----------------------------------------------------------

def datetime_operations():
    while True:

        print("\n----Datetime and Time Operations----")
        print("1.Display current date and time")
        print("2.Calculate diffrence between two dates/times")
        print("3.Formate date into custom format")
        print("4.Stopwatch")
        print("5.Countdown Timer")
        print("6.Back to Main Menu")

        choice = input("Enter your choice:")

        if choice == "1":
           now = datetime.datetime.now()

           print("Current Date and Time:",
               now.strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "2":
          date1 = input("Enter the first date(YYYY-MM-DD):")
          date2 = input("Enter the Second date(YYYY-MM-DD):")

          d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
          d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

          difference = abs((d2-d1).days)
          print("Difference:",difference,"days")


        elif choice == "3":
          date = input("Enter date(YYYY-MM-DD):")
          d = datetime.datetime.strptime(date,"%Y-%m-%d")
          print("Formatted Date",d.strftime("%d-%m-%Y"))


        elif choice == "4":
           print("Stopwatch started...")
           start = time.time()
           input("Press Enter to stop the stopwatch")
           end = time.time()

           print("Elapsed Time:",
           round(end - start, 2), "seconds")


        elif choice == "5":
            seconds = int(input("Enter countdown seconds: "))
            print("Countdown Started...")

            while seconds > 0:
                print(seconds)
                time.sleep(1)
                seconds -= 1

            print("Time's Up!")


        elif choice == "6":
            break
        else:
            print("Invalid choice!")


# ----------------------------------------------------------
# 3. RANDOM DATA GENERATION
# ----------------------------------------------------------

def random_operations():

    while True:

        print("\n--- Random Data Generation ---")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Random Sampling")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            number = random.randint(1, 100)

            print("Random Number:", number)

        elif choice == "2":

            numbers = []

            for i in range(5):
                numbers.append(random.randint(1, 50))

            print("Random List:", numbers)

        elif choice == "3":

            length = int(input("Enter password length: "))

            characters = (
                string.ascii_letters +
                string.digits +
                string.punctuation
            )

            password = ""

            for i in range(length):
                password += random.choice(characters)

            print("Generated Password:", password)

        elif choice == "4":

            otp = ""

            for i in range(6):
                otp += str(random.randint(0, 9))

            print("Generated OTP:", otp)

        elif choice == "5":

            data = [1, 2, 3, 4, 5,
                    6, 7, 8, 9, 10]

            sample = random.sample(data, 3)

            print("Original Data:", data)
            print("Random Sample:", sample)

        elif choice == "6":
            break

        else:
            print("Invalid choice!")


# ----------------------------------------------------------
# 4. UUID OPERATIONS
# ----------------------------------------------------------

def uuid_operations():
    print("\n--- Generate Unique Identifiers (UUID) ---")
    print("Generated UUID:", uuid.uuid4())


# ----------------------------------------------------------
# 6. MODULE ATTRIBUTES  
# ----------------------------------------------------------



def explore_module():
    print("\n--- Explore Module Attributes (dir()) ---")

    module_name = input(
        "Enter module name to explore: "
    )

    try:
        module = importlib.import_module(module_name)

        attributes = dir(module)

        print(
            f"Available Attributes in {module_name}:"
        )
        print(attributes)

    except ModuleNotFoundError:
        print("Module not found.")




# ----------------------------------------------------------
# MAIN MENU
# ----------------------------------------------------------

def main():

    print("=" * 50)
    print("WELCOME TO MULTI-UTILITY TOOLKIT")
    print("=" * 50)

    while True:

        print("\nChoose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_operations()

        elif choice == "2":
            mathematical_operation()

        elif choice == "3":
            random_operations()

        elif choice == "4":
            uuid_operations()

        elif choice == "5":
            file_operation()

        elif choice == "6":
            explore_module()

        elif choice == "7":

            print("\nThank you for using the Multi-Utility Toolkit!")
            break

        else:
            print("Invalid choice! Please try again.")


# ----------------------------------------------------------
# __name__ AND __main__
# ----------------------------------------------------------

if __name__ == "__main__":
    main()