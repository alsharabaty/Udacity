###############################################################################################

# Libraries

import os
import streamlit as st
import pandas as pd
from filters import cities as ct, months as mt, days as dy
from loading_data import month_filtering as mf, day_filtering as df
from time_stat import common_month as cm, common_day as cd, common_hour as ch

########################################################################################

# Logic for loading data and filtering
# This section handles the loading of data and filtering based on user input.


def load_data(selected_city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    city_csv = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "databases", city_csv[selected_city.lower()])
    city = pd.read_csv(path)
    
    city.columns = city.columns.str.strip()  # Clean column names
    city['Start Time'] = pd.to_datetime(city['Start Time'])
    city['End Time'] = pd.to_datetime(city['End Time'])

    if month != 'all':
        city = city[city['Start Time'].dt.month_name() == month].copy()

    if day != 'all':
        city = city[city['Start Time'].dt.day_name() == day].copy()
    
    return city


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        df - Pandas DataFrame containing city data
    Returns:
        common time stats - most common month, day, and hour of travel"""

    c_month = cm.common_month(df)
    c_day = cd.common_day(df)
    c_hour = ch.common_hour(df)
    
    return c_month, c_day, c_hour


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        df - Pandas DataFrame containing city data
    Returns:
        station stats - most commonly used start station, end station, and trip"""

    most_common_start_station = df['Start Station'].mode()[0] # display most commonly used start station

    most_common_end_station = df['End Station'].mode()[0] # display most commonly used end station

    df['Start-End'] = df['Start Station'] + " to " + df['End Station'] # create a new column for start and end station
    most_common_start_end = df['Start-End'].mode()[0] # display most frequent combination of start station and end station trip
    
    return most_common_start_station, most_common_end_station, most_common_start_end


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        df - Pandas DataFrame containing city data
    Returns:
        total_travel_sum - total travel time"""

    total_travel_filled = df["Trip Duration"].fillna(df["Trip Duration"].mean()) # fill missing values with mean
    
    total_travel_sum = total_travel_filled.sum() # display total travel time

    total_travel_mean = total_travel_filled.mean() # display mean travel time
    
    return total_travel_sum, total_travel_mean



def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
        df - Pandas DataFrame containing city data
    Returns:
        user_types - counts of user types"""

    df['User Type'] = df['User Type'].fillna('Unknown')
    df["Gender"] = df['Gender'].fillna('Unknown')
    df["Birth Year"] = df['Birth Year'].fillna(df['Birth Year'].mean())

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()


    # TO DO: Display counts of gender
    gender_counts = df["Gender"].value_counts()
    

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    most_recent_year = df['Birth Year'].max()
    most_common_year = df['Birth Year'].mode()[0]
    
    return user_types, gender_counts, earliest_year, most_recent_year, most_common_year
    

##############################################################################

# Main function to run the Streamlit app

st.title("US Bikeshare Data Explorer")

st.markdown("""
    This app allows you to explore bikeshare data for three major US cities: Chicago, New York City, and Washington.
    You can filter the data by month and day to analyze specific trends.
    """)

selected_city = st.selectbox("Choose a city:", ["Chicago", "New York City", "Washington"])


if st.checkbox("Add filters"):
    st.markdown("""
        You can filter the data by month and day to analyze specific trends.
        """)
    month = st.selectbox("Choose a month:", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    day = st.selectbox("Choose a day:", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
else:
    month = "all"
    day = "all"

with st.spinner("Loading data..."):
    city = load_data(selected_city, month, day)
    
if st.button("Check Data"):
    if city.empty:
        st.warning("No data available for the selected filters.")
    else:
        st.success(f"{len(city)} rows loaded for {selected_city}.")

if st.checkbox("Show Raw Data"):
    rows = st.selectbox("Select number of rows to display:", [5, 10, 20, 50])
    st.dataframe(city.head(rows))


if st.checkbox("More stats"):
    if st.button("Show Time Stats"):
        st.markdown("### Most Frequent Times of Travel")
        st.write("Most Common Month:", time_stats(city)[0])
        st.write("Most Common Day:", time_stats(city)[1])
        st.write("Most Common Hour:", time_stats(city)[2])

    if st.button("Show Station Stats"):
        st.markdown("### Most Popular Stations and Trip")
        st.write("Most Common Start Station:", station_stats(city)[0])
        st.write("Most Common End Station:", station_stats(city)[1])
        st.write("Most Common Start-End Station Trip:", station_stats(city)[2])

    if st.button("Show Trip Duration Stats"):
        st.markdown("### Trip Duration")
        st.write("Total Travel Time:", trip_duration_stats(city)[0]/60, " minutes")
        st.write("Mean Travel Time:", trip_duration_stats(city)[1]/60, " minutes")


    if st.button("Show User Stats"):
        st.markdown("### User Stats")
        st.write("Counts of User Types:", user_stats(city)[0])
        st.write("Counts of User Gender:", user_stats(city)[1])
        st.write("Earliest Year of Birth:", user_stats(city)[2])
        st.write("Most Recent Year of Birth:", user_stats(city)[3])
        st.write("Most Common Year of Birth:", user_stats(city)[4])