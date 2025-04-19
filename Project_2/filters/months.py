monthes = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December"
}


def months_f():
    """
    Filters the data by month.
    
    Returns:
        str - the month to filter by
    """
    month = str(input("Enter the month you want to filter by (e.g., January) and Enter to no filter \n You can use its abbreviation (Jan, Feb, etc.): ").strip().title())
    if month in monthes:
        return monthes[month] # Return the full month name if abbreviation is provided
    elif month in monthes.values():
        return month
    elif month == "":
        print("No filter applied. Showing all months.")
        return None
    else:
        print("Invalid month. Please enter a valid month name (e.g., January) or its abbreviation (e.g., Jan).")
        return months_f()