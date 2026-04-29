E-commerce Sales & Customer Analytics with Churn Prediction
📌 Project Overview
This project involves building a Customer Intelligence System using a dataset of ~100K orders from the Olist E-commerce marketplace. The goal was to transform raw transactional data into actionable business insights using RFM (Recency, Frequency, Monetary) Segmentation and Machine Learning to predict customer churn.

🛠️ Tech Stack
Data Engineering: SQL (Joins, Window Functions, Aggregations), Python (Pandas)

Machine Learning: Scikit-learn (Random Forest Classifier)

Visualization: Matplotlib, Seaborn, Power BI

Environment: VS Code, .pyenv (Python 3.10.13)

📂 Project Structure
preprocessing.py: Cleans raw datasets and engineers the order-level master file.

rfm_segmentation.py: Performs RFM analysis and categorizes 95K+ unique customers.

model_training.py: Trains a Random Forest model to flag at-risk users.

export_for_bi.py: Generates the final unified dataset for Power BI.

sql_queries.sql: Contains SQL logic for complex data transformations.

📊 Key Results & Insights
1. Model Performance

The Churn Prediction model achieved an 82% Accuracy.

Recall for Churned Class (1): 0.91 – The model is highly effective at identifying customers who have already left.

Weighted F1-Score: 0.81 – Demonstrates a strong balance between precision and recall across the dataset.

2. Drivers of Churn (Feature Importance)

As shown in the analysis, Monetary Value is the primary driver of the model's predictions. This suggests that the total spend of a customer is more indicative of their retention probability than simple purchase frequency in this marketplace.

3. Customer Segmentation

Using RFM scoring, customers were categorized into:

Champions: High-value, frequent shoppers.

At Risk: Previously high-value customers who haven't purchased in >90 days.

Hibernating: Low-frequency, low-spend customers.

💡 Business Recommendations
Value-Based Retention: Focus marketing budget on "At Risk" segments with high Monetary scores, as they represent the greatest potential recovered revenue.

Loyalty Programs: Since Frequency was a lower predictor of retention, implementing a tiered loyalty program could encourage second and third purchases to stabilize the customer base.

Geographic Optimization: Use the Power BI dashboard to identify states with higher-than-average churn rates to investigate delivery or logistics delays in those regions.

🚀 How to Run
Clone the repository:

Bash
git clone https://github.com/naitripanchal/E-commerce-Sales-Customer-Analytics-with-Churn-Prediction
Install dependencies:

Bash
pip install -r requirements.txt
Execute the pipeline:

Bash
python preprocessing.py
python rfm_segmentation.py
python model_training.py
Visualize: Open the power_bi_final.csv in Power BI to view the interactive dashboard.