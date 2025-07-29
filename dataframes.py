# generate_dataframes.py

import pandas as pd
from faker import Faker
import random

fake = Faker()
Faker.seed(0)
random.seed(0)

NUM_STUDENTS = 500

# 1. Students Table
students = []
genders = ["Male", "Female", "Other"]
for i in range(1, NUM_STUDENTS + 1):
    enroll_year = random.randint(2019, 2022)
    students.append({
        "student_id": i,
        "name": fake.name(),
        "age": random.randint(20, 25),
        "gender": random.choice(genders),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "enrollment_year": enroll_year,
        "course_batch": f"Batch-{enroll_year}",
        "city": fake.city(),
        "graduation_year": enroll_year + 3
    })

df_students = pd.DataFrame(students)

# 2. Programming Table
programming = []
languages = ["Python", "SQL", "JavaScript"]
for sid in df_students["student_id"]:
    programming.append({
        "programming_id": sid,
        "student_id": sid,
        "language": random.choice(languages),
        "problems_solved": random.randint(10, 200),
        "assessments_completed": random.randint(0, 10),
        "mini_projects": random.randint(0, 5),
        "certifications_earned": random.randint(0, 3),
        "latest_project_score": random.randint(0, 100)
    })

df_programming = pd.DataFrame(programming)

# 3. Soft Skills Table
softskills = []
for sid in df_students["student_id"]:
    softskills.append({
        "soft_skill_id": sid,
        "student_id": sid,
        "communication": random.randint(50, 100),
        "teamwork": random.randint(50, 100),
        "presentation": random.randint(50, 100),
        "leadership": random.randint(50, 100),
        "critical_thinking": random.randint(50, 100),
        "interpersonal_skills": random.randint(50, 100)
    })

df_softskills = pd.DataFrame(softskills)

# 4. Placements Table
placements = []
statuses = ["Ready", "Not Ready", "Placed"]
for sid in df_students["student_id"]:
    status = random.choice(statuses)
    is_placed = status == "Placed"
    placements.append({
        "placement_id": sid,
        "student_id": sid,
        "mock_interview_score": random.randint(0, 100),
        "internships_completed": random.randint(0, 3),
        "placement_status": status,
        "company_name": fake.company() if is_placed else None,
        "placement_package": round(random.uniform(4, 20), 2) if is_placed else None,
        "interview_rounds_cleared": random.randint(0, 5),
        "placement_date": fake.date_this_year().isoformat() if is_placed else None
    })

df_placements = pd.DataFrame(placements)

# Export to CSV if needed
# df_students.to_csv("students.csv", index=False)
# df_programming.to_csv("programming.csv", index=False)
# df_softskills.to_csv("softskills.csv", index=False)
# df_placements.to_csv("placements.csv", index=False)