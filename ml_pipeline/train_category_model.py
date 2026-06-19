import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import joblib
import os

def train_category_model():
    dataset_path = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'transactions.csv')
    
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset not found at {dataset_path}")
        return

    print("Loading data...")
    df = pd.read_csv(dataset_path)

    # We will predict 'category' based on the 'merchant' string
    X = df['merchant']
    y = df['category']

    print("Training Random Forest Categorization model with TF-IDF...")
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(lowercase=True)),
        ('clf', RandomForestClassifier(n_estimators=50, random_state=42))
    ])

    pipeline.fit(X, y)

    # Save the pipeline (includes vectorizer and model)
    models_dir = os.path.join(os.path.dirname(__file__), '..', 'backend', 'models')
    os.makedirs(models_dir, exist_ok=True)
    model_path = os.path.join(models_dir, 'category_model.pkl')
    
    joblib.dump(pipeline, model_path)
    print(f"Categorization pipeline successfully saved to {model_path}")

if __name__ == '__main__':
    train_category_model()
