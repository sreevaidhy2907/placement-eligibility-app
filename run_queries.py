from db_manager import DatabaseManager

# Define the 10 SQL insight queries
queries = {
    "1. Top 5 Students by Latest Project Score":
        """
        SELECT s.name, p.latest_project_score
        FROM Students s
        JOIN Programming p ON s.student_id = p.student_id
        ORDER BY p.latest_project_score DESC
        LIMIT 5;
        """,

    "2. Average Programming Performance per Batch":
        """
        SELECT s.course_batch,
               AVG(p.problems_solved) AS avg_problems_solved,
               AVG(p.latest_project_score) AS avg_project_score
        FROM Students s
        JOIN Programming p ON s.student_id = p.student_id
        GROUP BY s.course_batch;
        """,

    "3. Placement Status Distribution":
        """
        SELECT placement_status, COUNT(*) AS count
        FROM Placements
        GROUP BY placement_status;
        """,

    "4. Average Soft Skills Score per City":
        """
        SELECT s.city,
               ROUND(AVG(ss.communication + ss.teamwork + ss.presentation +
                         ss.leadership + ss.critical_thinking + ss.interpersonal_skills) / 6, 2) AS avg_soft_skills
        FROM Students s
        JOIN SoftSkills ss ON s.student_id = ss.student_id
        GROUP BY s.city
        ORDER BY avg_soft_skills DESC
        LIMIT 10;
        """,

    "5. Number of Students Placed per Company":
        """
        SELECT company_name, COUNT(*) AS num_students
        FROM Placements
        WHERE placement_status = 'Placed'
        GROUP BY company_name
        ORDER BY num_students DESC
        LIMIT 10;
        """,

    "6. Internship Count vs Placement Readiness":
        """
        SELECT internships_completed, placement_status, COUNT(*) AS count
        FROM Placements
        GROUP BY internships_completed, placement_status
        ORDER BY internships_completed;
        """,

    "7. Most Popular Programming Languages":
        """
        SELECT language, COUNT(*) AS num_students
        FROM Programming
        GROUP BY language
        ORDER BY num_students DESC;
        """,

    "8. High Achievers (Certifications > 2 and Internships > 1)":
        """
        SELECT s.name, p.certifications_earned, pl.internships_completed
        FROM Students s
        JOIN Programming p ON s.student_id = p.student_id
        JOIN Placements pl ON s.student_id = pl.student_id
        WHERE p.certifications_earned > 2 AND pl.internships_completed > 1;
        """,

    "9. Soft Skills Score vs Placement Outcome":
        """
        SELECT pl.placement_status,
               ROUND(AVG(ss.communication + ss.teamwork + ss.presentation +
                         ss.leadership + ss.critical_thinking + ss.interpersonal_skills) / 6, 2) AS avg_soft_skills
        FROM Placements pl
        JOIN SoftSkills ss ON pl.student_id = ss.student_id
        GROUP BY pl.placement_status;
        """,

    "10. Interview Rounds vs Average Package":
        """
        SELECT interview_rounds_cleared,
               ROUND(AVG(placement_package), 2) AS avg_package
        FROM Placements
        WHERE placement_status = 'Placed'
        GROUP BY interview_rounds_cleared
        ORDER BY interview_rounds_cleared;
        """
}

# Initialize the DB manager
db = DatabaseManager()

# Run and print each query
print("\n📊 Running Placement Insight Queries\n" + "-"*40)
for title, sql in queries.items():
    print(f"\n🔹 {title}\n")
    rows = db.run_query(sql)
    if rows:
        for row in rows:
            print(dict(row))
    else:
        print("No data found.")
    print("-" * 40)

db.close()
