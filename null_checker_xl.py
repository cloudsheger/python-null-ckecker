import pandas as pd

def check_null_values(file_path, sheet_name, column):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    if df[column].isnull().values.any():
        print(f'Null value found in column "{column}"')
    else:
        print(f'No null values found in column "{column}"')

# Example usage
check_null_values('data.xlsx', 'test', 'column1')
