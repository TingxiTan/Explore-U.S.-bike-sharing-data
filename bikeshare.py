# -*- coding: utf-8 -*-
# @Author: Tingxi Tan

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january','february','march','april','may','june','all']
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input_Parameter('\nPlease type a city name (chicago, new york city, washington)\n',
                 '\nError.Please type a city name (chicago, new york city, washington)\n' ,\
                  CITY_DATA.keys())
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input_Parameter('\nPlease type in the month name. (all, january, february, ... , june).\n',\
                 '\nError.Please type in the month name. (all, january, february, ... , june).\n' ,\
                  months)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input_Parameter('\nPlease type in the day of the week (all, monday, tuesday, ... sunday).\n',\
                 '\nError.Please type in the day of the week (all, monday, tuesday, ... sunday).\n' ,\
                  weekdays)
    print('-'*40)
    return city, month, day
def input_Parameter(input_print,error_print,enterable_list):
    ret = input(input_print).lower().strip()
    while ret not in enterable_list:
        ret = input(error_print).lower().strip()
    return ret

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['the day in the week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df["month"] == month]
    if day != 'all':
       df = df[df["the day in the week"] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    the_most_common_month = df['month'].mode()[0]
    print('The most common month is:', the_most_common_month)
    # TO DO: display the most common day of week
    the_most_common_day_of_week = df['the day in the week'].mode()[0]
    print('The most common day of week is:', the_most_common_day_of_week)
    # TO DO: display the most common start hour
    df['the_hour'] = df['Start Time'].dt.hour
    the_most_common_start_hour = df['the_hour'].mode()[0]
    print('The most common hour is:', the_most_common_start_hour)
 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    the_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station:\n', the_start_station)
    # TO DO: display most commonly used end station
    the_end_station = df['End Station'].mode()[0]
    print('The most  most commonly used end station is:\n',the_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    Trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most frequent combination of start station and end station trip is {} to {}".format(Trip[0], Trip[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("\nThe total duration is:\n",total_travel_time)

    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print('Mean travel time: {} seconds.'.format(mean_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    types = df['User Type'].value_counts()
    print("\nThe counts of user types is:\n",types)
    # TO DO: Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print("\nThe counts of gender is:\n", counts_of_gender)
    except:
        pass
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        the_earliest_of_birth = df['Birth Year'].min()
        the_most_recent = df['Birth Year'].max()
        the_most_common =  df['Birth Year'].mode()[0]
        print("\nThe earliest of birth is:\n", the_earliest_of_birth)
        print("\nThe most recent of birth is:\n", the_most_recent)
        print("\nThemost common year of birth is:\n", the_most_common)
    except:
        pass


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
