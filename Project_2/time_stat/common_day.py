def common_day(city):
    """Filters by month and day if applicable."""
    
    # check if month is not all
    city['day'] = city['Start Time'].dt.day_name()
    most_common_day = city['day'].mode()[0]
    print(f"The most common day of the week is: {most_common_day}")
    
    return most_common_day