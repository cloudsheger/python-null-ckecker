import pandas as pd
import argparse

def check_null_values(file_path, sheet_name, column):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    if df[column].isnull().values.any():
        print(f'Null value found in column "{column}"')
    else:
        print(f'No null values found in column "{column}"')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="The path to the Excel file")
    parser.add_argument("sheet_name", help="The name of the sheet in the Excel file")
    parser.add_argument("column", help="The name of the column to check for null values")
    args = parser.parse_args()
    check_null_values(args.file_path, args.sheet_name, args.column)

 #python script.py data.xlsx Sheet1 name   