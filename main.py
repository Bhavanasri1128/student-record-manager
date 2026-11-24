from records import (
    load_records,
    add_student,
    update_student,
    delete_student,
    rank_by_marks
)

def main():
    students = load_records()

    while True:
        print("\n--- STUDENT RECORD & ATTENDANCE MANAGEMENT ---")
        print("1. Add Student Record")
        print("2. Search Student by Roll Number")
        print("3. Update Marks & Attendance")
        print("4. Delete Student Record")
        print("5. Rank Students by Marks (Highest to Lowest)")
        print("6. View Attendance Shortage (<75%)")
        print("7. Exit")

        choice = input("Enter choice: ").strip()
        try:
            if choice == "1":
                roll = input("Roll Number: ").strip()
                name = input("Student Name: ").strip()
                marks = int(input("Marks (0-100): "))
                att = float(input("Attendance % (0-100): "))
                add_student(students, roll, name, marks, att)
                print("Student added and saved to file!")

            elif choice == "2":
                roll = input("Enter Roll Number: ").strip()
                if roll in students:
                    s = students[roll]
                    status = "Eligible" if s["attendance"] >= 75 else "Shortage (<75%)"
                    print(f"Name: {s['name']} | Marks: {s['marks']} | Attendance: {s['attendance']}% ({status})")
                else:
                    print("Student not found.")

            elif choice == "3":
                roll = input("Enter Roll Number: ").strip()
                marks = int(input("New Marks (0-100): "))
                att = float(input("New Attendance % (0-100): "))
                update_student(students, roll, marks, att)
                print("Record updated!")

            elif choice == "4":
                roll = input("Enter Roll Number to delete: ").strip()
                delete_student(students, roll)
                print("Student deleted!")

            elif choice == "5":
                ranked = rank_by_marks(students)
                if not ranked:
                    print("No records found.")
                for marks, name, roll, att in ranked:
                    print(f"Roll {roll} | {name} | Marks: {marks} | Attendance: {att}%")

            elif choice == "6":
                found = False
                for roll, s in students.items():
                    if s["attendance"] < 75:
                        print(f"Roll {roll} | {s['name']} | Attendance: {s['attendance']}% (Shortage)")
                        found = True
                if not found:
                    print("No students below 75% attendance.")

            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
