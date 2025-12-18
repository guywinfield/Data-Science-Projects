# ColumnTransformer — Detailed Explanation (with Dummy Data)

---

## What is `ColumnTransformer` really doing?

At a high level:

> **`ColumnTransformer` lets you apply different preprocessing steps to different columns, in parallel, and then stitch the results back together.**

In normal English:
- *These columns* → encode them
- *Those columns* → scale them
- *These others* → impute missing values
- Then **combine everything into one clean feature matrix**

---

## Why do we need it?

Real datasets look like this:

| Column | Type | Needs |
|-----|----|----|
| `District` | categorical | encoding |
| `Type` | categorical | encoding |
| `EnergyCertificate` | categorical | encoding |
| `TotalArea` | numeric | scaling |
| `Washrooms` | numeric | imputation |
| `ConstructionYear` | numeric | imputation |

If you apply **one transformation to everything**, something breaks.

`ColumnTransformer` solves this cleanly.

---

## Basic structure

```python
from sklearn.compose import ColumnTransformer
```

```python
preprocessor = ColumnTransformer(
    transformers=[
        ('name', transformer, columns),
        ('name', transformer, columns)
    ]
)
```

Each tuple means:

```
(step_name, what_to_do, which_columns)
```

---

## Example (simple but realistic)

```python
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
        ('num', StandardScaler(), numeric_cols)
    ]
)
```

### What happens internally?

```
categorical_cols → OneHotEncoder → encoded features
numeric_cols     → StandardScaler → scaled features
-----------------------------------------------
                 → combined into one matrix
```

---

# What kinds of things can go inside `ColumnTransformer`?

This is the key question.

---

## 1️⃣ Encoding categorical variables

### OneHotEncoder (most common)

```python
OneHotEncoder(
    handle_unknown='ignore',
    sparse_output=False
)
```

Why these options matter:
- `handle_unknown='ignore'` → avoids crashes on unseen categories
- `sparse_output=False` → needed if you want pandas output or SHAP

---

### OrdinalEncoder (ordered categories)

```python
OrdinalEncoder(
    categories=[["E", "D", "C", "B", "A"]]
)
```

Good for things like:
- Energy certificates
- Ratings
- Education levels

⚠️ Only use if order actually means something.

---

## 2️⃣ Imputing missing values

### Numeric imputation

```python
SimpleImputer(strategy='median')
```

Why median?
- Robust to outliers
- Sensible default for prices, areas, ages

---

### Categorical imputation

```python
SimpleImputer(strategy='most_frequent')
```

or explicitly mark missing:

```python
SimpleImputer(strategy='constant', fill_value='Missing')
```

This is often better for tree models.

---

## 3️⃣ Scaling numeric features

```python
StandardScaler()
```

Good for:
- Linear models
- KNN
- Neural networks

Not needed for:
- Tree-based models (RF, XGB, CatBoost)

But **still fine** to include if you want consistency.

---

## 4️⃣ Chaining multiple steps per column (very common)

This is where `Pipeline` + `ColumnTransformer` shine together.

### Example: numeric pipeline

```python
num_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])
```

### Example: categorical pipeline

```python
cat_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='Missing')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])
```

### Plug into ColumnTransformer

```python
preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_pipe, numeric_cols),
        ('cat', cat_pipe, categorical_cols)
    ]
)
```

🧠 This is **industry-standard preprocessing**.

---

# Advanced but VERY useful options

## 5️⃣ `remainder` argument

What about columns you *don’t mention*?

```python
ColumnTransformer(
    transformers=[...],
    remainder='drop'   # default
)
```

Options:

| Value | Meaning |
|----|----|
| `'drop'` | Remove unused columns |
| `'passthrough'` | Keep them unchanged |

Example:

```python
remainder='passthrough'
```

Useful when:
- You’ve already cleaned some columns
- You want to keep engineered features

---

## 6️⃣ Controlling output format (important for SHAP)

```python
preprocessor.set_output(transform='pandas')
```

Why this matters:
- Keeps column names
- SHAP needs this
- Easier debugging

⚠️ Requires:
```python
OneHotEncoder(sparse_output=False)
```

Otherwise you’ll get sparse matrix errors.

---

## 7️⃣ Creating “missing value flags”

```python
SimpleImputer(
    strategy='median',
    add_indicator=True
)
```

This creates extra columns like:

```
TotalArea_missing
Washrooms_missing
```

Why this helps:
- Models can learn that “missing” itself is informative
- Very useful in real-world data

---

## 8️⃣ Feature engineering inside ColumnTransformer

You can add **custom transformations**.

### Example: log transform areas

```python
from sklearn.preprocessing import FunctionTransformer
import numpy as np

log_transformer = FunctionTransformer(np.log1p)
```

```python
('log_area', log_transformer, ['TotalArea'])
```

This happens **inside the pipeline**, so:
- No leakage
- CV safe
- Deployment safe

---

## 9️⃣ Naming and debugging transformed features

Once fitted:

```python
preprocessor.get_feature_names_out()
```

You’ll see names like:

```
num__TotalArea
cat__District_Lisbon
cat__Type_Apartment
```

This is crucial for:
- SHAP
- Feature importance
- Debugging column order issues

---

# Common mistakes

### ❌ Sparse output + pandas output mismatch

Fix with:

```python
OneHotEncoder(sparse_output=False)
preprocessor.set_output(transform='pandas')
```

---

# Gold-standard template

```python
num_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median', add_indicator=True)),
    ('scaler', StandardScaler())
])

cat_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='Missing')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_pipe, numeric_cols),
        ('cat', cat_pipe, categorical_cols)
    ],
    remainder='drop'
)

preprocessor.set_output(transform='pandas')
```

---

# Dummy data example (runnable)

```python
import pandas as pd
import numpy as np

# Create dummy dataset
np.random.seed(42)

df = pd.DataFrame({
    'District': np.random.choice(['Lisbon', 'Porto', 'Coimbra'], size=100),
    'Type': np.random.choice(['Apartment', 'House'], size=100),
    'EnergyCertificate': np.random.choice(['A', 'B', 'C', 'D'], size=100),
    'TotalArea': np.random.normal(100, 20, size=100),
    'Washrooms': np.random.choice([1, 2, 3, np.nan], size=100),
    'ConstructionYear': np.random.choice([1990, 2000, 2010, np.nan], size=100),
    'Price': np.random.normal(300_000, 50_000, size=100)
})

X = df.drop(columns='Price')
y = df['Price']

categorical_cols = ['District', 'Type', 'EnergyCertificate']
numeric_cols = ['TotalArea', 'Washrooms', 'ConstructionYear']
```

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

num_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median', add_indicator=True)),
    ('scaler', StandardScaler())
])

cat_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='Missing')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_pipe, numeric_cols),
        ('cat', cat_pipe, categorical_cols)
    ]
)

preprocessor.set_output(transform='pandas')
```

```python
X_processed = preprocessor.fit_transform(X)
X_processed.head()
```

---

## Final intuition

> **`ColumnTransformer` is the control centre that decides *what happens to each column* before the model ever sees the data.**

