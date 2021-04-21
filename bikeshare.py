import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).

    while True:
        city=input('Please pick a city from Chicago, New York City and Washington \n')
        city=city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else: 
            print('\nIncorrect Input. Please pick a valid city \n')


    # get user input for month (all, january, february, ... , june)

    while True:
        month=input('\nPlease pick a month from January to June or select all \n')
        month=month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else: 
            print('\nIncorrect Input. Please pick a valid month \n')


    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day=input('\nPlease pick a day from Monday to Sunday or select all \n')
        day=day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else: 
            print('\nIncorrect Input. Please pick a valid day \n')


    print('-'*40)
    return city, month, day


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
    # obtain data for city
    df= pd.read_csv(CITY_DATA[city])
    

    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['Month']= df['Start Time'].dt.month
    df['Day']= df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour


    # filter by month
    if month!='all' :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df= df[df['Month']==month]

    # filter by day
    if day != 'all':
        
        df = df[df['Day'] == day.title()]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('Most common month of travel: ', months[df['Month'].mode()[0]-1].title(), '\n')

    # display the most common day of week
    print('Most common day of travel: ', df['Day'].mode()[0], '\n')

    # display the most common start hour
    print('Most common hour of travel: ', df['Hour'].mode()[0], '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most commonly used start station:", df['Start Station'].mode()[0], "\n")

    # display most commonly used end station
    print("Most commonly used end station:", df['End Station'].mode()[0], "\n")

    # display most frequent combination of start station and end station trip
    df['Roundtrip'] = df['Start Station'] + " and " + df['End Station']
    print("Most frequent combination of start station and end station trip: ", df['Roundtrip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time:", df['Trip Duration'].sum(), "\n")

    # display mean travel time
    print("Mean travel time: ", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Types\n',df['User Type'].value_counts())

    #Display counts of gender
    try:
      print('\nGender Types\n', df['Gender'].value_counts())
    except KeyError:
      print("\nNo data available for gender types")

    #Display earliest, most recent, and most common year of birth

    try:
      print('\nEarliest Year:', int(df['Birth Year'].min()))
    except KeyError:
      print("\nNo data available for earliest year of birth.")

    try:
      print('\nMost Recent Year:', int(df['Birth Year'].max()))
    except KeyError:
      print("\nNo data available for most recent year of birth")

    try:
      print('\nMost Common Year:', int(df['Birth Year'].value_counts().idxmax()))
    except KeyError:
      print("\nNo data available for most common year of birth")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    start = 0
    while True:
        if start==0:
            raw = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        else:
            raw = input('\nWould you like to see the next 5 lines of raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[start: start + 5])
            start = start + 5
        else:
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
