#!/usr/bin/env python3
"""
Data Analysis Script
Performs statistical analysis on maize pricing data
"""

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm


def analyze_data():
    print("=== DATA ANALYSIS SCRIPT ===")
    
    # Set random seed
    np.random.seed(42)
    
    # Load validated data
    df = pd.read_csv('data/processed/maize_data_validated.csv')
    
    print("1. DESCRIPTIVE STATISTICS:")
    print(df.describe())
    
    print("\n2. PRICE BY CATEGORICAL VARIABLES:")
    
    # Price by district
    district_prices = df.groupby('District')['Price_MWK_kg'].agg(['mean', 'std', 'count'])
    print("\nPrice by District:")
    print(district_prices)
    
    # Price by storage method
    storage_prices = df.groupby('Storage_Method')['Price_MWK_kg'].agg(['mean', 'std'])
    print("\nPrice by Storage Method:")
    print(storage_prices)
    
    # Price by transport access
    transport_prices = df.groupby('Transport_Access')['Price_MWK_kg'].agg(['mean', 'std'])
    print("\nPrice by Transport Access:")
    print(transport_prices)
    
    print("\n3. CORRELATION ANALYSIS:")
    numeric_cols = ['Farm_Size_acres', 'Fertilizer_Cost_MWK', 'Price_MWK_kg']
    correlation_matrix = df[numeric_cols].corr()
    print(correlation_matrix)
    
    # Save analysis results
    district_prices.to_csv('results/tables/price_by_district.csv')
    storage_prices.to_csv('results/tables/price_by_storage.csv')
    correlation_matrix.to_csv('results/tables/correlation_matrix.csv')

    print("\n4. ANALYSIS RESULTS SAVED to results/tables/")

    return df

if __name__ == "__main__":
    df = analyze_data()