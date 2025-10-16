# 🍔 Fast Food Marketing Campaign — A/B Test

### 🎯 Goal & Scope
This analysis evaluates the effectiveness of **three different promotional strategies** used by a major fast-food chain across multiple markets.  
The goal was to determine **which promotion drove the highest sales**, measured in thousands of dollars, and whether those differences were **statistically significant**.  

The project demonstrates practical applications of **bootstrapping**, **non-parametric hypothesis testing**, and **data-driven storytelling** in an experimental business context.


### 🚰 Data Source
- Kaggle Dataset → [Fast Food Marketing Campaign A/B Test](https://www.kaggle.com/datasets/chebotinaa/fast-food-marketing-campaign-ab-test)

| Column | Description |
|:--|:--|
| `MarketID` | Unique identifier for each market |
| `MarketSize` | Market size category (`Small`, `Medium`, `Large`) |
| `LocationID` | Unique identifier for each restaurant location |
| `AgeOfStore` | Age of store in years |
| `Promotion` | Promotional campaign applied (`1`, `2`, `3`) |
| `week` | Week number (1 – 4) |
| `SalesInThousands` | Weekly sales amount in $ thousands |

---

### 🧪 Statistical Methodology
**Approach:**  
Because the distribution of sales was **non-normal**, non-parametric and resampling methods were used.

| Step | Method | Purpose |
|:--|:--|:--|
| 1️⃣ | **Bootstrapping (1 000 iterations)** | Estimate sampling distribution of the median sales |
| 2️⃣ | **Kruskal–Wallis H test** | Test for overall group differences across all promotions |
| 3️⃣ | **Pairwise Mann–Whitney U-tests** | Identify which specific promotions differ |
| 4️⃣ | **95 % Confidence Intervals** | Evaluate overlap of bootstrapped medians |

---



### 🧠 Interpretation & Insights
- 🥇 **Promotion 1** achieved the **highest median sales** ($ 55 k), with a confidence interval **non-overlapping** the others → statistically superior performance.  
- 🥈 **Promotion 3** performed moderately ($ 51 k) — slightly below Promo 1 but above Promo 2.  
- 🥉 **Promotion 2** consistently under-performed ($ 45 k).  
- Both global and pairwise tests confirm **statistically significant differences** between promotions.  
- The results suggest that the creative or discount structure in **Promotion 1** produced a meaningful uplift in weekly store sales.

---

### ⚠️ Limitations
- Data covers **only four weeks**, limiting long-term insight.  
- Analysis aggregated at the **store-promotion level**, without controlling for demographics or regional variance.  
- Sales were expressed only in thousands of dollars — finer transaction-level metrics unavailable.  
- Results reflect **one campaign cycle**; replicating across periods would strengthen reliability.  

---

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
    
    # Download latest version
    path = kagglehub.dataset_download("chebotinaa/fast-food-marketing-campaign-ab-test")
    
    print("Path to dataset files:", path)
   ```

---

## 👤 Author

**Guy Winfield**  
📧 Discord: `@guyw7698`  


---

## 🗓 Version History
- 0.1 Initial Release — Fast Food A/B Testing Project 