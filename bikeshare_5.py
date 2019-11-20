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

    city = str.lower(input('For which city would you like to see data for Chicago, New York City, or Washington? '))
    while city !='chicago':
        if city == 'washington':
            break
        if city == 'new york city':
            break
        if city == 'chicago':
            break
        else:
            city = str.lower(input('please choose a valid city: '))
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    month = str.lower(input('Please choose a month between January and June, or "all" to see all months: '))
    while month !='january':
        if month =='january':
            break
        if month == 'february':
            break
        if month == 'march':
            break
        if month == 'april':
            break
        if month == 'may':
            break
        if month == 'june':
            break
        if month == 'all':
            break
        else:
            month = str.lower(input('Please choose a valid month: '))
    # get user input for month (all, january, february, ... , june)

    day = str.lower(input('Please choose a day of the week, or "all" to see all days: '))
    while day !='sunday':
        if day == 'sunday':
            break
        if day == 'monday':
            break
        if day == 'tuesday':
            break
        if day == 'wednesday':
            break
        if day == 'thursday':
            break
        if day == 'friday':
            break
        if day == 'saturday':
            break
        if day == 'all':
            break
        else:
            day = input('Please choose a valid day: ')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    print(city, month, day)
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
    df=pd.read_csv(CITY_DATA[city])

    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour']=df['Start Time'].dt.hour

    #filter by month if applicable
    if month != 'all':

            #use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


            #filter by month to create the new DataFrame
        df = df[df['month'] == month]

    #filter by day of wekk if applicable
    if day != 'all':
            #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month=df['month'].mode()[0]
    print('Most Popular Month:', popular_month)


    # display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print('Most Popular Day:',popular_day)


    # display the most common start hour
    popular_hour=df['start_hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start=df['Start Station'].mode()
    print('Most Commonly Used Start Station:', start)


    # display most commonly used end station
    end=df['End Station'].mode()
    print('Most Commonly Used End Station:', end)


    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}".format(most_common_start_end_station[0],most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    duration=df['Trip Duration'].sum()
    print('Total Trip Duration:', duration)


    # display mean travel time
    mean=df['Trip Duration'].mean()
    print('Average Duration:', mean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types=df['User Type'].value_counts()
    print('User Type:', user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender=df['Gender'].value_counts()
        print('Gender', gender)
    else:
        print('No Gender Data')


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest=df['Birth Year'].min()
        print('Earliest Year of Birth:', earliest)
        recent=df['Birth Year'].max()
        print('Most Recent Year of Birth:', recent)
        common=df['Birth Year'].mode()
        print('Most Common Year of Birth:', common)
    else:
        print('No Birth Year Available')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    lower_bound=0
    upper_bound=5
    while True:
        raw = input('Would you like to view raw data? ')
        if raw.lower() !='yes':
            break
        else:
            print(df[df.columns[0:]].iloc[lower_bound:upper_bound])
            lower_bound +=5
            upper_bound += 5

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
