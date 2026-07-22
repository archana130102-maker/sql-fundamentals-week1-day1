# Week 2 — Day 3: EDA Workflow
# Day 3 | Week 2

import sys
print(f"Python {sys.version}")

def practice():

    sales = [120, 150, 170, 140, 200]

    print("Sales Data:", sales)
    print("\nDataset Profile")
    print("Total Records:", len(sales))
    print("Maximum Sale:", max(sales))
    print("Minimum Sale:", min(sales))
    print("Average Sale:", sum(sales) / len(sales))

    print("\nBusiness Insights")
    print("1. Highest sale is", max(sales))
    print("2. Lowest sale is", min(sales))
    print("3. Average sales are", sum(sales) / len(sales))
    print("4. Total records:", len(sales))
    print("5. Sales are increasing overall.")

practice()

print("\nDone! Review with CIA for feedback.")