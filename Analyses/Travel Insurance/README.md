# 🧳 Travel Insurance Purchase Prediction

### Classification predicting customers to purchase travel insurance

------------------------------------------------------------------------

## 🎯 Goal & Scope

The purpose of this analysis is to explore **which customer attributes
influence the likelihood of purchasing travel insurance**, and to
evaluate which classification models performs best for doing so.

This notebook focuses on: 
- Building and evaluating baseline models
- Comparing performance across precision, recall, F1, ROC curves
- Understanding **how customer behaviours relate to insurance uptake**
- Identifying **limitations** in the dataset and **recommendations for
improvement**

This is **not** designed as a production-ready model, but as an
**exploratory predictive study**.



------------------------------------------------------------------------

# 🧠 Key Insights

## 📌 Customer Behaviour Insights

During the analysis, two clear relationships emerged:

### 💰 **Higher annual income → higher likelihood of purchasing travel insurance**

Customers with higher incomes appear more willing to purchase add-on
products.

### 🌍 **Customers with previous travel abroad → more likely to purchase**

This behaviour strongly correlates with interest in travel insurance and
may act as a strong targeting signal.

These insights can be used by marketing, product, or commercial teams to
refine **segmentation**, **targeting**, and **conversion messaging**.

## 📊 Model Improvements After Undersampling


-   **Hyperparameter tuning did not have a noticeable impact** ---
    performance remained stable across parameter grids.
-   The dataset is **narrow**, lacking deeper behavioural features or
    interactions.
-   Models struggled to capture decision complexity because the dataset
    does not include richer signals such as:
    -   combined features (e.g., *family size × travel history*)
    -   medical conditions
    -   trip type or destination
    -   policy history

However we acheived the best improvements to our model after undersampling our data. 

Metrics | LR No Undersampling | Naive Bayes No Undersampling | **LR After Undersampling**
|:--|:--------------------|:-------------|:----------------------|
|**Accuracy** | ⬆️ 0.6960 | 0.6800 | 0.6440 |
|**Precision** | ⬆️ 0.7222 | 0.6613 | 0.5591 |
|**Recall** | 0.3900 | 0.4100 | ⬆️ 0.5200 |
|**F1** | 0.5065 | 0.5062 | ⬆️ 0.5389 |
|**ROC AUC** | 0.6590 | 0.6481 | ⬆️ 0.6593 |

### ⭐ Why Undersampled LR Is Best
- It shows **clear gains in recall and F1**, meaning it identifies more true travel-insurance buyers.
- It **balances the two classes better** than any other model tested.
- It **outperforms Naive Bayes** on the most important business‑aligned metrics.

📌 **Recommendation:** Use an undersampled Logistic Regression model if the business aims to identify customers most likely to purchase travel insurance.


------------------------------------------------------------------------

## ⚠️ Limitations

-   The dataset is **feature-poor**, limiting predictive power.
-   No composite or interaction variables (e.g., *chronic illness +
    travel habits*) can be created because the raw data doesn't include
    them.
-   Hyperparameter tuning yields minimal benefit given the dataset's
    simplicity.

📌 **Because of these limitations, this model should not be moved into
production.** Further data collection is strongly recommended.

------------------------------------------------------------------------

## 🔮 Recommendations for Future Work

To significantly improve predictive performance:

### 1️⃣ Expand the dataset

Include more behavioural and demographic predictors, such as: 
- Past insurance purchase history
- Trip frequency and destinations
- Age group, family details
- Employment category
- Health indicators

### 2️⃣ Collect more data

The current dataset lacks volume.\
More samples = more signal = better generalisation.

------------------------------------------------------------------------


### 💻 Installation
1. Clone the repository:
   ```bash
   gh repo clone TuringCollegeSubmissions/gwinfi-DS.v3.3.1.7
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn 
   ```
3. Load the dataset:
   ```python
   import pandas as pd

   df = pd.read_csv("TravelInsurancePrediction.csv")
   print(df.shape)
   ```

---

## 👤 Author
**Guy Winfield**  
📧 Discord: `@guyw7698`

---

## 🗓 Version History
- 0.1 Initial Release — Travel Insurance Prediction Project  
