import pandas as pd

df = pd.read_csv("startup_funding.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())
print("\nMissing Values")
print(df.isnull().sum())
print("\nStatistical Summary")
print(df.describe(include="all"))
print("\nTop Startup Names")
print(df["Startup Name"].value_counts().head(10))
print(df.columns)
print("\nTop Cities")
print(df["City  Location"].value_counts().head(10))
print("\nTop Industries")
print(df["Industry Vertical"].value_counts().head(10))
df["Amount in USD"] = (
    df["Amount in USD"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

df["Amount in USD"] = pd.to_numeric(
    df["Amount in USD"],
    errors="coerce"
)

print("\nTop 10 Highest Funded Startups")
print(
    df.sort_values(
        by="Amount in USD",
        ascending=False
    )[["Startup Name", "Amount in USD"]].head(10)
)
import matplotlib.pyplot as plt

# Top 10 Cities
plt.figure(figsize=(8,5))
df["City  Location"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Startup Cities")
plt.xlabel("City")
plt.ylabel("Number of Startups")
plt.tight_layout()
plt.show()

# Top 10 Industries
plt.figure(figsize=(8,5))
df["Industry Vertical"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Industries")
plt.xlabel("Industry")
plt.ylabel("Count")
plt.tight_layout()
plt.show()