# Solar Radiation Measurement Data Analysis

This project performs an Exploratory Data Analysis (EDA) on Solar Radiation Measurement Data for Benin, Sierra Leone, and Togo. The data includes various measurements such as solar radiation, air temperature, relative humidity, barometric pressure, precipitation, wind speed, and wind direction. The goal is to gain insights into the data through summary statistics, quality checks, time series analysis, correlation analysis, wind analysis, temperature analysis, and more.

## Table of Contents
- [Business Objective](#business-objective)
- [Data Structure](#data-structure)
- [EDA Steps](#eda-steps)
- [Setup](#setup)
- [How to Run](#how-to-run)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Business Objective
The main objective of this analysis is to understand the patterns, trends, and anomalies in the solar radiation measurements and related environmental factors. This can help in optimizing the use of solar energy and improving the maintenance of solar panels.

## Data Structure
Each row in the data contains the following columns:
- `Timestamp` (yyyy-mm-dd hh:mm): Date and time of each observation.
- `GHI` (W/m²): Global Horizontal Irradiance.
- `DNI` (W/m²): Direct Normal Irradiance.
- `DHI` (W/m²): Diffuse Horizontal Irradiance.
- `ModA` (W/m²): Measurements from sensor A.
- `ModB` (W/m²): Measurements from sensor B.
- `Tamb` (°C): Ambient Temperature.
- `RH` (%): Relative Humidity.
- `WS` (m/s): Wind Speed.
- `WSgust` (m/s): Maximum Wind Gust Speed.
- `WSstdev` (m/s): Standard Deviation of Wind Speed.
- `WD` (°N): Wind Direction.
- `WDstdev`: Standard Deviation of Wind Direction.
- `BP` (hPa): Barometric Pressure.
- `Cleaning` (1 or 0): Indicator of cleaning events.
- `Precipitation` (mm/min): Precipitation rate.
- `TModA` (°C): Temperature of Module A.
- `TModB` (°C): Temperature of Module B.

## EDA Steps
1. **Summary Statistics:** Calculate mean, median, standard deviation, and other statistical measures for each numeric column.
2. **Data Quality Check:** Look for missing values, outliers, or incorrect entries.
3. **Time Series Analysis:** Plot GHI, DNI, DHI, and Tamb over time to observe patterns and anomalies.
4. **Correlation Analysis:** Visualize correlations between solar radiation components and temperature measures.
5. **Wind Analysis:** Analyze the distribution of wind speed and direction.
6. **Temperature Analysis:** Examine the influence of relative humidity on temperature.
7. **Histograms:** Visualize the frequency distribution of key variables.
8. **Z-Score Analysis:** Flag data points significantly different from the mean.
9. **Bubble Charts:** Explore complex relationships between variables.

## Setup
1. **Create a Virtual Environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
2. **Install Required Libraries:**
    pip install pandas numpy matplotlib seaborn gdown streamlit

## How to Run
1. **Download the Data:** The data files are stored on Google Drive. Use the script to download them:
import gdown

# Download the CSV files


2. **Download the Data:** Run the EDA Script: Use the main.py script to run the EDA analysis:
python main.py
3. **View the Results:** Open the eda.ipynb notebook to interactively explore the results of the EDA.

## Results
The analysis includes summary statistics, data quality checks, time series plots, correlation matrices, wind analysis, temperature analysis, histograms, Z-score analysis, and bubble charts. The cleaned dataset is saved as cleaned_solar_data.csv.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests with improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.