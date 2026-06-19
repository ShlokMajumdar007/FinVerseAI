import pandas as pd
import numpy as np
from datetime import timedelta, date
import random
import os

def generate_transactions(num_records=5000):
    np.random.seed(42)
    random.seed(42)

    categories = ['Food', 'Shopping', 'Travel', 'Entertainment', 'Utilities', 'Rent', 'Other']
    merchants = {
        'Food': ['Zomato', 'Swiggy', 'Starbucks', 'McDonalds', 'Local Grocery', 'Supermart'],
        'Shopping': ['Amazon', 'Flipkart', 'Zara', 'Apple Store', 'H&M', 'Myntra'],
        'Travel': ['Uber', 'Ola', 'IRCTC', 'MakeMyTrip', 'Indigo Airlines', 'Petrol Pump'],
        'Entertainment': ['Netflix', 'Spotify', 'PVR Cinemas', 'Steam', 'BookMyShow'],
        'Utilities': ['Electricity Board', 'Water Bill', 'Jio Fiber', 'Airtel'],
        'Rent': ['Landlord', 'Society Maintenance'],
        'Other': ['Pharmacy', 'Misc', 'Hardware Store']
    }

    start_date = date(2025, 1, 1)
    end_date = date(2026, 6, 1)
    days_between = (end_date - start_date).days

    data = []
    
    for _ in range(num_records):
        # Pick a random date
        random_number_of_days = random.randrange(days_between)
        txn_date = start_date + timedelta(days=random_number_of_days)
        
        category = random.choices(
            categories, 
            weights=[0.3, 0.2, 0.15, 0.1, 0.1, 0.05, 0.1], 
            k=1
        )[0]
        
        merchant = random.choice(merchants[category])
        
        # Base amounts
        if category == 'Rent':
            base_amount = 30000
            variance = 0
        elif category == 'Utilities':
            base_amount = 2000
            variance = 500
        elif category == 'Food':
            base_amount = 500
            variance = 400
        elif category == 'Shopping':
            base_amount = 3000
            variance = 2500
        elif category == 'Travel':
            base_amount = 800
            variance = 700
        else:
            base_amount = 1000
            variance = 800

        amount = max(50, np.random.normal(base_amount, variance))
        
        # Introduce anomalies
        is_anomaly = 0
        if random.random() < 0.02: # 2% chance of being an anomaly (e.g., buying a Macbook)
            amount = amount * random.uniform(5, 15)
            is_anomaly = 1
            
        data.append({
            'date': txn_date.strftime("%Y-%m-%d"),
            'merchant': merchant,
            'category': category,
            'amount': round(amount, 2),
            'is_anomaly': is_anomaly
        })

    df = pd.DataFrame(data)
    df = df.sort_values(by='date')
    
    os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'transactions.csv')
    df.to_csv(output_path, index=False)
    print(f"Generated {num_records} transactions and saved to {output_path}")

if __name__ == '__main__':
    generate_transactions(5000)
