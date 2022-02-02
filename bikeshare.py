import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago','new york city','washington']
days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
months = ['all','january','february','march','april','may','june']


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
    user_city = get_city()
    print('-'*40)
    # TO DO: get user input for month (all, january, february, ... , june)
    req_month = get_month()
    print('-'*40)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week = get_day()
    print('-'*40)
    return user_city, req_month, day_of_week
def get_city():
    while True:
        city=input('select the required city from chicago,new york city or washington: ').lower()
        if city not in cities(city):
                   print('invalid selection \n{}. \n please select valid input'.format(city))
        return city
def req_month():
    while True:
        month=input('select the required city from all, january, february, ..., june ').lower()
        if month not in cities(months):
                   print('invalid selection \n{}. \n please select valid input'.format(month))
        return month
def day_of_week():
    while True:
        day=input('select the required city from all, monday, tuesday, ..., sunday ').lower()
        if day not in cities(days):
                   print('invalid selection \n{}. \nPlease select valid input'.format(day))
        return month
             
        
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
    # convert the Start Time column to datetime
    df['dateTime'] = df['Start Time'].astype('datetime64[ns]')

    # extract hour from the Start Time column to create an hour column
    df['hour'] =df['dateTime'].dt.hour
    df['month'] =df['dateTime'].dt.month 
    df['day_of_week'] = df['datetime'].dt.weekday_name 
    if month !='all':
        month=months.index()
        df =df[df['month']==month]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month: {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('Most common day of week: {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('Most common start hour: {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common start station: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('Most common end station: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    trips=df.groupby(['Start Station', 'End Station'])['Start Time'].count()
    popular_trips=trips.sort_values(ascending=False, axis=0)
    print('Most popular trips are: \nStart station: {} \nEnd stations: {} '.format(popular_trips.index[0][0], popular_trips.index[0][1]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: {}'.format(df['Trip Duration'].sum()))
    
    # TO DO: display mean travel time
    print('Total travel time: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print( 'Total count of user types: {}'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print( 'Total count of each gender: {}'.format(df['Gender'].value_counts()))
    else:
        print('Invalid input please enter valed gender data')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print( 'Earlist year of birth: {}'.format(df['Birth Year'].min()))
        print( 'Most recent year of birth: {}'.format(df['Birth Year'].max()))
        print( 'Most common year of birth: {}'.format(df['Birth Year'].mode()[0]))
    else:
        print('Invalid input please enter valid birth date')

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
