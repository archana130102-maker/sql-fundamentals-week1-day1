import pandas as pd
import duckdb
import time


# CSV file path
file = "sales_100k.csv"


# -------------------------
# Pandas Analysis
# -------------------------

start_time = time.time()

# Load CSV using Pandas
df = pandas_df = pd.read_csv(file)

# Product-wise total sales
pandas_result = df.groupby("product")["sales"].sum()

# Calculate time
pandas_time = time.time() - start_time


print("===== Pandas Result =====")
print(pandas_result)

print("Pandas Execution Time:",
      pandas_time,
      "seconds")



# -------------------------
# DuckDB Analysis
# -------------------------

start_time = time.time()

# Connect DuckDB
con = duckdb.connect()

# SQL query
duckdb_result = con.execute(f"""
SELECT 
    product,
    SUM(sales) AS total_sales
FROM read_csv_auto('{file}')
GROUP BY product
ORDER BY total_sales DESC
""").df()


# Calculate time
duckdb_time = time.time() - start_time


print("\n===== DuckDB Result =====")
print(duckdb_result)

print("DuckDB Execution Time:",
      duckdb_time,
      "seconds")



# -------------------------
# Comparison
# -------------------------

print("\n===== Comparison =====")

if duckdb_time < pandas_time:
    print("DuckDB is faster")
else:
    print("Pandas is faster")