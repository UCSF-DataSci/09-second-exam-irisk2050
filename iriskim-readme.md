# DS-217 Final Exam: Multiple Sclerosis Analysis

## Question 1: Data Preparation with Command-Line Tools (20 points)

The data cleaning and extraction were fairly easy, with the tips and content from previous lecture slides. The most difficult part of the data preparation was the data validation step where we had to remove rows that had an invalid walking_speed not between 2.0 and 8.0 feet/second. I googled the awk command, which makes information retrieval and text manipulation easy. I looked up each componen of the awk command to correcly restrict the walking_speed.
  
## Question 2: Data Analysis with Python (25 points)

For step 2, I used a dictionary using the patient_id as keys to make sure that insurance_type was consistent per patient_id. I added random variation around the defined visit costs for each insurance type using np.random.

For step 3, I grouped months into seasons to do a seasonal analysis of the effect of age on walking speed. What I found is that for within each age group, Winter and Spring were the two seasons with the lowest average walking speed. This makes sense, as generally those seasons have harsh weather outside, making it unfriendly to go out. Aside from the seasonal analysis, there was a general trend where as the age increased, the average walking speed decreased. This tracks, as elderly people are less mobile and thus have more difficulty getting around.
  
## Question 3: Statistical Analysis (25 points)

I checked for outliers and removed them using boxplots and z-scores.

1. Analyze walking speed:
   - Multiple regression with education and age
   - Account for repeated measures
   - Test for significant trends

Carrying over from question 2, I added variables 'visit_cost' and 'season' to the data. For the multiple regression, I used a simple OLS model. To account for repeated measures (as in, the same person was measured multiple times), I clustered the standard errors by 'patient_id'. The r-squared was 0.807 and the adjusted r-squared was 0.807. This means that 80.7% of the variance in walking speed is explained by the independent variables age and education level. This suggests a strong fit, as the model is explaining a substantial portion of the variability in the data. Since both the r-squared and adjusted r-squared are the same (0.807), it suggests that there aren't irrelevant variables inflating the r-squared. This implies a well-specified model with a good balance of explanatory power without overfitting. 

                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
const            5.5986      0.008    690.039      0.000       5.583       5.615
Graduate         0.4146      0.007     59.771      0.000       0.401       0.428
High School     -0.7923      0.007   -117.342      0.000      -0.806      -0.779
Some College    -0.3903      0.007    -57.334      0.000      -0.404      -0.377
age             -0.0301      0.000   -218.957      0.000      -0.030      -0.030

All of the variables were significant (p-value < 0.05). We can see that education_level = 'Graduate' is positively correlated with walking speed. The others are negatively correlated, including age, which agrees with our intial exploratory data analysis: as age increases, walking speed decreases.

To examine trends, I re-did the regression but added in interaction terms between age and education level. The coefficients for the interaction terms (e.g., age_Graduate, age_SomeOtherLevel) explain how the relationship between age and walking speed differs across education levels. A significant p-value for these interaction terms suggests that the relationship between age and walking_speed changes depending on the education_level.

====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
const                5.6021      0.024    233.954      0.000       5.555       5.649
Graduate             0.4152      0.007     59.692      0.000       0.402       0.429
High School         -0.7952      0.018    -43.039      0.000      -0.831      -0.759
Some College        -0.3833      0.018    -20.861      0.000      -0.419      -0.347
age                 -0.0303      0.001    -31.590      0.000      -0.032      -0.028
age_High School   5.542e-05      0.000      0.166      0.868      -0.001       0.001
age_Some College    -0.0001      0.000     -0.409      0.682      -0.001       0.001
age_age           1.748e-06   8.94e-06      0.196      0.845   -1.58e-05    1.93e-05

Based off of the p-values, the interaction terms were not significant, showing that the relationship between age and walking_speed does not significantly change across education level.

2. Analyze costs:
   - Simple analysis of insurance type effect
   - Box plots and basic statistics
   - Calculate effect sizes

I did a simple analysis of visit costs using insurance type. Similar to above, I also accounted for repeated measurements by grouping standard errors by patient_id. The selected reference group was Medicaid.

                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        198.9878      0.401    496.275      0.000     198.201     199.775
Medicare     -99.0659      0.440   -225.291      0.000     -99.929     -98.203
Other        300.0318      0.905    331.699      0.000     298.257     301.807
Private     -148.9186      0.413   -361.002      0.000    -149.728    -148.109

Intercept (const = 198.9878) represents the mean visit_cost for Medicaid. The model predicts that for patients with Medicaid, the average visit_cost is approximately $198.99. Medicare (coef = -99.0659) shows that the average visit_cost for patients with Medicare is $99.07 lower than for patients with Medicaid. The p-value on all the coefficients are significant.

The box plot summarizes these statistics.

                 count        mean        std    min     25%     50%    75%     max
insurance_type                                                                
Medicaid        3532.0  198.987769  23.006670  160.0  178.95  198.10  219.0   240.0
Medicare        3981.0   99.921904  11.590122   80.0   90.00   99.60  110.3   120.0
Other           4340.0  499.019585  57.601562  400.0  449.50  499.50  548.5   600.0
Private         3578.0   50.069201   5.775010   40.0   45.00   50.05   55.1    60.0

