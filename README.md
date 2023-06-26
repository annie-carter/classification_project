# Classification_Project


## Project Description
This project determines factors contributing to customer churn for the TELCO company. The data collected from this project can help with future planning on ways to decrease customer churn and improve loyalty to the TELCO brand.

## Project Goals
1. This project goal is to identify factors that have a significant relationship to customers at a higher risk of churn, construct a classification model that accurately predicts factors for customer churn, and present findings to lead data scientists and other TELCO stakeholders

## Initial Questions 
1. Does contract type have a significant relationship to customer churn?
2. Does device protection have a significant relationship to customer churn?
3. Does streaming tv have a significant relationship to customer churn?
4. Does having Tech Support have a significant relationship to customer churn?


## Initial Hypotheses 
Hypothesis 1 
    • alpha = .05 
    • H0= Contract type is independent of customer churn 
    • Ha= Contract type is dependent on customer churn 
    • Outcome: #we rejected the Null Hypothesis. 
Hypothesis 2 
    • alpha = .05 
    • H0 = Data protection is independent of customer churn  
    • Ha = Data protection is dependent on customer churn
    • Outcome: #we rejected the Null Hypothesis.
    
Hypothesis 3 
    • alpha = .05 
    • H0 = Streaming_movies is independent of customer churn  
    • Ha = Streaming_movies is dependent on customer churn
    • Outcome: #we or reject the Null Hypothesis.

Hypothesis 4 
    • alpha = .05 
    • H0 = Tech support is independent of customer churn 
    • Ha = Tech support is dependent on customer churn  
    • Outcome: We reject the Null Hypothesis.


## Data Dictionary

There were 25 columns in the initial data and 29 columns after preparation; the central target column will be: 

| Target     |       Datatype        |    Definition      |
|------------|-----------------------|:------------------:|
| churn_Yes  | 7043 non-null: object |  0 or 1 (boolean)           |


| Feature                 |       Datatype        |    Definition            |
|-------------------------|-----------------------|--------------------------|
|contract type 	          |7043 non-null: object  |Month-to-month, One year, |
|                         |                       |Two year                  |
|device_protection_Yes	  |7043 non-null: uint8   |0 or 1 (boolean)          |
|streaming_tv_Yes	      |7043 non-null: uint8   |0 or 1 (boolean)          |
|tech_support_Yes	      |7043 non-null: uint8   |0 or 1 (boolean)          |


## Project Planning 
### Planning 
1. Identify the problem you wish to investigate. Ex. 4. Does having Tech Support significant to churn?
2. Identify the source of data to use the "telco.csv" database 
3. Create a README.md with all information required.
### Acquisition - Preparation 
4. Create aquire.py and prepare.py, which should have functions: acquire, prepare, and split data.
5. Create a .gitignore file to keep the environment safe from the exploitation of sensitive information to public add env and other files that should be used with discretion
### Exploratory Analysis 
6. Create non-final notebook(s) to: explore data, visual, stat tests, ex. chi-square test
### Modeling 
7. • Train - Decision Tree, Logistic Regression Random Forest,
   • Validate - Decision Tree, Logistic Regression Random Forest,
   • Test data Use best model ex. Logistic Regression
### Product Delivery
8. Create a final notebook to import the best visuals, models, and data beneficial to answering questions
9. Create a Prediction.csv file to aggregate test predictions.
10. Document the conclusion, takeaways, and recommendations for future testing in the Final notebook.


## Steps to Reproduce
1. Read this README.md
2. To run my final project notebook, you must create or use an env file with database credentials and all the files listed below. Add your env file to your directory. (user, password, host)
3. Clone classification_project from my Git Hub or Download the aquire.py, prepare.py, and final_report.ipynb files into your 
4. Run the final_report.ipynb notebook


## Key findings/ Conclusion
   After selecting four features and creating data visualizations, I chose the features that displayed visual significance and had a more significant relationship in chi-square statistical testing to train the Classification Model. The Logistic Regression model was my best model for the prediction of my target value, churn, because there was a consistent accuracy of 80% on the train, validate, and test sets; this model outperformed my baseline score of 73.56% 

Hypothesis 1  
    • Ha= Contract type is dependent on customer churn 
    • Outcome: we rejected the Null Hypothesis. 
    • But the relationship is fair of 710 out of 4225. It can be used in modeling.

Hypothesis 2  
    • Ha = Data protection is dependent on customer churn
    • Outcome: #we rejected the Null Hypothesis.
    • But the relationship is extremely low, of 17 out of 4225. This will not be used in modeling. 
Hypothesis 3  
    • Ha = Streaming_movies is dependent on customer churn
    • Outcome: #we rejected the Null Hypothesis.
    • But the relationship is extremely low of 15 out of 4225. This will not be used in modeling.  

Hypothesis 4  
    • Ha = Tech support is dependent on customer churn  
    • Outcome: We reject the Null Hypothesis.
    • But the relationship is weak at 110 to 4225. *Used for modeling to satisfy rubric requirements
 
    
    
## Recommendations/ Next Steps/If I had more time
   • I would drop the Data protection and Streaming_movie column during my preparation as these columns have a shallow relationship to customer churn
   • I would run chi-square statistical testing on the remaining columns to determine the significance to churn, creating a subset that excludes relationships less than 100 for modeling 
   • Change the hyperparameters on several different versions
   • Create exit survey for customers that have churned, considering churning and welcome survey that asks new customers why they left their previous company for TELCO
   
   
## Takeaways 
   Although the models used in this classification project were effectively executed and accurate, the information learned from the features selected could have been more helpful in determining the risk of customer churn. However, the data was valuable in identifying weak relationships that Data protection, Streaming movies, and even Tech support play on customer churn. These elements can be eliminated from future modeling.
