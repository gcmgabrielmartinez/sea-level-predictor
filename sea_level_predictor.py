import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.xlim(left = 1880, right =  2050)
    plt.ylim(-10, 20)
    

    # Create first line of best fit
    x_time = range(1880, 2051)
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    plt.plot(x_time, intercept + slope * x_time, color='red', label='fitted line 1')
    

  
    # Create second line of best fit
    x_time2 = range(2000, 2051)
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df["Year"][df["Year"]>=2000], df["CSIRO Adjusted Sea Level"][df["Year"]>=2000])
    plt.plot(x_time2, (intercept2 + slope2 * x_time2).tolist(), color='black', label='fitted line 2')
    
    
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.xticks(range(1850, 2090, 25))
  #1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()