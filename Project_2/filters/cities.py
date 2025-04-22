import pandas as pd
import os

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
            base_dir = os.path.dirname(__file__)
            path = os.path.join(base_dir, "..", "databases", city_csv[city])
            print("Looking for file at:", path)
            print("Exists?", os.path.exists(path))
            return pd.read_csv(path)
            
        else:
            print("Invalid input. Please enter a valid city name.")
            continue
        
if __name__ == "__main__":
    # Test the function
    print("Testing city_data function:")
    # Call the function and print the result    
    print(city_data().head())
    print(city_data().info())