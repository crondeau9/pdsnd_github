import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

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
        city = input("Which city would you like to explore:\n Chicago, New York City, or Washington?\n").lower()
        if city in cities:
            break
        else:
            print("City not valid. Please enter a valid city.")

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("Enter the month you would like to filter by:\n January, February, March, April, May, June, or type 'all' for all months\n").lower()
        if month in months:
            break
        else:
            print("Month not valid. Please enter a valid month.")
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Which day of the week would you like to filter by:\n Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or type 'all' for all days\n").lower()
        if day in days:
            break
        else:
            print("Day not valid. Please enter a valid day.")    
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
## load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
## convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
## extract month/day of week from the Start Time column to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

## filter by month if necessary
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

## filter by month for new dataframe
        df = df[df['month'] == month]

## filter by day of week if necessary
    if day != 'all':

## filter by month for new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    popular_month = df['month'].mode()[0]
    print('Most Common Month: \n', popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day: \n', popular_day)

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    popular_hour = df['Start Hour'].mode()[0]
    print('Most Common Hour: \n', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: \n', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station: \n', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combo_station = df['Start Station'] + "to" + df['End Station']
    popular_combo_station = combo_station.mode()[0]
    print('Most Frequent combination of start station and end station trip: \n {}'.format(popular_combo_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time_sec = df['Trip Duration'].sum()
    total_travel_time_hour = (total_travel_time_sec/60/60)
    print("The total trip travel time is:", total_travel_time_hour, 'hours.\n\n')
    
    # TO DO: display mean travel time
    avg_travel_time_sec = df['Trip Duration'].mean()
    avg_travel_time_min = avg_travel_time_sec/60
    if avg_travel_time_min < 60:
        print("The average travel time is: ", avg_travel_time_min, 'minutes')
    else:
        avg_travel_time_hour = (avg_travel_time_min/60)
        print("The average travel time is: ", avg_travel_time_hour, 'hours')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count for each user type is:", user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender = df['Gender'].value_counts()
        print("The counts for each gender are: ", counts_of_gender)
    else:
        print("The city of Washington data does not contain gender")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year_early = df['Birth Year'].min()
        print("The earliest year of birth is:", birth_year_early)
        birth_year_recent = df['Birth Year'].max()
        print("The most recent year of birth is:", birth_year_recent)
        birth_year_most_common = df['Birth Year'].mode()
        print("The most common year of birth is:", birth_year_most_common)
    else:
        print("The city of Washington data does not contain Birth Year")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    count = 5
    while True:
        if count == 5:
            raw_data = input("Would you like to see 5 lines of raw data? (Yes or No)").lower()
        else:
            raw_data = input("Would you like to see 5 more lines of raw data? (Yes or No)").lower()
        if raw_data == 'yes':
            print(df.head(count))
            count += 5
            if count >= len(df):
                print("There is no more data to display.")
                break
        elif raw_data == 'no':
            break
        else:
            print("This is not a valid input, please try again. (Yes or No")
    
         
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()