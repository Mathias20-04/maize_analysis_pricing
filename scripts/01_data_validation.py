#!/usr/bin/env python3
#This is a Python script that checks if our farmer survey data is healthy and ready for analysis
"""
Data Validation Script
Validates and cleans the maize pricing dataset
"""

import pandas as pd
import numpy as np

def validate_data():
    print(".... DATA VALIDATION SCRIPT ...")
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Load data
    df = pd.read_csv('data/raw/maize_data_clean.csv')
    print(f"Original data shape: {df.shape}")
    
    # Basic validation
    print("\n1. BASIC DATA CHECK:")
    print(f"Missing values:\n{df.isnull().sum()}")
    print(f"Data types:\n{df.dtypes}")
    
    # Data quality checks
    print("\n2. DATA QUALITY CHECKS:")
    print(f"Price range: {df['Price_MWK_kg'].min()} - {df['Price_MWK_kg'].max()} MWK/kg")
    print(f"Farm size range: {df['Farm_Size_acres'].min()} - {df['Farm_Size_acres'].max()} acres")
    
    # Check for duplicates
    duplicates = df.duplicated().sum()
    print(f"Duplicate rows: {duplicates}")
    
    # Save validated data
    df.to_csv('data/processed/maize_data_validated.csv', index=False)
    print("\n3. DATA SAVED: 'data/processed/maize_data_validated.csv'")

    return df

if __name__ == "__main__":
    df = validate_data()