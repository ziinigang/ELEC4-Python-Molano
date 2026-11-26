
# Name: Zheena Collene V. Molano
# Section: IV-BSIT-B
# Activity: P3 - Student Record Manager
# Date: November 26, 2026

students = []
student_names = set()


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
    elif name.casefold() in student_names:
        print("Student already exists.")
    else:
        students.append(name)
        student_names.add(name.casefold())
        print(f"{name} successfully added.")


def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.casefold() == name.casefold():
            students.remove(student)
            student_names.remove(student.casefold())
            print(f"{student} successfully removed.")
            return

    print("Student not found.")


def search_student():
    name = input("Enter name to search: ").strip().casefold()

    if not name:
        print("Please enter a name to search.")
        return

    results = [
        student for student in students
        if name in student.casefold()
    ]

    if results:
        print("\n===== SEARCH RESULTS =====")
        for student in results:
            print(student)
    else:
        print("No matching student found.")


def display_students():
    if not students:
        print("No students recorded yet.")
        return

    print("\n===== STUDENT LIST =====")

    for number, student in enumerate(
        sorted(students, key=str.casefold), start=1
    ):
        print(f"{number}. {student}")

    print(f"Total Students: {len(students)}")


def main():
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")

main()

# A list stores student names and allows us to add and remove entries.
# A set stores unique names and helps prevent duplicate student records.
# In this program, the students variable is a list, while student_names
# is a set that stores lowercase versions of names for duplicate checking.
# Both collections help manage student records correctly.