def add_time(start, duration, day=None):
    """
    Add a duration to a starting time in 12-hour AM/PM format.

    Parameters:
        start (str): Start time in format "H:MM AM/PM"
        duration (str): Duration time in format "H:MM"
        day (str, optional): Starting day of the week

    Returns:
        str: New calculated time with updated day information (if provided)
    """

    # Dictionary to map weekday names to numeric values
    st_date = {
        "Monday": 1, "Tuesday": 2, "Wednesday": 3,
        "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7
    }

    # Reverse mapping to convert numeric value back to weekday
    new_date = {
        1: "Monday", 2: "Tuesday", 3: "Wednesday",
        4: "Thursday", 5: "Friday", 6: "Saturday", 0: "Sunday"
    }

    # ----------------------------
    # Parse start time
    # ----------------------------
    start_parts = start.split(":")
    st_hour = int(start_parts[0])

    # Separate minutes and AM/PM
    minute_part = start_parts[1].split()
    st_min = int(minute_part[0])
    am_pm = minute_part[1]

    # ----------------------------
    # Parse duration time
    # ----------------------------
    duration_parts = duration.split(":")
    dr_hour = int(duration_parts[0])
    dr_min = int(duration_parts[1])

    # Add hours and minutes
    new_hour = st_hour + dr_hour
    new_min = st_min + dr_min
    no_of_days = 0  # Tracks how many days have passed

    # ----------------------------
    # Handle minute overflow
    # ----------------------------
    if new_min >= 60:
        extra_hours = new_min // 60
        new_hour += extra_hours
        new_min = new_min % 60

    # Format minutes to always have two digits
    if new_min == 0:
        new_min = "00"
    elif new_min < 10:
        new_min = f"0{new_min}"
    else:
        new_min = str(new_min)

    # ----------------------------
    # Handle hour overflow (convert to 12-hour format)
    # ----------------------------
    cycles = new_hour // 12

    while cycles >= 1 and new_hour > 12:
        new_hour = new_hour % 12
        if new_hour == 0:
            new_hour = 12
            break

    # ----------------------------
    # Handle AM/PM transitions
    # ----------------------------
    while cycles >= 1:
        if cycles >= 1 and am_pm == "AM":
            am_pm = "PM"
        elif cycles >= 1 and am_pm == "PM":
            am_pm = "AM"
            no_of_days += 1  # A full day passes when PM → AM
        cycles -= 1

    # ----------------------------
    # Handle optional weekday input
    # ----------------------------
    if day is not None:
        st_day = day.capitalize()
        current_day_num = st_date[st_day]
        new_day_num = (current_day_num + no_of_days) % 7
        new_day = new_date[new_day_num]

        if no_of_days == 1:
            return f"{new_hour}:{new_min} {am_pm}, {new_day} (next day)"
        elif no_of_days == 0:
            return f"{new_hour}:{new_min} {am_pm}, {st_day}"
        else:
            return f"{new_hour}:{new_min} {am_pm}, {new_day} ({no_of_days} days later)"

    # ----------------------------
    # If no weekday provided
    # ----------------------------
    else:
        if no_of_days == 1:
            return f"{new_hour}:{new_min} {am_pm} (next day)"
        elif no_of_days == 0:
            return f"{new_hour}:{new_min} {am_pm}"
        else:
            return f"{new_hour}:{new_min} {am_pm} ({no_of_days} days later)"
