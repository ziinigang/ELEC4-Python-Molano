# Name: Zheena Collene V. Molano
# Section: IV-BSIT-B
# Activity: P2 - Custom Module: student_utils
# Date: November 23, 2026

import student_utils
from datetime import datetime

print("===== STUDENT GRADE CALCULATOR")
print("Report Date and Time:", datetime.now().strftime("%B %d, %Y %I:%M %p"))

grades = []

while True:
    try:
        count = int(input("\nHow many grades will you enter?"))

        if count > 0:
            break

        print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

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

average = student_utils.calculate_average(grades)
result = student_utils.determine_result(average)

print("\n===== STUDENT RESULTS =====")
print("Grades:", grades)
print(f"Average: {average:.2f}")
print("Highest Grade:", student_utils.get_highest_grade(grades))
print("Lowest Grade:", student_utils.get_lowest_grade(grades))
print("Result:", result)