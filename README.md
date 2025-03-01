# University Management System

This is a Python-based University Management System that allows users to manage universities, faculties, departments, years, students, and their associated details. The system is designed to be interactive, with a command-line interface for user input.

## Features

- **University Management**: Create and manage universities with details such as name, address, email, phone number, and director.
- **Faculty Management**: Add, remove, and list faculties within a university.
- **Department Management**: Add and remove departments within a faculty.
- **Year Management**: Add years to a department and manage students within those years.
- **Student Management**: Add students to a year, set their details, and manage their notes.
- **Note Management**: Add notes for students in specific modules.
- **Director and Chief Management**: Set directors for universities, faculties, and departments, and calculate student marks.

## Classes Overview

### 1. `University`
- **Attributes**: 
  - `name`, `address`, `email`, `phone_number`, `director`, `faculties`, `universities`
- **Methods**:
  - `create_university()`: Creates a new university with user-provided details.
  - `add_faculty()`: Adds a new faculty to the university.
  - `remove_faculty()`: Removes a faculty from the university.
  - `set_director()`: Sets the director of the university.
  - `university_list()`: Lists all universities.
  - `faculties_list()`: Lists all faculties in the university.
  - `add_faculty_department()`: Adds a department to a faculty.
  - `remove_department()`: Removes a department from a faculty.

### 2. `Faculty`
- **Attributes**: 
  - `name`, `departments`, `director`
- **Methods**:
  - `add_department()`: Adds a new department to the faculty.
  - `remove_department()`: Removes a department from the faculty.

### 3. `Department`
- **Attributes**: 
  - `name`, `years`, `chief`
- **Methods**:
  - `add_year()`: Adds a new year to the department.
  - `set_chief()`: Sets the chief of the department.

### 4. `Year`
- **Attributes**: 
  - `name`, `students`, `modules`, `marks`
- **Methods**:
  - `add_student()`: Adds a new student to the year.
  - `students_list()`: Lists all students in the year.
  - `modules_list()`: Lists all modules in the year.
  - `marks_list()`: Lists all marks in the year.
  - `remove_student()`: Removes a student from the year.

### 5. `Student`
- **Attributes**: 
  - `name`, `address`, `phone_number`, `email`, `notes`
- **Methods**:
  - `set_details()`: Sets the details of the student.
  - `add_note()`: Adds a note for the student in a specific module.

### 6. `Module`
- **Attributes**: 
  - `name`, `coef`
- **Methods**:
  - `set_coef()`: Sets the coefficient for the module.

### 7. `Note`
- **Attributes**: 
  - `value`, `module`

### 8. `UniversityDirector`
- **Attributes**: 
  - `name`, `email`, `phone_number`
- **Methods**:
  - `set_faculty_director()`: Sets the director of a faculty.
  - `set_department_chief()`: Sets the chief of a department.

### 9. `FacultyDirector`
- **Attributes**: 
  - `name`, `email`, `phone_number`
- **Methods**:
  - `set_department_chief()`: Sets the chief of a department.

### 10. `DepartmentChief`
- **Attributes**: 
  - `name`, `email`, `phone_number`
- **Methods**:
  - `calculate_marks()`: Calculates the marks for students in a year.

## Usage

1. **Run the Script**: Execute the script to start the University Management System.
2. **Main Menu**: The system will display a menu with options to manage universities, faculties, departments, years, students, and more.
3. **Follow Prompts**: Follow the on-screen prompts to perform various actions such as creating a university, adding a faculty, setting a director, etc.
