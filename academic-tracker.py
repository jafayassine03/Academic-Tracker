import json
import os

FILE_NAME = "academictracker.json"


def ensure_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump({}, f)


def load_data():
    ensure_file()
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


students = load_data()


def add_student():
    name = input("Enter student name: ").strip()

    if name in students:
        print(" Student already exists!")
        return

    try:
        age = int(input("Enter student age: "))
        grade = float(input("Enter student grade: "))
    except ValueError:
        print(" Age must be number and grade must be numeric!")
        return

    major = input("Enter student major: ")
    note = input("Enter student note: ")

    students[name] = {
        "age": age,
        "grade": grade,
        "major": major,
        "note": note
    }

    save_data(students)
    print("✅ Student added successfully!")


def view_students():
    if not students:
        print("⚠ No students found.")
        return

    for name, info in students.items():
        print("-" * 30)
        print(f"Name  : {name}")
        print(f"Age   : {info['age']}")
        print(f"Grade : {info['grade']}")
        print(f"Major : {info['major']}")
        print(f"Note  : {info['note']}")
    print("-" * 30)


while True:
    print("\n" + "=" * 10 + " Academic Tracker " + "=" * 10)
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")