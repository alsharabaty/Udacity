

def days_f():
    """
    Filters the data by day of the week.
    
    Returns:
        str - the day of the week to filter by
    """
    
    days_dict = {
        "1": "Sunday",
        "2": "Monday",
        "3": "Tuesday",
        "4": "Wednesday",
        "5": "Thursday",
        "6": "Friday",
        "7": "Saturday",
        }
    
    day = input("Please enter the day of the week (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) or 'all' for no filter: ").title()
    
    if day in days_dict.values():
        print(f"Filtering data by {day}...")
        return day
    elif day in days_dict.keys():
        print(f"Filtering data by {days_dict[day]}...")
        return days_dict[day]
    elif day == "All":
        print("No filter applied for day of the week.")
        return "all"
    else:
        print("Invalid input. Please enter a valid day of the week or 'all'.")
        return days_f()
    
    
if __name__ == "__main__":
    # Test the function
    print("Testing days_f function:")
    # Call the function and print the result    
    print(days_f())
