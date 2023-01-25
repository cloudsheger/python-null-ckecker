import pandas as pd
import argparse

def check_null_values(file_path, sheet_name, columns):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    for column in columns:
        if column not in df.columns:
            print(f'Column "{column}" not found in the sheet')
            continue
        if df[column].isnull().values.any():
            print(f'Null value found in column "{column}"')
        else:
            print(f'No null values found in column "{column}"')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="The path to the Excel file")
    parser.add_argument("sheet_name", help="The name of the sheet in the Excel file")
    parser.add_argument("columns", help="The names of the columns to check for null values", nargs='+')
    args = parser.parse_args()
    check_null_values(args.file_path, args.sheet_name, args.columns)
