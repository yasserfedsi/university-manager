class University:
    def __init__(self):
        self.name = None
        self.address = None
        self.email = None
        self.phone_number = None
        self.director = None
        self.faculties = []
        self.universities = []

    def create_university(self):
        self.name = input("Enter university name: ")
        self.address = input("Enter university address: ")
        self.email = input("Enter university email: ")
        self.phone_number = input("Enter university phone number: ")
        self.director = input("Enter university director: ")

        university = {
            "name": self.name,
            "address": self.address,
            "email": self.email,
            "phone_number": self.phone_number,
            "director": self.director,
        }

        self.universities.append(university)
        print(f"University with name {self.name} created successfully.")

    def add_faculty(self):
        faculty_name = input("Enter faculty name: ")
        if faculty_name:
            faculty = Faculty(faculty_name)
            self.faculties.append(faculty)
            print(f"Faculty '{faculty_name}' added successfully.")
        else:
            print("Invalid faculty name.")

    def remove_faculty(self):
        faculty_name = input("Enter faculty name: ")
        for faculty in self.faculties:
            if faculty.name == faculty_name:
                self.faculties.remove(faculty)
                print(f"Faculty '{faculty_name}' removed successfully.")
                return
        print(f"Faculty '{faculty_name}' not found.")

    def set_director(self):
        self.director = input("Enter new university director: ")
        print(f"Director set to '{self.director}'.")

    def university_list(self):
        if self.universities:
            for university in self.universities:
                print(f"{university['name']}: {university['address']}")
        else:
            print("No university found.")

    def faculties_list(self):
        if self.faculties:
            print("Faculties:")
            for faculty in self.faculties:
                print(f"- {faculty.name}")
        else:
            print("No faculty found.")

    def add_faculty_department(self):
        faculty_name = input("Enter faculty name: ")
        department_name = input("Enter department name: ")

        for faculty in self.faculties:
            if faculty.name == faculty_name:
                faculty.add_department(department_name)
                return

        print(f"Faculty '{faculty_name}' not found. Please add the faculty first.")

    def remove_department(self):
        faculty_name = input("Enter faculty name: ")
        department_name = input("Enter department name: ")

        for faculty in self.faculties:
            if faculty.name == faculty_name:
                faculty.remove_department(department_name)
                return
        print(f"Faculty '{faculty_name}' not found.")


class Faculty:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.director = None

    def add_department(self, department_name):
        if department_name:
            department = Department(department_name)
            self.departments.append(department)
            print(f"Department '{department_name}' added successfully.")
        else:
            print("Invalid department name.")

    def remove_department(self, department_name):
        for department in self.departments:
            if department.name == department_name:
                self.departments.remove(department)
                print(f"Department '{department_name}' removed successfully.")
                return
        print(f"Department '{department_name}' not found.")


class Department:
    def __init__(self, name):
        self.name = name
        self.years = []
        self.chief = None

    def add_year(self):
        year_name = input("Enter year name: ")
        if year_name:
            year = Year(year_name)
            self.years.append(year)
            print(f"Year '{year_name}' added successfully.")
        else:
            print("Invalid year name.")

    def set_chief(self):
        chief_name = input("Enter chief name: ")
        if chief_name:
            self.chief = chief_name
            print(f"Chief set to '{chief_name}'.")
        else:
            print("Invalid chief name.")


class Year:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.modules = []
        self.marks = []

    def add_student(self):
        student_name = input("Enter student name: ")
        if student_name:
            student = Student(student_name)
            self.students.append(student)
            print(f"Student '{student_name}' added successfully.")
        else:
            print("Invalid student name.")

    def students_list(self):
        if self.students:
            print(f"Students in year '{self.name}':")
            for student in self.students:
                print(f"- {student.name}")
        else:
            print("No students found.")

    def modules_list(self):
        if self.modules:
            print(f"Modules in year '{self.name}':")
            for module in self.modules:
                print(f"- {module.name}")
        else:
            print("No modules found.")

    def marks_list(self):
        if self.marks:
            print(f"Marks in year '{self.name}':")
            for mark in self.marks:
                print(f"- {mark}")
        else:
            print("No marks found.")

    def remove_student(self):
        student_name = input("Enter student name: ")
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                print(f"Student '{student_name}' removed successfully.")
                return
        print(f"Student '{student_name}' not found.")


class Student:
    def __init__(self, name):
        self.name = name
        self.address = None
        self.phone_number = None
        self.email = None
        self.notes = []

    def set_details(self):
        self.address = input("Enter student address: ")
        self.phone_number = input("Enter student phone number: ")
        self.email = input("Enter student email: ")
        print(f"Details set for student '{self.name}'.")

    def add_note(self):
        module_name = input("Enter module name: ")
        value = float(input("Enter note value: "))
        module = Module(module_name)
        note = Note(value, module)
        self.notes.append(note)
        print(f"Note added for module '{module_name}'.")


