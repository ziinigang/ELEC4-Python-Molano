# Name: Zheena Collene V. Molano
# Section: IV-BSIT-B
# Activity: P4 - Safe Menu Program
# Date: November 26, 2026

def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2

    except ValueError:
        print("Invalid input. Please enter numbers only.")

    except ZeroDivisionError:
        print("Error. Division by zero is not allowed.")

    else:
        print(f"Result: {result}")

    finally:
        print("Division operation completed.")


def open_file():
    try:
        filename = input("Enter the file name: ")

        with open(filename, "r") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error. File not found.")

    else:
        print("\n===== FILE CONTENTS =====")
        print(content)

    finally:
        print("File operation completed.")


def main():
    while True:
        print("\n===== SAFE MENU PROGRAM =====")
        print("1. Divide Numbers")
        print("2. Open File")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_file()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid menu choice. Please select 1 to 3.")


main()