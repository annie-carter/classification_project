# Classification_Project


## Project Description
This project determines factors contributing to customer churn for the TELCO company. The data collected from this project can help with future planning on ways to decrease customer churn and improve loyalty to the TELCO brand.


## Project Goals
This project goal is to identify factors that have a significant relationship to customers at a higher risk of churn, construct a classification model that accurately predicts factors for customer churn, and present findings to lead data scientist and other TELCO stakeholders


## Initial Questions 
To guide our analysis, we initially posed the following questions:

1. Does the type of contract have a significant impact on customer churn?
2. Does having device protection influence customer churn?
3. Is there a relationship between streaming TV services and customer churn?
4. Does having tech support affect customer churn?


## Initial Hypotheses 
Hypothesis 1 
* alpha = .05 
* H0= Contract type is independent of customer churn 
* Ha= Contract type is dependent on customer churn 
* Outcome: We will accept or reject the Null Hypothesis.

Hypothesis 2 
* alpha = .05 
* H0 = Data protection is independent of customer churn  
* Ha = Data protection is dependent on customer churn
* Outcome: We will  accept or reject the Null Hypothesis.
    
Hypothesis 3 
* alpha = .05 
* H0 = Streaming_movies is independent of customer churn  
* Ha = Streaming_movies is dependent on customer churn
* Outcome: We will  accept or reject the Null Hypothesis.

Hypothesis 4 
* alpha = .05 
* H0 = Tech support is independent of customer churn 
* Ha = Tech support is dependent on customer churn  
* Outcome: We will accept or reject the Null Hypothesis.


## Data Dictionary

There were 25 columns in the initial data and 29 columns after preparation; the central target column will be: 

|   Targee    |       Datatype        |    Definition      |
|------------|-----------------------|:------------------: |
| churn_Yes  | 7043 non-null: object |  0 or 1 (boolean)   |


|        Feature          |       Datatype        |     Definition        |
|-------------------------|-----------------------|-----------------------|
|contract type_Yes 	      |7043 non-null: object  |0 or 1 (boolean)       |
|device_protection_Yes	  |7043 non-null: uint8   |0 or 1 (boolean)       |
|streaming_tv_Yes	      |7043 non-null: uint8   |0 or 1 (boolean)       |
|tech_support_Yes	      |7043 non-null: uint8   |0 or 1 (boolean)       |


## Project Planning
### Planning
1. Clearly define the problem to be investigated, such as the impact of tech support on churn.
2. Obtain the required data from the "telco.csv" database.
3. Create a comprehensive README.md file documenting all necessary information.
### Acquisition and Preparation
4. Develop the acquire.py and prepare.py scripts, which encompass functions for data acquisition, preparation, and data splitting.
5. Implement a .gitignore file to safeguard sensitive information and include files (e.g., env file) that require discretion.
### Exploratory Analysis
6. Create preliminary notebooks to conduct exploratory data analysis, generate informative visualizations, and perform relevant statistical tests (e.g., chi-square test).
### Modeling
7. Train and evaluate various models, such as Decision Tree, Logistic Regression, and Random Forest, utilizing a Random Seed value of 42.
    * Train the models using the available data.
    * Validate the models to assess their performance.
    * Select the most effective model (e.g., Logistic Regression) for further testing.
### Product Delivery
8, Prepare a final notebook that integrates the best visuals, models, and pertinent data to present comprehensive insights.
9. Generate a Prediction.csv file containing the predictions from the test


## Instructions  to Reproduce the Final Project Notebook
To successfully run/reproduce the final project notebook, please follow these steps:
1. Read this README.md document to familiarize yourself with the project details and key findings.
2. Before proceeding, ensure that you have the necessary database credentials. Create or use an environment (env) file that includes the required credentials, such as username, password, and host. Make sure not to add your env file to the project repository, but .gitignore.
3. Clone the classification_project repository from my GitHub or download the following files: aquire.py, prepare.py, and final_report.ipynb. You can find these files in the project repository.
4. Open the final_report.ipynb notebook in your preferred Jupyter Notebook environment or any compatible Python environment.
5. Ensure that all necessary libraries or dependent programs are installed. You may need to install additional packages if they are not already present in your environment.
6. Run the final_report.ipynb notebook to execute the project code and generate the results.

By following these instructions, you will be able to reproduce the analysis and review the project's final report. Feel free to explore the code, visualizations, and conclusions presented in the notebook.


## Key findings/ Conclusion
After selecting four features and creating data visualizations, I chose the features that displayed visual significance and had a more significant relationship in chi-square statistical testing to train the Classification Model which were Contract type and Tech Support. Among the tested models, Logistic Regression emerged as the most effective model for predicting customer churn, surpassing the baseline accuracy of 73.56% with a consistent accuracy of 80% across the train, validate, and test sets.
   
Hypothesis 1: Contract Type and Customer Churn
- Outcome: We rejected the Null Hypothesis, indicating that contract type is dependent on customer churn.
- However, the relationship between contract type and churn is moderate, with a count of 710 out of 4225. It can be utilized in the modeling process.

Hypothesis 2: Data Protection and Customer Churn
- Outcome: We rejected the Null Hypothesis, indicating that data protection is dependent on customer churn.
- Nevertheless, the relationship between data protection and churn is extremely weak, with a count of only 17 out of 4225. Hence, it will not be used in the modeling phase.

Hypothesis 3: Streaming Movies and Customer Churn
- Outcome: We rejected the Null Hypothesis, indicating that streaming movies are dependent on customer churn.
- However, the relationship between streaming movies and churn is extremely low, with a count of 15 out of 4225. Thus, it will not be considered in the modeling process.

Hypothesis 4: Tech Support and Customer Churn
- Outcome: We reject the Null Hypothesis, indicating that tech support is dependent on customer churn.
- Nevertheless, the relationship between tech support and churn is weak, with a count of 110 out of 4225. It will be used in modeling to fulfill the rubric requirements.

For modeling, I selected the features of Tech Support and Contract Type, aiming to exceed the baseline accuracy of 74%. Using Decision Tree, Logistic Regression, and Random Forest models with a Random Seed of 42, I strived to achieve higher accuracy without overfitting. 

While Decision Tree models scored higher than the baseline accuracy and exhibited consistent performance in both training and validation, Logistic Regression consistently outperformed Decision Tree with an overall accuracy of 80%. The logistic regression model was chosen over the Random Forest Model due to the notable 11% difference between the training and validation scores in the Random Forest Model. The chosen Logistic Regression Model was applied to the test data.

Logistic Regression performed the best of all three models with consistent 80% accuracy scores in training, validation and testing.
 
    
## Recommendations and Next Steps
Based on the findings, I propose the following recommendations and next steps:
- Exclude the Data Protection and Streaming Movies columns during the preparation phase, as their relationship with customer churn is shallow.
- Conduct chi-square statistical testing on the remaining columns to determine their significance in relation to churn, creating a subset that excludes relationships with counts less than 100 for modeling.
- Experiment with different hyperparameters to optimize the model's performance.
- Implement an exit survey for customers who have churned and consider conducting a churn and welcome survey for new customers to gather insights on why they left their previous company for TELCO.

   
## Takeaways 
Although the models employed in this classification project demonstrated effectiveness and accuracy, the selected features could have provided more valuable insights into the risk of customer churn. However, the data proved useful in identifying weak relationships associated with data protection, streaming movies, and even tech support in relation to customer churn. These elements can be excluded from future modeling efforts to enhance efficiency and accuracy.
