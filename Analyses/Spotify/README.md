# Top 50 Spotify Tracks Analysis
This analyse looks at the top 50 Spotify tracks from 2020 to identify patterns and trends in successful music. The aim is to uncover insights that can guide future song creation, maximising the chances of producing a hit that ranks as high as possible.


## Recommendations
Target Dominant Genres: 
- Focus on Pop and Hip-Hop/Rap since they make up 70% of the top 50 tracks. 
- Consider fusing Pop elements with Hip-Hop or Dance/Electronic to capture a wider audience. 
- Aim for a danceability score > 0.7 — 64% of top 50 tracks meet this mark.

However to make a concrete assessment we'd need more data. - Lacking Data. We could consider scraping the top 50 songs for each week of 2020 to build a more robust dataset.

## Summary of Analysis
After cleaning and consolidating genre categories (including niche genres):

Genres of the Top 50:
- Pop: 40%
- Hip-Hop / Rap: 30% 
- Dance / Electronic: ~14% 
- Other / Niche Genres: ~16%

Interesting Findings:
- Correlations suggest highly danceable 'Pop' songs (-0.47) have the best chance at rank higher in the charts   
- 64% of songs in are highly danceable (On a scale of 0 - 1, in this case over 0.7)
- Dance/Electronic on average (-5.3) has the loudest music but much louder & queiter music can be found in other categories such as Pop and Hip-Hop/Rap. There is a wide variety of music loudness.
- Dua Lipa is the only artist to feature at least 3 songs in the top 50
- Pop (40%) & Hip-Hop (30%) dominance as they make ip 70% of top 50 tracks.


Artist Representation:
- Out of 40 unique artists, 7 artists have multiple tracks in the Top 50.
- Variability Within Genres 
  - Significant variance in loudness across tracks within the same genre. 
  - Dance/Electronic music tends to be the loudest on average. 
  - Pop and Hip-Hop tracks span a wide loudness range, from very quiet to very loud.



## Limitations of the Data
Overall, the dataset is in good shape with no missing values. However, there are several points to note:

- Lacking Data
  - To make more sophisticated correlations, bigger comparisons in distributions we need more than 50 songs. We could consider scraping the top 50 songs for each week of 2020 to build a more robust dataset.

- Distribution Issues 
  - Certain float-based fields display unusual distributions:
    - 'Instrumentalness' is heavily skewed to 0. 
    - Energy shows a dip between 0.6 and 0.7, this could be random and due to insufficient data but should be consideration.

- Data Cleaning and Adjustments
  - rank field required updating. 
  - duration field stored in milliseconds needed conversion to a more usable format. 
  - Introduced a new genre field to consolidate smaller niche genres into broader categories.



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