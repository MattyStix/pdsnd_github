import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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
    while True:
        city = input(
            "\nPlease select a city to filter the data. 'Chicago', 'Washington' or 'New York City'.\n").lower()
        if city not in CITY_DATA:
            print("\nUnfortunately that data is unavailable. Please, try again.\n")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            "\nPlease choose a month to filter the data.\nJanuary, February, March, April, May and June are available, as well as 'all'.\n").lower()
        months = ['january', 'february', 'march',
                  'april', 'may', 'june', 'all']
        if month not in months:
            print("\nOops, that didn't work. Please, choose again.\n")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            "\nPlease select a day of the week, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, as well as 'all'.\n").lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday',
                'friday', 'saturday', 'sunday', 'all']
        if day not in days:
            print("\nHmm, something has gone wrong. Please try again.\n")
            continue
        else:
            break

    print('-' * 40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month # keep months a
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1 # int to month name
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()] # end with day name instead of int

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month, imported 'calendar to display name of month
    common_month = df['month'].mode()[0]
    print('The most popular month is:', calendar.month_name[common_month])
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most popular day is:', common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular starting hour is:', popular_hour, 'hundred hours.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    # to allow the user a chance to read
    print("\nPlease press any key to continue\n")
    input()


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most popular starting point is:', common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most popular end point is:', common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    common_trip = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('The most popular trip is between:',  common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    # to allow user a chance to read
    print("\nPlease press any key to continue\n")
    input()


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time. Divide by 60 to adjust seconds to minutes and rounded to 2 decimals
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_mins = (total_travel_time / 60).round(2)
    print('The total travel time is:', total_travel_time_mins, 'minutes.')
    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    avg_travel_time_mins = (avg_travel_time / 60).round(2)
    print('The average travel time is:', avg_travel_time_mins, 'minutes.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    # to allow the user a chance to read
    print("\nPlease press any key to continue\n")
    input()


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The types of users by counts are:', user_types)
    # TO DO: Display counts of gender
    try:
        # try statement for missing data - gender
        gender_counts = df['Gender'].value_counts()
        print('The count of users by gender is:', gender_counts)
    except KeyError:
        print("Sorry, gender data is unavaiable.")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        # try statement for missing data - birth year earliest
        earliest_birth = df['Birth Year'].min()
        print('The earliest birth year is:', earliest_birth)
    except KeyError:
        print("This data is unavailable.")

    try:
        # try statement for missing data - birth year most recent
        recent_birth = df['Birth Year'].max()
        print('The most recent birth year is:', recent_birth)
    except KeyError:
        print("This data is unavailable.")

    try:
        # try statement for missing birth years
        common_birth = df['Birth Year'].mode()[0]
        print('The most common birth year is:', common_birth)
    except KeyError:
        print('This data is unavailable.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

# Display raw data - while loop to ask the user if they would like to view raw data


def raw_data(df):
    view_data = input(
        '\nWould you like to display the first 5 rows of raw data? Please enter yes or no\n').lower()
    pd.set_option('display.max_columns', None)  # show all columns
    start_loc = 0
    more_data = True  # boolean to maintain loop
    while (more_data):
        if view_data == 'yes':
            more_data = True
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
        if view_data != 'yes':
            more_data = False


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input(
            '\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
