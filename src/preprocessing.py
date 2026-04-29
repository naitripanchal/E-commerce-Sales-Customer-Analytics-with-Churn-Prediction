import pandas as pd
import numpy as np

def load_and_clean_data():
    # 1. Load the core datasets
    orders = pd.read_csv('/Users/naitripanchal/Downloads/DA/olist_orders_dataset.csv')
    customers = pd.read_csv('/Users/naitripanchal/Downloads/DA/olist_customers_dataset.csv')
    payments = pd.read_csv('/Users/naitripanchal/Downloads/DA/olist_order_payments_dataset.csv')
    items = pd.read_csv('/Users/naitripanchal/Downloads/DA/olist_order_items_dataset.csv')

    # 2. Advanced Cleaning (The "Clean Dataset" part of your resume)
    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
    # Fill missing delivery dates with estimated dates to keep the data row count high
    orders['order_delivered_customer_date'] = orders['order_delivered_customer_date'].fillna(orders['order_estimated_delivery_date'])

    # 3. Complex Merging (The "Customer Intelligence System" part)
    # Merging to create the order-level dataset
    df = orders.merge(customers, on='customer_id') \
               .merge(payments, on='order_id') \
               .merge(items, on='order_id')
    
    # Filter for valid business transactions
    df = df[df['order_status'] == 'delivered']
    
    # 4. Aggregation for RFM
    latest_date = df['order_purchase_timestamp'].max()
    
    rfm = df.groupby('customer_unique_id').agg({
        'order_purchase_timestamp': lambda x: (latest_date - x.max()).days,
        'order_id': 'nunique', # Use nunique to count unique orders
        'payment_value': 'sum'
    }).reset_index()

    rfm.columns = ['customer_unique_id', 'Recency', 'Frequency', 'Monetary']

    # 5. Feature Engineering: Segmentation & Churn
    # Churn definition
    rfm['Churn'] = (rfm['Recency'] > 90).astype(int)
    
    # Save the professional clean dataset for Power BI and Modeling
    rfm.to_csv('processed_rfm_data.csv', index=False)
    df.to_csv('clean_order_level_data.csv', index=False) # For Power BI
    
    print("Pre-processing complete. Created both Customer and Order level datasets.")

if __name__ == "__main__":
    load_and_clean_data()