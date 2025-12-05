# **Housing Prices in Portugal Predictor**

## **🎯 Goal & Scope**
This project explores property prices in Portugal with the goals of:
1. Performing an exploratory data analysis (EDA) to understand the drivers of price variation.
2. Running hypothesis tests to statistically evaluate which property characteristics have a measurable effect on price.
3. Building a machine learning model capable of predicting housing prices accurately.
4. Preparing the model for cloud deployment.

We'll use the Jupyter Notebook as a demonstration of our findings and how we made the model put into deployment.

---
## **☁️ Cloud Deployment**

We deployed an application to a cloud environment using Google Cloud Platform (GCP). This allows the model to be run in browser for public use.

You can access the deployed application using the link below:
- https://houseprices-img-43887047938.europe-west4.run.app/

---

## **📊 Key Insights**


### 1. Market Composition and Price Distribution
The dataset shows that of all listings:
- Apartments make up 35% 
- Houses account for 27%
- Land represents 23%

Together, these three categories make up 85% of all listings, forming the core of the market.

Price distributions for apartments, houses, and land all exhibit strong right skew:
- Apartments have the highest median price, reflecting their concentration in urban districts where prices are typically higher.
- Houses have a lower median price due to the large volume of rural housing.
- Land shows extreme variation, as its value is highly location-dependent.

### 2. Are Property Types Over- or Under-Valued?

To understand whether certain property types contribute disproportionately to the total value of listings, we compared:
- % share of total market value
- % share of total listing volume

If all property types had similar value per square metre, these percentages would match. Deviations indicate over- or under-valuation relative to their prevalence.

We found that:
- Houses contribute +4 percentage points more to total market value than their share of listings would suggest.
- Land is heavily undervalued, contributing –11 percentage points relative to its listing volume.

This could suggest a supply-demand imbalance where excess land supply depresses its value, while houses—particularly in desirable districts—attract disproportionately high demand.

### 3. Strong Feature Relationships with Price

Using non‑linear correlations (Spearman), we identified a set of features that consistently showed strong relationships with property price. The most influential were:
- Number of washrooms
- Total number of rooms
- Presence of parking
- Construction year
- Total living area
- Washrooms‑to‑rooms ratio (a proxy for overall property quality and layout)


In addition to the correlation analysis, our best-performing machine learning model — the CatBoost Regressor separately confirmed several other predictors. Based on CatBoost's built‑in feature importance analysis, the most significant contributors to property valuation were:

- District
- Type of property (e.g., apartment, house, building, land)
- Energy Certificate rating
- Total area
- Number of washrooms

---

## **🚀 Future Improvements**
- Expand dataset with additional geographic or macroeconomic variables.
- Improve feature interactions using automated feature engineering.
- Deploy a monitored prediction service with feedback loops.

---

## **📁 Repository Structure**
```
Portugal Housing Prices/
│
    ├── Application/                      
        ├──templates
            ├──index.html
        ├──Dockerfile
        ├──explainer.pkl
        ├──main.py
        ├──metadata.json
        ├──model.cbm
        ├──requirements.txt
    ├── local_db/                    
        ├──db/
            ├──project_filebrowser.db/
    ├── House Prices Prediction.ipynb
    ├── helper_functions.py
    ├── README.md                  
    
```

---

## **🙌 Acknowledgements**

