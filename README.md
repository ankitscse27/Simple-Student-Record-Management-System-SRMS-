# Simple-Student-Record-Management-System-SRMS-
A basic, command-line CRUD (Create, Read, Update, Delete) application written in Python that manages student data. It uses the standard csv module for persistent storage, saving all records to a file named students.csv.

Features
The system provides a text-based menu interface with the following functionalities:

Add New Student: Prompts the user for student details (Roll No, Name, Age, Email, Address) and appends the new record to the CSV file.

View All Students: Reads and displays all stored student records in a formatted table.

Search Student: Searches for a student by their Roll No and displays their complete details if found.

Update Student: Finds a student by Roll No and allows the user to selectively update fields (Name, Age, Email, Address).

Delete Student: Removes a student record from the database based on their Roll No.

Persistent Storage: Automatically creates and maintains the students.csv file to ensure data is saved between sessions.

🛠️ Requirements & Setup
Requirements
Python 3.x

No external libraries are required; the code uses only csv and os, which are part of Python's standard library.

How to Run
Save the provided code into a file named srms.py (or any other name ending in .py).

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Execute the script using the Python interpreter:

Bash

python srms.py
The main menu will appear, and you can start managing student records. A file named students.csv will be automatically created in the same directory upon first run.

💡 Code Structure Overview
The code is logically divided into three main sections:

1. File Handling Helpers
Functions responsible for reading and writing data to the students.csv file, ensuring data persistence and file integrity.

ensure_database_exists(): Checks if the CSV file exists and writes the header row if it doesn't.

load_all_records(): Reads all student data from the file.

save_all_records(records): Overwrites the file with the current list of records.

2. Core System Functions (CRUD)
The main logic for interacting with the student data. Each function corresponds to a menu option.

add_student()

view_students()

search_student()

#Creator- ankitscse27

update_student()

delete_student()

3. Main Menu
The entry point of the application, which displays the menu and handles user input to call the core system functions.

main_menu(): The primary loop that runs until the user chooses to exit.
