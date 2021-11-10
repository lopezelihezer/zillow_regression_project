## Zillow Regression Project

<img src="zillow_logo.png" title="zillow_logo" width="500" height="200" />

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Project Summary

The goal of this project was to find drivers that affect tax value using the Zillow data set. Bedroom count, bathroom count, and area(sqft) all had a linear correlation with taxvalue. Using this data, I created a ML Regression Model that predicts tax value. I documented the entire process to be presented or read like a report. My best model (Quadratic Polynomial) beat the baseline (mean) RMSE value by 12,259 points. I also found that Single Unit Properties assessed from May-Aug 2017 in the Zillow dataset were located in the following counties: Orange, Ventura, and Los Angeles. All in the state of California.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### Project Objectives
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
> - Create modules (wrangle_zillow.py) that make your process repeateable.
> - Construct an ML Regression model to predict tax value using regression techniques.
> - Deliver a 5 minute presentation consisting of slides on canva to the dedicated Zillow Data Science Team.
> - Answer panel questions about your code, process, findings and key takeaways, and model.

#### Business Goals
> - Find drivers that affect tax value using the Zillow data set. 
> - Construct an ML Regression model that predicts tax value.
> - Document your process well enough to be presented or read like a report.

#### Audience
> - Zillow Data Science Team

#### Project Deliverables
> - A final report jupyter notebook 
> - A final report slide presentation
> - All necessary modules to make my project reproducible
> - Github repository containing all my work

#### Project Context
> - The zillow dataset I'm using came from the Codeup database.


#### Data Dictionary

|Target|Datatype|Definition|
|:-------|:--------|:----------|
| taxvalue | float64 | Value assessed to a home for tax purposes |

|Feature|Datatype|Definition|
|:-------|:--------|:----------|

 |  yearbuilt  | non-null   float64 | The year the property was built. |
 |:-------|:--------|:----------|
 |  taxamount  | non-null   float64 | The amount of tax paid on the property |
 |  fips       | non-null   float64 | Federal Information Processing Standard (county code)|
 |  area       | non-null   float64 | Calculated square feet of property|
 |  bed        | non-null   float64 | Number of bedrooms|
 |  bath       | non-null   float64 | Number of bathrooms|
 |  tdate_month| non-null   int64   | Transaction date month|
 |  tdate_day  | non-null   int64   | Transaction date day|
 |  tdate_week | non-null   int64   | Transaction date week|
 |  county     | non-null   object  | The county corresponding to the fips id|
 |  taxrate    | non-null   float64 | Calculated rate by dividing taxamount by taxvalue|
 



#### Initial Hypotheses

> - **Hypothesis 1 -**
> - alpha = .05
> - $H_0$: There is no linear correlation between bedroom count and taxvalue.  
> - $H_a$: There is a linear correlation between bedroom count and taxvalue. 
> - Outcome: I rejected the Null Hypothesis; Therefore we reject that there is no linear correlation between bedroom count and taxvalue.

> - **Hypothesis 2 -**
> - alpha = .05
> - $H_0$: There is no linear correlation between bathroom count and taxvalue.  
> - $H_a$: There is a linear correlation between bathroom count and taxvalue. 
> - Outcome: I rejected the Null Hypothesis; Therefore we reject that there is no linear correlation between bathroom count and taxvalue.

> - **Hypothesis 3 -**
> - alpha = .05
> - $H_0$: There is no linear correlation between area and taxvalue.  
> - $H_a$: There is a linear correlation between area and taxvalue. 
> - Outcome: I rejected the Null Hypothesis; Therefore we reject that there is no linear correlation between area and taxvalue.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - Bedroom count, bathroom count, and area(sqft) all have a linear correlation with taxvalue
> - Both taxvalue and taxamount have normal distributions
> - Our best model (Quadratic Polynomial) beat our baseline (mean) RMSE value by 12,259.
> - Single Unit Properties assessed from May-Aug 2017 found in the Zillow dataset were located in the following counties: Orange, Ventura, Los Angeles. All in the state of California.


### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

##### Plan
- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the Codeup Database and create a function to automate this process. Save the function in a wrangle_zillow.py file to import into the Zillow_Regression_Project.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a wrangle_zillow.py module, and prepare data in Zillow_Regression_Project by importing and using the function.
- [x]  Clearly define three hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline mean and document well.
- [x] Train three different regression models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model that performs the best and evaluate that single model on the test dataset.
- [x] Document conclusions, takeaways, and next steps in the Zillow_Regression_Project.

___

##### Plan -> Acquire
> - Store functions that are needed to acquire data from the measures and species tables from the zillow database on the Codeup data science database server; make sure the wrangle_zillow.py module contains the necessary imports to run my code.
> - Import the acquire function from the wrangle_zillow.py module and use it to acquire the data in the Zillow_Regression_Project.
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
> - Plot distributions of individual variables.
___

##### Plan -> Acquire -> Prepare
> - Store functions needed to prepare the zillow data; make sure the module contains the necessary imports to run the code. The final function should do the following:
    - Split the data into train/validate/test.
    - Handle any missing values.
    - Handle erroneous data and/or outliers that need addressing.
    - Encode variables as needed.
    - Create any new features, if made for this project.
> - Import the prepare function from the wrangle_zillow.py module and use it to prepare the data in the Zillow_Regression_Project.
___

##### Plan -> Acquire -> Prepare -> Explore
> - Answer key questions, my hypotheses, and figure out the features that can be used in a regression model to best predict the target variable, taxvalue. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships. The goal is to identify features that are related to taxvalue (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model
> - Establish a baseline mean to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver
> - Introduce myself and my project goals at the very beginning of my slide presentation.
> - Summarize my findings at the beginning like I would for an Executive Summary.
> - Walk Zillow Data Science Team through the analysis I did to answer my questions and that lead to my findings.
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [x] Download the wrangle_zillow.py file into your working directory
- [x] Add your own env file to your directory. (user, password, host)
- [x] Run the Zillow_Regression_Project.ipynb notebook