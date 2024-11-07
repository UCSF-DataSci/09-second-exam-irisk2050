import os
import pandas as pd

# Set working directory.
os.chdir("/Users/iriskim/Desktop/09-second-exam-irisk2050")



# Q2



# Q2.1 Load and structure the data:

# Read the processed CSV file
df = pd.read.csv("ms_data.csv")
# Convert visit_date to datetime
df['visit_date'] = pd.to_datetime(df['visit_date'])
#  Sort by patient_id and visit_date
df = df.sort_values(by = ['patient_id', 'visit_date'])