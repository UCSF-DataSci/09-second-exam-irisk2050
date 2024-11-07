# DS-217 Final Exam: Multiple Sclerosis Analysis

## Question 1: Data Preparation with Command-Line Tools (20 points)

The data cleaning and extraction were fairly easy, with the tips and content from previous lecture slides. The most difficult part of the data preparation was the data validation step where we had to remove rows that had an invalid walking_speed not between 2.0 and 8.0 feet/second. I googled the awk command, which makes information retrieval and text manipulation easy. I looked up each componen of the awk command to correcly restrict the walking_speed.
  
## Question 2: Data Analysis with Python (25 points)

Using the cleaned data and insurance category file from Question 1:

1. Load and structure the data:
   - Read the processed CSV file
   - Convert visit_date to datetime
   - Sort by patient_id and visit_date

2. Add insurance information:
   - Read insurance types from `insurance.lst`
   - Randomly assign (but keep consistent per patient_id)
   - Generate visit costs based on insurance type:
     - Different plans have different effects on cost
     - Add random variation

3. Calculate summary statistics:
   - Mean walking speed by education level
   - Mean costs by insurance type
   - Age effects on walking speed

- All questions: Summarize your efforts and results in `readme.md`
- Q2: All patients should have consistent insurance types across visits
  
## Question 3: Statistical Analysis (25 points)

Perform statistical analysis on both outcomes:

1. Analyze walking speed:
   - Multiple regression with education and age
   - Account for repeated measures
   - Test for significant trends

2. Analyze costs:
   - Simple analysis of insurance type effect
   - Box plots and basic statistics
   - Calculate effect sizes

3. Advanced analysis:
   - Education age interaction effects on walking speed
   - Control for relevant confounders
   - Report key statistics and p-values

- All questions: Summarize your efforts and results in `readme.md`
- Q3: Check for outliers before running statistical tests
  
## Question 4: Data Visualization (30 points)

Create visualizations for both walking speed and cost analyses in a Jupyter notebook:

1. Walking speed analysis:
   - Scatter plot of age vs walking speed with regression line
   - Box plots by education level
   - Line plot showing education age interaction

2. Cost analysis:
   - Bar plot of mean costs by insurance type
   - Box plots showing cost distributions
   - Add error bars or confidence intervals

3. Combined visualizations:
   - Pair plot of key variables
   - Faceted plots by education/insurance
   - Time trends where relevant

- All questions: Summarize your efforts and results in `readme.md`
- Q4: Verify plot readability by viewing at different zoom levels
  
### Bonus Points (10 points)

- Implement advanced statistical methods
- Create interactive visualizations
- Analyze additional patterns
- Add command-line argument parsing
