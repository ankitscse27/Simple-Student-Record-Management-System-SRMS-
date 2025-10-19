1
2
import csv
import os

# Define the file name for persistent storage
STUDENT_DATABASE = 'students.csv'
# Define the fields for each student record
STUDENT_FIELDS = ['Roll No', 'Name', 'Age', 'Email', 'Address']

# --- Helper Functions for File Operations ---

def ensure_database_exists():
    """Ensures the CSV file exists and has headers if it's new."""
    if not os.path.exists(STUDENT_DATABASE) or os.path.getsize(STUDENT_DATABASE) == 0:
        with open(STUDENT_DATABASE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(STUDENT_FIELDS)

def load_all_records():
    """Loads all student records from the CSV file."""
    ensure_database_exists()
    records = []
    with open(STUDENT_DATABASE, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None) # Skip header row
        for row in reader:
            if row:
                records.append(row)
    return records

def save_all_records(records):
    """Writes all records (including header) back to the CSV file."""
    with open(STUDENT_DATABASE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(STUDENT_FIELDS)
        writer.writerows(records)

# --- Core System Functions (CRUD) ---

def add_student():
    """Adds a new student record to the CSV file."""
    print("\n--- Add New Student ---")
    student_data = []
    for field in STUDENT_FIELDS:
        value = input(f"Enter {field}: ")
        student_data.append(value)
    
    # Check for empty fields (basic validation)
    if any(not val for val in student_data):
        print("Error: All fields must be filled. Record not added.")
        return

    try:
        with open(STUDENT_DATABASE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(student_data)
        print("Student record added successfully!")
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")


def view_students():
    """Displays all student records."""
    print("\n--- View All Students ---")
    records = load_all_records()
    if not records:
        print("No student records found.")
        return
    
    # Print Header
    print("-" * 75)
    print(f"{'Roll No':<10} | {'Name':<20} | {'Age':<5} | {'Email':<20} | {'Address':<10}")
    print("-" * 75)
    
    # Print Records
    for row in records:
        print(f"{row[0]:<10} | {row[1]:<20} | {row[2]:<5} | {row[3]:<20} | {row[4]:<10}")
    print("-" * 75)


def search_student():
    """Searches for a student record by Roll No."""
    print("\n--- Search Student ---")
    roll_no = input("Enter Roll No. to search: ")
    records = load_all_records()
    
    found = False
    for row in records:
        if row[0] == roll_no:
            print("\n----- Student Found -----")
            for field, value in zip(STUDENT_FIELDS, row):
                print(f"{field}: {value}")
            found = True
            break
            
    if not found:
        print(f"Roll No. {roll_no} not found in the database.")


def update_student():
    """Updates an existing student record by Roll No."""
    print("\n--- Update Student ---")
    roll_no_to_update = input("Enter Roll No. of student to update: ")
    records = load_all_records()
    
    index_to_update = -1
    for i, row in enumerate(records):
        if row[0] == roll_no_to_update:
            index_to_update = i
            break
            
    if index_to_update == -1:
        print(f"Roll No. {roll_no_to_update} not found.")
        return

    print("Student found. Enter new details (leave blank to keep current value):")
    current_data = records[index_to_update]
    updated_data = list(current_data)
    
    for i, field in enumerate(STUDENT_FIELDS):
        # Skip updating 'Roll No' for simplicity, as it's the identifier
        if field == 'Roll No':
            print(f"{field} (Current): {current_data[i]}")
            continue

        new_value = input(f"Enter new {field} (Current: {current_data[i]}): ")
        if new_value:
            updated_data[i] = new_value
            
    records[index_to_update] = updated_data
    save_all_records(records)
    print(f"Record for Roll No. {roll_no_to_update} updated successfully!")


def delete_student():
    """Deletes a student record by Roll No."""
    print("\n--- Delete Student ---")
    roll_no_to_delete = input("Enter Roll No. to delete: ")
    records = load_all_records()
    
    initial_count = len(records)
    # Filter out the record to delete
    updated_records = [row for row in records if row[0] != roll_no_to_delete]
    
    if len(updated_records) < initial_count:
        save_all_records(updated_records)
        print(f"Record for Roll No. {roll_no_to_delete} deleted successfully!")
    else:
        print(f"Roll No. {roll_no_to_delete} not found.")

# --- Main Menu Loop ---

def main_menu():
    """Displays the main menu and handles user choice."""
    ensure_database_exists()
    
    while True:
        print("\n" + "="*30)
        print("  Student Record System  ")
        print("="*30)
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("-" * 30)
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()