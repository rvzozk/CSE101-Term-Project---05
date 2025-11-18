import json
import os

def _read_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def _write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_state(base_dir="data"):
    students = _read_json(os.path.join(base_dir, "students.json"), [])
    courses = _read_json(os.path.join(base_dir, "courses.json"), [])
    gradebook = _read_json(os.path.join(base_dir, "grades.json"), {})
    return students, courses, gradebook

def save_state(base_dir, students, courses, gradebook, settings):
    _write_json(os.path.join(base_dir, "students.json"), students)
    _write_json(os.path.join(base_dir, "courses.json"), courses)
    _write_json(os.path.join(base_dir, "grades.json"), gradebook)


