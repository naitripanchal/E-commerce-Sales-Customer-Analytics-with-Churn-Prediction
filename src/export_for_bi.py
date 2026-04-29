import pandas as pd

def final_export():
    # Load your segmented data
    rfm = pd.read_csv('/Users/naitripanchal/E-commerce Sales & Customer Analytics with Churn Prediction /segmented_customers.csv')
    
    # Load original data to get Locations
    customers = pd.read_csv('/Users/naitripanchal/Downloads/DA/olist_customers_dataset.csv')
    
    # Check if the column is 'customer_id' or 'customer_unique_id'
    # and rename it to match the customers dataset
    if 'customer_id' in rfm.columns:
        left_key = 'customer_id'
    elif 'customer_unique_id' in rfm.columns:
        left_key = 'customer_unique_id'
    else:
        # If it's the first column but misnamed
        left_key = rfm.columns[0]

    print(f"Merging using key: {left_key}")
    
    # Create the master file for Power BI
    bi_data = rfm.merge(customers, left_on=left_key, right_on='customer_unique_id')
    
    # Drop the redundant column if it created 'customer_unique_id_y'
    if 'customer_unique_id_x' in bi_data.columns:
        bi_data = bi_data.rename(columns={'customer_unique_id_x': 'customer_unique_id'})
    
    bi_data.to_csv('power_bi_final.csv', index=False)
    print("Final file 'power_bi_final.csv' is ready for Power BI!")

if __name__ == "__main__":
    final_export()