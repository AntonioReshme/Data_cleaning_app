import pandas as pd
import numpy as np
import openpyxl
import xlrd
import time
import os
import random

def data_cleaning_master(data_path,data_name):
    print("Thank you for entering the details!!")

    if not os.path.exists(data_path):
        print("Invalid path..Please enter the correct file..")
        return
    else:
        if data_path.endswith(".csv"):
            print("Dataset is in csv file")
            data = pd.read_csv(data_path,encoding_errors="ignore")

        elif data_path.endswith(".xlsx"):
            print("Dataset is in excel file")
            data = pd.read_excel(data_path)
        else:
            print("Invalid file")
            return

    print(f"Total number of rows:{data.shape[0]} and \nTotal number of columns:{data.shape[1]}")
    duplicates = data.duplicated()
    total_duplicates = data.duplicated().sum()

    print(f"Total number of dulpicates in tha dataset:{total_duplicates}")

    if total_duplicates>0:
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f"{data_name}_duplicates.csv",index=None)

    df = data.drop_duplicates()

    missing_values_colm = df.isnull().sum()
    total_missing_values = df.isnull().sum().sum()

    print(f"Missing values by each column in the dataset:{missing_values_colm}")
    print(f"Total missing values in the dataset:{total_missing_values}")

    columns = df.columns

    for cols in columns:
        if df[cols].dtypes in (float,int):
            df[cols] = df[cols].fillna(df[cols].mean())
        else:
            df.dropna(subset=cols,inplace=True)
    print(f"Congrats!!Your Dataset is cleaned now..\nTotal number of rows:{df.shape[0]}\nTotal number of columns:{df.shape[1]}")
    df.to_csv(f"{data_name}_cleaned_data.csv",index=None)
    print("Dataset is saved")

if __name__=="__main__":

    data_path = input("Enter the datasetpath:")
    data_name = input("Enter the datasetname:")

    data_cleaning_master(data_path,data_name)
