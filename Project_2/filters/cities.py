import pandas as pd
import databases as db # import databases as db


def city_data():
    """
    Loads data for the specified city.
    
    Returns:
        df - Pandas DataFrame containing city data
    """
    
    city_csv = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    
    while True:
        # Get user input for city (chicago, new york city, washington)
        city = input("Please enter the name of the city (chicago, new york city, washington): ").lower()
        if city in city_csv:
            print(f"Loading data for {city.title()}...")
            return pd.read_csv("databases\{}".format(city_csv[city]))
        else:
            print("Invalid input. Please enter a valid city name.")
            continue