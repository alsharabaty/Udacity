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
    month = str(input("Enter the month you want to filter by (e.g., January) or All for no filter \nYou can use its abbreviation (Jan, Feb, etc.): ").strip().title())
    
    if month in monthes:
        return monthes[month] # Return the full month name if abbreviation is provided
    elif month in monthes.values():
        return month
    elif month == "All":
        print("Showing all months.")
        return "all"
    else:
        print("Invalid month. Please enter a valid month name (e.g., January) or its abbreviation (e.g., Jan).")
        return months_f()
    
if __name__ == "__main__":
    # Test the function
    print("Testing months_f function:")
    # Call the function and print the result    
    print(months_f())