def month_filtering(df, month):
    """
    Filters the data by month.
    
    Args:
        df - Pandas DataFrame containing city data
        month - name of the month to filter by, or "all" to apply no month filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month
    """
    
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['Start Time'].dt.month_name() == month].copy()
        print(f"Filtering data by month: {month}")
        
    return df