
KEY_ID = "id"
KEY_NAME = "name"

def record_student(roster, student_id, student_name):
    if student_id in roster:
        print(f"Student with ID '{student_id}' already exists.")
        return
    
    if student_id == "":
        print("Student ID cannot be empty.")
        return
    
    if student_name == "":
        print("Student name cannot be empty.")
        return
    
    roster[student_id] = {
        KEY_ID: student_id,
        KEY_NAME: student_name
    }
    print(f"Student '{student_name}' added successfully.")

def update_student(roster, student_id, new_name):
    if student_id not in roster:
        print(f"Student with ID '{student_id}' not found.")
        return
    
    roster.update({
        student_id: {
            KEY_ID: student_id,
            KEY_NAME: new_name
        }
    })
    print(f"Student '{student_id}' updated successfully.")

def delete_student(roster, student_id):
    if student_id in roster:
        del roster[student_id]
        print(f"Student '{student_id}' deleted successfully.")
    else:
        print(f"Student with ID '{student_id}' not found.")
