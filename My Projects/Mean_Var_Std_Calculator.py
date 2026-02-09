import numpy as np


def calculate(list):
    """
    Calculate mean, variance, standard deviation, max, min, and sum
    for a 3x3 matrix created from a list of nine numbers.

    The calculations are performed along:
    - Columns (axis=0)
    - Rows (axis=1)
    - The entire matrix

    Parameters:
        list (list): A list containing exactly nine numerical values.

    Returns:
        dict: A dictionary containing statistical calculations.
    """

    # ------------------------------------------------
    # Convert input list into a NumPy array
    # ------------------------------------------------
    arr3 = np.array(list)

    # Ensure the list can be reshaped into a 3x3 matrix
    try:
        arr3 = arr3.reshape(3, 3)
    except ValueError:
        raise ValueError("List must contain nine numbers.")

    # ------------------------------------------------
    # Initialize containers for results
    # ------------------------------------------------
    mean = []
    variance = []
    standard_deviation = []
    max = []
    min = []
    sum = []

    # ------------------------------------------------
    # Mean calculations
    # ------------------------------------------------
    mean_columns = arr3.mean(axis=0)   # Column-wise mean
    mean_rows = arr3.mean(axis=1)      # Row-wise mean
    mean_all = arr3.mean()             # Overall mean

    mean.append(mean_columns.tolist())
    mean.append(mean_rows.tolist())
    mean.append(mean_all)

    # ------------------------------------------------
    # Variance calculations
    # ------------------------------------------------
    var_columns = arr3.var(axis=0)
    var_rows = arr3.var(axis=1)
    var_all = arr3.var()

    variance.append(var_columns.tolist())
    variance.append(var_rows.tolist())
    variance.append(var_all)

    # ------------------------------------------------
    # Standard deviation calculations
    # ------------------------------------------------
    std_columns = arr3.std(axis=0)
    std_rows = arr3.std(axis=1)
    std_all = arr3.std()

    standard_deviation.append(std_columns.tolist())
    standard_deviation.append(std_rows.tolist())
    standard_deviation.append(std_all)

    # ------------------------------------------------
    # Maximum value calculations
    # ------------------------------------------------
    max_columns = arr3.max(axis=0)
    max_rows = arr3.max(axis=1)
    max_all = arr3.max()

    max.append(max_columns.tolist())
    max.append(max_rows.tolist())
    max.append(max_all)

    # ------------------------------------------------
    # Minimum value calculations
    # ------------------------------------------------
    min_columns = arr3.min(axis=0)
    min_rows = arr3.min(axis=1)
    min_all = arr3.min()

    min.append(min_columns.tolist())
    min.append(min_rows.tolist())
    min.append(min_all)

    # ------------------------------------------------
    # Sum calculations
    # ------------------------------------------------
    sum_columns = arr3.sum(axis=0)
    sum_rows = arr3.sum(axis=1)
    sum_all = arr3.sum()

    sum.append(sum_columns.tolist())
    sum.append(sum_rows.tolist())
    sum.append(sum_all)

    # ------------------------------------------------
    # Combine all calculations into a dictionary
    # ------------------------------------------------
    calculations = {
        "mean": mean,
        "variance": variance,
        "standard deviation": standard_deviation,
        "max": max,
        "min": min,
        "sum": sum,
    }

    return calculations
