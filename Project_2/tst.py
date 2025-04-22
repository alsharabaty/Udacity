import time
import pandas as pd
from filters import cities as ct, months as mt, days as dy
from loading_data import month_filtering as mf, day_filtering as df
from time_stat import common_month as cm, common_day as cd, common_hour as ch


def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'* 40)
    
    city_dataframe = ct.city_data()
    m_filter = mt.months_f()
    d_filter = dy.days_f()

    print('-'* 40)
    return city_dataframe, m_filter, d_filter


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    city['Start Time'] = pd.to_datetime(city['Start Time'])
    city['End Time'] = pd.to_datetime(city['End Time'])
    
    print(day , month)
    
    # filter by month to create the new dataframe
    city = mf.month_filtering(city, month)

    # filter by day of week to create the new dataframe
    city = df.day_filtering(city, day)
    
    return city


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    cm.common_month(df)

    # TO DO: display the most common day of week
    cd.common_day(df)

    # TO DO: display the most common start hour
    ch.common_hour(df)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {most_common_start_station}")

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {most_common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End'] = df['Start Station'] + " to " + df['End Station']
    most_common_start_end = df['Start-End'].mode()[0]
    print(f"The most frequent combination of start and end station is: {most_common_start_end}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_filled = df["Trip Duration"].fillna(df["Trip Duration"].mean())
    
    # TO DO: display total travel time
    total_travel_sum = total_travel_filled.sum()
    print(f"The total travel time is: {total_travel_sum/60} minutes")

    # TO DO: display mean travel time
    total_travel_mean = total_travel_filled.mean()
    print(f"The mean travel time is: {total_travel_mean/60} minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    df['User Type'] = df['User Type'].fillna('Unknown')
    df["Gender"] = df['Gender'].fillna('Unknown')
    df["Birth Year"] = df['Birth Year'].fillna(df['Birth Year'].mean())

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"Counts of user types: \n{user_types}")

    # TO DO: Display counts of gender
    gender_counts = df["Gender"].value_counts()
    print(f"Counts of user gender: \n{gender_counts}")

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    most_recent_year = df['Birth Year'].max()
    most_common_year = df['Birth Year'].mode()[0]
    print(f"The earliest year of birth is: {earliest_year}")
    print(f"The most recent year of birth is: {most_recent_year}")
    print(f"The most common year of birth is: {most_common_year}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        if df.empty:
            print("Oops! No data found for your filter. Try another month or day.")
            
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n')
        
        if view_data.lower() == 'yes':
            print(df.head(5))
            print(df.info())
            
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # print(df.head())
        # print(df.info())

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
