days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
        }

def days_f():
    """
    Filters the data by day of the week.
    
    Returns:
        str - the day of the week to filter by
    """
    day = str(input("Enter the day you want to filter by (e.g., Monday) or Enter for no filter\n You can use its numbers (0 = no filter, 1 = Sunday and so on): ").strip().title())
    
    try:
        if int(day) in days:
            return days[int(day)]
        elif int(day) == 0:
            print("No filter applied. Showing all days.")
            return None
        else:
            print("Invalid day. Please enter a valid day name (e.g., Monday) or its numbers (1 = Sunday).")
            return days_f()
    except:
        if day in days.values():
            return day
        elif day == "":
            print("No filter applied. Showing all days.")
            return None
        else:
            print("Invalid day. Please enter a valid day name (e.g., Monday) or its numbers (1 = Sunday).")
            return days_f()