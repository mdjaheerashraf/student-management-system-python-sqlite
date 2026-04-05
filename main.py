import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")
conn.commit()


# ➕ Add Student
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()
    print("✅ Student added successfully!")


# 📋 View Students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n--- Student List ---")

    if not students:
        print("⚠️ No students found")
        return

    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Course: {student[3]}")

# ✏️ Update Student
def update_student():
    student_id = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")

    cursor.execute("""
    UPDATE students
    SET name = ?, age = ?, course = ?
    WHERE id = ?
    """, (name, age, course, student_id))

    conn.commit()
    print("✏️ Student updated successfully!")


# ❌ Delete Student
def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

    print("❌ Student deleted successfully!")


# 📌 Menu System
def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")


# Run program
menu()

# Close connection
conn.close()