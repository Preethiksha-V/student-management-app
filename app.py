# Student Management System
# Console-based Python Application

students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    if roll_no in students:
        print("Student already exists.")
        return

    name = input("Enter Name: ")
    department = input("Enter Department: ")
    marks = int(input("Enter Marks: "))

    students[roll_no] = {
        "name": name,
        "department": department,
        "marks": marks
    }
    print("Student added successfully.")

def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for roll_no, details in students.items():
        print(f"Roll No: {roll_no}")
        print(f"Name: {details['name']}")
        print(f"Department: {details['department']}")
        print(f"Marks: {details['marks']}")
        grade = calculate_grade(details['marks'])
        print(f"Grade: {grade}")

        print("------------------------")


def search_student():
    roll_no = input("Enter Roll Number to search: ")
    if roll_no in students:
        details = students[roll_no]
        print("\nStudent Found")
        print(f"Name: {details['name']}")
        print(f"Department: {details['department']}")
        print(f"Marks: {details['marks']}")
    else:
        print("Student not found.")

def main_menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please try again.")

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"


if __name__ == "__main__":
    main_menu()