Since I randomly assigned insurance types, the counts are roughly the same. However, I gave different visit_cost values to each insurance type, which is revealed in the mean, median, min, and max values.

I measured effect size using ANOVA because my insurance type variable had more than 2 cateogries. The Eta Squared value of 0.967 is very high and indicates that approximately 96.7% of the variance in the visit_cost can be explained by the differences in insurance_type. This suggests a very strong effect size, meaning that the type of insurance has a significant impact on visit costs.

3. Advanced analysis:
   - Education age interaction effects on walking speed
   - Control for relevant confounders
   - Report key statistics and p-values

                                         coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------------------------
Intercept                              5.5973      0.013    418.464      0.000       5.571       5.623
C(education_level)[T.Graduate]         0.4166      0.010     41.083      0.000       0.397       0.436
C(education_level)[T.High School]     -0.7896      0.016    -50.740      0.000      -0.820      -0.759
C(education_level)[T.Some College]    -0.3862      0.022    -17.785      0.000      -0.429      -0.344
age                                   -0.0301      0.000   -121.494      0.000      -0.031      -0.030
age_education_interaction          -2.697e-05      0.000     -0.201      0.841      -0.000       0.000

The r-squared and adjusted r-squared are both 0.807, the same as the regression without interaction terms. We can also see that the interaction term is not significant. This means that the interaction terms did not improve the explanatory power of the model. 

One of the most significant variables is age. The coefficient for age is -0.0301, which indicates that as age increases by one unit, the walking speed decreases by 0.0301 units. The extremely low p-value suggests this variable has a strong effect on the dependent variable. For education levels, Graduate has a positive coefficient (0.4166), indicating that graduates have a higher walking speed compared to the baseline education level (likely the lowest category). High School shows a negative coefficient (-0.7896), implying that individuals with only a high school education tend to have significantly lower walking speed. All education levels are highly significant, with p-values of 0.000, indicating their importance in the model.

The interaction term has coefficient -2.697e-05 with a p-value of 0.841, suggesting that the interaction between age and education level does not have a statistically significant effect on walking speed. This implies that the relationship between age and walking speed is not notably influenced by different education levels.
  
## Question 4: Data Visualization (30 points)

Create visualizations for both walking speed and cost analyses in a Jupyter notebook:

1. Walking speed analysis:
   - Scatter plot of age vs walking speed with regression line
   - Box plots by education level
   - Line plot showing education age interaction

The walking speed analysis shows that there is a slight downwards trend in average walking speed as age increases. This makes sense, as people generally are less mobile and active the older they are. The box plots by education level showed that those with higher levels of education (Bachelors, Graduate) had higher average walking speeds than those with lower levels of education (High School, Some College). There was also one outlier in each education level. The line plot showing the education and age interaction shows that within each education_level, the trend of older = slower average walking speed generally holds true. For example, within the group High School (which has the lowest median walking speed according to the boxplot), the age group 70-79 is hovering around an average monthly walking speed of 2.5 feet/sec while the age group 20-29 is hovering between 4.0-4.5 feet/sec.

2. Cost analysis:
   - Bar plot of mean costs by insurance type
   - Box plots showing cost distributions
   - Add error bars or confidence intervals

The bar plot shows them mean visit costs by insurance type, with a black bar representing the standard deviation. Private insurance had the lowest average visit cost while Other insurance had the highest. The boxplot showcasing the distirbution of visit costs per insurance type showed that there were no outliers per insurance group. Other insurance had the widest variation in visit cost. The frequency histogram of number of visits of eaach visit cost showed that there were many more visits that cost <= $100. This could imply a few things:
   1) Many more people have Private or Medicaid insurance than other types of insurance.
   2) People who have Private or Medicaid insurance have more visits/go more often, and are thus more represented.

3. Combined visualizations:
   - Pair plot of key variables
   - Faceted plots by education/insurance
   - Time trends where relevant

The pair plots confirm a lot of our earlier findings. In the age vs walking speed plot, we can clearly see within each education level there is a downwards trend in average walking speed as age increases. When examining the walking speed vs. visit cost plot, we can see that education levels are spread across visit costs evenly. This makes sense, as I randomly assigned insurance (and thus visit costs) to each patient_id. However, we see the trend of Graduate education level people having higher average walking speeds across all visit costs and high school education level people having lower average walking speeds across all visits costs. The faceted plots show that regardless of education level or insurance type, the trend of increase in age = slower walking speed holds. This implies that age is the most important factor in predicting walking speed, since its trend is unaffected by education level or insurance type. Examining time trends, there were noticable "peaks" and "valleys" in all education levels and age groups. Groups "peaked" in walking speed during summer and fall and "valley-ed" in spring and winter. This makes sense; generally, weather is nicer in summer and more pleasant to go out in, whereas in the winter, it's harder to move around because of ice and snow, forcing people to walk slower and be more cautious.