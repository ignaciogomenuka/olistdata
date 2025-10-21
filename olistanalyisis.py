# %%
# 🧠 Olist Data Analysis - Ignacio Muñoz Gomeñuka
# Dataset: https://wagon-public-datasets.s3.amazonaws.com/olist/olist.zip

# %%
# 📦 1. Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Config
pd.set_option('display.max_columns', None)
sns.set(style='whitegrid', palette='pastel', font_scale=1.1)

# %%
# 📂 2. Load datasets
path = "data/csv/"

orders = pd.read_csv(path + 'olist_orders_dataset.csv')
customers = pd.read_csv(path + 'olist_customers_dataset.csv')
order_items = pd.read_csv(path + 'olist_order_items_dataset.csv')
products = pd.read_csv(path + 'olist_products_dataset.csv')
payments = pd.read_csv(path + 'olist_order_payments_dataset.csv')
reviews = pd.read_csv(path + 'olist_order_reviews_dataset.csv')
sellers = pd.read_csv(path + 'olist_sellers_dataset.csv')

# %%
# 🔍 3. Quick EDA
print("Orders:", orders.shape)
print("Customers:", customers.shape)
print("Order items:", order_items.shape)
print("Products:", products.shape)

orders.head()

# %%
# 🧩 4. Merge base datasets
df = (orders
      .merge(order_items, on='order_id', how='left')
      .merge(customers, on='customer_id', how='left')
      .merge(payments, on='order_id', how='left')
      .merge(reviews, on='order_id', how='left')
      .merge(products, on='product_id', how='left')
      .merge(sellers, on='seller_id', how='left'))

df.shape

# %%
# 🧼 5. Data cleaning & feature engineering
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['delivery_time'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days

df = df[df['delivery_time'].notnull()]

# %%
# 📊 6. Basic descriptive analysis
print("Average delivery time:", df['delivery_time'].mean())
print("Average review score:", df['review_score'].mean())

# Distribution of delivery times
plt.figure(figsize=(8,5))
sns.histplot(df['delivery_time'], bins=30, kde=True)
plt.title('Delivery Time Distribution')
plt.show()

# %%
# ⭐ 7. Relationship between delivery time and review score
avg_review_by_delivery = df.groupby('delivery_time')['review_score'].mean().reset_index()

plt.figure(figsize=(8,5))
sns.lineplot(data=avg_review_by_delivery, x='delivery_time', y='review_score')
plt.title('Review Score vs Delivery Time')
plt.show()

# %%
# 💰 8. Revenue and order analysis
df['total_value'] = df['price'] + df['freight_value']

revenue_by_state = df.groupby('customer_state')['total_value'].sum().sort_values(ascending=False).head(10)
revenue_by_state.plot(kind='bar', figsize=(8,5), title='Top 10 States by Revenue')
plt.show()

# %%
# 🧠 9. Insights summary (print basic takeaways)
print("""
✅ Key Insights:
- Average delivery time: {:.1f} days
- Average review score: {:.2f}
- {}% of reviews are 4 or 5 stars
""".format(
    df['delivery_time'].mean(),
    df['review_score'].mean(),
    round((df['review_score'] >= 4).mean() * 100, 1)
))
