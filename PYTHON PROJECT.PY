Student Management System


students = {}

def add_student():
    roll = input("Enter Roll Number: ")

    students[roll] = {
        "Name": input("Enter Name: "),
        "Age": input("Enter Age: "),
        "Gender": input("Enter Gender: "),
        "Course": input("Enter Course: "),
        "Course Code":input("Enter Course Code:"), 
        "Email": input("Enter Email: "),
        "Phone": input("Enter Phone Number: "),
        "Address": input("Enter Address: "),
        "Marks": input("Enter Marks: "),
        "class": input("Enter class: "),
        "BirthDate": input("Enter Birth Date (YYYY-MM-DD): ")
    }

    print("Student Added Successfully!")

def display_students():
    if not students:
        print("No Records Found!")
        return

    for roll, data in students.items():
        print("\n----------------------------")
        print("Roll No:", roll)
        for key, value in data.items():
            print(f"{key}: {value}")

def search_student():
    roll = input("Enter Roll Number to Search: ")

    if roll in students:
        print("\nStudent Found:")
        for key, value in students[roll].items():
            print(f"{key}: {value}")
    else:
        print("Student Not Found!")

def update_student():
    roll = input("Enter Roll Number to Update: ")

    if roll in students:
        students[roll]["Name"] = input("Enter New Name: ")
        students[roll]["Age"] = input("Enter New Age: ")
        students[roll]["Course"] = input("Enter New Course: ")
        print("Student Updated Successfully!")
    else:
        print("Student Not Found!")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")

def count_students():
    print("Total Students:", len(students))

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Count Students")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        count_students()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
