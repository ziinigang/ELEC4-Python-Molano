# Name = Zheena Collene V. Molano
# Section = IV-BSIT-B
# Activity: P1 - Student Grade Calculator
# Date: November 22, 2026

def accept_grades():
    grades = []

    while True:
        try:
            count = int(input("How many grades will you enter?"))
            if  count > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please  enter a whole number.")

    for i in range(count):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1} (0-100): "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades  



def compute_average(grades):
    return sum(grades) / len(grades)


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)


def determine_result(average):
    if average >= 75:
        return "PASSED"
    return "FAILED"


def main():
    grades = []

    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("1. Enter Student Grades")
        print("2. View Results")
        print("3. Exit")


        choice = input("Choose an option: ")


        if choice == "1":
            grades = accept_grades()
            print("Grades successfully recorded.")
        elif choice == "2":
            if not grades:
                print("Please enter grades first.")
            else:
                average = compute_average(grades)
                highest = get_highest_grade(grades)
                lowest = get_lowest_grade(grades)
                result = determine_result(average)

                print("\n===== STUDENT RESULTS =====")
                print(f"Grades: {grades}")
                print(f"Average: {average:.2f}")
                print(f"Highest Grade: {highest}")
                print(f"Lowest Grade: {lowest}")
                print(f"Result: {result}")

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break


        else:
            print("Invalid choice. Please select 1, 2, or 3.")


main()


# Local variables are created inside a function and can only be used
# within that function. For example, grades inside accept_grades()
# is a local variable. A global variable is created outside functions
# and can be accessed throughout the program. In this program, there
# is no global variable because grades inside main() is local to main().
