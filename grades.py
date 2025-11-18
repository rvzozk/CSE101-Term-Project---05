


def record_grade(gradebook, course_id, student_id, assessment):
    if course_id not in gradebook:
        gradebook[course_id] = {}
    if student_id not in gradebook[course_id]:
        gradebook[course_id][student_id] = []
    if assessment["score"] < 0 or assessment["score"] > 100:
        print("-1 : Error for scores.")
        return gradebook
    existing = [a for a in gradebook[course_id][student_id] if a.get("id") == assessment.get("id")]
    if existing:
        raise ValueError(f"Assessment with id {assessment.get('id')} already exists for student {student_id}.")
    gradebook[course_id][student_id].append(assessment)
    return gradebook



def update_grade(gradebook, course_id, student_id, assessment_id, new_score):
    if course_id not in gradebook or student_id not in gradebook[course_id]:
        raise KeyError("Course or student is not found.")
    for a in gradebook[course_id][student_id]:
        if a.get("id") == assessment_id:
            a["score"] = new_score
            return gradebook
    raise KeyError("Assessment id not found.")


def delete_grade(gradebook, course_id, student_id, assessment_id):
    if course_id not in gradebook or student_id not in gradebook[course_id]:
        raise KeyError("Course or student not found.")
    original = gradebook[course_id][student_id]
    updated = [a for a in original if a.get("id") != assessment_id]
    if len(updated) == len(original):
        raise KeyError("Assessment id not found.")
    gradebook[course_id][student_id] = updated
    return gradebook


def calculate_student_average(gradebook, course_id, student_id):
    if course_id not in gradebook or student_id not in gradebook[course_id]:
        raise KeyError("Course or student not found.")
    assessments = gradebook[course_id][student_id]
    if not assessments:
        return 0.0
    total_weight = sum((a.get("weight", 0) for a in assessments))
    if total_weight == 0:
        return sum((a.get("score", 0) for a in assessments)) / len(assessments)
    weighted_sum = sum((a.get("score", 0) * a.get("weight", 0) for a in assessments))
    return weighted_sum / total_weight * 100 / 100


def calculate_course_average(gradebook, course_id):
    if course_id not in gradebook:
        raise KeyError("Course not found.")
    students = gradebook[course_id]
    if not students:
        return 0.0
    avgs = []
    for sid in students:
        avgs.append(calculate_student_average(gradebook, course_id, sid))
    return sum(avgs) / len(avgs)
































