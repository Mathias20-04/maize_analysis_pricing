#!/usr/bin/env python3
"""
Data Visualization Script
Creates plots and charts for the analysis
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
    plt.rcParams['figure.figsize'] = (8, 5)
    np.random.seed(42)
    
    # Load processed dataset
    df = pd.read_csv('data/processed/maize_data_validated.csv')

    print("1. Generating visualizations...")

    # Figure 1: Price distribution by district
    plt.figure()
    sns.boxplot(data=df, x='District', y='Price_MWK_kg')
    plt.title('Maize Price Distribution by District')
    plt.ylabel('Price (MWK/kg)')
    plt.tight_layout()
    plt.savefig('results/figures/price_by_district.png', dpi=300)
    plt.close()

    # Figure 2: Average price by storage method
    plt.figure()
    sns.barplot(data=df, x='Storage_Method', y='Price_MWK_kg', estimator=np.mean, ci="sd")
    plt.title('Average Maize Price by Storage Method')
    plt.ylabel('Average Price (MWK/kg)')
    plt.tight_layout()
    plt.savefig('results/figures/price_by_storage.png', dpi=300)
    plt.close()

      # Figure 3: Scatter plot (farm size vs price)
    plt.figure(figsize=(8, 5))
    df_sample = df.sample(n=1000) if len(df) > 1000 else df
    sns.scatterplot(data=df_sample, x='Farm_Size_acres', y='Price_MWK_kg', hue='Buyer_Type')
    plt.title('Relationship Between Farm Size and Maize Price')
    plt.xlabel('Farm Size (acres)')
    plt.ylabel('Price (MWK/kg)')
    plt.tight_layout()
    plt.savefig('results/figures/price_vs_farm_size.png', dpi=150)
    plt.close()

    # Figure 4: Transport access effect
    plt.figure()
    sns.boxplot(data=df, x='Transport_Access', y='Price_MWK_kg', order=['Poor', 'Average', 'Good'])
    plt.title('Price Variation by Transport Access Quality')
    plt.ylabel('Price (MWK/kg)')
    plt.tight_layout()
    plt.savefig('results/figures/price_by_transport.png', dpi=300)
    plt.close()

    print("2. Visualizations saved to: results/figures/")

if __name__ == "__main__":
    generate_visuals()
