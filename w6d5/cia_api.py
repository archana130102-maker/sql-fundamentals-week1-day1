from flask import Flask, request, jsonify

app = Flask(__name__)


# Simple Natural Language → SQL
def generate_sql(question):

    question = question.lower()

    if "count customers" in question:
        return "SELECT COUNT(*) FROM Customers;"

    elif "show customers" in question:
        return "SELECT * FROM Customers;"

    elif "total sales" in question:
        return "SELECT SUM(amount) AS total_sales FROM Sales;"

    elif "sales by region" in question:
        return "SELECT region, SUM(amount) AS total_sales FROM Sales GROUP BY region;"

    elif "highest sale" in question:
        return "SELECT MAX(amount) AS highest_sale FROM Sales;"

    elif "lowest sale" in question:
        return "SELECT MIN(amount) AS lowest_sale FROM Sales;"

    elif "average sale" in question:
        return "SELECT AVG(amount) AS average_sale FROM Sales;"

    elif "show employees" in question:
        return "SELECT * FROM Employees;"

    elif "show orders" in question:
        return "SELECT * FROM Orders;"

    else:
        return None


@app.route("/cia/sql-analyst", methods=["POST"])
def sql_analyst():

    data = request.get_json()

    question = data.get("question", "")

    sql = generate_sql(question)

    if sql is None:
        return jsonify({
            "error": "Question not supported"
        }), 400

    return jsonify({
        "question": question,
        "sql": sql
    })


@app.route("/")
def home():
    return "W6D5 CIA SQL Analyst API is running!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)