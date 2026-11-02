# Dataset Profiler

A lightweight Python tool that analyses raw tabular CSV datasets and generates structured JSON data quality reports to support exploratory data analysis, data understanding, and preprocessing prior to machine learning.

---

## 📌 The Problem

Before training machine learning models or designing data transformation pipelines, data practitioners must thoroughly understand the quality, structure, and quirks of their raw datasets. In practice, raw incoming data frequently suffers from silent data quality defects:

- **Missing or null values** that cause training errors or distorted feature distributions.
- **Duplicate records** that introduce training bias and data leakage between train/test splits.
- **Schema discrepancies** where missing or misspelled columns break downstream ingestion scripts.
- **Numerical outliers** that skew normalization, statistical aggregations, and model convergence.

Performing these checks manually in ad-hoc scripts or one-off Jupyter notebooks is repetitive, error-prone, and difficult to integrate into automated workflows. **Dataset Profiler** solves this by providing a lightweight, modular, and automated profiling pipeline that audits raw CSV data and outputs machine-readable JSON quality reports.

---

## 🚀 What It Does

1. **Ingests Raw Data**: Safely loads tabular CSV files using pandas with robust exception handling.
2. **Executes Quality Checks**: Runs validation metrics across the dataset to measure missing values, row duplication, schema conformity, and numerical outlier frequency.
3. **Generates Structured Reports**: Outputs a structured `quality_report.json` file and prints a formatted summary to the console for quick terminal inspection.

---

## ✨ Features (From Codebase)

The codebase is organized modularly under `src/`:

- **Safe CSV Data Ingestion** ([`src/loader.py`](file:///c:/Users/hp/Desktop/New%20folder/data_quality_tool/src/loader.py)): Handles file loading via `load_data(file_path)` with try-catch error handling to safeguard against missing or malformed files.
- **Missing Value Detection** ([`src/checks.py`](file:///c:/Users/hp/Desktop/New%20folder/data_quality_tool/src/checks.py)): Computes per-column null value counts (`check_missing_values`) using pandas' vectorized `.isnull().sum()`.
- **Duplicate Row Detection** ([`src/checks.py`](file:///c:/Users/hp/Desktop/New%20folder/data_quality_tool/src/checks.py)): Identifies the total count of duplicate rows across the dataset via `check_duplicates`.
- **Schema Validation** ([`src/checks.py`](file:///c:/Users/hp/Desktop/New%20folder/data_quality_tool/src/checks.py)): Includes `validate_schema` to verify expected column headers against loaded data.
- **Outlier Detection via IQR** ([`src/checks.py`](file:///c:/Users/hp/Desktop/New%20folder/data_quality_tool/src/checks.py)): Includes `detect_outliers` which calculates Interquartile Range ($Q1$, $Q3$, and $\text{IQR} = Q3 - Q1$) across numerical columns (`int64`, `float64`) and counts values outside $[Q1 - 1.5 \times \text{IQR}, Q3 + 1.5 \times \text{IQR}]$.
- **JSON Report Generation** ([`src/reporter.py`](file:///c:/Users/hp/Desktop/New%20folder/data_quality_tool/src/reporter.py)): Formats validation findings into JSON (`generate_report`), persists the result to `quality_report.json`, and pretty-prints the output to stdout.

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Data Analysis**: [Pandas](https://pandas.pydata.org/)
- **Output Format**: JSON (Python standard library `json`)

---

## 📁 Project Structure

```text
dataset-profiler/
├── data/
│   └── read.csv              # Sample CSV dataset for profiling
├── src/
│   ├── __init__.py           # Package marker
│   ├── checks.py             # Data quality checks (missing values, duplicates, schema, outliers)
│   ├── loader.py             # CSV loading utility with error handling
│   └── reporter.py           # Report formatting and JSON file exporter
├── main.py                   # Pipeline execution entry point
├── quality_report.json       # Generated JSON quality report
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore rules
└── README.md                 # Project documentation
```

---

## ⚡ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/Shayan1104/dataset-profiler.git
cd dataset-profiler
```

### 2. Set Up a Virtual Environment & Install Dependencies
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Linux / macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Profiler
Execute the pipeline using the entry point in `main.py`:

```bash
python main.py
```

`main.py` loads the sample data from `data/read.csv`, runs the quality checks, displays the report on the terminal, and saves the results to `quality_report.json`.

---

## 📊 Sample Output Format

When running on `data/read.csv`, the tool prints to the console:

```text
=== DATA QUALITY REPORT ===
{
    "missing_values": {
        "id": 0,
        "Name": 1,
        "age": 0,
        "salary": 1
    },
    "duplicate_rows": 0
}
```

The resulting [`quality_report.json`](file:///c:/Users/hp/Desktop/New%20folder/data_quality_tool/quality_report.json) excerpt:

```json
{
    "missing_values": {
        "id": 0,
        "Name": 1,
        "age": 0,
        "salary": 1
    },
    "duplicate_rows": 0
}
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
