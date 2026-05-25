# Cafe Sales Data Analysis

## Project Overview

This project focuses on cleaning, validating, and analyzing a dirty cafe sales dataset using Python and Pandas.

The dataset contains transactional sales data with missing values, inconsistent entries, invalid records, and incorrect data types.
The main goal of this project was to perform data cleaning and exploratory data analysis (EDA) to extract useful business insights.

## Technologies Used
-Python

-Pandas

-NumPy

-Matplotlib

-Seaborn

-Jupyter Notebook

## Project Structure
PROJECT/
│
├── DATA/
│   └── raw/
│       └── dirty_cafe_sales.csv
│
├── notebooks/
│   ├── 01-data_understanding.ipynb
│   ├── 02-data_cleaning.ipynb
│   └── 03-data_analysis.ipynb
│
├── cleaning.py
│
└── README.md

## Data Cleaning Process
The following cleaning steps were performed:

-Replaced invalid entries such as "ERROR", "UNKNOWN" and similar values with NaN

-Removed extra spaces from text columns

-Standardized text values to lowercase

-Converted numerical columns to numeric types

-Converted the Transaction Date column to datetime format

-Checked for duplicated records

-Validated invalid and inconsistent values

-Recalculated the Total Spent column using:

## Exploratory Data Analysis (EDA)
The project includes several analyses and visualizations, such as:

-Most sold products

-Revenue by product

-Monthly sales analysis

-Revenue by location

-Payment methods analysis

-Sales trends over time

## Main Insights
-Coffee and juice were the most sold items

-Salad generated the highest revenue

-Sales remained relatively stable throughout the year, with a slight increase in June

-Payment methods showed balanced usage among customers

-In-store sales generated higher revenue compared to other locations

## Example Visualizations
Examples of generated visualizations include:

-Bar charts

-Revenue analysis graphs

-Monthly sales trends

-Payment method distributions

## Conclusion
This project demonstrates a complete real-world data analysis workflow, including:

-Data cleaning

-Data validation

-Exploratory data analysis

-Data visualization

-Business insight extraction

The project was developed to strengthen practical skills in Python and data analysis.

## Author
Renan Sampaio.