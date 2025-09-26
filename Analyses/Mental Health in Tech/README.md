# 📊 Mental Health in Tech — Analysis Summary
### Goal & Scope

This analysis explores mental health in the technology sector, using survey data to understand:
- Demographics of respondents.
- Prevalence and diagnosis of mental health disorders.
- Comfort levels in discussing mental health in the workplace.
- Employer support and stigma-related factors.

The goal was to practice exploratory data analysis (EDA) and data visualization while drawing actionable insights about workplace mental health.


### 🔑 Key Findings

**Demographics**
- Age skewed toward younger working professionals.
- Gender imbalance in respondents (tech-heavy male representation).
  - Majority respondents aged 18–35 (≈65%).
  - Gender imbalance: ~70% male, ~25% female, ~5% non-binary/other.

**Prevalence of Mental Health Disorders**
- Significant proportion of respondents (Approx 40%) reported experiencing or being diagnosed with a mental health condition.
- Many reported interference of mental health with daily work and productivity.

**Workplace Comfort & Stigma**
- Respondents were less comfortable discussing mental health with employers/supervisors (~35%) compared to coworkers or family/friends (~70%). 
- Stigma and fear of negative career consequences remained a barrier.

**Employer Support**
- 70% agreed employers supported physical health, but only 40% agreed on mental health support.

**Trends Across Surveys (2017 vs 2019)**
- Gradual improvement in willingness to discuss mental health at work.
- Some positive shifts in employer recognition of mental health importance.

### ⚡️ One Chart to Rule them all
These two charts show the perceived relationship between the importance of physical and mental health, and the levels of industry support for mental health:

First chart:
- In both years (2017 in red, 2019 in blue), responses cluster strongly in the mid-to-high importance range (around values 4–8).
- The diagonal line represents a one-to-one relationship—where mental health is rated as equally important as physical health. Points below the line indicate that employers place greater importance on physical health relative to mental health.
- A higher concentration of data falls below the line, suggesting that employers tend to prioritize physical health over mental health.

Second chart:
- This chart shows the distribution of perceived industry support for mental health on a scale from 1 (Very Low) to 5 (Very High).
- The distributions are nearly identical between 2017 and 2019, indicating no meaningful progress over this period. The median value remains below 3, reflecting generally low levels of perceived support.


![Physical vs Mental Health Importance](images/Physical%20vs%20Mental%20Health%20Importance.png)


### 📌 Key Takeaways
- Workplace stigma persists: Mental health conversations are still riskier with managers than with peers.
  - Only ~1 in 3 respondents feel safe disclosing to supervisors. 
- Support gap: Employers provide more visible support for physical health than mental health.
  - Employers are 30pp more likely to be seen as supporting physical health vs. mental health. 
- Need for policies: Training, clear policies, and cultural changes are necessary to normalize mental health discussions.
- Data-driven monitoring: Continued survey analysis is vital to track progress over time.


## Limitations of the Data
There were a number of limitations with the dataset:

- Limited Data:
  - The number of respondents varied wildly between 2014 and 2016 
- Lacking Consistency
  - Many fields lack consistent responses over tine making year to year comparisons difficult
- Stale Data
  - The latest survey responses were from 2019 which is a full 6 years ago. 
  - Many events have happened since this data was collected such as Covid-19, Working From Home culture which would have greatly affected tech workers.
  - This makes this data much less applicable for current day insights. 


## Getting Started

### Prerequisites
- Python 3.6 or later
- Jupyter Notebook
- pandas
- matplotlib
- seaborn
- statsmodels
- duckdb

You can also find the Google Sheets doc which helped group the questions in the following link:
https://docs.google.com/spreadsheets/d/1BklBsd5qp3z7aleweZmFdswfzLq4Tqv0QIZhPEaR4Wc/edit?usp=sharing

### Installation
1. Clone the repository
```
gh repo clone TuringCollegeSubmissions/gwinfi-DS.v3.2.1.5
```
- Install dependencies: None


You will need to download the Mental Health dataset, you can follow either of these steps:

2a. Download from the terminal 

```
import kagglehub

# Download latest version
path = kagglehub.dataset_download("anth7310/mental-health-in-the-tech-industry")

print("Path to dataset files:", path)
```
- Once downloaded you will need to move the csv file from your cache to the cloned repo directory 
  - On mac you can find the download here: /Users/yourusername/.cache/kagglehub/datasets/


2b. Download zip file from kaggle
- You can do this via https://www.kaggle.com/datasets/anth7310/mental-health-in-the-tech-industry
- Please make sure sqlite database is saved in the directory where you've downloaded 'Analysis: Mental Health in Tech.ipynb'  

## The Notebook

The 'Analysis: Mental Health in Tech.ipynb' Notebook is made up of 5 sections:
- **Summary**: A summary of the most important finings found in the notebook
- **Imports**: A short section to group all required packages to successfully run the notebook
- **Data Preparation / Cleaning**: This section is dedicated to importing the data, cleaning and adding additional fields.
- **Exploratory Data Analysis**: Analysis to find any overarching trends
- **Probabilities - What's the Likelihood**: A small segment exploring the various categorical probability based on demographics.  

## Authors
Contributors names and contact info:

Guy Winfield

Discord: @guyw7698

## Version History
- 0.1 Initial Release 
