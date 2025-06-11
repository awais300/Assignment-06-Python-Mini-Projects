# Student Report Card Generator

students = {}

def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def add_student():
    name = input("Enter student name: ").title()
    roll = int(input("Enter roll number: "))
    marks = []
    for i in range(5):
        m = int(input(f"Enter marks for Subject {i+1}: "))
        marks.append(m)
    
    total = sum(marks)
    average = total / 5
    grade = calculate_grade(average)
    
    students[name] = {
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

def show_report():
    for name, data in students.items():
        print(f"\nStudent Name: {name}")
        print(f"Roll No: {data['roll']}")
        print(f"Marks: {data['marks']}")
        print(f"Total: {data['total']}")
        print(f"Average: {data['average']:.2f}")
        print(f"Grade: {data['grade']}")

# Main
while True:
    print("\nStudent Report Card System")
    print("1. Add Student\n2. Show Reports\n3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        show_report()
    elif choice == '3':
        print("Exiting Report Card Generator.")
        break
    else:
        print("Invalid choice.")
