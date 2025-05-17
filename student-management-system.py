import json
def add_students(students):
    student_id = int(input("Enter students Id"))
    name = input("Enter student name")
    age = input("Enter student age")
    major = input("Enter major")
    students[student_id] = {
        "name": name,
        "age": age,
        "major": major
    }
    print("Student added successfully!\n")
         
def view_students(students):
    if not students:
        print("No student found")
        return
    for student_id, details in students.items():
        print(f"student id {student_id}")
        print(f"student name {details['name']}")
        print(f"student age {details['age']}")
        print(f"student major {details['major']}")
        
    
def save_to_file(students, filename):
        with open(filename, 'w') as file:
            json.dump(students, file,indent = 4)
        print(f"Data saved to {filename}\n")
    
  
  
  
def load_from_file(filename):
    try:
        with open(filename , 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}    
                
                
def main():
    filename = "students.json"
    students = load_from_file(filename)

    while True:
        print("\n1. Add Student\n2. View Students\n3. Save to File\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_students(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            save_to_file(students, filename)
        elif choice == '4':
            save_to_file(students, filename)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")                
if __name__ == "__main__":
    main()               
    
    
                    