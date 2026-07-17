import pandas as pd
import random
from datetime import datetime, timedelta
import os

random.seed(42)

products = {
    "Laptop": ("Electronics", 850, 1500),
    "Mouse": ("Accessories", 10, 40),
    "Keyboard": ("Accessories", 20, 100),
    "Monitor": ("Electronics", 150, 500),
    "Headphones": ("Electronics", 30, 200),
    "Smartphone": ("Electronics", 300, 1200),
    "Tablet": ("Electronics", 200, 900),
    "USB Cable": ("Accessories", 5, 20),
    "Power Bank": ("Accessories", 20, 80),
    "Printer": ("Electronics", 100, 350),
}

regions = ["North", "South", "East", "West"]
payment_methods = ["Credit Card", "Debit Card", "UPI", "Cash", "Net Banking"]
customers = [f"Customer_{i}" for i in range(1, 301)]

start_date = datetime(2023, 1, 1)

rows = []

for order_id in range(1001, 2001):  # 1000 rows
    product = random.choice(list(products.keys()))
    category, min_price, max_price = products[product]

    quantity = random.randint(1, 5)
    price = round(random.uniform(min_price, max_price), 2)
    sales = round(price * quantity, 2)

    region = random.choice(regions)
    payment = random.choice(payment_methods)
    customer = random.choice(customers)

    order_date = (
        start_date + timedelta(days=random.randint(0, 730))
    ).strftime("%Y-%m-%d")

    rows.append([
        order_id,
        product,
        category,
        quantity,
        price,
        sales,
        region,
        payment,
        customer,
        order_date
    ])

df = pd.DataFrame(rows, columns=[
    "Order_ID",
    "Product",
    "Category",
    "Quantity",
    "Price",
    "Sales",
    "Region",
    "Payment_Method",
    "Customer",
    "Order_Date"
])

os.makedirs("dataset", exist_ok=True)

df.to_csv("dataset/amazon_sales.csv", index=False)

print("Dataset created successfully!")
print(df.head())
print("Shape:", df.shape)