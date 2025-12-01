#!/usr/bin/env python3
"""
Data Validation Script
Validates and cleans the Farmer Survey dataset
"""

import pandas as pd
import numpy as np

def validate_data():
    print("=== DATA VALIDATION SCRIPT ===")
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Load data
    df = pd.read_csv('data/raw/farmers_survey.csv') # <-- CHANGED FILENAME
    print(f"Original data shape: {df.shape}")
    
    # Basic validation
    print("\n1. BASIC DATA CHECK:")
    print(f"Missing values:\n{df.isnull().sum()}")
    print(f"Data types:\n{df.dtypes}")
    
    # Data Cleaning & Renaming for key columns
    print("\n2. DATA CLEANING & FEATURE ENGINEERING:")
    
    # Rename key columns for easier handling
    column_mapping = {
        '11. What is the average price when you sell locally?': 'local_price',
        '12. City price': 'city_price', 
        '14. Do you transport to city markets?': 'transports_to_city',
        '15. Transport cost': 'transport_cost',
        '16. Challenges': 'challenges',
        '17. Do you own a mobile phone?': 'phone_ownership',
        '20. Would you use a mobile app?': 'use_app_willingness',
        '22. Solutions preferred': 'preferred_solutions',
        '3. In which district do you live?': 'district'
    }
    df.rename(columns=column_mapping, inplace=True)
    
    # Create a new calculated column: Potential Price Gain
    # First, ensure we have numeric values (handle missing city prices)
    df['local_price'] = pd.to_numeric(df['local_price'], errors='coerce')
    df['city_price'] = pd.to_numeric(df['city_price'], errors='coerce')
    df['price_difference'] = df['city_price'] - df['local_price']
    
    # Convert transport cost to numeric
    df['transport_cost'] = pd.to_numeric(df['transport_cost'], errors='coerce')
    
    # Create a simple profit potential metric (Price Gain - Transport Cost)
    df['profit_potential'] = df['price_difference'] - df['transport_cost']
    
    # Data quality checks
    print("\n3. DATA QUALITY CHECKS:")
    print(f"Local price range: {df['local_price'].min():.2f} - {df['local_price'].max():.2f} MWK")
    print(f"City price range: {df['city_price'].min():.2f} - {df['city_price'].max():.2f} MWK")
    print(f"Price difference range: {df['price_difference'].min():.2f} - {df['price_difference'].max():.2f} MWK")
    print(f"Transport cost range: {df['transport_cost'].min():.2f} - {df['transport_cost'].max():.2f} MWK")
    
    # Check for duplicates
    duplicates = df.duplicated().sum()
    print(f"Duplicate rows: {duplicates}")
    
    # Save validated data
    df.to_csv('data/processed/survey_data_validated.csv', index=False) # <-- CHANGED FILENAME
    print("\n4. VALIDATED DATA SAVED: 'data/processed/survey_data_validated.csv'")

    return df

if __name__ == "__main__":
    df = validate_data()