def check_missing_values(df):
    return df.isnull().sum().to_dict()

def check_duplicates(df):
    return df.duplicated().sum()

def detect_outliers(df):
    outliers = {}
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers[col] = int(((df[col] < lower) | (df[col] > upper)).sum())

    return outliers