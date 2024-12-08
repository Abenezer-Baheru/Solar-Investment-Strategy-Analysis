import os
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
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
print(summary_stats)

# Check for missing values
missing_values = data.isnull().sum()
print('Missing Values:')
print(missing_values)

# Outliers detection
for column in ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']:
    plt.figure()
    data[column].plot(kind='box')
    plt.title(f'Boxplot of {column}')
    plt.show()

# Plot time series for GHI, DNI, DHI, and Tamb
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data.set_index('Timestamp', inplace=True)
data[['GHI', 'DNI', 'DHI', 'Tamb']].plot(subplots=True, figsize=(10, 8))
plt.show()

# Visualize correlations using a heatmap
correlation_matrix = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Wind Speed Distribution Analysis
data['WS'].plot(kind='hist', bins=30)
plt.title('Wind Speed Distribution')
plt.xlabel('Wind Speed (m/s)')
plt.show()

# Examine the influence of relative humidity on temperature
sns.scatterplot(x='RH', y='Tamb', data=data)
plt.title('Relative Humidity vs. Ambient Temperature')
plt.show()

# Create histograms for key variables
data[['GHI', 'DNI', 'DHI', 'WS', 'Tamb']].hist(bins=30, figsize=(10, 8))
plt.show()

# Z-Score Analysis
data['GHI_zscore'] = zscore(data['GHI'])
outliers = data[data['GHI_zscore'].abs() > 3]
print('Outliers:')
print(outliers)

# Bubble Chart Analysis
sns.scatterplot(x='GHI', y='Tamb', size='WS', hue='RH', data=data, sizes=(20, 200))
plt.title('GHI vs. Tamb vs. WS (Bubble Size: RH)')
plt.show()