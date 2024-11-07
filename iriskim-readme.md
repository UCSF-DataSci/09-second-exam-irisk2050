# DS-217 Final Exam: Multiple Sclerosis Analysis

## Question 1: Data Preparation with Command-Line Tools (20 points)

The data cleaning and extraction were fairly easy, with the tips and content from previous lecture slides. The most difficult part of the data preparation was the data validation step where we had to remove rows that had an invalid walking_speed not between 2.0 and 8.0 feet/second. I googled the awk command, which makes information retrieval and text manipulation easy. I looked up each componen of the awk command to correcly restrict the walking_speed.
  
## Question 2: Data Analysis with Python (25 points)

For step 2, I used a dictionary using the patient_id as keys to make sure that insurance_type was consistent per patient_id. I added random variation around the defined visit costs for each insurance type using np.random.

For step 3, I grouped months into seasons to do a seasonal analysis of the effect of age on walking speed. What I found is that for within each age group, Winter and Spring were the two seasons with the lowest average walking speed. This makes sense, as generally those seasons have harsh weather outside, making it unfriendly to go out. Aside from the seasonal analysis, there was a general trend where as the age increased, the average walking speed decreased. This tracks, as elderly people are less mobile and thus have more difficulty getting around.
  
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
