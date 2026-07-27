import polars as pl
import time


file = "sales_100k.csv"


# -------------------------
# Polars Analysis
# -------------------------

start_time = time.time()

# Load CSV using Polars
df = pl.read_csv(file)


# Product-wise total sales
result = (
    df
    .group_by("product")
    .agg(
        pl.col("sales").sum().alias("total_sales")
    )
    .sort("total_sales", descending=True)
)


polars_time = time.time() - start_time


print("===== Polars Result =====")
print(result)

print("\nPolars Execution Time:",
      polars_time,
      "seconds")