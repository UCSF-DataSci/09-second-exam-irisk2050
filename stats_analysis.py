import scipy.stats
import statsmodels
import os
import pandas as pd
import numpy as np

# Set working directory.
os.chdir("/Users/iriskim/Desktop/09-second-exam-irisk2050")

# Set random seed.
np.random.seed(42)

# Read the processed CSV file.
df = pd.read_csv("ms_data.csv")

# Convert visit_date to datetime.
df['visit_date'] = pd.to_datetime(df['visit_date'])

#  Sort by patient_id and visit_date.
df = df.sort_values(by = ['patient_id', 'visit_date'])

# Read insurance types from `insurance.lst`.
with open('insurance.lst', 'r') as f:
    insurance_types = [line.strip() for line in f.readlines()]

# Randomly assign (but keep consistent per patient_id).
unique_patients = df['patient_id'].unique()
patient_insurance_map = {patient_id: np.random.choice(insurance_types) for patient_id in unique_patients}
df['insurance_type'] = df['patient_id'].map(patient_insurance_map)

# Generate visit costs based on insurance type. Different plans have different effects on cost.
base_costs = {'Medicare': 100,
    'Medicaid': 200,
    'Private': 50,
    'Other': 500
}

# Add random variation.
variation_factor = 0.2 # 20% variation
df['visit_cost'] = df['insurance_type'].map(base_costs) * (1 + np.random.uniform(-variation_factor, variation_factor, len(df))).round(3)

# Set appropriate data types.
df['patient_id'] = df['patient_id'].astype(str)
df['education_level'] = df['education_level'].astype(str)
df['insurance_type'] = df['insurance_type'].astype(str)



# Q3



# 1. Analyze walking speed:
#    - Multiple regression with education and age (report coeffcients and confidence intervals)
#    - Account for repeated measures
#    - Test for significant trends

# 2. Analyze costs:
#    - Simple analysis of insurance type effect
#    - Box plots and basic statistics (report coeffcients and confidence intervals)
#    - Calculate effect sizes

# 3. Advanced analysis:
#    - Education age interaction effects on walking speed
#    - Control for relevant confounders
#    - Report key statistics and p-values (report coeffcients and confidence intervals)