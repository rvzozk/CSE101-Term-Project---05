def record_grade(gradebook, course_id, student_id, assessment):
    # geçerli not aralığında mı kontrol et
    if assessment["score"] < 0 or assessment["score"] > 100:
        print("Score is not valid.")
        return gradebook
    
    # setdefault ile içeriden eksik yapıları oluştur
    # https://www.w3schools.com/python/ref_dictionary_setdefault.asp
    gradebook.setdefault(course_id, {}).setdefault(student_id, []).append(assessment)
    return gradebook



def update_grade(gradebook, course_id, student_id, assessment_id, new_score):
    if assessment["score"] < 0 or assessment["score"] > 100: # update edilirken de yanlış girilmesin
        print("Score is not valid.")
        return gradebook
        
    for a in gradebook[course_id][student_id]:
        if a.get("id") == assessment_id:
            a["score"] = new_score # a dict'in id'si eşitse skoru güncellemek için
            return gradebook


def delete_grade(gradebook, course_id, student_id, assessment_id):
    original = gradebook[course_id][student_id]
    updated = [a for a in original if a.get("id") != assessment_id] # eşit olanı seçmektense çıkarıp güncelle
    gradebook[course_id][student_id] = updated
    return gradebook


def calculate_student_average(gradebook, course_id, student_id):    
    assessments = gradebook[course_id][student_id]
    total_weight = sum((a.get("weight", 0) for a in assessments)) # weight al, bulamazsan hata verme 0 kabul et
    weighted_sum = sum((a.get("score", 0) * a.get("weight", 0) for a in assessments))
    return weighted_sum / total_weight # ağırlıklı ortalama olduğu için 100'e tamamlayacak 
    #(division by 0 olabilir)*


def calculate_course_average(gradebook, course_id):
    students = gradebook[course_id]
    avgs = [] # öğrenci ortalamalarını buna at
    for sid in students:
        avgs.append(calculate_student_average(gradebook, course_id, sid))
    return sum(avgs) / len(avgs)
    
    