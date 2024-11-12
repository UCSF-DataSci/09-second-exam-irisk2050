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

Carrying over from question 2, I added variables 'visit_cost' and 'season' to the data. For the multiple regression, I used a simple OLS model. To account for repeated measures (as in, the same person was measured multiple times), I clustered the standard errors by 'patient_id'. The r-squared was 0.807 and the adjusted r-squared was 0.807. This means that 80.7% of the variance in walking speed is explained by the independent variables age and education level. This suggests a strong fit, as the model is explaining a substantial portion of the variability in the data. Since both the r-squared and adjusted r-squared are the same (0.807), it suggests that there aren't irrelevant variables inflating the r-squared. This implies a well-specified model with a good balance of explanatory power without overfitting. 

                  coef       std err      p-value        Conf. Interval
const            5.5992      0.008        0.00000e+000   [ 5.5832782   5.61510059]
Graduate         0.4152      0.007        0.00000e+000   [ 0.40164808  0.4288372 ]
High School     -0.7923      0.007        0.00000e+000   [-0.80557048 -0.77906352]
Some College    -0.3903      0.007        3.91879e-318   [-0.40368752 -0.37696296]
age             -0.0301      0.000        0.00000e+000   [-0.03040785 -0.02986839]

All of the variables were significant (p-value < 0.05). We can see that education_level = 'Graduate' is positively correlated with walking speed. The others are negatively correlated, including age, which agrees with our intial exploratory data analysis: as age increases, walking speed decreases.

To examine trends, I re-did the regression but added in interaction terms between age and education level. The coefficients for the interaction terms (e.g., age_Graduate, age_SomeOtherLevel) explain how the relationship between age and walking speed differs across education levels. A significant p-value for these interaction terms suggests that the relationship between age and walking_speed changes depending on the education_level.

age                 -0.0303      0.001    -31.590      0.000      -0.032      -0.028
age_High School   5.542e-05      0.000      0.166      0.868      -0.001       0.001
age_Some College    -0.0001      0.000     -0.409      0.682      -0.001       0.001
age_age           1.748e-06   8.94e-06      0.196      0.845   -1.58e-05    1.93e-05

Based off of the p-values, the interaction terms were not significant, showing that the relationship between age and walking_speed does not significantly change across education level.

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
