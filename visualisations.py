# ==========================================
# Week 2 - Day 1: Data Visualisation
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Apply Seaborn theme
sns.set_theme(style="whitegrid")

# Create sample dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [120, 150, 170, 140, 200]
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# ==========================================
# 1. Line Chart
# ==========================================
plt.figure(figsize=(6,4))
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("line_chart.png")
plt.show()

# ==========================================
# 2. Bar Chart
# ==========================================
plt.figure(figsize=(6,4))
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("bar_chart.png")
plt.show()

# ==========================================
# 3. Scatter Plot
# ==========================================
plt.figure(figsize=(6,4))
plt.scatter(df["Month"], df["Sales"])
plt.title("Monthly Sales - Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("scatter_plot.png")
plt.show()

# ==========================================
# 4. Histogram
# ==========================================
plt.figure(figsize=(6,4))
plt.hist(df["Sales"], bins=5)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()

# ==========================================
# 5. Box Plot
# ==========================================
plt.figure(figsize=(6,4))
plt.boxplot(df["Sales"])
plt.title("Sales Box Plot")
plt.ylabel("Sales")
plt.savefig("box_plot.png")
plt.show()

print("\nAll charts created successfully!")
print("PNG files saved:")
print("- line_chart.png")
print("- bar_chart.png")
print("- scatter_plot.png")
print("- histogram.png")
print("- box_plot.png")