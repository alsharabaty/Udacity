import streamlit as st
import pandas as pd
import os

# Load Data
def load_data(city):
    city_csv = {
        'Chicago': 'chicago.csv',
        'New York City': 'new_york_city.csv',
        'Washington': 'washington.csv'
    }
    
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "databases", city_csv[city])
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()  # Clean column names
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    return df

st.title("🚲 US Bikeshare Data Explorer")

city = st.selectbox("Choose a city:", ["Chicago", "New York City", "Washington"])

if city:
    df = load_data(city)
    st.success(f"{len(df)} rows loaded for {city}.")

    if st.checkbox("Show Raw Data"):
        st.dataframe(df.head())

    # Most Common Month
    if 'month' in df.columns:
        most_common_month = df['month'].mode()[0]
        st.write(f"📅 Most common month: {most_common_month}")

    # Most Common Day
    if 'day' in df.columns:
        most_common_day = df['day'].mode()[0]
        st.write(f"📆 Most common day: {most_common_day}")

    # Most Common Start Hour
    most_common_hour = df['hour'].mode()[0]
    st.write(f"⏰ Most common start hour: {most_common_hour}")

    # Most Common Stations
    start_station = df['Start Station'].mode()[0]
    end_station = df['End Station'].mode()[0]
    st.write(f"🚏 Most common start station: {start_station}")
    st.write(f"🏁 Most common end station: {end_station}")
