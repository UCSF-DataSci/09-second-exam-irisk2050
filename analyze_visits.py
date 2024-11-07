import os
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

# Set working directory.
os.chdir("/Users/iriskim/Desktop/09-second-exam-irisk2050")
# Set random seed.
np.random.seed(42)



# Q2



# Q2.1: Load and structure the data.

# Read the processed CSV file.
df = pd.read_csv("ms_data.csv")

# Convert visit_date to datetime.
df['visit_date'] = pd.to_datetime(df['visit_date'])

#  Sort by patient_id and visit_date.
df = df.sort_values(by = ['patient_id', 'visit_date'])

# Q2.2: Add insurance information.

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
## print(df.dtypes)
df['patient_id'] = df['patient_id'].astype(str)
df['education_level'] = df['education_level'].astype(str)
df['insurance_type'] = df['insurance_type'].astype(str)

# Q2.3: Calculate summary statistics.

# Check for missing data.
print(f"Number of missing values in each column: {df.isnull().sum()}") # No missing values.
print(f"Number of rows with at least one missing value: {df.isnull().any(axis=1).sum()}") # No missing values.

# Mean walking speed by education level.
print(f"Mean walking speed by education level: {df.groupby('education_level', observed = False)['walking_speed'].mean()}")

# Mean costs by insurance type.
print(f"Mean costs by insurance type: {df.groupby('insurance_type', observed = False)['visit_cost'].mean()}")

# Age effects on walking speed.
## print(min(df['age'])) # 19.2
## print(max(df['age'])) # 83.82
age_bins = pd.cut(df['age'], bins = range(10, 91, 10), right = False)
print(f"Mean walking speed by age group: {df.groupby(age_bins, observed = False)['walking_speed'].mean()}")

# Consider seasonal variations in the data.
# Check file seasonal_variation.ipynb for analysis.