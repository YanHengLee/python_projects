import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    """
    Draw a scatter plot of historical sea level data and two lines of best fit.

    The first regression line uses all available data and projects sea level
    rise through the year 2050. The second regression line uses data from
    the year 2000 onward to show a more recent trend.
    """

    # ------------------------------------------------
    # Load dataset
    # ------------------------------------------------
    # Read sea level data from CSV file
    df = pd.read_csv("epa-sea-level.csv", float_precision="legacy")

    # ------------------------------------------------
    # Scatter plot of observed data
    # ------------------------------------------------
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # ------------------------------------------------
    # First line of best fit (1880–2050)
    # ------------------------------------------------
    # Perform linear regression on the full dataset
    slope, intercept, r_value, p_value, std_err = linregress(
        x=df["Year"],
        y=df["CSIRO Adjusted Sea Level"]
    )

    # Extend years to 2050 for prediction
    year_extended = list(range(1880, 2050))
    line = [intercept + slope * year for year in year_extended]

    # Plot regression line
    plt.plot(year_extended, line, linewidth=2, color="r")

    # ------------------------------------------------
    # Second line of best fit (2000–2050)
    # ------------------------------------------------
    # Filter data from year 2000 onwards
    mod_df = df.loc[df["Year"] >= 2000]

    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        x=mod_df["Year"],
        y=mod_df["CSIRO Adjusted Sea Level"]
    )

    year2 = list(range(2000, 2050))
    line2 = [intercept2 + slope2 * year for year in year2]

    # Plot second regression line
    plt.plot(year2, line2, linewidth=3, color="k")

    # ------------------------------------------------
    # Labels and title
    # ------------------------------------------------
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # ------------------------------------------------
    # Save figure and return axis
    # ------------------------------------------------
    plt.savefig("sea_level_plot.png")
    return plt.gca()
