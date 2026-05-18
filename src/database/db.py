from src.database.config import supabase
import bcrypt


def hash_pass(pwd):
    # Hash a password using bcrypt
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()


def check_pass(pwd, hashed):
    # Verify a password against its hashed value
    return bcrypt.checkpw(pwd.encode(), hashed.encode())


def check_teacher_exists(username):
    # Check if a teacher with the given username exists
    response = (
        supabase.table("teachers").select("username").eq("username", username).execute()
    )
    return len(response.data) > 0


def create_teacher(username, password, name):
    # Create a new teacher record
    data = {"username": username, "password": hash_pass(password), "name": name}
    response = supabase.table("teachers").insert(data).execute()
    return response.data


def teacher_login(username, password):
    # Authenticate a teacher and return their record if credentials are valid
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher["password"]):
            return teacher
    return None


def get_all_students():
    # Retrieve all students from the database
    response = supabase.table("students").select("*").execute()
    return response.data


def create_student(new_name, face_embedding=None, voice_embedding=None):
    # Create a new student record with optional embeddings
    data = {
        "name": new_name,
        "face_embedding": face_embedding,
        "voice_embedding": voice_embedding,
    }
    response = supabase.table("students").insert(data).execute()
    return response.data


def create_subject(subject_code, name, section, teacher_id):
    # Create a new subject record
    data = {
        "subject_code": subject_code,
        "name": name,
        "section": section,
        "teacher_id": teacher_id,
    }
    response = supabase.table("subjects").insert(data).execute()
    return response.data


def get_teacher_subjects(teacher_id):
    # Get all subjects for a teacher with student count and class session info
    response = (
        supabase.table("subjects")
        .select("*, subject_students(count), attendance_logs(timestamp)")
        .eq("teacher_id", teacher_id)
        .execute()
    )
    subjects = response.data

    for sub in subjects:
        sub["total_students"] = (
            sub.get("subject_students", [{}])[0].get("count", 0)
            if sub.get("subject_students")
            else 0
        )
        attendance = sub.get("attendance_logs", [])
        unique_sessions = len(set(log["timestamp"] for log in attendance))
        sub["total_classes"] = unique_sessions

        sub.pop("subject_students", None)
        sub.pop("attendance_logs", None)

    return subjects


def enroll_student_to_subject(student_id, subject_id):
    # Enroll a student in a subject
    data = {"student_id": student_id, "subject_id": subject_id}
    response = supabase.table("subject_students").insert(data).execute()
    return response.data


def unenroll_student_to_subject(student_id, subject_id):
    # Remove a student's enrollment from a subject
    response = (
        supabase.table("subject_students")
        .delete()
        .eq("student_id", student_id)
        .eq("subject_id", subject_id)
        .execute()
    )
    return response.data


def get_student_subjects(student_id):
    # Get all subjects a student is enrolled in
    response = (
        supabase.table("subject_students")
        .select("*, subjects(*)")
        .eq("student_id", student_id)
        .execute()
    )
    return response.data


def get_student_attendance(student_id):
    # Get attendance records for a student
    response = (
        supabase.table("attendance_logs")
        .select("*, subjects(*)")
        .eq("student_id", student_id)
        .execute()
    )
    return response.data


def create_attendance(logs):
    # Create attendance log records
    response = supabase.table("attendance_logs").insert(logs).execute()
    return response.data


def get_attendance_for_teacher(teacher_id):
    # Get all attendance logs for a teacher's subjects
    response = (
        supabase.table("attendance_logs")
        .select("*, subjects!inner(*)")
        .eq("subjects.teacher_id", teacher_id)
        .execute()
    )
    return response.data
