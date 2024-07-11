import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    file_path = 'epa-sea-level.csv'
    df = pd.read_csv(file_path)

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended = np.arange(df['Year'].min(), 2051)
    sea_level_fit = intercept + slope * years_extended
    plt.plot(years_extended, sea_level_fit, color='red', label='Line of Best Fit')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]

    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    years_extended_recent = np.arange(2000, 2051)
    sea_level_fit_recent = intercept_recent + slope_recent * years_extended_recent
    plt.plot(years_extended_recent, sea_level_fit_recent, color='green', label='Best Fit (2000 onwards)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()