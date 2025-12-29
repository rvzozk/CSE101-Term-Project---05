from storage import load_state, save_state

from courses import record_course, update_course, delete_course
from courses import add_assessment, remove_assessment, update_assessment
from courses import add_student_to_course, remove_student_from_course
from courses import KEY_CODE, KEY_NAME, KEY_INSTRUCTOR, KEY_ASSESSMENTS

from roster import record_student, update_student, delete_student 
from roster import KEY_ID, KEY_NAME

from grades import record_grade, update_grade, delete_grade
from grades import calculate_student_average, calculate_course_average

from analytics import grade_distribution, top_students, student_progress_report


# COURSES MENU

def view_courses_menu(courses):
    if not courses:
        print("\nNo courses available.")
        return
    
    print(f"\n{"Code":<10} {"Name":<30} {"Instructor":<20}")
    for course in courses.values():
        print(f"{course[KEY_CODE]:<10} {course[KEY_NAME]:<30} {course[KEY_INSTRUCTOR]:<20}")

def record_course_menu(courses):
    course_code = input("\nEnter course code: ").strip()
    course_name = input("Enter course name: ").strip()
    instructor = input("Enter instructor name: ").strip()
    record_course(courses, course_code, course_name, instructor)

def update_course_menu(courses):
    course_code = input("\nEnter course code to update: ").strip()
    new_name = input("Enter new course name (leave blank to keep current): ").strip()
    new_instructor = input("Enter new instructor name (leave blank to keep current): ").strip()

    if course_code not in courses:
        print(f"Course with code '{course_code}' not found.")
        return

    update_course(courses, course_code, new_name, new_instructor)

def delete_course_menu(courses):
    course_code = input("\nEnter course code to remove: ").strip()
    delete_course(courses, course_code)

def assessments_menu(courses):
    while True:
        print("\n--- Assessments Menu ---")
        print("1. View Assessments")
        print("2. Add Assessment")
        print("3. Remove Assessment")
        print("4. Update Assessment")
        print("5. Back to Courses Menu")
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            course_code = input("\nEnter course code: ")
            if course_code not in courses:
                print(f"Course with code '{course_code}' not found.")
                continue
            assessments = courses[course_code][KEY_ASSESSMENTS]
            if not assessments:
                print(f"\nNo assessments available for course '{course_code}'.")
                continue
            print(f"\nAssessments for Course '{course_code}':")
            print(f"{'ID':<15} {'Name':<30} {'Weight':<10}")
            for assessment in assessments.values():
                print(f"{assessment['id']:<15} {assessment['name']:<30} {assessment['weight']:<10}")
        elif choice == "2":
            course_code = input("\nEnter course code: ")
            assessment_id = input("Enter assessment ID: ")
            assessment_name = input("Enter assessment name: ")
            weight = float(input("Enter assessment weight (as a percentage): "))
            add_assessment(courses, course_code, assessment_id, assessment_name, weight)
        elif choice == "3":
            course_code = input("\nEnter course code: ")
            assessment_id = input("Enter assessment ID to remove: ")
            remove_assessment(courses, course_code, assessment_id)
        elif choice == "4":
            course_code = input("\nEnter course code: ")
            assessment_id = input("Enter assessment ID to update: ")
            new_name = input("Enter new assessment name (leave blank to keep current): ")
            new_weight_input = input("Enter new assessment weight (leave blank to keep current): ")
            new_weight = float(new_weight_input) if new_weight_input else None
            update_assessment(courses, course_code, assessment_id, new_name, new_weight)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def courses_menu(courses):
    while True:
        print("\n--- Courses Menu ---")
        print("1. View Courses")
        print("2. Add Course")
        print("3. Update Course")
        print("4. Remove Course")
        print("5. Manage Assessments")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            view_courses_menu(courses)
        elif choice == "2":
            record_course_menu(courses)
        elif choice == "3":
            update_course_menu(courses)
        elif choice == "4":
            delete_course_menu(courses)
        elif choice == "5":
            assessments_menu(courses)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


# STUDENTS MENU

