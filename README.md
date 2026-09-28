# ApexPlanet Data Analytics Internship – Task 1

## Overview

This repository contains my work for Task 1 of the **ApexPlanet Data Analytics Internship**.

The task focused on **data cleaning and transformation using Python and Pandas**. The raw sales dataset was provided as part of the internship task. The workflow cleans missing values, fixes duplicated order identifiers, standardizes text fields, converts dates, creates useful analytical columns, validates sales calculations, and exports a cleaned dataset.

> **Dataset note:** The original internship dataset was provided by ApexPlanet Software Pvt. Ltd. Public sharing of the dataset has been permitted for this project.

## Objectives

- Inspect the raw sales dataset
- Identify missing values and duplicate identifiers
- Handle missing `Age` and `City` values
- Resolve repeated `Order_ID` values
- Convert order dates to a proper datetime format
- Standardize text columns
- Create age-group and date-based analytical columns
- Validate `Total_Sales`
- Export the cleaned data to CSV

## Dataset

The original dataset contains **1,000 rows and 12 columns**:

- `Order_ID`
- `Order_Date`
- `Customer_ID`
- `Customer_Name`
- `Age`
- `Gender`
- `City`
- `Product`
- `Category`
- `Quantity`
- `Unit_Price`
- `Total_Sales`

The cleaned dataset contains the original 12 columns plus:

- `Age_Group`
- `Order_Month`
- `Order_Year`

## Data Quality Issues Identified

The assessment identified:

- **20** missing `Age` values
- **13** missing `City` values
- **1** repeated `Order_ID` affecting **9 rows**
- No fully duplicated rows
- `Order_Date` stored as text rather than a date type
- No categorical spelling/case issues identified
- Quantity and age ranges were considered reasonable
- High-value sales were treated as legitimate values associated with different product categories

## Cleaning & Transformation Process

### 1. Missing values

- Missing `Age` values were replaced with the median age.
- Missing `City` values were replaced with `Unknown`.

### 2. Duplicate Order IDs

The repeated `Order_ID` issue was investigated. Because the affected records represented different customers, dates, and products, the IDs were reassigned to unique order identifiers.

### 3. Date conversion

`Order_Date` was converted from text to a Pandas datetime column.

### 4. Text standardization

The following columns were stripped of unnecessary whitespace and standardized to title case:

- City
- Gender
- Product
- Category

### 5. Feature creation

An `Age_Group` column was created using the following groups:

- 18–25
- 26–35
- 36–45
- 46–55
- 56+

Two date-based columns were also created:

- `Order_Month`
- `Order_Year`

### 6. Sales validation

The script checks whether:

`Total_Sales = Quantity × Unit_Price`

The calculated values are rounded to two decimal places and compared with the existing `Total_Sales` values.

## Technologies Used

- Python
- Pandas
- Excel
- CSV
- Data Cleaning
- Data Transformation

## Project Structure

```text
ApexPlanet-Data-Analytics-Internship/
│
├── README.md
├── data_cleaning.py
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── ApexPlanet_DataAnalytics_Dataset.xlsx
│   └── Cleaned_Sales_Dataset.csv
│
└── documentation/
    ├── Data_Dictionary.xlsx
    └── Data_Quality_Assessment.xlsx
```

If permitted by the internship/company, supporting datasets and documentation can be added separately.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ApexPlanet-Data-Analytics-Internship.git
cd ApexPlanet-Data-Analytics-Internship
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Update the input file path

Open `data_cleaning.py` and change the `file_path` variable to the location of the internship Excel dataset on your computer.

### 4. Run the script

```bash
python data_cleaning.py
```

The script will generate:

```text
Cleaned_Sales_Dataset.csv
```

## Key Learning Outcomes

Through this task, I practiced:

- Data quality assessment
- Missing-value handling
- Duplicate detection and resolution
- Date and text transformation
- Feature engineering
- Data validation
- Exporting cleaned analytical data
- Building a reproducible Pandas workflow

## Internship

**ApexPlanet Software Pvt. Ltd.**  
Data Analytics Internship — 2026

## Author

**Mohammed Zeshan Mohiuddin**

GitHub: `https://github.com/mohammedzeshanm7-tech`
