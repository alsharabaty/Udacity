def common_hour(city):
    """Filters by month and day if applicable."""
    
    # check if month is not all
    city['hour'] = city['Start Time'].dt.hour
    most_common_hour = city['hour'].mode()[0]
    print(f"The most common start hour is: {most_common_hour}")
    
    return most_common_hour
