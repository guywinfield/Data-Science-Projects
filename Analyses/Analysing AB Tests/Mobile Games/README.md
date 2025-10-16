# 🎮 Cookie Cats A/B Test — Analysis Summary

### Goal & Scope
This analysis explores player engagement in the mobile puzzle game **Cookie Cats** by evaluating the impact of moving a level gate from **level 30 → level 40**.  
The analysis uses real experiment data to understand:
- How game design changes affect **player engagement** and **retention**.
- Whether moving the gate increases or decreases the **number of rounds played**.

The goal was to practice **A/B testing**, **statistical inference**, and **data visualization** using real-world mobile game data.

---

### 🔑 Key Findings

**🎯 Primary Metric — Game Rounds Played**
- Primary engagement metric: `sum_gamerounds` (number of rounds played in 14 days).  
- Chosen because it’s a **direct measure of engagement**, unlike binary retention flags.  
- Used **1-day and 7-day retention** as “guardrail” checks for consistency.

**🧪 Statistical Test**
- **Test Used:** Independent two-sample **t-test**  
- **Confidence Level:** 95% (α = 0.05)  
- **Transformation:** Applied **log transformation** due to strong right skew (exponential distribution).  
- **Assumptions:** Normality checked via histograms / Q-Q plots on transformed data.  

### 📌 Key Takeaways
- Workplace stigma persists: Mental health conversations are still riskier with managers than with peers.
  - Only ~1 in 3 respondents feel safe disclosing to supervisors. 
- Support gap: Employers provide more visible support for physical health than mental health.
  - Employers are 30pp more likely to be seen as supporting physical health vs. mental health. 
- Need for policies: Training, clear policies, and cultural changes are necessary to normalize mental health discussions.
- Data-driven monitoring: Continued survey analysis is vital to track progress over time.


### 🧠 Interpretation & Insights

- The new version (gate moved to level 40) **did not significantly change** engagement levels.  
- Average gameplay dropped slightly (≈ –1.3%), but the difference is **not statistically meaningful**.  
- Retention metrics (`retention_1`, `retention_7`) showed minor decreases, suggesting:
  - Players might churn earlier when more content is unlocked up-front.
  - Earlier gating (at level 30) may better encourage pacing and repeat play.

## Limitations of the Data

- **Engagement distribution** is heavily skewed (few players play a lot).  
- **Short measurement window:** only 14 days of gameplay.  
- **No player segmentation:** differences might vary by region, device, or prior activity.  
- **Single metric focus:** other KPIs (e.g. in-app purchases, ad impressions) not analysed.


---

## 🧰 Getting Started

### Data Used 

| Column | Description |
|:-------|:-------------|
| `userid` | Unique player ID |
| `version` | Experimental variant (`gate_30` = control, `gate_40` = treatment) |
| `sum_gamerounds` | Number of rounds played (first 14 days) |
| `retention_1` | Played again 1 day after install (True/False) |
| `retention_7` | Played again 7 days after install (True/False) |


### Prerequisites
- Python 3.8 or later  
- Jupyter Notebook  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- scipy  

### Installation

1. Clone the repository:
   ```bash
   gh repo clone TuringCollegeSubmissions/gwinfi-DS.v3.2.2.5
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy
   ```
3. Download the dataset:
   ```python
   import kagglehub
   path = kagglehub.dataset_download("mursideyarkin/mobile-games-ab-testing-cookie-cats")
   print("Path to dataset files:", path)
   ```

---

## 👤 Author

**Guy Winfield**  
📧 Discord: `@guyw7698`  


---

## 🗓 Version History
- 0.1 Initial Release — Cookie Cats A/B Testing Project 