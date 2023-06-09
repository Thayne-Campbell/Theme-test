import time
import pandas as pd
import numpy as np
import datetime

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
        city = input("Which city's data would you like to explore? Chicago, New York City, or Washington?\n").lower()
        if city in ["Chicago".lower(), "New York City".lower(), "Washington".lower()]:
            print(f"{city} it is!")
            break
        else:
            print("Oops! That's not a valid city. Please try again.")
            
            # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month = input("Which month's data would you like to look at? Please type the full name of the month, or \"all\" to select all months.\n").lower()
        if month in ["January".lower(), "February".lower(), "March".lower(), "April".lower(), "May".lower(), "June".lower(), "all".lower()]:
            print (f"{month}? You got it!")
            break
        else:
            print("Erm... you may have misspelled something. Try again!")
            
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            
    while True:
        day = input("Lastly, which day of the week would you like to look at? Please enter the full name of the day, or select \"all\" to choose no day filter.\n").lower()
        if day in ("Monday".lower(), "Tuesday".lower(), "Wednesday".lower(), "Thursday".lower(), "Friday".lower(), "Saturday".lower(), "Sunday".lower(), "all".lower()):
            print(f"{day}? Great choice!")
            break
        else:
            print("hmm.. That's not a day of the week I'm familiar with. Want to try again?")
            

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
    
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    print (f'Here are the stats for {city} in {month}:\n')
    
    

    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    
    #Converting the Start time column to Date time so that we can separate the months from days, minutes from seconds etc.
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour
    
 
    # TO DO: display the most common month
    Popular_month = df['month'].mode()[0]
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    else:
        print("most popular month: ", Popular_month)
        

    
    
    # TO DO: display the most common day of week
    Popular_day = df['day_of_week'].mode()[0]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        print()
    else:
        print("Most popular day: ", Popular_day)
    
    
    

    # TO DO: display the most common start hour
    Popular_hour = df['Hour'].mode()[0]
    
    
    print("Most popular start time: ", Popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
    
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
     
    Popular_Station = df['Start Station'].mode()[0] 
    
    print('The most popular Start Station: \n', Popular_Station)
    

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('The most popular End Station: \n', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    start_end = df.groupby(['Start Station','End Station']).size().idxmax() #using size to get the total number of elements in each column, and then idxmax to find the max from each.
    
    print('The most frequent combination of start station and end station trips: \n', start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
    
    
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = pd.to_timedelta(df['Trip Duration'].sum(), unit = 's') #setting the argument unit to 's' or 'seconds' to override the default in argument of 'nanoseconds'. 
    print('Total travel time was: ', total_time)

    # TO DO: display mean travel time
    mean_time = pd.to_timedelta(df['Trip Duration'].mean(), unit = 's')
    print('The average travel time was: ', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
    
    
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users = df['User Type'].value_counts()
    print(users.to_string())  # printing the results to string to rid the results of the data types (uncessecary information). Got this idea from my classmates.
     
    # TO DO: Display counts of gender
    
    df['Gender'] = df.get('Gender')
    gender_count = df['Gender'].value_counts()
    
    if city != 'washington':
        print(gender_count.to_string())
        
    else:
        print()
    
    
    # TO DO: Display earliest, most recent, and most common year of birth
    df['Birth Year'] = df.get('Birth Year')
    years = df['Birth Year']
    
    earliest_year = (years).min()
    most_recent_year = (years).max()
    common_year = (years).mean()
    
    for i in years:
        if i in range(0,2022): #programs that prompt you to enter your birth year don't often give you the option to enter one from the future. I figured this was a safe bet.
            print(f'The earliest birth year is {earliest_year}')
            print(f'The most recent birth year is {most_recent_year}') #learned about this new formatting trick from Tal
            print(f'The most common birth year is {common_year}')
            break
        else:
            print()
            break
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    #insert some way to increase index value by 5 each time
    
    i = 0 # assigning value to 'i' to be used to increase the index value in the following iloc statement.
    
    # creating a prompt to ask the user if they would like to see 5 lines of raw data.
    answer = input('\nWould you like to see the raw data? Enter yes or no.\n')
    if answer != 'no'.lower():
        print('You got it!')
        print(print(df.iloc[i:i+5])) 
        while True:
            question = input('\nWould you like to see more? Yes or no?\n')    #asking the user again if they would like to continue to look at raw data 5 lines at a time.
            if question != 'no'.lower():    #technically, anything aside from 'no' will ask as a 'yes' response, but will not break the code. following the example from the main function below.
                print(df.iloc[i:i+5])
                i += 5
            else:
                break
        
    else:
        print('Suit yourself!')  #my sassy exit statement for those who choose not to view the raw data. 
      
    return df


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":                              #and that's it! thanks for reviewing my project!
	main()