# Sales Data ETL Pipeline (PostgreSQL)

## Overview
This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python and PostgreSQL.

It simulates a real-world data engineering workflow by:
- Extracting raw data from a CSV file
- Transforming and cleaning data using Python (Pandas)
- Loading the processed data into a PostgreSQL database
- Running SQL queries to generate business insights

---

## Project Structure

sales-etl-pipeline/
  ├── data/
  ├── scripts/
  ├── README.md
  ├── requirements.txt

---

## 🛠️ Tech Stack
- Python (Pandas)
- PostgreSQL
- SQLAlchemy
- SQL

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/nerdy-lochead/sales-etl-pipeline.git
cd sales-etl-pipeline

### 2. Install dependencies

pip install -r requirements.txt

### 3. Set up PostgreSQL
Create a database:

CREATE DATABASE sales_db;

Update connection string in `etl.py`:

postgresql://username:password@localhost:5432/sales_db

### 4. Run the ETL pipeline

python scripts/etl.py

---

## Analysis
Run queries in `analysis.sql` using PostgreSQL tools like pgAdmin or DBeaver.

---

## Key Insights
- Total revenue calculation
- Revenue breakdown by product
- Top-performing customers

---

## Future Improvements
- Add a REST API (Flask/FastAPI)
- Build a dashboard (Power BI/Tableau)
- Deploy to cloud (AWS/GCP)
- Automate pipeline scheduling
