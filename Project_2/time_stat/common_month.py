def common_month(city):
    """Filters by month and day if applicable."""
    
    # check if month is not all
    city['month'] = city['Start Time'].dt.month_name()
    most_common_month = city['month'].mode()[0]
    print(f"The most common month is: {most_common_month}")
    