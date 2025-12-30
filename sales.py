# Import pandas library
import pandas as pd

# -------------------------------
# Step 1: Load the dataset
# -------------------------------
df = pd.read_csv("sales_data.csv")

# Display the dataset
print("Original Dataset:")
print(df)

# -------------------------------
# Step 2: Explore the data
# -------------------------------
print("\nDataset Info:")
print(df.info())

# -------------------------------
# Step 3: Handle missing values
# -------------------------------

# Fill missing Quantity with 0
df["Quantity"] = df["Quantity"].fillna(0)

# Fill missing Price with average price
df["Price"] = df["Price"].fillna(df["Price"].mean())

# -------------------------------
# Step 4: Create new column - Revenue
# -------------------------------
df["Revenue"] = df["Quantity"] * df["Price"]

# -------------------------------
# Step 5: Calculate Metrics
# -------------------------------

# Metric 1: Total Revenue
total_revenue = df["Revenue"].sum()

# Metric 2: Total Quantity Sold
total_quantity = df["Quantity"].sum()

# Metric 3: Best Selling Product
best_product = df.groupby("Product")["Revenue"].sum().idxmax()

# -------------------------------
# Step 6: Generate Report
# -------------------------------
print("\n📊 SALES REPORT")
print("------------------------")
print(f"Total Revenue: ₹{total_revenue:.2f}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Best Selling Product: {best_product}")

print("\nFinal Cleaned Dataset:")
print(df)
