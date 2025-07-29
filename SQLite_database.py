# insert_into_sqlite.py

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
    name TEXT, age INTEGER, gender TEXT,
    email TEXT, phone TEXT,
    enrollment_year INTEGER, course_batch TEXT,
    city TEXT, graduation_year INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Programming (
    programming_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    language TEXT, problems_solved INTEGER,
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
    placement_status TEXT, company_name TEXT,
    placement_package REAL, interview_rounds_cleared INTEGER,
    placement_date TEXT,
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