# BlockstackML

# Campaign Analysis
This repository contains a comprehensive analysis of a marketing campaign dataset. The analysis includes both statistical and exploratory data analysis (EDA) to uncover insights and address critical business challenges. Furthermore, the repository showcases the application of machine learning models for predicting customer subscriptions and provides comparisons between different models.

# Key Insights
## Statistical Analysis
* Subscription and Balance: There's no significant difference in account balance between subscribers and non-subscribers, implying that subscription decisions are influenced by other factors.
*Work and Subscription: Occupation is associated with subscription choices, indicating that the type of job can impact a customer's decision.
*Marital Status and Subscription: A strong correlation exists between marital status and subscription, suggesting that marital status is a crucial factor.
*Education and Subscription: Education level is linked to subscription decisions, making it a significant predictor.
*Default and Subscription: The presence of a credit default does not significantly affect subscription decisions.
*Loans: Both personal and housing loans affect subscription decisions, indicating their importance.
*Contact Method and Subscription: The choice of contact method is influenced by subscription status, highlighting the role of communication style.
*Month and Poutcome: Subscription decisions correlate with the campaign month and prior campaign results.
*Balance by Education Levels: While balance doesn't vary significantly by marital status, it does exhibit variation across different education levels, with higher education linked to higher account balances.

## Exploratory Data Analysis
* Age Distribution: Most clients are between 30 and 60 years old, reflecting the campaign's targeting demographic.
* Job Categories: Blue-collar, management, and technician jobs are the most common among clients.
* Marital Status: Married clients are the majority, followed by single and divorced clients.
* Education Levels: Primary, tertiary, and secondary education levels are prevalent among clients.
* Credit Default: Very few clients experience credit defaults.
* Balance Distribution: The majority of clients have relatively low balances.
* Housing and Personal Loans: Most clients have housing loans, while personal loans are less common.
* Contact Methods: The phone is the primary contact method.
* Contact Month: May is the month with the most contacts.
* Duration of Last Contact: Right-skewed distribution in the length of the most recent contact.
* Number of Contacts: Most clients received very few communications during the campaign.
* Previous Contacts: Clients contacted previously show a wide range of days between contacts.
* Previous Campaign Outcomes: "Unknown" is the most common prior campaign result.
* Subscription Imbalance: The dataset exhibits an imbalance, with significantly more clients not subscribing.

## Business Problems and Solutions
Based on the insights gained from the analysis, the following business issues and solutions are proposed:

* Low Subscription Rate: Implement specialized campaigns, custom offers, and enhanced analysis of past campaign results.
* Age-Based Targeting: Tailor campaigns and timing to different age groups.
* Strategies Dependent on Occupation: Customize messaging and explore industry collaborations.
* Leveraging the Influence of Marital Status: Create family-focused ads and social network strategies.
* Focusing on Educational Background: Offer tailored content and educational workshops based on clients' educational backgrounds.
* Optimization of Contact Methods: Maximize mobile optimization and multi-channel strategies.
* Marketing of Loan Products: Develop customized loan offers and cross-promotional opportunities.
* Get in Touch with Frequency Management: Experiment with touch frequency and A/B testing.
* Managing "Unknown" Results: Implement improved data gathering and client feedback processes.
* Increasing Credits to Increase Subscription Rate: Highlight the rarity of credit defaults in marketing materials.

## Model Comparison
The analysis includes a comparison of two machine learning models: Decision Tree and Naive Bayes. Here's a summary of the key findings:

* Decision Tree (Hyperparameter Tuned):
Accuracy: 0.89
Precision ('yes'): 0.49
Recall ('yes'): 0.38
F1-Score ('yes'): 0.43

* Decision Tree (Without Hyperparameter Tuning):
Accuracy: 0.87
Precision ('yes'): 0.38
Recall ('yes'): 0.36
F1-Score ('yes'): 0.37

* Naive Bayes (Hyperparameter Tuned):
Accuracy: 0.87
Precision ('yes'): 0.38
Recall ('yes'): 0.41
F1-Score ('yes'): 0.40

* Naive Bayes (Without Hyperparameter Tuning):
Accuracy: 0.87
Precision ('yes'): 0.38
Recall ('yes'): 0.41
F1-Score ('yes'): 0.40
In summary, the Decision Tree model with hyperparameter tuning outperforms other models, especially regarding precision, recall, and F1-Score for the 'yes' class. However, the model choice should consider factors like processing capacity, ease of maintenance, and business-specific needs.
  
