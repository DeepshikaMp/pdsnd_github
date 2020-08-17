'''
Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:

Gender
Birth Year

Data for the first 10 rides in the new_york_city.csv file

The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them (Chicago, New York City, Washington). These files had more columns and they differed in format in many cases. Some data wrangling has been performed to condense these files to the above core six columns to make your analysis and the evaluation of your Python skills more straightforward. In the Data Wrangling course that comes later in the Data Analyst Nanodegree program, students learn how to wrangle the dirtiest, messiest datasets, so don't worry, you won't miss out on learning this important skill!

Statistics Computed
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

#1 Popular times of travel (i.e., occurs most often in the start time)

most common month
most common day of week
most common hour of day
#2 Popular stations and trip

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)
#3 Trip duration

total travel time
average travel time
#4 User info

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)
'''
import time
import pandas as pd
import numpy as np

chicago = 'chicago.csv'
new_york = 'new_york_city.csv'
washington = 'washington.csv'

def get_city():
    '''Let the user input city and the function returns the filename for
    that city's bike share data.
    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input("Enter name of the city you would like to explore (Chicago (CH), Washington (WA), New York (NY):")
    city = city.strip().lower()

    while True:
        if city == 'ny' or city == 'new york':
            print('\nWe\'re going to explore its New York City\'s bikeshare data\n')
            return new_york
        elif city == 'wa' or city == 'washington':
            print('\nWe\'re going to explore its Washington City\'s bikeshare data\n')
            return washington
        elif city == 'ch' or city == 'chicago':
            print('\nWe\'re going to explore its Chicago City\'s bikeshare data\n')
            return chicago
        city = input("Please choose between one of the three cities - Chicago (CH), New York (NY), or Washington (WA)")
        city = city.lower()

def get_month():
    '''Lets the user input for a month and returns the specified month.
    Args:
       none
    Returns:
        (str) Month information.
    '''
    month = input('\nPick a month between January, February, March, April, May, June? Please type the full month name or type \'All\' if you wish to see data for all months.\n')
    while month.strip().lower() not in ['january', 'february', 'march', 'april', 'may', 'june','all']:
        month = input('\nPlease choose between January, February, March, April, May, June or All? Please type the full month name.\n')
    return month.strip().lower()


def get_day():
    '''Lets the user input for a day and returns the specified day.
    Args:
        none
    Returns:
        (str) Day information.
    '''
    day = input('\nWhich day of the week? Please type a day Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. \n')
    while day.lower().strip() not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            day = input('\nPlease type a day as a choice from Mon, Tue, Wed, Thur, Fri, Sat, Sun. \n')
    return day.lower().strip()


def load_data(city):
    """
    Reads the data for the specified city and loads it to a dataframe.
    Args:
        (str) city - name of the city to analyze
    Returns:
        df - Pandas DataFrame containing city data used for computation with month and day columns added.
    """
    df = pd.read_csv(city)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    return df


def get_filters(df, month, day):
    """
    Reads the data for the specified city and loads it to a dataframe.
    Args:
       (str) city - name of the city to analyze
    Returns:
        df - Pandas DataFrame containing city data used for computation with month and day columns added.
    """
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
         df = df[df['day_of_week'] == day.title()]

    return df

def most_popular_month(df):
    '''Which is the most popular month?
    INPUT:
        df - dataframe returned from get_filters()
    OUTPUT:
       Returns most_popular_month
    '''
    print(df)
    print('\n1. The most popular month for bike traveling:')
    popular_month_index = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[popular_month_index - 1].capitalize()
    return popular_month

def most_popular_day_of_week(df):
    '''Which is the most popular day of the week?
    INPUT:
        df - dataframe returned from get_filters()
    OUTPUT:
       Returns opular_day_of_week
    '''
    print('\n2. The most popular week for bike traveling:')
    popular_day_of_week = df['day_of_week'].mode()[0]
    return popular_day_of_week

def most_popular_hour(df):
    '''Which is the most popular hour?
    INPUT:
        df - dataframe returned from get_filters()
    OUTPUT:
       Returns popular_hour
    '''
    print('\n3. The most popular hour for bike traveling:')
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    return popular_hour


def station_stats(df):
    '''Which is the most popular start station and most popular end station and popular trip?
    INPUT:
        df - dataframe returned from get_filters()
    OUTPUT:
        tuple = Returns most popular start, end stations and popular combination of the two.
    '''
    print('\n4. The most popular start station:\n')
    popular_start_station = df['Start Station'].mode()[0]
    print(popular_start_station)

    print('\n5. The most popular end station:\n')
    popular_end_station = df['End Station'].mode()[0]
    print(popular_end_station)

    print('\n6. The most popular combination of start and end station:\n')
    df['Station'] = df['Start Station'].str.cat(df['End Station'], sep = " - ")
    popular_combination_station = df['Station'].mode()[0]
    print(popular_combination_station)
    return popular_start_station,popular_end_station, popular_combination_station


def trip_duration_stats(df):
    '''What is the total trip duration and average trip duration?
    INPUT:
        df - dataframe returned from get_filters()
    OUTPUT:
        tuple = total trip duration, average trip durations
    '''
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']

    print('\n7. The total traveling time spent on each trip:')
    total_travel_time = np.sum(df['Travel Time'])
    total_number_of_Days = str(total_travel_time).split()[0]
    print ("\nThe total travel time:" + total_number_of_Days + ' days')

    print('\n8. The average traveling time spent on each trip?')
    average_travel_time = np.mean(df['Travel Time'])
    average_number_of_Days = str(average_travel_time).split()[0]
    print("The average travel time in days:" + average_number_of_Days + ' days')
    return total_travel_time, average_travel_time

def users(df):
    '''What are the counts of each user type - subscribers, customers, or dependents?
    INPUT:
        df - dataframe returned from get_filters()
    OUTPUT:
        Returns counts for each user type
    '''
    print('\n9. Total count of subscribers, customers, or dependents:\n')

    return df['User Type'].value_counts()


def gender(df):
    '''What are the counts of gender?
    INPUT:
        df - dataframe returned from get_filters()
    OUTPUT:
        gender - counts for each gender
    '''
    try:
        print('\n10. The breakdown of gender among users:\n')

        return df['Gender'].value_counts()
    except:
        '''There are empty fields for certain tuples in the data'''
        print('There is no gender data in the source filtered.')


def birth_year(df):
    '''Which is the earliest, latest, and most frequent birth year?
    INPUT:
        df - dataframe returned from get_filters()
    OUTPUT:
        tuple of earliest, latest, and most frequent year of birth
    '''
    try:
        print('\n11. The earliest, latest, and most frequent year of birth, respectively:')
        earliest_year = int(np.min(df['Birth Year']))
        print ("\nThe earliest year of birth is " + str(earliest_year) + "\n")
        latest_year = int(np.max(df['Birth Year']))
        print ("The latest year of birth is " + str(latest_year) + "\n")
        most_frequent_year= int(df['Birth Year'].mode()[0])
        print ("The most frequent year of birth is " + str(most_frequent_year) + "\n")
        return earliest_year, latest_year, most_frequent_year
    except:
        print('No available birth date data for this period.')

def compute_time(fun, df):
    """
    Calculates the time it takes to commpute a stat
    INPUT:
      fun  - the applied stats function
      df - the dataframe with all the data
    OUTPUT:
        prints to console, doesn't return a value
    """

    start_time = time.time()
    functionToCompute = fun(df)
    print(functionToCompute)
    print("\n\nComputing this function took %s seconds." % (time.time() - start_time))

def display_data(df):
    '''Displays raw and filtered data bsaed on the argument.
    INPUT:
        df - dataframe returned from get_filters()
    OUTPUT:
        none.
    '''
    print('***Bike Share Data***\n',df)

def main_stats():
    '''Calculates the statitics about the city based on the user input.
    Args:
        none.
    Returns:
        none.
    '''
    city = get_city()

    df = load_data(city)

    month = get_month()
    day = get_day()

    df = get_filters(df, month, day)

    sfunction_list = [most_popular_month,
    most_popular_day_of_week, most_popular_hour,
    station_stats, trip_duration_stats, users, birth_year, gender]

    for fun in sfunction_list:
        print('function execution:', fun)
        compute_time(fun, df)

    #Display filtered data
    display = input("\n * Would you like to display the filtered data? Type \'yes\' or \'no\'.\n")
    if display.upper() == 'YES' or display.upper() == "Y":
        display_data(df)

    # Restart?
    restart = input("\n * Would you like to restart and perform another analysis? Type \'yes\' or \'no\'.\n")
    if restart.upper() == 'YES' or restart.upper() == "Y":
        main_stats()


if __name__ == "__main__":
	main_stats()
