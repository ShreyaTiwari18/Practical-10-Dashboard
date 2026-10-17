import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("cafe_sales.xlsx")
fig, ax = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle(f"Cafe Sales Dashboard  |  Total Revenue: Rs. {df['Revenue'].sum():,}")

df.groupby("Month", sort=False)["Revenue"].sum().plot(ax=ax[0, 0], marker="o", title="Monthly Revenue")
df.groupby("Category")["Revenue"].sum().plot.bar(ax=ax[0, 1], color="orange", title="Revenue by Category")
df.groupby("Item")["Quantity"].sum().nlargest(5).plot.barh(ax=ax[1, 0], color="green", title="Top 5 Items")
df["Payment"].value_counts().plot.pie(ax=ax[1, 1], autopct="%1.0f%%", title="Payment Mode")

plt.tight_layout()
plt.show()
