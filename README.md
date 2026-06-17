House Price Prediction App
Overview

This project predicts residential house prices using Machine Learning. The model is trained on the House Prices: Advanced Regression Techniques dataset and deployed through a Streamlit web application.
Users can enter property details and receive an estimated house price instantly.

Dataset

Dataset: House Prices: Advanced Regression Techniques
The dataset contains 1,460 residential properties with 80 different features describing house characteristics such as:
Living area
Basement size
Garage capacity
Overall quality
Year built
Neighborhood
Kitchen quality
Number of bathrooms
And many more
Project Workflow

1. Data Cleaning
Removed columns with more than 50% missing values
Filled numerical missing values using mean/median imputation
Filled categorical missing values using mode

2. Feature Engineering
Dropped unnecessary columns such as Id
Applied One-Hot Encoding to categorical features
Handled unknown categories using:
OneHotEncoder(
    drop="first",
    handle_unknown="ignore"
)

3. Data Preprocessing
Missing value imputation using SimpleImputer
Feature scaling using StandardScaler
Created 259 final features after encoding

4. Model Training
The following models were evaluated:

Model	R² Score
Linear Regression	0.10
Ridge Regression	0.83
Lasso Regression	0.83
KNN Regressor	0.75
SVR	-0.02
Decision Tree	0.77
Random Forest	0.88
Gradient Boosting	0.89
AdaBoost	0.83
XGBoost	0.90

5. Hyperparameter Tuning
Randomized Search CV was used to optimize the XGBoost model.

Best parameters:

{
    'subsample': 0.8,
    'n_estimators': 500,
    'max_depth': 2,
    'learning_rate': 0.1,
    'col_bytree': 0.8
}
Final Performance
Metric	Score
MAE	16,042
RMSE	25,421
R² Score	0.916
Most Important Features

Top features identified by XGBoost:

OverallQual
GarageCars
GarageType_Attchd
GrLivArea
MSZoning_RM
Fireplaces
TotalBsmtSF
YearBuilt
KitchenQual_TA
LotArea
Streamlit Application


The web app provides:
Basic Mode

Quick prediction using:
Overall Quality
Living Area
Garage Capacity
Basement Area
Year Built
Lot Area


Advanced Mode

Detailed prediction using:
Overall Quality
Overall Condition
Living Area
1st Floor Area
2nd Floor Area
Basement Area
Lot Area
Year Built
Year Remodeled
Garage Capacity
Garage Area
Fireplaces
Bathrooms
Bedrooms
Neighborhood
Kitchen Quality


Technologies Used
Python
Pandas
NumPy
Scikit-Learn
XGBoost
Streamlit
Matplotlib
Seaborn


Installation
git clone https://github.com/sandhyaj2912/house-price-predictor.git

cd house-price-predictor

pip install -r requirements.txt

streamlit run app.py

Files
house-price-predictor/
│
├── app.py
├── HPP.ipynb
├── xg_model.pkl
├── columns.pkl
├── default_house.pkl
├── requirements.txt
└── README.md


Future Improvements
Add feature importance visualization
Display prediction confidence intervals
Add interactive charts and dashboards
Deploy on AWS/Heroku
Improve UI with custom CSS and themes


Author
Sandhya Joshi
Machine Learning Project using XGBoost and Streamlit.