def view_students(students):
    if not students:
        print("\nNo students available.")
        return
    
    print(f"\n{'ID':<10} {'Name':<30}")
    for student in students.values():
        print(f"{student[KEY_ID]:<10} {student[KEY_NAME]:<30}")

def add_student(students):
    student_id = input("\nEnter student ID: ").strip()
    student_name = input("Enter student name: ").strip()
    record_student(students, student_id, student_name)

def update_student(students):
    student_id = input("\nEnter student ID to update: ").strip()
    new_name = input("Enter new student name (leave blank to keep current): ").strip()
    update_student(students, student_id, new_name or students[student_id]['name'])

def delete_student(students):
    student_id = input("\nEnter student ID to delete: ").strip()
    delete_student(students, student_id)

def students_menu(students):
    while True:
        print("\n--- Students Menu ---")
        print("1. View Students")
        print("2. Add Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            view_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


# ENROLLMENT MENU

def add_student_to_course_menu(courses, students):
    course_code = input("\nEnter course code to add student to: ").strip()
    student_id = input("Enter student ID to add: ").strip()
    add_student_to_course(courses, students, course_code, student_id)

def remove_student_from_course_menu(courses, students):
    course_code = input("\nEnter course code to remove student from: ").strip()
    student_id = input("Enter student ID to remove: ").strip()
    remove_student_from_course(courses, course_code, student_id)

def enrollment_menu(courses, students):
    while True:
        print("\n--- Enrollment Menu ---")
        print("1. Add Student to Course")
        print("2. Remove Student from Course")
        print("3. Back to Main Menu")

        choice = input("Enter your choice (1-3): ").strip()
        if choice == "1":
            add_student_to_course_menu(courses, students)
        elif choice == "2":
            remove_student_from_course_menu(courses, students)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


# GRADES MENU

def view_grades_menu(gradebook, courses):
    course_id = input("\nEnter course ID to view grades: ").strip()
    if course_id not in gradebook:
        print(f"Course with ID '{course_id}' not found or has no grades.")
        return
    
    print(f"\nGrades for Course '{course_id}':")
    assessments = courses[course_id][KEY_ASSESSMENTS]
    for assessment_id, assessment_info in assessments.items():
        print(f"\nAssessment ID: {assessment_id}, Name: {assessment_info['name']}, Weight: {assessment_info['weight']}")
        if assessment_id in gradebook[course_id]:
            print(f"{'Student ID':<15} {'Score':<10}")
            for student_id, score in gradebook[course_id][assessment_id].items():
                print(f"{student_id:<15} {score:<10}")
        else:
            print("No grades recorded for this assessment.")

def record_grade_menu(gradebook, courses, students):
    try:  
        course_id = input("\nEnter course ID: ").strip()
        assessment_id = input("Enter assessment ID: ").strip()
        student_id = input("Enter student ID: ").strip()
        score = float(input("Enter score (0-100): ").strip())
        record_grade(gradebook, courses, students, course_id, assessment_id, student_id, score)
    except ValueError:
        print("Invalid input. Please enter numeric values for score.")

def update_grade_menu(gradebook):
    try:
        course_id = input("\nEnter course ID: ").strip()
        assessment_id = input("Enter assessment ID: ").strip()
        student_id = input("Enter student ID: ").strip()
        new_score = float(input("Enter new score (0-100): ").strip())
        update_grade(gradebook, course_id, student_id, assessment_id, new_score)
    except ValueError:
        print("Invalid input. Please enter numeric values for score.")

def delete_grade_menu(gradebook):
    course_id = input("\nEnter course ID: ").strip()
    assessment_id = input("Enter assessment ID: ").strip()
    student_id = input("Enter student ID: ").strip()
    delete_grade(gradebook, course_id, student_id, assessment_id)

def calculate_student_average_menu(gradebook, courses):
    course_id = input("\nEnter course ID: ").strip()
    student_id = input("Enter student ID: ").strip()
    average = calculate_student_average(gradebook,courses, course_id, student_id)
    if average != -1:
        print(f"Average grade for student '{student_id}' in course '{course_id}': {average:.2f}")

def calculate_course_average_menu(gradebook, courses):
    course_id = input("\nEnter course ID: ").strip()
    average = calculate_course_average(gradebook, courses, course_id)
    if average != -1:
        print(f"Average grade for course '{course_id}': {average:.2f}")

def grades_menu(gradebook, courses, students):
    while True:
        print("\n--- Grades Menu ---")
        print("1. View Grades")
        print("2. Record Grade")
        print("3. Update Grade")
        print("4. Delete Grade")
        print("5. Calculate Student Average")
        print("6. Calculate Course Average")
        print("7. Back to Main Menu")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            view_grades_menu(gradebook, courses)
        elif choice == "2":
            record_grade_menu(gradebook, courses, students)
        elif choice == "3":
            update_grade_menu(gradebook)
        elif choice == "4":
            delete_grade_menu(gradebook)
        elif choice == "5":
            calculate_student_average_menu(gradebook, courses)
        elif choice == "6":
            calculate_course_average_menu(gradebook, courses)
        elif choice == "7":
            break


# ANALYTICS MENU

def view_grade_distribution_menu(gradebook, courses):
    course_id = input("\nEnter course ID: ").strip()
    bins_input = input("Enter grade bins as comma-separated values (e.g., 0,60,75,85,100): ").strip()
    try:
        bins = list(map(int, bins_input.split(',')))
        distribution = grade_distribution(gradebook, courses, course_id, bins)
        print(distribution)
        print("\nGrade Distribution:")
        for grade_range, count in distribution.items():
            print(f"{grade_range[0]} - {grade_range[1]}: {count} students")
    except ValueError:
        print("Invalid input. Please enter numeric values for bins.")

def view_top_students_menu(gradebook, courses):
    course_id = input("\nEnter course ID: ").strip()
    limit_input = input("Enter number of top students to view (default 5): ").strip()
    limit = int(limit_input) if limit_input else 5
    top_students_list = top_students(gradebook, courses, course_id, limit)
    print(f"\nTop {limit} Students in Course '{course_id}':")
    for student_id, avg in top_students_list:
        print(f"Student ID: {student_id}, Average: {avg:<3.2f}")

def view_student_progress_report_menu(gradebook, courses):
    course_id = input("\nEnter course ID: ").strip()
    student_id = input("Enter student ID: ").strip()
    report = student_progress_report(gradebook, courses, course_id, student_id)
    print(f"\nProgress Report for Student '{student_id}' in Course '{course_id}':")
    print(f"Average: {report['average']:.2f}")
    print(f"Status: {report['status']}")
    print("Assessments:")
    for assessment_id, details in report['assessments'].items():
        print(f"  ID: {assessment_id}, Name: {details['name']}, Weight: {details['weight']}")

def analytics_menu(gradebook, courses):
    while True:
        print("\n--- Analytics Menu ---")
        print("1. View Grade Distribution")
        print("2. View Top Students")
        print("3. View Student Progress Report")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            view_grade_distribution_menu(gradebook, courses)
        elif choice == "2":
            view_top_students_menu(gradebook, courses)
        elif choice == "3":
            view_student_progress_report_menu(gradebook, courses)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


# SETTINGS MENU

def settings_menu(settings):
    while True:
        print("\nSettings Menu:")
        print("1. View Settings")
        print("2. Back to Main Menu")

        choice = input("Select an option: ")
        
        if choice == '1':
            pass
        
        elif choice == '2':
            break
        
        else:
            print("Invalid option. Please try again.")


# MAIN PROGRAM LOOP

def main():
    DATA_DIR = "data"
    students, courses, gradebook, settings = load_state(DATA_DIR)

    print("Welcome to the Student Gradebook System")
    while True:
        print("\nMain Menu:")
        print("1. Students")
        print("2. Courses")
        print("3. Enrollment")
        print("4. Grades")
        print("5. Analytics")
        print("6. Settings")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            students_menu(students)
        elif choice == "2":
            courses_menu(courses)
        elif choice == "3":
            enrollment_menu(courses, students)
        elif choice == "4":
            grades_menu(gradebook, courses, students)
        elif choice == "5":
            analytics_menu(gradebook, courses)
        elif choice == "6":
            settings_menu(settings)
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    save_state(DATA_DIR, students, courses, gradebook, settings)

if __name__ == "__main__":
    main()

