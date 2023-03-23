import datetime


class Student:
    def __init__(self, name, attendance=[]):
        self.name = name
        self.attendance = attendance

    def mark_attendance(self, date):
        self.attendance.append(date)

    def check_attendance(self, date):
        return date in self.attendance


def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def mark_attendance(student, date=None):
    if not date:
        date = get_current_date()
    student.mark_attendance(date)
    print(f"Attendance marked for {student.name} on {date}")


def check_attendance(student, date=None):
    if not date:
        date = get_current_date()
    if student.check_attendance(date):
        print(f"{student.name} was present on {date}")
    else:
        print(f"{student.name} was absent on {date}")


students = {}

while True:
    user_input = input("Enter 'mark' to mark attendance, 'check' to check attendance, 'quit' to exit: ")
    if user_input.lower() == "quit":
        break
    elif user_input.lower() == "mark":
        name = input("Enter the student's name: ")
        if name in students:
            student = students[name]
        else:
            student = Student(name)
            students[name] = student
        mark_attendance(student)
    elif user_input.lower() == "check":
        name = input("Enter the student's name: ")
        try:
            student = students[name]
        except KeyError:
            print(f"No record found for student {name}.")
        else:
            check_attendance(student)
    else:
        print("Invalid input.")
