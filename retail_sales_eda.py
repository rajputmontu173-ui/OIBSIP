import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# OASIS INFOBYTE - DATA ANALYTICS TASK 1
# Exploratory Data Analysis on Retail Sales
# ==========================================


# 1. LOAD DATASET
df = pd.read_csv("retail_sales_dataset.csv")

print("\n========== DATASET OVERVIEW ==========")

print("Shape of Dataset:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())


# ==========================================
# 2. DESCRIPTIVE STATISTICS
# ==========================================

print("\n========== DESCRIPTIVE STATISTICS ==========")

print(df.describe())


# ==========================================
# 3. DATA PREPARATION
# ==========================================

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.to_period("M").astype(str)

df["Quarter"] = df["Date"].dt.to_period("Q").astype(str)


# ==========================================
# 4. BASIC SALES INFORMATION
# ==========================================

total_sales = df["Total_Sales"].sum()

total_transactions = len(df)

total_quantity = df["Quantity"].sum()

average_transaction = df["Total_Sales"].mean()

unique_customers = df["Customer_ID"].nunique()


print("\n========== SALES SUMMARY ==========")

print("Total Sales:", round(total_sales, 2))

print("Total Transactions:", total_transactions)

print("Total Quantity Sold:", total_quantity)

print("Average Transaction Value:",
      round(average_transaction, 2))

print("Unique Customers:", unique_customers)


# ==========================================
# 5. MONTHLY SALES TREND
# ==========================================

monthly_sales = (
    df.groupby("Month")["Total_Sales"]
    .sum()
    .reset_index()
)


print("\n========== MONTHLY SALES ==========")

print(monthly_sales)


plt.figure(figsize=(12, 5))

sns.lineplot(
    data=monthly_sales,
    x="Month",
    y="Total_Sales",
    marker="o"
)

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# ==========================================
# 6. QUARTERLY SALES TREND
# ==========================================

quarterly_sales = (
    df.groupby("Quarter")["Total_Sales"]
    .sum()
    .reset_index()
)


print("\n========== QUARTERLY SALES ==========")

print(quarterly_sales)


plt.figure(figsize=(8, 5))

sns.barplot(
    data=quarterly_sales,
    x="Quarter",
    y="Total_Sales"
)

plt.title("Quarterly Sales")

plt.xlabel("Quarter")

plt.ylabel("Total Sales")

plt.tight_layout()

plt.show()


# ==========================================
# 7. CUSTOMER DEMOGRAPHICS
# ==========================================

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Age",
    bins=12,
    kde=True
)

plt.title("Customer Age Distribution")

plt.xlabel("Age")

plt.ylabel("Number of Customers")

plt.tight_layout()

plt.show()


# ==========================================
# 8. GENDER DISTRIBUTION
# ==========================================

plt.figure(figsize=(6, 5))

sns.countplot(
    data=df,
    x="Gender"
)

plt.title("Customer Gender Distribution")

plt.xlabel("Gender")

plt.ylabel("Number of Customers")

plt.tight_layout()

plt.show()


# ==========================================
# 9. TOP PRODUCTS
# ==========================================

top_products = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)


print("\n========== TOP 10 PRODUCTS ==========")

print(top_products)


plt.figure(figsize=(10, 6))

sns.barplot(
    data=top_products,
    x="Total_Sales",
    y="Product"
)

plt.title("Top 10 Products by Revenue")

plt.xlabel("Total Sales")

plt.ylabel("Product")

plt.tight_layout()

plt.show()


# ==========================================
# 10. CATEGORY REVENUE
# ==========================================

category_sales = (
    df.groupby("Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)


print("\n========== CATEGORY REVENUE ==========")

print(category_sales)


plt.figure(figsize=(9, 5))

sns.barplot(
    data=category_sales,
    x="Category",
    y="Total_Sales"
)

plt.title("Revenue by Product Category")

plt.xlabel("Category")

plt.ylabel("Total Sales")

plt.xticks(rotation=20)

plt.tight_layout()

plt.show()


# ==========================================
# 11. CORRELATION HEATMAP
# ==========================================

correlation_columns = [
    "Price_Per_Unit",
    "Quantity",
    "Total_Sales",
    "Age"
]


correlation = df[correlation_columns].corr()


plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.show()


# ==========================================
# 12. EXTRA VISUALIZATION
# SALES CHANNEL
# ==========================================

channel_sales = (
    df.groupby("Channel")["Total_Sales"]
    .sum()
    .reset_index()
)


print("\n========== SALES BY CHANNEL ==========")

print(channel_sales)


plt.figure(figsize=(7, 5))

sns.barplot(
    data=channel_sales,
    x="Channel",
    y="Total_Sales"
)

plt.title("Sales by Sales Channel")

plt.xlabel("Channel")

plt.ylabel("Total Sales")

plt.tight_layout()

plt.show()


# ==========================================
# 13. BUSINESS INSIGHTS
# ==========================================

best_product = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .idxmax()
)


best_category = (
    df.groupby("Category")["Total_Sales"]
    .sum()
    .idxmax()
)


best_month = (
    df.groupby("Month")["Total_Sales"]
    .sum()
    .idxmax()
)


best_channel = (
    df.groupby("Channel")["Total_Sales"]
    .sum()
    .idxmax()
)


print("\n========== BUSINESS INSIGHTS ==========")

print("Highest Selling Product:", best_product)

print("Highest Revenue Category:", best_category)

print("Highest Revenue Month:", best_month)

print("Best Sales Channel:", best_channel)


# ==========================================
# 14. ACTIONABLE RECOMMENDATIONS
# ==========================================

print("\n========== RECOMMENDATIONS ==========")

print(
    "1. Increase inventory for high-performing "
    "product categories."
)

print(
    "2. Run special offers and marketing campaigns "
    "during high-sales months."
)

print(
    "3. Focus promotions on the stronger sales "
    "channel and high-performing products."
)


print("\n========== TASK 1 COMPLETED ==========")