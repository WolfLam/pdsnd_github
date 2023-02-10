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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
         city = input('Would yo like to see data for Chicago, New York City or Washington? \n').lower()
         if city in CITY_DATA:
             print('Look like you wnat to hear about {}! If this not true, please restat the programe. \n'.format(city).title())
             break
         else:
            
             print('Type wrong. please try again. \n')
             continue
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    month = None
    day = None
    while True:
        mod = input('Would you like to filter the data by month, day, or not at all? Type "no" for no filter. \n').lower()
        if mod == 'month':
            m = input('Which month? january, february, march, april, may, june? please type full month name. \n').lower()
            if m in months:
                month = m
                break
            else:
                print('Type wrong. please try again. \n')
                continue
        elif mod == 'day':
            d = input('Which day? monday, tuesday, wednesday, thursday, friday, saturday, sunday? please type full day name. \n').lower()
            if d in days:
                day = d
                break
            else:
                print('please try again. \n')
            continue
        elif mod == 'no':
            break
        else:
            print('please try again. \n')
            continue
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    if month != None:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
   
    elif day != None:
        df = df[df['day'] == day.title()]
    else:
        pass
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    print('The most common month is: {}.'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    print('The most common day of week is: {}.'.format(df['day'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common hour is: {}.'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    ss = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}.'.format(ss))
    # TO DO: display most commonly used end station
    es = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}.'.format(es))
    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent start station is: {}, and the most frequest end station is: {}.'.format(ss, es))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
  
    # TO DO: display total travel time
    print('The total travel time is: {}.'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The total travel time is: {}.'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print('The counts of user types is: {}.'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if 'Gender' not in list(df.columns):
        pass
    else:
        print('The counts of gnder is: \n{}.'.format(df['Gender'].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' not in list(df.columns):
        pass
    else:
        maxy = df['Birth Year'].max()
        miny = df['Birth Year'].min()
        comy = df['Birth Year'].mode()[0]
        print('The earliest year of birth is: {}. \nThe most recent year of birth is: {}.\nThe most commo year if birth is: {}.'.format(int(miny), int(maxy), int(comy)))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
def read_data(df):
        ans = input('would you like to view 5 row of individual trip data? Enter yes or no? \n').lower()
        start_loc = 0
        while True:
            if ans == 'yes':
                start_loc += 5
                ls = df.iloc[(start_loc - 5): start_loc]
                print(ls)
                print('\n[{} row x {} columns]'.format(ls.shape[0], ls.shape[1]))
                ans = input("Do you wish to continue?: ").lower()
                
            elif ans == 'no':
                break
            else:
                print('Type wrong. please try again. \n')
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        read_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
