# 📋 Placement Eligibility Streamlit App

An interactive web application built using **Python**, **Streamlit**, and **SQLite** to filter and view eligible students for placements based on dynamic criteria. The app uses **Faker** to simulate student data and applies **Object-Oriented Programming (OOP)** principles for clean database interactions.

---

## 🚀 Features

- 🎛️ Dynamic filtering by problem-solving, soft skills, and placement readiness
- 📊 SQL-powered insights on student performance and placement outcomes
- 🧠 Modular OOP-based architecture
- 🧪 Fully simulated database with 500 synthetic students using `Faker`
- 🖥️ Streamlit dashboard for interactive analytics

---

## 📁 Project Structure
.
├── app.py # Streamlit UI
├── db_manager.py # OOP class for DB handling
├── generate_dataframes.py # Faker-based dataset generator
├── insert_into_sqlite.py # Loads DataFrames into SQLite
├── queries.py # Contains 10 SQL insight queries
├── placement.db # SQLite database (auto-created)
├── requirements.txt # Python dependencies
├── .gitignore # Ignore environment/db files
└── README.md # Project overview

---

## 🔧 Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/placement-eligibility-app.git
cd placement-eligibility-app

2. Set up the environment
pip install -r requirements.txt

3. Generate and populate data
python dataframes.py
python SQLite_database.py
This creates a database (placement.db) with 500 fake student records.

4. Run the Streamlit app
streamlit run app.py

📊 Insights Preview
The app includes built-in SQL queries to show insights like:

Top 5 students by project score

Average problems solved per batch

Placement status distribution

Soft skills score by city

Students placed per company

You can generate it dynamically with:
pip freeze > requirements.txt

📬 Author
Sreelakshmi Vaidhyanathan
Email: sree.vaidhy.98@gmail.com
GitHub: @sreevaidhy2907

🧾 License
This project is open-source under the MIT License.
---

## ✅ `requirements.txt`

```txt
streamlit==1.35.0
pandas==2.2.2
faker==25.2.0