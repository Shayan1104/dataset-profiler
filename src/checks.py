def check_missing_values(df):
    return df.isnull().sum().to_dict()

def check_duplicates(df):
    return df.duplicated().sum()
def validate_schema(df):
    expected_columns = ["id", "name", "age", "salary"]
    return list(df.columns) == expected_columns