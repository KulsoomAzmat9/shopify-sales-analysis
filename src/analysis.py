import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('data/shopify_orders.csv')
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
os.makedirs('charts', exist_ok=True)

total_sales = df[df['Order_Status']=='Delivered']['Total_Amount'].sum()
total_orders = len(df[df['Order_Status']=='Delivered'])
avg_order = total_sales / total_orders if total_orders else 0

print(f"Total Sales: Rs {total_sales}")
print(f"Delivered Orders: {total_orders}")
print(f"Average Order Value: Rs {avg_order:.2f}")

df_delivered = df[df['Order_Status']=='Delivered'].copy()
df_delivered['Month'] = df_delivered['Order_Date'].dt.to_period('M').astype(str)
monthly = df_delivered.groupby('Month')['Total_Amount'].sum()

plt.figure(figsize=(8,4))
monthly.plot(kind='bar')
plt.title('Monthly Sales - Shopify Store')
plt.xlabel('Month')
plt.ylabel('Total Sales (Rs)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/monthly_sales.png')
plt.close()

top_products = df_delivered.groupby('Product_Name')['Quantity'].sum().sort_values(ascending=False)
plt.figure(figsize=(8,4))
top_products.plot(kind='bar', color='orange')
plt.title('Top Selling Products')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('charts/top_products.png')
plt.close()

payment = df_delivered['Payment_Method'].value_counts()
plt.figure(figsize=(6,4))
payment.plot(kind='pie', autopct='%1.1f%%')
plt.title('Payment Methods')
plt.ylabel('')
plt.tight_layout()
plt.savefig('charts/payment_method.png')
plt.close()

print("Charts saved in charts/ folder")