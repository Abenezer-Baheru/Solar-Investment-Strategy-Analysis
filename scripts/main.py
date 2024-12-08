import os
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import gdown

# Define the Google Drive file IDs
benin_file_id = '1tWqBclEvqNpreKvoPznNPMBInykyKGIE'
sierraleone_file_id = '1T72qp5zLFTCy7Ri1R6ydVIIRRDwP6LbZ'
togo_file_id = '1UoaAKfSHWXiRxz2BrHPm3YNf2EWMgn97'

# Define the download URLs
benin_url = f'https://drive.google.com/uc?id={benin_file_id}'
sierraleone_url = f'https://drive.google.com/uc?id={sierraleone_file_id}'
togo_url = f'https://drive.google.com/uc?id={togo_file_id}'

# Download the CSV files
gdown.download(benin_url, 'benin_data.csv', quiet=False)
gdown.download(sierraleone_url, 'sierraleone_data.csv', quiet=False)
gdown.download(togo_url, 'togo_data.csv', quiet=False)

# Load the data into DataFrames
benin_data = pd.read_csv('benin_data.csv')
sierraleone_data = pd.read_csv('sierraleone_data.csv')
togo_data = pd.read_csv('togo_data.csv')

# Combine the data into one DataFrame
data = pd.concat([benin_data, sierraleone_data, togo_data], keys=['Benin', 'Sierra Leone', 'Togo'])

# Calculate summary statistics for each numeric column
summary_stats = data.describe()
# print(summary_stats)

# Missing values
missing_values = data.isnull().sum()
print(missing_values)

# Outliers detection
import matplotlib.pyplot as plt

for column in ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']:
    data[column].plot(kind='box')
    plt.title(f'Boxplot of {column}')
    plt.show()






