import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def train_churn_model():
    df = pd.read_csv('/Users/naitripanchal/E-commerce Sales & Customer Analytics with Churn Prediction /segmented_customers.csv')

    # We use Frequency and Monetary to predict Churn
    # We exclude Recency because Churn is defined by it (to avoid data leakage)
    X = df[['Frequency', 'Monetary']]
    y = df['Churn']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 1. Check Performance
    y_pred = model.predict(X_test)
    print("\n--- Model Performance ---")
    print(classification_report(y_test, y_pred))

    # 2. Visualizing Feature Importance
    importances = model.feature_importances_
    features = X.columns
    sns.barplot(x=importances, y=features)
    plt.title('Drivers of Customer Churn')
    plt.savefig('feature_importance.png')
    
    print("Model training complete. Feature importance saved as 'feature_importance.png'")

if __name__ == "__main__":
    train_churn_model()