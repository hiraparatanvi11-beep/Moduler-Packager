# ----------------------------------------------------------
# 5. FILE OPERATIONS 
# ----------------------------------------------------------

def file_operation():

    while True:

        print("\n--- File Operations (Custom Module) ---")
        print("1. Create a New File")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            filename = input("Enter file name: ")

            try:

                with open(filename, "w") as file:
                    pass

                print("File created successfully!")

            except Exception as e:

                print("Error:", e)

        elif choice == "2":

            filename = input("Enter file name: ")
            data = input("Enter data to write: ")

            try:

                with open(filename, "w") as file:
                    file.write(data)

                print("Data written successfully!")

            except Exception as e:

                print("Error:", e)

        elif choice == "3":

            filename = input("Enter file name: ")

            try:

                with open(filename, "r") as file:
                    data = file.read()

                print("\nFile Content:")
                print(data)

            except FileNotFoundError:

                print("File not found!")

        elif choice == "4":

            filename = input("Enter file name: ")
            data = input("Enter data to append: ")

            try:

                with open(filename, "a") as file:
                    file.write("\n" + data)

                print("Data appended successfully!")

            except Exception as e:

                print("Error:", e)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")

