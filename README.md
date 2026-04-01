# IS537 Data Cleaning Project

**Chicago Food Inspections – Data Quality & Cleaning Analysis**

## Overview

This project focuses on evaluating and improving the quality of the Chicago Food Inspections dataset for use in a restaurant recommendation system. While the dataset is publicly available and widely used, it contains several real-world data issues such as duplicates, missing values, inconsistent formats, and policy-driven changes over time.

The goal of this project is to identify these issues, apply appropriate cleaning strategies, and assess how data quality impacts downstream analysis.

---

## Datasets Used

* **Chicago Food Inspections Dataset**
  Source: Chicago Data Portal
  Contains inspection results, violations, and restaurant details.

* **Chicago Business Licenses Dataset**
  Source: Chicago Data Portal
  Used to cross-check and validate restaurant records.

> Note: Raw datasets are not included in this repository due to size constraints. They can be downloaded directly from the Chicago Data Portal.

---

## Project Structure

```
is537-project/
│
├── data/
│   ├── raw/              # (not tracked) original datasets
│   ├── cleaned/          # (not tracked) cleaned datasets
│
├── scripts/
│   ├── 01_profiling.py   # initial data quality assessment
│   ├── 02_cleaning.py    # data cleaning and transformations
│   ├── 03_matching.py    # dataset integration and matching
│   ├── 04_impact.py      # impact analysis of cleaning
│
├── outputs/
│   └── tables/           # summary outputs used for analysis
│
├── requirements.txt
└── README.md
```

---

## Key Data Quality Issues Identified

* Duplicate inspection records
* Missing values in key fields (risk, results, violations)
* Inconsistent text formatting (names, addresses)
* Free-text violations that are difficult to analyze
* Structural change in violation definitions after July 1, 2018

---

## Cleaning Approach

The cleaning process was structured in phases:

### 1. Data Profiling

* Checked missing values across key columns
* Identified duplicate inspection IDs
* Analyzed distributions (results, years)

### 2. Data Cleaning

* Removed duplicate inspection records
* Standardized text fields (uppercase, trimming whitespace)
* Parsed dates and extracted year information
* Created pre/post-2018 policy indicator

### 3. Data Integration

* Matched food inspections with business licenses
* Used name and address fields for approximate matching

### 4. Impact Analysis

* Compared dataset before and after cleaning
* Evaluated how cleaning affected distributions and counts

---

## How to Run the Project

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run scripts in order

```
python scripts/01_profiling.py
python scripts/02_cleaning.py
python scripts/03_matching.py
python scripts/04_impact.py
```

---

## Outputs

The `outputs/tables/` folder contains summary tables such as:

* Missing value reports
* Distribution of inspection results
* Year-wise inspection counts
* Before vs after cleaning comparison

---

## Key Takeaways

* Even high-quality public datasets contain significant issues
* Duplicate and missing data can directly impact analysis outcomes
* Policy changes (like the 2018 violation update) must be explicitly handled
* Data cleaning is essential for building fair and reliable recommendation systems

---

## Limitations

* Violations are stored as free text and require advanced parsing for deeper analysis
* Matching between datasets is approximate and may introduce errors
* Inspections represent point-in-time observations, not continuous conditions

---

## Future Improvements

* Apply NLP techniques to structure violation data
* Improve entity matching using fuzzy matching or embeddings
* Incorporate recency-based scoring for recommendations

---

## Author

Harshi Dagli
MS Information Management (Data Analytics)
University of Illinois Urbana-Champaign

---