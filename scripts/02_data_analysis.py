#!/usr/bin/env python3
"""
Data Analysis Script
Performs statistical analysis on the Farmer Survey data
"""

import pandas as pd
import numpy as np
from scipy import stats
import os

def analyze_data():
    print("=== DATA ANALYSIS SCRIPT ===")
    
    # Ensure output directory exists
    os.makedirs('results/tables', exist_ok=True)
    
    # Set random seed
    np.random.seed(42)
    
    # Load validated data
    df = pd.read_csv('data/processed/survey_data_validated.csv')
    
    print("1. DESCRIPTIVE STATISTICS FOR KEY VARIABLES:")
    key_columns = ['local_price', 'city_price', 'price_difference', 'transport_cost', 'profit_potential']
    print(df[key_columns].describe())
    
    print("\n2. PRICE ANALYSIS BY CATEGORICAL VARIABLES:")
    
    # Price by district
    district_analysis = df.groupby('district')[['local_price', 'city_price', 'price_difference']].agg(['mean', 'std', 'count'])
    print("\nPrice Analysis by District:")
    print(district_analysis)
    
    # Price difference by transport behavior
    transport_analysis = df.groupby('transports_to_city')['price_difference'].agg(['mean', 'std', 'count'])
    print("\nPrice Difference by Transport Behavior:")
    print(transport_analysis)
    
    # Willingness to use app by phone ownership
    app_willingness = pd.crosstab(df['phone_ownership'], df['use_app_willingness'], margins=True)
    print("\nApp Willingness by Phone Ownership:")
    print(app_willingness)
    
    print("\n3. STATISTICAL TESTS:")
    
    # T-test: Is the price difference statistically significant from zero?
    # Remove rows where we can't calculate price difference
    price_diff_clean = df['price_difference'].dropna()
    t_stat, p_value_ttest = stats.ttest_1samp(price_diff_clean, 0)
    print(f"\nT-test for Price Difference ≠ 0:")
    print(f"T-statistic: {t_stat:.4f}, P-value: {p_value_ttest:.4f}")
    print(f"Mean price difference: {price_diff_clean.mean():.2f} MWK")
    
    # ANOVA: Do prices differ significantly by district?
    districts_to_test = ['Lilongwe', 'Dedza', 'Blantyre','Mangochi','Mzimba','Nkhata-bay','Karonga']  # Focus on central region
    district_data = [df[df['district'] == dist]['local_price'].dropna() for dist in districts_to_test if dist in df['district'].values]
    
    if len(district_data) >= 2:  # Ensure we have at least 2 groups to compare
        f_stat, p_value_anova = stats.f_oneway(*district_data)
        print(f"\nANOVA - Price differences by district (Lilongwe, Dedza,Blantyre,Mzimba,Nkhata-bay,Karonga,Mangochi ):")
        print(f"F-statistic: {f_stat:.4f}, P-value: {p_value_anova:.4f}")
    
    # Correlation analysis
    print("\n4. CORRELATION ANALYSIS:")
    numeric_cols = ['local_price', 'city_price', 'price_difference', 'transport_cost', 'profit_potential']
    correlation_matrix = df[numeric_cols].corr()
    print(correlation_matrix)
    
    # Challenge frequency analysis
    print("\n5. CHALLENGE FREQUENCY ANALYSIS:")
    # Split the challenges column (which contains multiple challenges separated by commas)
    all_challenges = df['challenges'].str.split(', ').explode()
    challenge_counts = all_challenges.value_counts()
    print("Most common challenges faced:")
    print(challenge_counts.head(10))
    
    # Solution preference analysis
    print("\n6. SOLUTION PREFERENCE ANALYSIS:")
    all_solutions = df['preferred_solutions'].str.split(', ').explode()
    solution_counts = all_solutions.value_counts()
    print("Most preferred solutions:")
    print(solution_counts.head(10))
    
    # Save analysis results
    print("\n7. SAVING RESULTS...")
    district_analysis.to_csv('results/tables/price_analysis_by_district.csv')
    transport_analysis.to_csv('results/tables/price_by_transport_behavior.csv')
    correlation_matrix.to_csv('results/tables/correlation_matrix.csv')
    challenge_counts.to_csv('results/tables/challenge_frequency.csv')
    solution_counts.to_csv('results/tables/solution_preference.csv')
    
    # Save key statistical test results
    stats_results = pd.DataFrame({
        'test': ['One-sample t-test (Price Difference)'],
        'statistic': [t_stat],
        'p_value': [p_value_ttest],
        'interpretation': [
            'Price difference is statistically significant' if isinstance(p_value_ttest, float) and p_value_ttest < 0.05 else 'No significant price difference'
        ]
    })
    stats_results.to_csv('results/tables/statistical_tests.csv', index=False)
    
    print("ANALYSIS RESULTS SAVED to results/tables/")

    return df

if __name__ == "__main__":
    df = analyze_data()