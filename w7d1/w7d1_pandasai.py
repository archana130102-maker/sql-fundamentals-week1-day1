import pandas as pd
from pandasai import SmartDataframe

# ==============================
# W7D1: CIA Data Analyst Mode
# ==============================

CSV_PATH = r"C:\Users\yashika\OneDrive\Intership\startup_funding.csv"

print("===== W7D1: CIA Data Analyst Mode =====")

# ==============================
# STEP 1: Load CSV
# ==============================

try:
    df = pd.read_csv(CSV_PATH)

    print("CSV loaded successfully!")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    print("\nColumn names:")
    for column in df.columns:
        print("-", column)

    print("\nFirst 5 rows:")
    print(df.head())

except Exception as e:
    print("Error loading CSV:", e)
    exit()


# ==============================
# STEP 2: Create PandasAI DataFrame
# ==============================

try:
    smart_df = SmartDataframe(df)

    print("\nPandasAI dataframe created successfully!")

except Exception as e:
    print("Error creating PandasAI dataframe:", e)
    exit()


# ==============================
# STEP 3: 10 Natural Language Queries
# ==============================

questions = [
    "How many startups are in the dataset?",
    "Which city has the most startups?",
    "Which industry vertical appears most often?",
    "What are the top 5 startup names by number of entries?",
    "Which investment type appears most often?",
    "How many startups are located in Bangalore?",
    "How many startups are located in Mumbai?",
    "Show the top 5 cities by number of startups.",
    "Which industry vertical has the most entries?",
    "How many records have missing investor names?"
]

print("\n===== 10 NATURAL LANGUAGE QUERIES =====")

query_results = []

for i, question in enumerate(questions, 1):

    print(f"\nQuery {i}: {question}")

    try:
        answer = smart_df.chat(question)

        print("PandasAI Answer:", answer)

        query_results.append({
            "Query": question,
            "Answer": str(answer),
            "Status": "Success"
        })

    except Exception as e:

        print("Query failed:", e)

        query_results.append({
            "Query": question,
            "Answer": str(e),
            "Status": "Failed"
        })


# ==============================
# STEP 4: Manual Pandas Comparison
# ==============================

print("\n===== PANDASAI VS MANUAL PANDAS =====")

comparison_questions = [
    "How many startups are in the dataset?",
    "Which city has the most startups?",
    "Which investment type appears most often?"
]

for i, question in enumerate(comparison_questions, 1):

    print(f"\nQuestion {i}: {question}")

    # PandasAI
    try:
        ai_answer = smart_df.chat(question)
        print("PandasAI:", ai_answer)

    except Exception as e:
        print("PandasAI: Failed -", e)

    # Manual Pandas
    if i == 1:

        manual_answer = len(df)

    elif i == 2:

        city_data = df["City  Location"].dropna()
        manual_answer = city_data.value_counts().idxmax()

    elif i == 3:

        investment_data = df["InvestmentnType"].dropna()
        manual_answer = investment_data.value_counts().idxmax()

    print("Manual Pandas:", manual_answer)


# ==============================
# STEP 5: Save Query Results
# ==============================

try:

    results_df = pd.DataFrame(query_results)

    results_df.to_csv(
        "w7d1_query_results.csv",
        index=False
    )

    print("\nQuery results saved to:")
    print("w7d1_query_results.csv")

except Exception as e:

    print("\nCould not save query results:", e)


print("\n===== W7D1 COMPLETED =====")