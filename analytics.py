import json
import os # işletim sistemi operasyonlarına (terminal komutları vs) erişmek için 

from grades import calculate_student_average
from courses import KEY_STUDENTS, KEY_ASSESSMENTS

def export_report(report, filename):
    os.makedirs("reports", exist_ok=True) # reports klasörü oluştur
    path = os.path.join("reports", filename) # path terminaldeki '/' veya '\' içeren ifade, join ise slashlar

    with open(path, "w") as f:
        json.dump(report, f, indent=4)

    return path
    

def grade_distribution(gradebook, courses, course_id, bins):
    #(bins'in sıralanmış olduğundan emin olmamız lazım)*
    # {(0,60): 0, (60,75): 0, ...} gibi bir yapı oluşuyor
    distribution = {(bins[i], bins[i+1]): 0 for i in range(len(bins)-1)} #range indexlerini dolaşır
    #başlangıç değeri hepsini 0 ata

    for student_id in courses[course_id][KEY_STUDENTS]:
        avg = calculate_student_average(gradebook, courses, course_id, student_id)
        print(f"Student '{student_id}' average: {avg}")
        # Uygun aralığı bul
        for i in range(len(bins)-1):
            if bins[i] <= avg <= bins[i+1]:
                key = (bins[i], bins[i+1])
                distribution[key] += 1
                break

    return distribution


def top_students(gradebook, courses, course_id, limit=5):
    scores = []
    for student_id in courses[course_id][KEY_STUDENTS]:
        avg = calculate_student_average(gradebook, courses, course_id, student_id)
        scores.append((student_id, avg)) #tuple

    # sort'a bakması gereken elemanı belirlemek için yardımcı fonksiyon (element_2) kullandım
    scores.sort(key=element_2, reverse=True)

    return scores[:limit]


def element_2(tup): 
    return tup[1]


def student_progress_report(gradebook, courses, course_id, student_id):
    assessments = courses[course_id][KEY_ASSESSMENTS]
    avg = calculate_student_average(gradebook, courses, course_id, student_id)

    report = {
        "student_id": student_id,
        "assessments": assessments,
        "average": avg,
        "status": "AA" if avg >= 90 else
                  "BA" if avg >= 85 else
                  "BB" if avg >= 80 else
                  "CB" if avg >= 75 else
                  "CC" if avg >= 70 else
                  "DC" if avg >= 60 else
                  "DD" if avg >= 50 else
                  "FF"
    }

    return report



    
