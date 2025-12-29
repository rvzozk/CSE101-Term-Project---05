
# dictionary yapısı kullandığımız için key'leri sabit tutmak adına
# constant'lar tanımlıyoruz
# bu sayede olası bir typo hatasını engellemiş oluruz

KEY_CODE = "code"
KEY_NAME = "name"
KEY_INSTRUCTOR = "instructor"
KEY_STUDENTS = "students"
KEY_ASSESSMENTS = "assessments"

KEY_A_ID = "id"
KEY_A_NAME = "name"
KEY_A_WEIGHT = "weight"

def record_course(courses, course_code, course_name, instructor):
    # aynı kodda bir course zaten var mı kontrol et
    # varsa ekleme yapma, uyarı ver
    # ayrı güncelleme fonksiyonu var
    if course_code in courses:
        print(f"Course with code '{course_code}' already exists.")
        return
    
    if course_code == "":
        print("Course code cannot be empty.")
        return
    
    if course_name == "":
        print("Course name cannot be empty.")
        return
    
    if instructor == "":
        print("Instructor name cannot be empty.")
        return
    
    # course yapısını oluştur ve ekle
    courses[course_code] = {
        KEY_CODE: course_code,
        KEY_NAME: course_name,
        KEY_INSTRUCTOR: instructor,
        KEY_STUDENTS: [],
        KEY_ASSESSMENTS: {}
    }
    print(f"Course '{course_name}' added successfully.")

def update_course(courses, course_code, new_name=None, new_instructor=None):
    #güncelleme fonksiyonu ekleme için değil, var olan bir course'u güncellemek için
    if course_code not in courses:
        print(f"Course with code '{course_code}' not found.")
        return
    
    # or yapısı ile eğer yeni bir değer verilmemişse eski değeri koru
    # or yapısı eğer eski değer falsy ise (None, "", 0 vs.) sağdaki değeri alır
    # mesela new_name None, boş string, ya da 0 ise courses[course_code][KEY_NAME] alınır

    # güncellenmiş yapıyı tekrar courses dictionary'sinde güncelle
    courses.update({
        course_code: {
            KEY_CODE: course_code,
            KEY_NAME: new_name or courses[course_code][KEY_NAME],
            KEY_INSTRUCTOR: new_instructor or courses[course_code][KEY_INSTRUCTOR],
            KEY_STUDENTS: courses[course_code][KEY_STUDENTS],
            KEY_ASSESSMENTS: courses[course_code][KEY_ASSESSMENTS]
        }
    })
    print(f"Course '{course_code}' updated successfully.")

def delete_course(courses, course_code):
    # course varsa sil, yoksa uyarı ver
    if course_code in courses:
        del courses[course_code]
        print(f"Course '{course_code}' deleted successfully.")
    else:
        print(f"Course with code '{course_code}' not found.")

def add_student_to_course(courses, students, course_code, student_id):
    # bir öğrenciyi course'a ekleyebilmek için
    # hem course'un var olması lazım
    # hem de öğrencinin var olması lazım

    if course_code not in courses:
        print(f"Course with code '{course_code}' not found.")
        return
    
    if student_id not in students:
        print(f"Student with ID '{student_id}' not found.")
        return
    
    courses[course_code][KEY_STUDENTS].append(student_id)
    print(f"Student '{student_id}' added to course '{course_code}'.")

def remove_student_from_course(courses, course_code, student_id):
    # course ve student kontrolü yap
    if course_code not in courses:
        print(f"Course with code '{course_code}' not found.")
        return
    
    if student_id not in courses[course_code][KEY_STUDENTS]:
        print(f"Student with ID '{student_id}' not enrolled in course '{course_code}'.")
        return
    
    courses[course_code][KEY_STUDENTS].remove(student_id)
    print(f"Student '{student_id}' removed from course '{course_code}'.")

def add_assessment(courses, course_code, assessment_id, assessment_name, weight):
    # eğer aynı id'de bir assessment varsa ekleme yapma
    if assessment_id in courses[course_code][KEY_ASSESSMENTS]:
        print(f"Assessment with ID '{assessment_id}' already exists in course '{course_code}'.")
        return
    
    # course içerisindeki assessments yapısı assesment hakkında bilgi tutar
    # notlar gradebook'ta tutulur
    courses[course_code][KEY_ASSESSMENTS][assessment_id] = {
        KEY_A_ID: assessment_id,
        KEY_A_NAME: assessment_name,
        KEY_A_WEIGHT: weight
    }
    print(f"Assessment '{assessment_name}' added to course '{course_code}'.")

def remove_assessment(courses, course_code, assessment_id):
    # assessment varsa sil, yoksa uyarı ver
    if assessment_id in courses[course_code][KEY_ASSESSMENTS]:
        del courses[course_code][KEY_ASSESSMENTS][assessment_id]
        print(f"Assessment '{assessment_id}' removed from course '{course_code}'.")
    else:
        print(f"Assessment with ID '{assessment_id}' not found in course '{course_code}'.")

def update_assessment(courses, course_code, assessment_id, new_name=None, new_weight=None):
    # verilen assessment id'sini bulmayı dene, bulamazsa uyarı ver
    assessment = courses[course_code][KEY_ASSESSMENTS].get(assessment_id)
    if not assessment:
        print(f"Assessment with ID '{assessment_id}' not found in course '{course_code}'.")
        return
    
    assessment[KEY_A_NAME] = new_name or assessment[KEY_A_NAME]
    assessment[KEY_A_WEIGHT] = new_weight or assessment[KEY_A_WEIGHT]
    print(f"Assessment '{assessment_id}' updated successfully in course '{course_code}'.")
