import pandas as pd
import numpy as np

np.random.seed(42)

products = [
    "Laptop", "Smartphone", "Headphones", "Tablet", "Smartwatch",
    "T-Shirt", "Jeans", "Jacket", "Sneakers", "Hoodie",
    "Coffee Maker", "Mixer", "Air Fryer",
    "Face Wash", "Perfume",
    "Cricket Bat", "Football", "Yoga Mat",
    "Running Shoes", "Badminton Racket"
]

categories = [
    "Electronics", "Electronics", "Electronics", "Electronics", "Electronics",
    "Clothing", "Clothing", "Clothing", "Clothing", "Clothing",
    "Home & Kitchen", "Home & Kitchen", "Home & Kitchen",
    "Beauty", "Beauty",
    "Sports", "Sports", "Sports", "Sports", "Sports"
]

price_ranges = {
    "Electronics": (800, 90000),
    "Clothing": (400, 6000),
    "Home & Kitchen": (500, 12000),
    "Beauty": (200, 5000),
    "Sports": (400, 10000)
}

data = []

for i in range(1500):

    product_index = np.random.randint(0, len(products))

    product = products[product_index]
    category = categories[product_index]

    price = np.random.randint(
        price_ranges[category][0],
        price_ranges[category][1]
    )

    quantity = np.random.randint(1, 6)

    total_sales = price * quantity

    date = pd.Timestamp("2025-01-01") + pd.Timedelta(
        days=np.random.randint(0, 365)
    )

    age = np.random.randint(18, 70)

    gender = np.random.choice(["Male", "Female"])

    channel = np.random.choice(["Online", "Store"])

    payment = np.random.choice(
        ["UPI", "Credit Card", "Debit Card", "Cash"]
    )

    customer_id = "C" + str(
        np.random.randint(1001, 1251)
    )

    data.append([
        "T" + str(i + 1),
        customer_id,
        product,
        category,
        price,
        quantity,
        total_sales,
        date,
        age,
        gender,
        channel,
        payment
    ])


columns = [
    "Transaction_ID",
    "Customer_ID",
    "Product",
    "Category",
    "Price_Per_Unit",
    "Quantity",
    "Total_Sales",
    "Date",
    "Age",
    "Gender",
    "Channel",
    "Payment_Method"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("retail_sales_dataset.csv", index=False)

print("Dataset successfully created!")
print("Total rows:", len(df))
print(df.head())