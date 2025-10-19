# Simple Student Record Management System (SRMS)

**Project Name:** Simple Student Record Management System (SRMS)

**Creator:** ankitscse27

---

### 🌟 Project Overview

The **Simple Student Record Management System (SRMS)** is a command-line utility built in **Python** for efficiently managing student data. It implements the essential **CRUD** (Create, Read, Update, Delete) operations, making it a foundational example of database interaction using flat files. The system achieves **data persistence** by storing all records in a structured **CSV file** named `students.csv`, relying only on Python's powerful standard library modules.

---

### ✨ Key Features and Functionality

The application presents a user-friendly, text-based menu offering robust record management capabilities:

| Feature | Description | Technical Implementation |
| :--- | :--- | :--- |
| **Add New Student** | Prompts for five key fields: **Roll No**, **Name**, **Age**, **Email**, and **Address**, then securely appends the new record to the `students.csv` file. | Uses the `csv.writer` in append mode (`'a'`). |
| **View All Students** | Retrieves the entire dataset from the CSV file and displays it in a clean, formatted, columnar table. | Uses the `csv.reader` and string formatting for alignment. |
| **Search Student** | Allows quick retrieval of a single student's complete details by matching their **Roll No**. | Iterates through records, comparing the input identifier. |
| **Update Student** | Locates a record by **Roll No** and offers the user the ability to selectively modify any field (excluding Roll No) while keeping existing data unchanged if left blank. | Loads all records, modifies the target list element, then rewrites the entire file. |
| **Delete Student** | Removes a record from the database entirely based on the provided **Roll No**. | Filters the list of records to exclude the target, then rewrites the entire file. |
| **Persistent Storage** | Automatically handles file creation (`students.csv`) and ensures the header row is present upon the first run, guaranteeing data integrity across sessions. | Utilizes the `os` module for file existence and size checks. |

---

### 💻 Technical Requirements and Setup

#### Requirements

This system is designed for maximum accessibility and requires minimal dependencies:

* **Platform:** Python **3.x**
* **Libraries:** No external (PyPI) packages are necessary. The system relies solely on the built-in standard libraries:
    * `csv`: For reading and writing structured data.
    * `os`: For file path and integrity checks.

#### Execution

Follow these steps to deploy and run the system:

1.  **Save:** Save the complete Python script as `srms.py`.
2.  **Terminal Access:** Open your command line interface (Terminal, Command Prompt, PowerShell).
3.  **Navigate:** Change the directory to the location where you saved `srms.py`.
4.  **Run:** Execute the application using the Python interpreter:

    ```bash
    python srms.py
    ```
5.  **Interaction:** The system's main menu will launch, ready for record management. The `students.csv` file will be automatically initialized in the current directory if it doesn't already exist.

---

### 🧠 Code Architecture

The Python source code is structured into three clear, modular sections to enhance readability, maintenance, and logical flow:

#### 1. File Handling Helpers (Data Layer)
These functions abstract the complexities of file I/O, ensuring data is managed safely and persistently.

* `ensure_database_exists()`
* `load_all_records()`
* `save_all_records(records)`

#### 2. Core System Functions (Business Logic/CRUD)
These are the main operational functions that perform the database-like actions on the loaded data.

* `add_student()`
* `view_students()`
* `search_student()`
* `update_student()`
* `delete_student()`

#### 3. Main Menu Loop (Presentation Layer)
This is the application's entry point, which provides the user interface and coordinates calls to the Core System Functions based on user selection.

* `main_menu()`: The continuous loop that drives the entire application.
