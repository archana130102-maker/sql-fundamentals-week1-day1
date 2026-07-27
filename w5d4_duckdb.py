import duckdb
con = duckdb.connect()
file = "sales_100k.csv"
print("1. Total Sales")

result = con.execute(f"""
SELECT SUM(sales) AS total_sales
FROM read_csv_auto('{file}')
""").df()

print(result)
print("\n2. Average Sales")

result = con.execute(f"""
SELECT AVG(sales) AS average_sales
FROM read_csv_auto('{file}')
""").df()

print(result)
print("\n3. Product Wise Sales")

result = con.execute(f"""
SELECT 
    product,
    SUM(sales) AS total_sales
FROM read_csv_auto('{file}')
GROUP BY product
ORDER BY total_sales DESC
""").df()

print(result)
print("\n4. Top Customers")

result = con.execute(f"""
SELECT
    customer_id,
    SUM(sales) AS revenue
FROM read_csv_auto('{file}')
GROUP BY customer_id
ORDER BY revenue DESC
LIMIT 10
""").df()

print(result)
print("\n5. Quantity Analysis")

result = con.execute(f"""
SELECT
    MAX(quantity) AS max_quantity,
    MIN(quantity) AS min_quantity,
    AVG(quantity) AS avg_quantity
FROM read_csv_auto('{file}')
""").df()

print(result)