class Module:
    def __init__(self, name):
        self.name = name
        self.coef = None

    def set_coef(self):
        self.coef = float(input("Enter module coefficient: "))
        print(f"Coefficient set for module '{self.name}'.")


class Note:
    def __init__(self, value, module):
        self.value = value
        self.module = module


class UniversityDirector:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def set_faculty_director(self, faculty, director):
        faculty.director = director
        print(f"Faculty director set to '{director.name}'.")

    def set_department_chief(self, department, chief):
        department.chief = chief
        print(f"Department chief set to '{chief.name}'.")


class FacultyDirector:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def set_department_chief(self, department, chief):
        department.chief = chief
        print(f"Department chief set to '{chief.name}'.")


class DepartmentChief:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def calculate_marks(self, year):
        for student in year.students:
            total = 0
            for note in student.notes:
                total += note.value * note.module.coef
            average = total / len(student.notes)
            year.marks.append((student.name, average))
        print(f"Marks calculated for year '{year.name}'.")


if __name__ == "__main__":
    uni = University()

    while True:
        print("====== Welcome to University Management ======")
        print("\n1. Create University")
        print("2. Add Faculty")
        print("3. Remove Faculty")
        print("4. Set Director")
        print("5. University List")
        print("6. Faculty List")
        print("7. Add Department")
        print("8. Remove Department")
        print("9. Add Year")
        print("10. Set Department Chief")
        print("11. Add Student")
        print("12. Set Student Details")
        print("13. Add Note")
        print("14. Calculate Marks")
        print("15. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            uni.create_university()
        elif choice == "2":
            uni.add_faculty()
        elif choice == "3":
            uni.remove_faculty()
        elif choice == "4":
            uni.set_director()
        elif choice == "5":
            uni.university_list()
        elif choice == "6":
            uni.faculties_list()
        elif choice == "7":
            uni.add_faculty_department()
        elif choice == "8":
            uni.remove_department()
        elif choice == "9":
            faculty_name = input("Enter faculty name: ")
            department_name = input("Enter department name: ")
            for faculty in uni.faculties:
                if faculty.name == faculty_name:
                    for department in faculty.departments:
                        if department.name == department_name:
                            department.add_year()
            print(f"Faculty '{faculty_name}' or department '{department_name}' not found.")
        elif choice == "10":
            faculty_name = input("Enter faculty name: ")
            department_name = input("Enter department name: ")
            chief_name = input("Enter chief name: ")
            chief_email = input("Enter chief email: ")
            chief_phone = input("Enter chief phone number: ")
            chief = DepartmentChief(chief_name, chief_email, chief_phone)
            for faculty in uni.faculties:
                if faculty.name == faculty_name:
                    for department in faculty.departments:
                        if department.name == department_name:
                            department.set_chief(chief)
            print(f"Faculty '{faculty_name}' or department '{department_name}' not found.")
        elif choice == "11":
            faculty_name = input("Enter faculty name: ")
            department_name = input("Enter department name: ")
            year_name = input("Enter year name: ")
            for faculty in uni.faculties:
                if faculty.name == faculty_name:
                    for department in faculty.departments:
                        if department.name == department_name:
                            for year in department.years:
                                if year.name == year_name:
                                    year.add_student()
            print(f"Faculty '{faculty_name}', department '{department_name}', or year '{year_name}' not found.")
        elif choice == "12":
            faculty_name = input("Enter faculty name: ")
            department_name = input("Enter department name: ")
            year_name = input("Enter year name: ")
            student_name = input("Enter student name: ")
            for faculty in uni.faculties:
                if faculty.name == faculty_name:
                    for department in faculty.departments:
                        if department.name == department_name:
                            for year in department.years:
                                if year.name == year_name:
                                    for student in year.students:
                                        if student.name == student_name:
                                            student.set_details()
            print(f"Student '{student_name}' not found.")
        elif choice == "13":
            faculty_name = input("Enter faculty name: ")
            department_name = input("Enter department name: ")
            year_name = input("Enter year name: ")
            student_name = input("Enter student name: ")
            for faculty in uni.faculties:
                if faculty.name == faculty_name:
                    for department in faculty.departments:
                        if department.name == department_name:
                            for year in department.years:
                                if year.name == year_name:
                                    for student in year.students:
                                        if student.name == student_name:
                                            student.add_note()
            print(f"Student '{student_name}' not found.")
        elif choice == "14":
            faculty_name = input("Enter faculty name: ")
            department_name = input("Enter department name: ")
            year_name = input("Enter year name: ")
            for faculty in uni.faculties:
                if faculty.name == faculty_name:
                    for department in faculty.departments:
                        if department.name == department_name:
                            for year in department.years:
                                if year.name == year_name:
                                    if department.chief:
                                        department.chief.calculate_marks(year)
                                    else:
                                        print("No chief set for this department.")
            print(f"Faculty '{faculty_name}', department '{department_name}', or year '{year_name}' not found.")
        elif choice == "15":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 15.")
