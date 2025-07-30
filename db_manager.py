import sqlite3
from typing import Optional, Dict, Any
import pandas as pd

class DatabaseManager:
    def __init__(self, db_path: str = "placement.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row  # Enables column-name access in results
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                student_id INTEGER PRIMARY KEY,
                name VARCHAR(100), age INTEGER, gender VARCHAR(100),
                email VARCHAR(100), phone VARCHAR(100),
                enrollment_year INTEGER, course_batch VARCHAR(100),
                city VARCHAR(100), graduation_year INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Programming (
                programming_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                language VARCHAR(100), problems_solved INTEGER,
                assessments_completed INTEGER, mini_projects INTEGER,
                certifications_earned INTEGER, latest_project_score INTEGER,
                FOREIGN KEY(student_id) REFERENCES Students(student_id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS SoftSkills (
                soft_skill_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                communication INTEGER, teamwork INTEGER,
                presentation INTEGER, leadership INTEGER,
                critical_thinking INTEGER, interpersonal_skills INTEGER,
                FOREIGN KEY(student_id) REFERENCES Students(student_id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Placements (
                placement_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                mock_interview_score INTEGER, internships_completed INTEGER,
                placement_status VARCHAR(100), company_name VARCHAR(100),
                placement_package REAL, interview_rounds_cleared INTEGER,
                placement_date VARCHAR(100),
                FOREIGN KEY(student_id) REFERENCES Students(student_id)
            )
        ''')
        self.conn.commit()

    def insert_dataframe(self, df: pd.DataFrame, table_name: str):
        """
        Insert a pandas DataFrame into a specified table
        """
        df.to_sql(table_name, self.conn, if_exists='append', index=False)

    def run_query(self, sql: str, params: Optional[tuple] = None) -> list[sqlite3.Row]:
        """
        Execute a SELECT query and return rows as dictionaries
        """
        if params is None:
            params = ()
        return self.conn.execute(sql, params).fetchall()

    def fetch_eligible_students(self, criteria: Dict[str, Any]) -> list[sqlite3.Row]:
        """
        Dynamically construct a WHERE clause based on input filters
        """
        sql = '''
        SELECT s.name, s.email, p.language, p.problems_solved,
               ss.communication, pl.mock_interview_score, pl.placement_status
        FROM Students s
        JOIN Programming p ON s.student_id = p.student_id
        JOIN SoftSkills ss ON s.student_id = ss.student_id
        JOIN Placements pl ON s.student_id = pl.student_id
        WHERE 1=1
        '''
        params = []

        if criteria.get("min_problems_solved"):
            sql += " AND p.problems_solved >= ?"
            params.append(criteria["min_problems_solved"])

        if criteria.get("min_communication"):
            sql += " AND ss.communication >= ?"
            params.append(criteria["min_communication"])

        if criteria.get("mock_score"):
            sql += " AND pl.mock_interview_score >= ?"
            params.append(criteria["mock_score"])

        if criteria.get("status") and criteria["status"] != "Any":
            sql += " AND pl.placement_status = ?"
            params.append(criteria["status"])

        if criteria.get("city"):
            sql += " AND s.city LIKE ?"
            params.append(f"%{criteria['city']}%")

        if criteria.get("batch"):
            sql += " AND s.course_batch LIKE ?"
            params.append(f"%{criteria['batch']}%")

        return self.conn.execute(sql, params).fetchall()

    def close(self):
        self.conn.close()
