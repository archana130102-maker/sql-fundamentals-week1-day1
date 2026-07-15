# Python for Data — Pandas Basics
# Day 5 | Week 1

import sys
print(f"Python {sys.version}")

import pandas as pd

def practice():
    # Sample dataset
    data = {
        "Name": ["Archana", "Ravi", "Priya", "Anita", "Rahul"],
        "Department": ["IT", "HR", "IT", "Finance", "HR"],
        "Salary": [50000, 45000, 60000, 55000, 48000]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    print("\nDataFrame:")
    print(df)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nInformation:")
    print(df.info())

    print("\nSummary Statistics:")
    print(df.describe())

    print("\nDepartment Count:")
    print(df["Department"].value_counts())

    print("\nEmployees in IT Department:")
    print(df[df["Department"] == "IT"])

    print("\nAverage Salary by Department:")
    print(df.groupby("Department")["Salary"].mean())

    # Export to CSV
    df.to_csv("employees_cleaned.csv", index=False)
    print("\nCSV file exported successfully.")

practice()

print("\nDone! Review with CIA for feedback.")