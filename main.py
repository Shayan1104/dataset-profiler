from src.loader import load_data
from src.checks import check_missing_values, check_duplicates
from src.reporter import generate_report

def main():
    df = load_data("data/read.csv")

    if df is not None:
        missing = check_missing_values(df)
        duplicates = check_duplicates(df)

        generate_report(missing, duplicates)

if __name__ == "__main__":
    main()