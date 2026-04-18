# Hospital Patient Data Analysis using Python, SQL, and Excel

This project analyzes hospital patient records to identify disease patterns, doctor workload, and treatment cost insights.

Hospitals generate large amounts of healthcare data, but without proper analysis, valuable insights remain hidden. This project helps transform raw patient data into meaningful information that supports better hospital management, resource allocation, and decision-making.

The project uses:
- Python (Pandas) for data analysis
- SQL (MySQL) for structured querying
- Microsoft Excel for pivot tables and charts

---

## Problem Statement

Hospital management needs to understand patient trends, doctor workload distribution, and treatment expenses to improve operational efficiency.

This project answers important business questions such as:

- Which diseases are most common?
- Which doctors handle the highest number of patients?
- What is the average treatment cost?
- Which treatment cases generate the highest expenses?

The goal is to convert raw healthcare data into actionable insights.

---

## Repository Contents

- `patients.csv` → Raw dataset used for analysis
- `analysis.py` → Python script for exploratory data analysis and insights
- `SQL_queries.sql` → SQL script for table creation, data insertion, and analysis queries
- `patients_processed.xlsx` → Processed Excel file for pivot tables and dashboard creation
- `patients_processed.csv` → Processed CSV file generated from Python script
- `project_report.pdf` → Final project documentation report

---

## Dataset Schema

The dataset contains the following columns:

- `patient_id` → Unique patient ID
- `age` → Age of patient
- `gender` → Male / Female
- `disease` → Diagnosed disease
- `doctor` → Assigned doctor
- `treatment_cost` → Cost of treatment

---

## Python Analysis (`analysis.py`)

The Python script performs:

- Display of first 5 rows
- Dataset structure check using `.info()`
- Summary statistics using `.describe()`
- Disease frequency analysis
- Doctor workload analysis
- Average treatment cost calculation
- Highest treatment cost patient identification
- Age-group classification:
  - Young
  - Adult
  - Senior
- Export of processed data to `patients_processed.csv`

This helps in identifying patterns and generating useful business insights.

---

## SQL Analysis (`SQL_queries.sql`)

The SQL script includes:

### Database Operations

1. Database creation (`hospital_db`)
2. Patient table creation
3. Sample data insertion

### Analysis Queries

- Display all patient records
- Count patients by disease
- Calculate average treatment cost
- Identify doctor treating the most patients

These queries help in structured database-level analysis.

---

## Excel Analysis

Microsoft Excel is used for:

- Creating Pivot Tables
- Disease-wise patient count analysis
- Doctor workload analysis
- Pie Chart → Disease Distribution
- Bar Chart → Doctor Workload

This provides visual representation of the data for easier understanding.
