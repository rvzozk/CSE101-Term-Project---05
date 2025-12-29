from courses import KEY_ASSESSMENTS, KEY_A_WEIGHT
from courses import KEY_STUDENTS

def record_grade(gradebook, courses, students, course_id, assessment_id, student_id, score):
    # course geçerli olmalı, kullanıcı not girişi için bilinmeyen bir course seçemez
    if course_id not in courses:
        print(f"Course with ID '{course_id}' not found.")
        return
    
    # assessment seçilen course'a ait olmalı ve tanımlı olmalı
    if assessment_id not in courses[course_id][KEY_ASSESSMENTS]:
        print(f"Assessment with ID '{assessment_id}' not found in course '{course_id}'.")
        return

    # student geçerli olmalı
    if student_id not in students:
        print(f"Student with ID '{student_id}' not found.")
        return

    # geçerli not aralığında mı kontrol et
    if score < 0 or score > 100:
        print("Score is not valid.")
        return
    
    # setdefault ile içeriden eksik yapıları oluştur
    # https://www.w3schools.com/python/ref_dictionary_setdefault.asp
    assesments = gradebook.setdefault(course_id, {}).setdefault(assessment_id, {})

    # halihazırda not girilmiş mi kontrol et
    # eğer girilmişse üzerine yazma, uyarı ver, update için ayrı fonksiyon var
    if student_id in assesments:
        print(f"Grade for student '{student_id}' in assessment '{assessment_id}' already exists.")
        return
    
    # kod buraya gelirse her şey yolundadır, notu kaydet ve başarılı mesajı ver
    assesments[student_id] = score
    print(f"Grade for student '{student_id}' in assessment '{assessment_id}' recorded successfully.")



def update_grade(gradebook, course_id, student_id, assessment_id, new_score):
    # zaten var olan bir notu güncelleyeceğiz
    # o yüzden varlığını gradebook'ta kontrol etmemiz yeterli
    # çünkü record_grade fonksiyonu zaten geçerlilik kontrollerini yapıyor

    # gradebook'ta course var mı
    if course_id not in gradebook:
        print(f"Course with ID '{course_id}' not found.")
        return
    
    # gradebook'ta bu assessment var mı
    if assessment_id not in gradebook.get(course_id, {}):
        print(f"Assessment with ID '{assessment_id}' not found in course '{course_id}'.")
        return
    
    # assessment içinde bu student'ın notu var mı
    if student_id not in gradebook[course_id][assessment_id]:
        print(f"Grade for student '{student_id}' in assessment '{assessment_id}' not found.")
        return
    
    # yeni not geçerli aralıkta mı
    if new_score < 0 or new_score > 100: # update edilirken de yanlış girilmesin
        print("Score is not valid.")
        return
        
    # notu güncelle ve başarılı mesajı ver
    gradebook[course_id][assessment_id][student_id] = new_score
    print(f"Grade for student '{student_id}' in assessment '{assessment_id}' updated successfully.")


def delete_grade(gradebook, course_id, student_id, assessment_id):
    # var olan bir notu sileceğiz
    # o yüzden varlığını gradebook'ta kontrol etmemiz yeterli

    if course_id not in gradebook:
        print(f"Course with ID '{course_id}' not found.")
        return
    
    if assessment_id not in gradebook.get(course_id, {}):
        print(f"Assessment with ID '{assessment_id}' not found in course '{course_id}'.")
        return
    
    if student_id not in gradebook[course_id][assessment_id]:
        print(f"Grade for student '{student_id}' in assessment '{assessment_id}' not found.")
        return
    
    # silinmek istenen not var, sil ve başarılı mesajı ver
    del gradebook[course_id][assessment_id][student_id]
    print(f"Grade for student '{student_id}' in assessment '{assessment_id}' deleted successfully.")


def calculate_student_average(gradebook, courses, course_id, student_id):
    # course gradebook'ta var mı kontrol et
    # eğer varsa, record_grade zaten geçerlilik kontrollerini yapmıştır
    # o yüzden burada tekrar kontrol etmeye gerek yok

    if course_id not in gradebook:
        print(f"Course with ID '{course_id}' not found or has no grades.")
        return -1
    
    # assessments yapısı:
    # {
    #   assessment_id: {
    #       student_id: score, 
    #       ...
    #   }, 
    #   ...
    # }
    assessments = gradebook[course_id]

    weighted_sum = 0
    total_weight = 0

    # assesment id'lerini dolaş
    for aid in assessments:
        # her bir assessment'ın ağırlığını bul
        # courses yapısını kullan, single source of truth orası
        weight = courses[course_id][KEY_ASSESSMENTS][aid][KEY_A_WEIGHT]
        total_weight += weight

        # eğer öğrenci bu assessment için not almamışsa uyarı ver
        # ve notu 0 kabul et
        if student_id not in assessments[aid]:
            print(f"Student '{student_id}' does not have a grade for assessment '{aid}'.")
            print("Accepting missing grades as zero for average calculation.")
            continue
        
        # notunu ekle
        score = assessments[aid][student_id]
        weighted_sum += score * weight

    return weighted_sum / total_weight # ağırlıklı ortalama olduğu için 100'e tamamlayacak 
    #(division by 0 olabilir)*
    


def calculate_course_average(gradebook, courses, course_id):
    # üstteki aynı kontrolü yap
    if course_id not in gradebook:
        print(f"Course with ID '{course_id}' not found or has no grades.")
        return -1
    
    avgs = [] # öğrenci ortalamalarını buna at

    # öğrencileri courses üzerinden alıyoruz
    # bunun sebebi, gradebook'ta notu olmayan öğrenciler olabilir
    # ama bir öğrenci course'a kayıtlı ise ortalamaya dahil edilmeli
    # eğer notu yoksa calculate_student_average fonksiyonu uyarı verecek ve 0 kabul edecek
    for sid in courses[course_id][KEY_STUDENTS]:
        avgs.append(calculate_student_average(gradebook, courses, course_id, sid))
    return sum(avgs) / len(avgs)
    
    
