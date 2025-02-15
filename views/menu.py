from controllers.student import StudentController

def main_menu():
    manager = StudentController()
    
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            if age.isdigit():
                manager.add_student(name, int(age))
            else:
                print("Invalid age. Please enter a number.")
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            index = input("Enter student index to edit: ")
            if index.isdigit():
                name = input("Enter new name (leave blank to keep current): ")
                age = input("Enter new age (leave blank to keep current): ")
                manager.edit_student(int(index) - 1, name if name else None, int(age) if age.isdigit() else None)
            else:
                print("Invalid index. Please enter a number.")
        elif choice == "4":
            index = input("Enter student index to delete: ")
            if index.isdigit():
                manager.delete_student(int(index) - 1)
            else:
                print("Invalid index. Please enter a number.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
