```bash
# Malawi Farmer Market Access Analysis

## Project Overview
This project analyzes market access barriers and digital solution preferences among smallholder farmers in Malawi using survey data from 200 farmers across 8 districts. The research investigates price disparities, transport challenges, and technology adoption readiness to inform rural development policies.


## Research Focus
 Market Access Barriers: Transport costs, infrastructure limitations, middlemen

 Economic Analysis: Price differentials between local and urban markets

Technology Adoption: Mobile app willingness and digital literacy

Policy Recommendations: Evidence-based solutions for rural development

## Key Findings
 Significant price differences (182.50 MWK average) between local and city markets

 Transport costs identified as primary barrier by 36% of farmers

 44% of farmers prefer mobile app solutions for market information

 Challenges are consistent across all districts (no significant regional variation)



## Outputs
After running the pipeline, check the results/ folder for:

results/tables/ - Statistical analysis and frequency tables

results/figures/ - Data visualizations and charts

## Dependencies
Python 3.10+

pandas, numpy, scipy, matplotlib, seaborn

See requirements.txt for complete list

# Reproducibility
```bash
This project follows reproducible research principles with:

Version-controlled code

Automated data processing pipeline

Clear documentation

Environment management

# Contact
```bash

Researcher: Group 3

Email: mphandemathias0@gmail.com

Repository: https://github.com/Mathias20-04/maize_analysis_pricing
### Prerequisites
- Python 3.10 or higher
- pip package manager

### Installation Steps
```bash
# Clone this repository
git clone https://github.com/Mathias20-04/maize_analysis_pricing.git
cd maize_analysis_pricing

# Create virtual environment (recommended)
python -m maize_env venv
source maize_env\scripts\activate  # On Windows: maize_env\scripts\activate
#how to run it 
python scripts/main.py
# Install required packages
pip install -r requirements.txt