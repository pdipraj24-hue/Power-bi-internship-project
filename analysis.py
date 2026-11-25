import pandas as pd
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
print("Total Sales:", df["Total_Sales"].sum())
print(df.groupby("Region")["Total_Sales"].sum())
print(df.groupby("Category")["Total_Sales"].sum())
print(df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False).head(5))
