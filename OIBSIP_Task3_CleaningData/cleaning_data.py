import pandas as pd
import numpy as np

df = pd.read_csv("messy_customer_data.csv")

print("Initial shape:", df.shape)
print("Nulls:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["Purchase_Amount"] = df["Purchase_Amount"].fillna(df["Purchase_Amount"].median())
df["Age"] = df["Age"].fillna(df["Age"].median())
df = df.dropna(subset=["Purchase_Date"]).drop_duplicates().copy()

df["Gender"] = (df["Gender"].astype(str).str.strip().str.lower()
                .replace({"m":"Male","male":"Male","f":"Female","female":"Female"}))
df["City"] = df["City"].astype(str).str.strip().str.title()

df["Customer_ID"] = df["Customer_ID"].astype("string")
df["Customer_Name"] = df["Customer_Name"].astype("string")
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"], errors="coerce")
df["Purchase_Amount"] = pd.to_numeric(df["Purchase_Amount"], errors="coerce")
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

median_age = df.loc[df["Age"].between(18,100), "Age"].median()
df.loc[~df["Age"].between(18,100), "Age"] = median_age

df.to_csv("cleaned_customer_data.csv", index=False)
print("Cleaning completed.")
print("Final shape:", df.shape)
