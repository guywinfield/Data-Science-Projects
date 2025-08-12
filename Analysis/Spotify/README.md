# Top 50 Spotify Tracks Analysis

## Key Figures
After cleaning and consolidating genre categories (including niche genres):

Genres of the Top 50:
- Pop: 40%
- Hip-Hop / Rap: 30% 
- Dance / Electronic: ~14% 
- Other / Niche Genres: ~16%

Interesting Findings:
- 64% of songs in are highly danceable (On a scale of 0 - 1, in this case over 0.7)
- Dance/Electronic on average (-5.3) has the loudest music but much louder & queiter music can be found in other categories such as Pop and Hip-Hop/Rap. There is a wide variety of music loudness.
- Dua Lipa is the only artist to feature at least 3 songs in the top 50


## Summary of Analysis
- Pop (40%) & Hip-Hop (30%) dominance as they make ip 70% of top 50 tracks.

- Musical Characteristics 
  - Most tracks are highly danceable (danceability between 0.7–0.9), often paired with high energy scores. 
  - Positive correlation observed between energy and loudness. 
  - Acousticness tends to be higher in Alternative/Indie tracks, reflecting their guitar-based nature.

- Artist Representation 
  - Out of 40 unique artists, 7 artists have multiple tracks in the Top 50.

- Variability Within Genres 
  - Significant variance in loudness across tracks within the same genre. 
  - Dance/Electronic music tends to be the loudest on average. 
  - Pop and Hip-Hop tracks span a wide loudness range, from very quiet to very loud.


## Limitations of the Data
Overall, the dataset is in good shape, with clean field naming and no missing values. However, there are several points to note:

- Data Completeness 
  - No missing values detected. 
  - Minimal cleaning required, though some fields needed adjustments.

- Distribution Issues 
  - Certain float-based fields display unusual distributions:
    - Instrumentalness is heavily skewed between 0 and 0.6, with most values near 0. 
    - Energy shows a dip between 0.6 and 0.7, this could be random and due to insufficient data but should be consideration.

- Data Cleaning and Adjustments
  - rank field required updating. 
  - duration field stored in milliseconds needed conversion to a more usable format. 
  - Introduced a new genre field to consolidate smaller niche genres into broader categories.

- Lacking Data
  - To make more sophisticated correlations, bigger comaprisons in distributions we need more than 50 songs. We could consider scraping the top 50 songs for each week of 2020 to build a more robust dataset.

## Getting Started

### Prerequisites
- Python 3.6 or later
- Jupyter Notebook

_No additional external packages are required._


### Installation
1. Clone the repository
```
git clone https://github.com/TuringCollegeSubmissions/gwinfi-DS.v3.1.3.5
cd '2020 Spotify Top 50 Tracks Analysis'
```
- Install dependencies: None


You will need to download the spotify dataset, you can follow either of these steps:

2a. Download from the terminal

```
import kagglehub

# Download latest version
path = kagglehub.dataset_download("atillacolak/top-50-spotify-tracks-2020")

print("Path to dataset files:", path)
```
- Once downloaded you will need to move the csv file from your cache to the cloned repo directory 
  - On mac you can find the download here: /Users/yourusername/.cache/kagglehub/datasets/


2b. Download zip file from kaggle
- You can do this via https://www.kaggle.com/datasets/atillacolak/top-50-spotify-tracks-2020
- Please make sure spotifytoptracks.csv is saved in the directory where you've downloaded 2020 Spotify Top 50 Tracks Analysis.ipynb  

## The Notebook

The '2020 Spotify Top 50 Tracks Analysis.ipynb' Notebook is made up of 4 sections:
- Data Import & Scoping: Import data and understand how it's made up
- Data Preparations: Based on scoping, refines and cleans data
- Question Requirements: Findings based on requirements in https://github.com/TuringCollegeSubmissions/gwinfi-DS.v3.1.3.5/blob/main/135.md
- Exploratory Data Analysis: Analysis to find any overarching trends

## Authors
Contributors names and contact info:

Guy Winfield

Discord: @guyw7698

## Version History
0.1
Initial Release