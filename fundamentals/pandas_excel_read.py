import pandas as pd

# pip install xlrd
# pip instal openpyxl
# pip install pandas

# df = pd.read_excel("pandas.xlsx")
# print(df)

# df_sheet_name = pd.read_excel("pandas.xlsx", sheet_name="Sheet2")
# print(df_sheet_name)

# df_sheet_index = pd.read_excel('pandas.xlsx', sheet_name=0)
# print(df_sheet_index)


df_sheet_all = pd.read_excel('pandas.xlsx', sheet_name=[0, 1])
# print(df_sheet_all)
# print(df_sheet_all[1])
print(df_sheet_all[0][1])
