# 🎓 Student Management System

A simple **Python-based Student Management System** built to practice Python fundamentals, functions, dictionaries, loops, conditional statements, and basic code refactoring.

The project allows users to add, view, search, update, and delete student records through a command-line interface.

## ✨ Features

- ➕ Add a new student
- 👀 View all students
- 🔍 Search for a student using their ID
- ✏️ Update student information
- 🗑️ Delete a student
- 🆔 Automatically generate a unique 6-digit student ID
- ✅ Validate student age between 4 and 18
- ⚠️ Handle invalid student IDs
- 📭 Handle empty student data
- 🎨 Display a custom ASCII-art logo

## 🛠️ Technologies Used

- **Python 3**
- `random` module
- `art` module
- Dictionaries
- Functions
- Loops
- Conditional statements
- User input
- Basic input validation

## 📂 Project Structure

```text
Student Management System/
│
├── main.py
├── art.py
└── README.md
```

### `main.py`

Contains the main application logic, including:

- Student registration
- Student ID generation
- Student search
- Student deletion
- Student updating
- Student display
- Menu system

### `art.py`

Contains the ASCII-art logo displayed when the application starts.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-management-system.git
```

### 2. Open the project

```bash
cd student-management-system
```

### 3. Install the required package

The project uses the `art` module.

```bash
pip install art
```

### 4. Run the program

```bash
python main.py
```

## 📋 How It Works

When the program starts, you are presented with a menu:

```text
Welcome to the Student System

What do you want to do?
1. Add a student
2. Delete a student
3. View all students
4. Search for a student
5. Update a student
6. Exit
```

### Add Student

The program asks for:

- Student name
- Age
- Class
- Percentage

A unique 6-digit student ID is automatically generated and assigned to the student.

### View Students

Displays all registered students and their:

- ID
- Name
- Age
- Class
- Percentage

If there are no students, the program displays an appropriate message.

### Search Student

Enter a student ID to display the student's details.

If the ID does not exist, the program asks for another ID.

### Update Student

You can update:

- Name
- Class
- Percentage
- Age

Age validation is also performed when updating the student's age.

### Delete Student

Enter a student ID and the corresponding student record is removed from the dictionary.

## 🧠 What I Practiced

This project was created as a practical Python learning project. Through it, I practiced:

- Variables and data types
- `if`, `elif`, and `else`
- `while` and `for` loops
- Functions
- Function parameters and return values
- Dictionaries
- Nested dictionaries
- Dictionary keys and values
- The `random` module
- Input validation
- CRUD operations
- Code organization
- Refactoring
- Avoiding repeated code
- Basic documentation with docstrings

## 🔄 CRUD Operations

This project implements the four basic CRUD operations:

| Operation  | Feature                |
| ---------- | ---------------------- |
| **Create** | Add a student          |
| **Read**   | View / Search students |
| **Update** | Update student details |
| **Delete** | Delete a student       |

## 📌 Future Improvements

Possible improvements for future versions:

- [✔️] Add persistent data storage using JSON
- [ ] Add better exception handling for invalid input
- [ ] Add a confirmation before deleting a student
- [ ] Add more detailed validation for percentage and class
- [ ] Convert the project to Python OOP
- [ ] Store students using `Student` objects
- [ ] Add a graphical user interface
- [ ] Connect the project to a database

## 🎯 Purpose

This project was built as part of my journey learning **Python and full-stack development**.

The goal was not only to make the program work, but also to practice breaking a larger problem into smaller functions and then refactoring repeated logic into reusable functions.

## 👨‍💻 Author

**Chewang Tamang**

Built with Python 🐍
