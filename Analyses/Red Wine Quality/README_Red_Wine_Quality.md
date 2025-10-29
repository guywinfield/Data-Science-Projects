# 🍷 Red Wine Quality Analysis

### 🎯 Goal & Scope
This analysis explores which **chemical properties** most influence the **perceived quality** of red wine, based on sensory ratings from wine experts.  
Rather than aiming to predict wine quality with maximum accuracy, the goal is **explanatory** — to understand the **drivers of quality** and their relative importance.  

The project demonstrates practical applications of **multiple linear regression**, **multicollinearity diagnostics (VIF)**, and **residual analysis** to evaluate model validity and interpretability.

### **Null Hypothesis** : 
There is no linear relationship between wine quality and the predictor variables (alcohol, sulphates, volatile acidity, and density)

---

### 🧠 Interpretation & Insights

Based on the regression output, the coefficients for alcohol, sulphates, and volatile acidity are statistically significant (p < 0.05). This provides strong evidence against the null hypothesis.

**Therefore we reject H₀**

There is a relationship between wine quality and the predictor variables (alcohol, sulphates, volatile acidity)**


- 🍷 **Alcohol, sulphates, and volatile acidity** are the strongest predictors of wine quality.  
- The model explains a **statistically significant portion** of variation in ratings, though not all — subjective taste remains a factor.  
- **High VIF values** were detected among several chemical variables, indicating **multicollinearity** (some predictors are strongly correlated).  
  - This means coefficients should be interpreted with caution — while significant relationships exist, their *independent effects* are less certain.  
- Residual plots suggest no major violations of linearity or homoscedasticity, but slight heteroscedasticity was observed at higher fitted values.

### 📈 Model Summary

$$
Quality = 2.57 + 0.31(Alcohol) + 0.68(Sulphates) - 1.24(Volatile\ Acidity)
$$

| Variable | Coefficient | Interpretation |
|:--|:--|:--|
| **Alcohol** | +0.31 | Higher alcohol content generally increases perceived quality |
| **Sulphates** | +0.68 | Wines with higher sulphate levels tend to score higher |
| **Volatile Acidity** | −1.24 | Higher volatile acidity (vinegary aroma) lowers perceived quality |


---

### 🧪 Statistical Methodology

**Approach:**  
A **multiple linear regression** was used to model the relationship between wine quality and physicochemical variables.  
Diagnostic checks were conducted to ensure the assumptions of linear regression were met.

| Step | Method | Purpose |
|:--|:--|:--|
| 1️⃣ | **Correlation analysis & pairplots** | Identify initial linear relationships |
| 2️⃣ | **Variance Inflation Factor (VIF)** | Detect multicollinearity among predictors |
| 3️⃣ | **Model fitting** | Estimate coefficients and interpret direction/strength of relationships |
| 4️⃣ | **Residual plots & homoscedasticity checks** | Assess model fit and assumption validity |
| 5️⃣ | **Interpretation of coefficients** | Understand which features most influence perceived quality |


---

### 🍇 Data Source
- UCI Machine Learning Repository → [Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality)
- The dataset contains physicochemical test results for 1,599 red wines from the Portuguese Vinho Verde region.

| Column | Description |
|:--|:--|
| `fixed acidity` | Tartaric acid concentration |
| `volatile acidity` | Acetic acid level (linked to vinegary taste) |
| `citric acid` | Adds freshness and flavor |
| `residual sugar` | Remaining sugar after fermentation |
| `chlorides` | Salt content |
| `free sulfur dioxide` | Preservative gas |
| `total sulfur dioxide` | Sum of bound and free SO₂ |
| `density` | Correlates with alcohol and sugar content |
| `pH` | Acidity measure (lower = more acidic) |
| `sulphates` | Stabilizing and antioxidant agent |
| `alcohol` | Percentage by volume |
| `quality` | Wine rating (0–10 scale by tasters) |

---


### ⚠️ Limitations
- High **multicollinearity** between chemical variables may distort coefficient estimates.   
- Ratings are based on **human sensory judgment**, which introduces subjective variability.  
- A **non-linear model** (e.g. Random Forest or Polynomial Regression) could potentially capture more complex relationships.

---

### 🔧 Prerequisites
- Python 3.8+  
- Jupyter Notebook  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- statsmodels  

---

### 💻 Installation
1. Clone the repository:
   ```bash
   gh repo clone TuringCollegeSubmissions/gwinfi-DS.v3.3.1.7
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn statsmodels
   ```
3. Load the dataset:
   ```python
   import pandas as pd

   df = pd.read_csv("winequality-red.csv")
   print(df.shape)
   ```

---

## 👤 Author
**Guy Winfield**  
📧 Discord: `@guyw7698`

---

## 🗓 Version History
- 0.1 Initial Release — Red Wine Quality Linear Regression Project  
