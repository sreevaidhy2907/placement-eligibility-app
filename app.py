# app.py

import streamlit as st
from db_manager import DatabaseManager

# Initialize DB connection
db = DatabaseManager()

# -----------------------------
# UI Layout
# -----------------------------
st.set_page_config(page_title="Placement Eligibility App", layout="wide")
st.title("📋 Placement Eligibility Dashboard")

with st.sidebar:
    st.header("🎯 Filter Eligibility Criteria")

    # Add filters
    min_problems = st.slider("Min Problems Solved", 0, 200, 50)
    min_comm = st.slider("Min Communication Score", 0, 100, 70)
    mock_score = st.slider("Min Mock Interview Score", 0, 100, 60)
    status = st.selectbox("Placement Status", ["Any", "Ready", "Not Ready", "Placed"])

    city_filter = st.text_input("City (optional)", "")
    batch_filter = st.text_input("Course Batch (optional)", "")

    submit = st.button("🔍 Find Eligible Students")

# -----------------------------
# Eligibility Query
# -----------------------------
if submit:
    filters = {
        "min_problems_solved": min_problems,
        "min_communication": min_comm,
        "mock_score": mock_score,
        "status": status
    }

    results = db.fetch_eligible_students(filters)

    # Filter extra fields in Python (optional enhancements)
    filtered = []
    for row in results:
        row_dict = dict(row)
        # Additional optional filters (client-side)
        if city_filter and city_filter.lower() not in row_dict.get("city", "").lower():
            continue
        if batch_filter and batch_filter.lower() not in row_dict.get("course_batch", "").lower():
            continue
        filtered.append(row_dict)

    st.subheader("✅ Eligible Students")
    if filtered:
        st.dataframe(filtered)
        st.success(f"{len(filtered)} students matched the criteria.")
    else:
        st.warning("No students found with the given filters.")

# -----------------------------
# SQL Insights Dashboard
# -----------------------------
st.markdown("---")
st.subheader("📊 Placement Insights")

from run_queries import queries

for title, sql in queries.items():
    st.markdown(f"### {title}")
    rows = db.run_query(sql)
    st.dataframe([dict(r) for r in rows])