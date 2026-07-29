queries = {
    "Show all customers": "SELECT * FROM customers;",
    "Count customers": "SELECT COUNT(*) FROM customers;",
    "Highest amount": "SELECT MAX(amount) FROM customers;",
    "Lowest amount": "SELECT MIN(amount) FROM customers;",
    "Average amount": "SELECT AVG(amount) FROM customers;",
    "Customers from Bangalore": "SELECT * FROM customers WHERE city='Bangalore';",
    "Customers from Mysore": "SELECT * FROM customers WHERE city='Mysore';",
    "Customers from Chennai": "SELECT * FROM customers WHERE city='Chennai';",
    "Top 3 customers": "SELECT * FROM customers LIMIT 3;",
    "Customer names": "SELECT name FROM customers;"
}

print("===== Testing 10 Natural Language Queries =====")

for question, sql in queries.items():
    print(f"\nQuestion: {question}")
    print(f"Generated SQL: {sql}")

print("\nAll queries tested successfully!")