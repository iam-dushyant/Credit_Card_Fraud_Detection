import pandas as pd
import matplotlib as plt

# Importing dataframe
df = pd.read_csv("PS_20174392719_1491204439457_log.csv")

# Determining Dataframe properties
print("\n The shape of the dataframe is", df.shape)
print("\n The column names of the dataframe are:")
print(df.columns.tolist())

'''
Having observed the column name 'oldbalanceOrg' is an odd one out, as other columns
relating to origin account end with 'Orig'. To avoid unnecessary typo errors, changing
this to match other columns
'''
df.rename(columns={'oldbalanceOrg' : 'oldbalanceOrig'}, inplace=True)
print("\n The modified column names are:")
print(df.columns.tolist())