## Zillow Classification Project

<img src="zillow_logo.png" title="zillow_logo" width="500" height="200" />

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Project Summary
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### Project Objectives
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
> - Create modules (acquire.py, prepare.py) that make your process repeateable.
> - Construct a model to predict customer churn using classification techniques.
> - Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.
> - Answer panel questions about your code, process, findings and key takeaways, and model.

#### Business Goals
> - Find drivers for customer churn at Telco. Why are customers churning?
> - Construct a ML classification model that accurately predicts customer churn.
> - Document your process well enough to be presented or read like a report.

#### Audience
> - Codeup Data Science students

#### Project Deliverables
> - A final report notebook 
> - A final report notebook presentation
> - All necessary modules to make my project reproducible

#### Project Context
> - The telco_churn dataset I'm using came from the Codeup database.


#### Data Dictionary

|Target|Datatype|Definition|
|:-------|:--------|:----------|
| churn | object | Whether or not someone has churned |

|Feature|Datatype|Definition|
|:-------|:--------|:----------|

 |  payment_type_id           | non-null   int64  | ID associated to payment type (1, 2, 3, 4) |
 |:-------|:--------|:----------|
 |  internet_service_type_id  | non-null   int64  | ID associated with internet service type (1, 2, 3) |
 |  contract_type_id          | non-null   int64  | ID associated with contract type (1,2,3) |
 |  customer_id               | non-null   object | ID associated to customer ####-ABCDE |
 |  gender                    | non-null   object | Gender of customer (Male/Female)|
 |  senior_citizen            | non-null   int64  | Whether a customer is a Senior Citizen (0, 1)|
 |  partner                   | non-null   object | Whether a customer has a partner (Yes, No)|
 |  dependents                | non-null   object | Whether a customer has dependents (Yes, No)|
 |  tenure                    | non-null   int64  | How long a customer has been with us in terms of months|
 |  phone_service             | non-null   object | Whether a customer has phone service (Yes, No)|
 |  multiple_lines            | non-null   object | Whether a customer has multiple lines (Yes, No, No phone service)|
 |  online_security           | non-null   object | Whether a customer has online security (Yes, No, No internet service)|
 |  online_backup             | non-null   object | Whether a customer has online backup (Yes, No, No internet service)|
 |  device_protection         | non-null   object | Whether a customer has device protection (Yes, No, No internet service)|
 |  tech_support              | non-null   object | Whether a customer has tech support (Yes, No, No internet service)|
 |  streaming_tv              | non-null   object | Whether a customer has streaming tv (Yes, No, No internet service)|
 |  streaming_movies          | non-null   object | Whether a customer has streaming movies (Yes, No, No internet service)|
 |  paperless_billing         | non-null   object | Whether a customer has paperless billing (Yes, No, No internet service)|
 |  monthly_charges           | non-null   float64 | The amount charged monthly ($##.##)|
 |  total_charges             | non-null   object | Total amount charged ($##.##)|
 |  contract_type             | non-null   object | The type of contract (Month-to-month, One year, Two year)|
 |  internet_service_type     | non-null   object | The type of internet service (DSL, Fiber optic, None)|
 |  payment_type              | non-null   object | The type of payment (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))|




#### Initial Hypotheses

> - **Hypothesis 1 -**
> - alpha = .05
> - $H_0$: Tenure over 18 months is independent of churn  
> - $H_a$: Tenure over 18 months is not independent of churn
> - Outcome: I rejected the Null Hypothesis; Therefore we reject that tenure over 18 months is independent of churn. 

> - **Hypothesis 2 -**
> - alpha = .05
> - $H_0$: Having a 2 year contract is independent of churn  
> - $H_a$: Having a 2 year contract is not independent of churn
> - Outcome: I rejected the Null Hypothesis; Therefore we reject that having a 2 year contract is independent of churn. 

> - **Hypothesis 3 -**
> - alpha = .05
> - $H_0$: Having no internet is independent of churn  
> - $H_a$: Having no internet is not independent of churn
> - Outcome: I rejected the Null Hypothesis; Therefore we reject that having no internet is independent of churn. 

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - I found that all of the classification models I created, LogisticRegression, DecisionTree, and RandomForest predicted the churn rate with an accuracy no higher than 81%.
> - I chose my Random Forest model with a max depth of 5 as my best model and got 82% accuracy rate for predicting churn when applied to the test split. This model outperformed my baseline score of 73% accuracy.
> - Some initial exploration and statistical testing revealed that engineering some new features like "add_ons" and "tenure_over_18_mos" might help my models predict with even more accuracy. However once applied to different models, they made little difference. 

## Key Takeaways
The following were the 5 most influential features to churn: (least to greatest)

   - paperless billing
   - auto pay
   - internet_type_None
   - Tenure over 18 months
   - 2 Yr Contract

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

##### Plan
- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Telco_Classification_Project.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Telco_Classification_Project by importing and using the function.
- [x]  Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train three different classification models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Create csv file with the customer_id, the probability of churn, and the model's prediction for each observation in my test dataset.
- [x] Document conclusions, takeaways, and next steps in the Telco_Classification_Project.

___

##### Plan -> Acquire
> - Store functions that are needed to acquire data from the measures and species tables from the telco_churn database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
> - Import the acquire function from the acquire.py module and use it to acquire the data in the Telco_Classification_Project.
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
> - Plot distributions of individual variables.
___

##### Plan -> Acquire -> Prepare
> - Store functions needed to prepare the telco_churn data; make sure the module contains the necessary imports to run the code. The final function should do the following:
    - Split the data into train/validate/test.
    - Handle any missing values.
    - Handle erroneous data and/or outliers that need addressing.
    - Encode variables as needed.
    - Create any new features, if made for this project.
> - Import the prepare function from the prepare.py module and use it to prepare the data in the Telco_Classification_Project.
___

##### Plan -> Acquire -> Prepare -> Explore
> - Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, species. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships. The goal is to identify features that are related to churn (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model
> - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver
> - Introduce myself and my project goals at the very beginning of my notebook walkthrough.
> - Summarize my findings at the beginning like I would for an Executive Summary.
> - Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings.
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [x] Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- [x] Add your own env file to your directory. (user, password, host)
- [x] Run the Telco_Classification_Project.ipynb notebook