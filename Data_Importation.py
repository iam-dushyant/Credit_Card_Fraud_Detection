# Libraries required
import pandas as pd
import kaggle
import zipfile
import os

!kaggle datasets download -d ealaxi/paysim1

zip_path = "paysim1.zip"
extract_path = os.getcwd()
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
    
df = pd.read_csv("PS_20174392719_1491204439457_log.csv")
print("First 5 records:", df.head())