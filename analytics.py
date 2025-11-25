import json
import os # işletim sistemi operasyonlarına (terminal komutları vs) erişmek için 

from grades import calculate_student_average

def export_report(report, filename):
    os.makedirs("reports", exist_ok=True) # reports klasörü oluştur
    path = os.path.join("reports", filename) # path terminaldeki '/' veya '\' içeren ifade, join ise slashlar

    with open(path, "w") as f:
        json.dump(report, f, indent=4)

    return path
    

def grade_distribution(gradebook, course_id, bins):
    #(bins'in sıralanmış olduğundan emin olmamız lazım)*
    # {"0-60": 0, "60-75": 0, ...} gibi bir yapı oluşuyor
    distribution = {f"{bins[i]}-{bins[i+1]}": 0 for i in range(len(bins)-1)} #range indexlerini dolaşır
    #başlangıç değeri hepsini 0 ata

    for student_id in gradebook[course_id]:
        avg = calculate_student_average(gradebook, course_id, student_id)

        # Uygun aralığı bul
        for i in range(len(bins)-1):
            if bins[i] <= avg <= bins[i+1]:
                key = f"{bins[i]}-{bins[i+1]}"
                distribution[key] += 1
                break

    return distribution


def top_students(gradebook, course_id, limit=5):
    scores = []
    for student_id in gradebook[course_id]:
        avg = calculate_student_average(gradebook, course_id, student_id)
        scores.append((student_id, avg)) #tuple

    # sort'a bakması gereken elemanı belirlemek için yardımcı fonksiyon (element_2) kullandım
    scores.sort(key=element_2, reverse=True)

    return scores[:limit]


def element_2(tup): 
    return tup[1]


def student_progress_report(gradebook, course_id, student_id):
    assessments = gradebook[course_id][student_id]
    avg = calculate_student_average(gradebook, course_id, student_id)

    report = {
        "student_id": student_id,
        "assessments": assessments,
        "average": avg,
        "status": "Excellent" if avg >= 90 else
                  "Good" if avg >= 75 else
                  "Needs Improvement"
    }

    return report



    