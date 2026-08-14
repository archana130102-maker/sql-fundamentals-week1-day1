import sqlite3

DB_PATH = "sales.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


def validate_sql(sql):
    sql = sql.strip().upper()

    # Allow only SELECT queries
    if not sql.startswith("SELECT"):
        return False

    # Block dangerous SQL commands
    blocked = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "TRUNCATE"]

    for command in blocked:
        if command in sql:
            return False

    return True


print("===== SQL Validation Test =====")

test_sql = "SELECT * FROM Sales;"

if validate_sql(test_sql):
    print("SQL validation passed ✅")
else:
    print("SQL validation failed ❌")

conn.close()
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/cia/sql-analyst", methods=["POST"])
def sql_analyst():

    data = request.get_json()

    question = data.get("question", "")

    sql_patterns = {
        "show all sales": "SELECT * FROM Sales;",
        "total sales": "SELECT SUM(amount) AS total_sales FROM Sales;",
        "sales by region": "SELECT region, SUM(amount) AS total_sales FROM Sales GROUP BY region;",
        "highest sale": "SELECT MAX(amount) AS highest_sale FROM Sales;",
        "average sale": "SELECT AVG(amount) AS average_sale FROM Sales;"
    }

    question_lower = question.lower()

    for pattern, sql in sql_patterns.items():
        if pattern in question_lower:

            if validate_sql(sql):
                return jsonify({
                    "question": question,
                    "sql": sql,
                    "status": "validated"
                })

    return jsonify({
        "question": question,
        "sql": None,
        "status": "No matching SQL pattern found"
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)