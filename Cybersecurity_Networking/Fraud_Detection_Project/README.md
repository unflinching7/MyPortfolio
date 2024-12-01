# Predicting Credit Card Fraud

## Overview
This project investigates the efficacy of various machine learning models for predicting credit card fraud. The study addresses three main research questions:
1. Which models perform best in fraud detection?
2. What variables contribute the most to the model performance?
3. What is the relationship between the top variables and fraudulent transactions?

## Key Findings
- **Logistic Regression**: Emerged as the top-performing model with an accuracy of 98.8% and an AUC score of 98.0%.
- **Stacked Model**: Demonstrated superior predictive performance with an AUC-ROC score of 0.975 compared to both Logistic Regression and Neural Network models.
- **Top Variables**: Identified V14, V3, and V17 as key features with robust negative correlations to fraudulent transactions.

## Implementation
The project involves implementing and evaluating machine learning models using Python and various libraries including NumPy, pandas, scikit-learn, and more. The code showcases:
- Model training and evaluation procedures.
- Feature engineering techniques for fraud detection.
- Comparative analysis of model performance.

## Future Directions
Considering the potential for improved predictive performance with larger datasets, future work may involve:
- Scaling the model with additional data.
- Exploring advanced feature engineering strategies.
- Enhancing model interpretability and real-time application.

## Appendix
The appendix includes a detailed analysis of the stacked model's comparative performance and insights into its scalability and potential enhancements. 