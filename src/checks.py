def check_missing_values(df):
    return df.isnull().sum().to_dict()

def check_duplicates(df):
    return df.duplicated().sum()