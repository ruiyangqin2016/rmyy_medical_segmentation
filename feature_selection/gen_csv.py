import xlrd
import csv
import pandas as pd

data = pd.read_excel("tof_prognosis_ct_measures_20220113.xlsx", sheet_name='Sheet1')
# print(data.head())
# l = data.values.tolist()
data.to_csv('data.csv', encoding='utf-8', index=False)