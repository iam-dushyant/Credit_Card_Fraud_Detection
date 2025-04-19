# Libraries required
import pandas as pd
import kaggle
import zipfile
import os

!kaggle datasets download -d mlg-ulb/creditcardfraud

zip_path = "creditcardfraud.zip"
extract_path = os.getcwd()
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
    
df = pd.read_csv("creditcard.csv")
print("First 5 records:", df.head())