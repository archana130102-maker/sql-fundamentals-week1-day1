import pandas as pd
import random

data = {
    "order_id": range(1,100001),
    "customer_id": [random.randint(1,5000) for _ in range(100000)],
    "product": [random.choice(["Laptop","Mobile","Tablet","Watch"]) for _ in range(100000)],
    "quantity": [random.randint(1,10) for _ in range(100000)],
    "price": [random.randint(500,50000) for _ in range(100000)]
}

df = pd.DataFrame(data)

df["sales"] = df["quantity"] * df["price"]

df.to_csv("sales_100k.csv", index=False)

print("Dataset created successfully")