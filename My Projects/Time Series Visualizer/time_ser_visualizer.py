import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

# Register matplotlib converters for datetime handling
register_matplotlib_converters()

# ------------------------------------------------
# Load and clean data
# ------------------------------------------------
# Read forum page view data, parse dates, and set 'date' as index
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    index_col="date",
    parse_dates=True
)

# Remove outliers by keeping values within the 2.5th and 97.5th percentiles
df = df[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    """
    Draw a line plot showing daily website forum page views
    from May 2016 to December 2019.
    """

    # ------------------------------------------------
    # Draw line plot
    # ------------------------------------------------
    fig, axes = plt.subplots(figsize=(18, 7))
    plt.plot(df, color="red")

    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return figure (required by FCC)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    """
    Draw a bar plot showing the average monthly page views
    grouped by year.
    """

    # ------------------------------------------------
    # Prepare data for bar plot
    # ------------------------------------------------
    df_copy = df.copy()
    df_copy["year"] = df_copy.index.year
    df_copy["month"] = df_copy.index.month

    # Group by year and month and calculate the mean page views
    df_bar = df_copy.groupby(["year", "month"]).mean()
    df_bar = df_bar.unstack()

    # Month labels for legend
    months = [
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ]

    # ------------------------------------------------
    # Draw bar plot
    # ------------------------------------------------
    fig = df_bar.plot(kind="bar", figsize=(10, 5)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(fontsize=10, labels=months)

    # Save image and return figure
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    """
    Draw two box plots:
    - Year-wise box plot to show trends over time
    - Month-wise box plot to show seasonality
    """

    # ------------------------------------------------
    # Prepare data for box plots
    # ------------------------------------------------
    df_box = df.copy()
    df_box.reset_index(inplace=True)

    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")
    df_box["month_num"] = df_box["date"].dt.month

    # Sort months chronologically for correct ordering
    df_box = df_box.sort_values("month_num")

    # ------------------------------------------------
    # Draw box plots
    # ------------------------------------------------
    fig, (ax_year, ax_month) = plt.subplots(
        nrows=1, ncols=2, figsize=(10, 5)
    )

    sns.boxplot(
        x="year",
        y="value",
        data=df_box,
        ax=ax_year
    )
    ax_year.set_xlabel("Year")
    ax_year.set_ylabel("Page Views")
    ax_year.set_title("Year-wise Box Plot (Trend)")

    sns.boxplot(
        x="month",
        y="value",
        data=df_box,
        ax=ax_month
    )
    ax_month.set_xlabel("Month")
    ax_month.set_ylabel("Page Views")
    ax_month.set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return figure
    fig.savefig("box_plot.png")
    return fig
