# Coursera Dataset EDA
### Goal & Scope

Exploratory data analysis of scraped Coursera courses focusing on difficulty, enrolment, certificate type, and ratings.

**Aim**: build a general understanding of course supply, demand (enrolment), and quality (weighted ratings).

## Key Findings
Dataset size: 891 courses.
#### Ratings
- Median rating ≈ 4.70/5 
- Ratings by certificate type (mean weighted): Courses 4.688, Specializations 4.661, Professional Certificates 4.689

#### General
- Enrolment is highly concentrated (long tail with a few mega-courses at 1–3M+ students).
- Professional Certificates are scarce but have the highest average enrolment per course, suggesting strong credential/value pull, though overall demand share is still small because supply is tiny.
- Beginner content dominates the catalogue (>50%), but ratings are uniformly high (4.6–4.7+) across categories.
- Total enrolments ≈ 80.7M, with ~90.6k per course on average (median ~42k) — very right-skewed.


#### Certificate type Mix
- Courses: 582 ( 65.3% of all courses)
- Specializations: 297 ( 33.3%)
- Professional Certificates: 12 ( 1.3%)

#### Difficulty mix
- Beginner: 487 (54.7%)
- Intermediate: 198 (22.2%)
- Mixed: 187 (21.0%)
- Advanced: 19 (2.1%)


## Takeaways
- Courses skew generalist and entry-level, while advanced certificate types become more specialized and challenging which are less common on Coursera.
- Coursera offers a huge varierty of subjects which are excellent for introductory/entry level learning on any given topic
- If you want to study the best of the best:
  - Best Rated Organisation: Google - Spectrum Sharing (4.82 weighted rating)
  - Best Rated Course: Machine Learning by Stanford University (4.89 weighted rating)
- If you want to see how bad it can get:
  - Worst Rated Organisation: The State University of New York (4.47 weighted rating)
  - Worst Rated Course: How To Create a Website in a Weekend! (Project-Centered Course) by The State University of New York (3.93 weighted rating)


## Limitations of the Data
Overall, the dataset is in good shape with no missing values. However, there are several points to note:

- Lacking Data: To make more sophisticated correlations, bigger comparisons in distributions we need a wider dataset with more varied fields (timestamps, completion rates, price, refunds ..etc)


## Getting Started

### Prerequisites
- Python 3.6 or later
- Jupyter Notebook

_No additional external packages are required._


### Installation
1. Clone the repository
```
git clone https://github.com/TuringCollegeSubmissions/gwinfi-DS.v3.1.4.5.git
```
- Install dependencies: None


You will need to download the Coursera dataset, you can follow either of these steps:

2a. Download from the terminal 

```
import kagglehub

 Download latest version
path = kagglehub.dataset_download("siddharthm1698/coursera-course-dataset")

print("Path to dataset files:", path)
```
- Once downloaded you will need to move the csv file from your cache to the cloned repo directory 
  - On mac you can find the download here: /Users/yourusername/.cache/kagglehub/datasets/


2b. Download zip file from kaggle
- You can do this via https://www.kaggle.com/datasets/siddharthm1698/coursera-course-dataset
- Please make sure coursera_data.csv is saved in the directory where you've downloaded 'Coursera EDA.ipynb'  

## The Notebook

The 'Coursera ESA.ipynb' Notebook is made up of 5 sections:
- **Key Findings**: A summary of the most important finings found in the notebook
- **Imports**: A short section to group all required packages to successfully run the notebook  
- **--- Helper Functions ---** : To streamline the notebook I've grouped helpful functions at the top of the page
- **Data Preparation**: This section is dedicated to importing the data, cleaning and adding additional fields.
- **Exploratory Data Analysis**: Analysis to find any overarching trends

## Authors
Contributors names and contact info:

Guy Winfield

Discord: @guyw7698

## Version History
0.1 Initial Release

0.2 Update Notebook Commentary

0.3 PEP 8 Standards - black