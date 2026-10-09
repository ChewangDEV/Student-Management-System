from art import logo
import random
import json # gives Python the tools to read and write JSON data.
from pathlib import Path  # Helps us work with file paths.
import sys

STUDENT_DATA = {}
DATA_FILE = Path(__file__).with_name("students.json") # This tells Python to keep students.json in the same folder as

#Code	What it means
# def save_data():	Creates a function to save our data.
# DATA_FILE.open("w", ...)	Opens the file in write mode. Creates it if it doesn't exist.
# as file	Gives the opened file a temporary name we can use.
# json.dump(...)	Converts our dictionary into JSON and writes it to the file.
# indent=4	Formats the file with indentation so it's easy to read.
                                                # main.py.
def save_data():
    """Save the current student data to the JSON file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(STUDENT_DATA, file, indent=4)


def load_data():
    if not DATA_FILE.exists():
        return {}

    with DATA_FILE.open("r", encoding="utf-8") as file:
        saved_data = json.load(file)

    return {
        int(student_id): details
        for student_id, details in saved_data.items()
}

def home_screen():
    print(
        "\nWelcome to the Student System\n"
        "What do you want to do?\n"
        "1. Add a student\n"
        "2. Delete a student\n"
        "3. View all students\n"
        "4. Search student by name\n"
        "5. Update a student\n"
        "6. Exit"
    )

    user_choice = int(input("Enter your choice (1/2/3/4/5/6): "))

    if user_choice == 1:
        adding_student()
    elif user_choice == 2:
        delete_student()
    elif user_choice == 3:
        view_all_students()
    elif user_choice == 4:
        search_student()
    elif user_choice == 5:
        update_student()
    elif user_choice == 6:
        sys.exit()
    else:
        print("Invalid Number!")


def adding_student():
    """Here we ask for the age if age is correcter than we can make our id. """

    age = int(input("Enter Student Age: "))

    if age < 4 or age > 18:
        print("Student Age must be between 4 and 18")
        return

    name = input("Enter Student Name: ").title()
    class_num = int(input("Enter Student Class Standard: "))
    percentage = float(input("Enter Student Percentage: "))

    storing_data(name, age, class_num, percentage)


def storing_data(stu_name, stu_age, stu_class_num, stu_percentage):
    """We call the name and other details we register here and get id and store data"""
    student_id = student_id_generator()

    details = {
        "Name": stu_name,
        "Age": stu_age,
        "Class": stu_class_num,
        "Percentage": stu_percentage,
    }

    STUDENT_DATA[student_id] = details
    save_data()

    print(f"Student has been registered. Your ID is {student_id}")
    print("Remember your student ID!")


def student_id_generator():
    """This is id generator"""
    random_id = random.randint(100000, 999999)

    while random_id in STUDENT_DATA:
        random_id = random.randint(100000, 999999)

    return random_id


def get_student_id():
    """We check if student id exists or not"""
    while True:
        student_id = int(input("Enter the ID number: "))

        if student_id in STUDENT_DATA:
            return student_id

        print("Student with ID number does not exist!")


def display_student(student_id):
    """We then call student details here """
    student = STUDENT_DATA[student_id]

    print(
        f"\nID: {student_id}\n"
        f"- Name: {student['Name']}\n"
        f"- Age: {student['Age']}\n"
        f"- Class: {student['Class']}\n"
        f"- Percentage: {student['Percentage']}%"
    )

    print("\n" * 2)


def view_all_students():
    """If dictionary is empty it will not show"""
    if not STUDENT_DATA:
        print("Student Data is empty!")
        return

    for student_id in STUDENT_DATA:
        display_student(student_id)


def delete_student():
    """Student id is called and delete that """
    student_id = get_student_id()

    del STUDENT_DATA[student_id]

    save_data()

    print(f"Student with ID {student_id} has been deleted.")



def search_student():
    """Search students by name and display all matching records."""

    if not STUDENT_DATA:
        print("Student Data is empty!")
        return

    search_name = input("Enter student name to search: ").strip().casefold()

    if not search_name:
        print("Please enter a student name!")
        return

    found = False

    # Loop through every student ID and their details.
    for student_id, student in STUDENT_DATA.items():

        # Search without worrying about uppercase or lowercase.
        if search_name in student["Name"].casefold():

            # Display the ID and all details of the matching student.
            display_student(student_id)
            found = True

    if not found:
        print(f"No student found matching '{search_name}'.")



def update_student():
    """To update the particular student detail"""
    student_id = get_student_id()

    update = int(
        input(
            "\nWhat would you like to update?\n"
            "1. Name\n"
            "2. Class\n"
            "3. Percentage\n"
            "4. Age\n"
            "Ans: "
        )
    )

    if update == 1:
        updated_name = input("Enter new name: ").title()
        STUDENT_DATA[student_id]["Name"] = updated_name

    elif update == 2:
        updated_class = int(input("Enter new class: "))
        STUDENT_DATA[student_id]["Class"] = updated_class

    elif update == 3:
        updated_percentage = float(input("Enter new percentage: "))
        STUDENT_DATA[student_id]["Percentage"] = updated_percentage

    elif update == 4:
        updated_age = int(input("Enter new age: "))

        if updated_age < 4 or updated_age > 18:
            print("Student Age must be between 4 and 18")
            return

        STUDENT_DATA[student_id]["Age"] = updated_age

    else:
        print("Wrong input!")
        return

    save_data()
    print("Student details updated successfully!")


def main():
    global STUDENT_DATA

    STUDENT_DATA = load_data()

    print(logo)
    while True:
        home_screen()


if __name__ == "__main__":
    main()
