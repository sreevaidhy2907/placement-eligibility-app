import sqlite3
from dataframes import (
    df_students, df_programming, df_softskills, df_placements
)

# Connect to SQLite
conn = sqlite3.connect("placement.db")

# Create tables
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY,
    name VARCHAR(100), age INTEGER, gender VARCHAR(100),
    email VARCHAR(100), phone VARCHAR(100),
    enrollment_year INTEGER, course_batch VARCHAR(100),
    city VARCHAR(100), graduation_year INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Programming (
    programming_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    language VARCHAR(100), problems_solved INTEGER,
    assessments_completed INTEGER, mini_projects INTEGER,
    certifications_earned INTEGER, latest_project_score INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(student_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS SoftSkills (
    soft_skill_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    communication INTEGER, teamwork INTEGER,
    presentation INTEGER, leadership INTEGER,
    critical_thinking INTEGER, interpersonal_skills INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(student_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Placements (
    placement_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    mock_interview_score INTEGER, internships_completed INTEGER,
    placement_status VARCHAR(100), company_name VARCHAR(100),
    placement_package FLOAT, interview_rounds_cleared INTEGER,
    placement_date VARCHAR(100),
    FOREIGN KEY(student_id) REFERENCES Students(student_id)
)
''')

conn.commit()

# Insert DataFrames into tables
df_students.to_sql("Students", conn, if_exists="append", index=False)
df_programming.to_sql("Programming", conn, if_exists="append", index=False)
df_softskills.to_sql("SoftSkills", conn, if_exists="append", index=False)
df_placements.to_sql("Placements", conn, if_exists="append", index=False)

conn.commit()
conn.close()
