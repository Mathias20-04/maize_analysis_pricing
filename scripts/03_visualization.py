#!/usr/bin/env python3
"""
Data Visualization Script
Creates plots and charts for the Farmer Survey analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def generate_visuals():
    print("=== DATA VISUALIZATION SCRIPT ===")
    
    # Ensure output folder exists
    os.makedirs('results/figures', exist_ok=True)

    # Set style
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (10, 6)
    np.random.seed(42)
    
    # Load processed dataset
    df = pd.read_csv('data/processed/survey_data_validated.csv')

    print("1. Generating visualizations for Farmer Survey Analysis...")

    # Figure 1: Local vs City Price Distribution by District
    plt.figure(figsize=(12, 6))
    
    # Prepare data for plotting (melt to long format)
    price_data = df[['district', 'local_price', 'city_price']].melt(
        id_vars=['district'], 
        value_vars=['local_price', 'city_price'],
        var_name='price_type', 
        value_name='price'
    )
    price_data['price_type'] = price_data['price_type'].replace({
        'local_price': 'Local Price', 
        'city_price': 'City Price'
    })
    
    # Filter out districts with very few data points for better visualization
    district_counts = df['district'].value_counts()
    main_districts = district_counts[district_counts >= 5].index
    price_data_filtered = price_data[price_data['district'].isin(main_districts)]
    
    sns.boxplot(data=price_data_filtered, x='district', y='price', hue='price_type')
    plt.title('Local vs City Price Distribution by District')
    plt.ylabel('Price (MWK)')
    plt.xlabel('District')
    plt.xticks(rotation=45)
    plt.legend(title='Price Type')
    plt.tight_layout()
    plt.savefig('results/figures/price_comparison_by_district.png', dpi=150, bbox_inches='tight')
    plt.close()

    # Figure 2: Price Difference by Transport Behavior
    plt.figure()
    # Filter out rows where transport behavior or price difference is missing
    plot_data = df[['transports_to_city', 'price_difference']].dropna()
    sns.boxplot(data=plot_data, x='transports_to_city', y='price_difference')
    plt.title('Price Difference by Transport to City Markets')
    plt.ylabel('Price Difference (City - Local) MWK')
    plt.xlabel('Transports to City Markets')
    plt.tight_layout()
    plt.savefig('results/figures/price_difference_by_transport.png', dpi=150)
    plt.close()

    # Figure 3: Willingness to Use App by Phone Ownership
    plt.figure()
    # Create cross-tabulation for plotting
    app_data = pd.crosstab(df['phone_ownership'], df['use_app_willingness'], normalize='index') * 100
    app_data.plot(kind='bar', stacked=True)
    plt.title('Willingness to Use Mobile App by Phone Ownership')
    plt.ylabel('Percentage (%)')
    plt.xlabel('Phone Ownership')
    plt.legend(title='Would Use App?', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('results/figures/app_willingness_by_phone.png', dpi=150, bbox_inches='tight')
    plt.close()

    # Figure 4: Most Common Challenges (Top 10)
    plt.figure(figsize=(10, 6))
    # Calculate challenge frequencies directly from the data
    all_challenges = df['challenges'].str.split(', ').explode()
    challenge_counts = all_challenges.value_counts().head(10)
    
    if len(challenge_counts) > 0:
        sns.barplot(x=challenge_counts.values, y=challenge_counts.index)
        plt.title('Top 10 Most Common Challenges Faced by Farmers')
        plt.xlabel('Frequency')
        plt.tight_layout()
        plt.savefig('results/figures/top_challenges.png', dpi=150)
        plt.close()
    else:
        print("Warning: No challenge data available for plotting.")

    # Figure 5: Most Preferred Solutions (Top 10)
    plt.figure(figsize=(10, 6))
    # Calculate solution preferences directly from the data
    all_solutions = df['preferred_solutions'].str.split(', ').explode()
    solution_counts = all_solutions.value_counts().head(10)
    
    if len(solution_counts) > 0:
        sns.barplot(x=solution_counts.values, y=solution_counts.index)
        plt.title('Top 10 Most Preferred Solutions by Farmers')
        plt.xlabel('Frequency')
        plt.tight_layout()
        plt.savefig('results/figures/top_solutions.png', dpi=150)
        plt.close()
    else:
        print("Warning: No solution data available for plotting.")

    # Figure 6: Profit Potential vs Transport Cost
    plt.figure()
    # Filter out rows with missing values
    scatter_data = df[['transport_cost', 'profit_potential']].dropna()
    if len(scatter_data) > 0:
        sns.scatterplot(data=scatter_data, x='transport_cost', y='profit_potential')
        plt.axhline(y=0, color='red', linestyle='--', alpha=0.7, label='Break-even')
        plt.title('Profit Potential vs Transport Cost')
        plt.xlabel('Transport Cost (MWK)')
        plt.ylabel('Profit Potential (MWK)')
        plt.legend()
        plt.tight_layout()
        plt.savefig('results/figures/profit_vs_transport_cost.png', dpi=150)
        plt.close()
    else:
        print("Warning: Insufficient data for profit vs transport cost plot.")

    # Figure 7: Distribution of Price Differences
    plt.figure()
    price_diff_clean = df['price_difference'].dropna()
    if len(price_diff_clean) > 0:
        plt.hist(price_diff_clean, bins=20, alpha=0.7, edgecolor='black')
        plt.axvline(price_diff_clean.mean(), color='red', linestyle='--', label=f'Mean: {price_diff_clean.mean():.1f} MWK')
        plt.title('Distribution of Price Differences (City - Local)')
        plt.xlabel('Price Difference (MWK)')
        plt.ylabel('Frequency')
        plt.legend()
        plt.tight_layout()
        plt.savefig('results/figures/price_difference_distribution.png', dpi=150)
        plt.close()

    print("2. Visualizations saved to: results/figures/")

if __name__ == "__main__":
    generate_visuals()