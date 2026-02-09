import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------
# Load dataset
# ----------------------------------------------------
# Read medical examination data into a pandas DataFrame
df = pd.read_csv("medical_examination.csv")

# ----------------------------------------------------
# Feature engineering
# ----------------------------------------------------
# Add 'overweight' column based on BMI calculation
# BMI = weight(kg) / height(m)^2
df["overweight"] = (df["weight"] / (df["height"] ** 2)) * 10000
df["overweight"] = df["overweight"].apply(lambda x: 1 if x > 25 else 0)

# Normalize data so that:
#   0 = good health condition
#   1 = bad health condition
# For 'cholesterol' and 'gluc':
#   - value 1 becomes 0 (normal)
#   - values >1 become 1 (above normal)
df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["cholesterol"] > 1, "cholesterol"] = 1
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)


def draw_cat_plot():
    """
    Draw a categorical plot showing the counts of several health-related
    features split by cardiovascular disease status.
    """

    # ------------------------------------------------
    # Prepare data for categorical plot
    # ------------------------------------------------
    # Transform the DataFrame to long format
    df_cat = pd.melt(
        df,
        id_vars="cardio",
        value_vars=[
            "active",
            "alco",
            "cholesterol",
            "gluc",
            "overweight",
            "smoke"
        ],
    )

    # ------------------------------------------------
    # Draw categorical plot
    # ------------------------------------------------
    g = sns.catplot(
        x="variable",
        hue="value",
        col="cardio",
        data=df_cat,
        kind="count"
    )

    g.set_ylabels("total")
    g.set_xlabels("variable")

    fig = g.fig
    fig.savefig("catplot.png")
    return fig


def draw_heat_map():
    """
    Draw a heatmap showing the correlation matrix of the dataset
    after cleaning out invalid and extreme values.
    """

    # ------------------------------------------------
    # Clean the data
    # ------------------------------------------------
    # Remove:
    #   - Rows where diastolic pressure > systolic pressure
    #   - Height and weight outliers (below 2.5% or above 97.5%)
    df_heat = df.loc[
        ~(df["ap_lo"] > df["ap_hi"])
        & ~(df["height"] < df["height"].quantile(0.025))
        & ~(df["height"] > df["height"].quantile(0.975))
        & ~(df["weight"] < df["weight"].quantile(0.025))
        & ~(df["weight"] > df["weight"].quantile(0.975))
    ]

    # ------------------------------------------------
    # Correlation matrix
    # ------------------------------------------------
    corr = df_heat.corr()

    # Create a mask for the upper triangle of the heatmap
    mask = np.triu(corr)

    # ------------------------------------------------
    # Draw heatmap
    # ------------------------------------------------
    fig, ax = plt.subplots(figsize=(9, 9))

    sns.heatmap(
        corr,
        mask=mask,
        linewidths=1,
        vmax=0.8,
        center=0.09,
        annot=True,
        square=True,
        fmt=".1f",
        cbar_kws={"shrink": 0.5}
    )

    fig.savefig("heatmap.png")
    return fig
