# ETL Cleaning Project

This is a simple ETL (Extract, Transform, Load) pipeline built in Python.  
It reads a CSV file, detects missing values, removes incomplete rows, and exports the cleaned data to a new CSV file.

### Features:
- Extract: Reads user-provided CSV file
- Transform: Drops rows with missing data
- Load: Saves cleaned data as `cleaned_filename.csv`

### How to run:
```bash
python3 etl_script.py
