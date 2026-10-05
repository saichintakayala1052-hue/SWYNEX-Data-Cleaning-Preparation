# SWYNEX-Data-Cleaning-Preparation
 Identifying missing values, duplicate records, incorrect data types and inconsistent values. Clean the dataset using Excel, SQL or Python.
 
# Titanic Dataset – Data Cleaning Project

## Objective
Identify and clean missing values, duplicate records, incorrect data types, and inconsistent values in a public Titanic dataset.

## Dataset
The supplied Titanic dataset contains **891 records and 12 columns**.

## Data Quality Findings

- Missing `Age`: **177**
- Missing `Cabin`: **687**
- Missing `Embarked`: **2**
- Exact duplicate rows: **0**
- Duplicate `PassengerId` values: **0**
- `Name` had **2 trailing-space records**, which were standardized.
- `Sex` values were standardized to `Male` / `Female`.
- `Embarked` values were standardized to uppercase.
- Numeric columns were explicitly converted to numeric data types.

## Cleaning Steps

### 1. Missing Values
- `Age`: Filled using the median age for the passenger's `Pclass` and `Sex`; overall median used as fallback.
- `Embarked`: Filled using the most frequent value.
- `Cabin`: Missing values replaced with `Unknown` because the absence of a recorded cabin is meaningful and should not be treated as a real cabin number.

### 2. Duplicate Records
Exact duplicate rows and duplicate `PassengerId` records were checked and removed if present.

### 3. Incorrect Data Types
Numeric fields were converted to numeric types:
`PassengerId`, `Survived`, `Pclass`, `Age`, `SibSp`, `Parch`, and `Fare`.

### 4. Inconsistent Values
Text fields were trimmed. `Sex` was standardized to `Male/Female`, and `Embarked` to uppercase codes.

## Files

- `data/titanic_raw.tsv` – original uploaded dataset
- `data/titanic_cleaned.csv` – cleaned dataset
- `data/data_quality_audit.csv` – initial quality audit
- `data/post_cleaning_audit.csv` – post-cleaning audit
- `scripts/data_cleaning.py` – reproducible Python cleaning script

## Tools
Python, Pandas, CSV/TSV

## Result
The cleaned dataset is ready for analysis and can be uploaded to GitHub as a data-cleaning portfolio project.
