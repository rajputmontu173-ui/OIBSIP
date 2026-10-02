# OIBSIP Data Analytics — Level 1 Task 3
## Cleaning Data

### Objective
Transform a deliberately messy customer dataset into a clean, analysis-ready dataset and document each cleaning decision.

### Tech Stack
Python, pandas, numpy, Jupyter Notebook

### Files
- `Cleaning_Data.ipynb` — complete notebook
- `cleaning_data.py` — standalone Python version
- `messy_customer_data.csv` — intentionally messy source dataset
- `cleaned_customer_data.csv` — cleaned output dataset
- `README.md` — documentation

### Cleaning Methods
- Null count and data quality report
- Mode imputation for categorical fields
- Median imputation for numeric fields
- Row deletion for missing transaction dates
- Duplicate removal
- Category/text standardisation
- IQR outlier detection
- Invalid age correction
- Data type correction
- Before-vs-after quality summary
- Cleaned CSV export

### Run
```bash
pip install pandas numpy jupyter
python cleaning_data.py
```

Or open the notebook:
```bash
jupyter notebook Cleaning_Data.ipynb
```

## Task Checklist
- [x] Data quality report
- [x] Missing data handling with justification
- [x] Duplicate removal
- [x] Standardisation
- [x] IQR outlier detection and documented decision
- [x] Data type correction
- [x] Before vs after summary
- [x] Save cleaned dataset to a new CSV
