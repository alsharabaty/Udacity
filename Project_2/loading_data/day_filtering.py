def day_filtering(df, day):
    """
    Filters the data by day of the week.
    
    Args:
        df - Pandas DataFrame containing city data
        day - name of the day of the week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by day
    """
    
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Start Time'].dt.day_name() == day].copy()
        print(f"Filtering data by day: {day}")
        
    return df