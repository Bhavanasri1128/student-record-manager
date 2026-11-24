import os

FILE_NAME = "students.txt"

def load_records(filename=FILE_NAME):
    students = {}
    if not os.path.exists(filename):
        return students

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                roll_no, name, marks, attendance = line.split(",")
                students[roll_no] = {
                    "name": name,
                    "marks": int(marks),
                    "attendance": float(attendance)
                }
    return students

def save_records(students, filename=FILE_NAME):
    with open(filename, "w") as file:
        for roll_no, data in students.items():
            file.write(f"{roll_no},{data['name']},{data['marks']},{data['attendance']}\n")

def add_student(students, roll_no, name, marks, attendance):
    if roll_no in students:
        raise ValueError("Roll number already exists.")
    if not (0 <= marks <= 100):
        raise ValueError("Marks must be between 0 and 100.")
    if not (0 <= attendance <= 100):
        raise ValueError("Attendance percentage must be between 0 and 100.")

    students[roll_no] = {
        "name": name,
        "marks": marks,
        "attendance": attendance
    }
    save_records(students)

def update_student(students, roll_no, new_marks, new_attendance):
    if roll_no not in students:
        raise KeyError("Student not found.")
    students[roll_no]["marks"] = new_marks
    students[roll_no]["attendance"] = new_attendance
    save_records(students)

def delete_student(students, roll_no):
    if roll_no not in students:
        raise KeyError("Student not found.")
    del students[roll_no]
    save_records(students)

def rank_by_marks(students):
    marks_list = []
    for roll_no, data in students.items():
        marks_list.append((data["marks"], data["name"], roll_no, data["attendance"]))
    marks_list.sort(reverse=True)
    return marks_list
