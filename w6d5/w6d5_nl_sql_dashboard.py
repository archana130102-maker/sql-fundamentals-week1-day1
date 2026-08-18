import sqlite3

DB_PATH = r"C:\Users\yashika\OneDrive\Intership\sales.db"


# SQL validation function
def validate_sql(sql):
    sql = sql.strip().upper()

    # Only SELECT queries are allowed
    if not sql.startswith("SELECT"):
        return False

    # Dangerous SQL commands are blocked
    blocked_commands = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE"
    ]

    for command in blocked_commands:
        if command in sql:
            return False

    return True


# Connect to database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("===== W6D5: SQL Validation =====")

# Safe SQL
safe_sql = "SELECT * FROM Customers;"

print("\nTesting safe SQL:")
print(safe_sql)

if validate_sql(safe_sql):
    print("✅ SQL is VALID")
else:
    print("❌ SQL is BLOCKED")


# Dangerous SQL
dangerous_sql = "DELETE FROM Customers;"

print("\nTesting dangerous SQL:")
print(dangerous_sql)

if validate_sql(dangerous_sql):
    print("✅ SQL is VALID")
else:
    print("❌ SQL is BLOCKED")


conn.close()

print("\n===== SQL Validation Completed! =====")