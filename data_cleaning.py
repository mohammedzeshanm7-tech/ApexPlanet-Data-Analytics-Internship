# Task - Data Cleaning & Transformation
# ApexPlanet Data Analytics Internship

import pandas as pd

# Step 1: Load the raw data
file_path = r"C:\Users\Mohammed Zeshan\Desktop\Step 1\ApexPlanet_DataAnalytics_Dataset.xlsx"
df = pd.read_excel(file_path)

print("Number of rows and columns:")
print(df.shape)

print("Missing values before cleaning:")
print(df.isnull().sum())


# Step 2: Fix missing values
# Calculate the median age first
median_age = df["Age"].median()
print("Median age is:", median_age)

# Fill the missing Age cells with the median age
df["Age"] = df["Age"].fillna(median_age)

# Fill missing City cells with the word "Unknown"
df["City"] = df["City"].fillna("Unknown")


# Step 3: Fix the duplicate Order_ID problem
# Check how many duplicate Order_IDs exist before fixing
duplicate_count = df["Order_ID"].duplicated().sum()
print("Duplicate Order_IDs found:", duplicate_count)

# Reset the row numbers so they go 0, 1, 2, 3... in order
df = df.reset_index(drop=True)

# Create a new list of unique Order_IDs, one for each row
new_order_ids = []
for i in range(len(df)):
    new_id = "ORD" + str(100000 + i)
    new_order_ids.append(new_id)

# Replace the old Order_ID column with the new unique IDs
df["Order_ID"] = new_order_ids


# Step 4: Fix the date format
# Convert Order_Date from text into a real date type
df["Order_Date"] = pd.to_datetime(df["Order_Date"], format="%Y-%m-%d")


# Step 5: Cleaning up text columns
text_columns = ["City", "Gender", "Product", "Category"]

for column in text_columns:
    df[column] = df[column].astype(str)
    df[column] = df[column].str.strip()
    df[column] = df[column].str.title()


# Step 6: Adding a few new useful columns
age_bins = [0, 25, 35, 45, 55, 100]
age_labels = ["18-25", "26-35", "36-45", "46-55", "56+"]

df["Age_Group"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels)


#Create Order_Month and Order_Year columns
df["Order_Month"] = df["Order_Date"].dt.month_name()
df["Order_Year"] = df["Order_Date"].dt.year


# Step 7: Check that Total_Sal"Order_Month"es is correct
# Total_Sales should equal Quantity multiplied by Unit_Price
calculated_sales = df["Quantity"] * df["Unit_Price"]
calculated_sales = calculated_sales.round(2)

actual_sales = df["Total_Sales"].round(2)

mismatch_count = (calculated_sales != actual_sales).sum()
print("Number of Total_Sales mismatches:", mismatch_count)


# Step 8: Final check before saving
print("Missing values after cleaning:")
print(df.isnull().sum())

print("Final number of rows and columns:")
print(df.shape)


# Step 9: Save the cleaned file
output_path = r"C:\Users\Mohammed Zeshan\Desktop\Step 1\Cleaned_Sales_Dataset.csv"
df.to_csv(output_path, index=False)

print("Cleaned dataset saved as Cleaned_Sales_Dataset.csv")
