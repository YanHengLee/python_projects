# Read input and split into two date strings
dates = input().split('),')

# Number of days in each month (non-leap year)
month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0

# ------------------------------------------------
# Clean and parse input dates
# ------------------------------------------------
# Remove parentheses and convert each date into a list of integers:
# [year, month, day]
for i in range(2):
    dates[i] = dates[i].strip()
    dates[i] = dates[i].strip("(")
    dates[i] = dates[i].strip(")")
    dates[i] = list(map(int, dates[i].split(",")))


# ------------------------------------------------
# Check if a year is a leap year
# ------------------------------------------------
def isleap(n):
    """
    Determine whether a given year is a leap year.

    Parameters:
        n (int): Year

    Returns:
        int: 1 if leap year, otherwise 0
    """
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return 1
    return 0


# ------------------------------------------------
# Ensure the first date is earlier than the second
# ------------------------------------------------
# Swap dates if necessary to maintain chronological order
if dates[0][0] > dates[1][0]:
    dates[0], dates[1] = dates[1], dates[0]
elif dates[0][0] == dates[1][0]:
    if dates[0][1] > dates[1][1]:
        dates[0], dates[1] = dates[1], dates[0]
    elif dates[0][1] == dates[1][1]:
        if dates[0][2] > dates[1][2]:
            dates[0], dates[1] = dates[1], dates[0]


# ------------------------------------------------
# Assign date components for readability
# ------------------------------------------------
year1, month1, day1 = dates[0]
year2, month2, day2 = dates[1]


# ------------------------------------------------
# Calculate the number of days between the two dates
# ------------------------------------------------
# Case 1: Same year and same month
if year1 == year2 and month1 == month2:
    days = day2 - day1
else:
    # Difference in years
    years = year2 - year1

    # Remaining days in the starting month
    days += month_list[month1 - 1] - day1
    if days < 0:
        days = 0

    # Add full months between the two dates
    for i in range(month1, month2 + 12 * years):
        days += month_list[i % 12]

    # Adjust for the ending month
    days = days - month_list[month2 - 1] + day2


# ------------------------------------------------
# Adjust for leap years
# ------------------------------------------------
# Add leap day if the first date is before Feb 29 in a leap year
if month1 <= 2:
    if isleap(year1):
        if day1 < 29:
            days += 1

# Add leap days for full years between the two dates
if year2 > year1:
    t = 1 if month2 > 2 else 0
    for i in range(year1 + 1, year2 + t):
        if isleap(i):
            days += 1


# ------------------------------------------------
# Output result
# ------------------------------------------------
print("The total number of days:", days)
