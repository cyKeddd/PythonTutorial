# we often need current date and time when logging errors and saving data
# to get current date and time
# we need to use the datetime library
from datetime import datetime

# The specified formats depend on the formatting options supported by the platform and the C library used. However, some common format specifiers used in strftime are:

# %a - abbreviated weekday name
# %A - full weekday name
# %b - abbreviated month name
# %B - full month name
# %c - preferred local date and time representation
# %d - zero-padded day of the month as a decimal number [01,31]
# %H - hour (24-hour clock) as a decimal number [00,23]
# %I - hour (12-hour clock) as a decimal number [01,12]
# %m - month as a zero-padded decimal number [01,12]
# %M - minute as a zero-padded decimal number [00,59]
# %p - locale’s equivalent of either AM or PM
# %S - second as a zero-padded decimal number [00,61]
# %U - Sunday as the first day of the week, week number of the year as a decimal number [00,53]
# %w - weekday as a decimal number [0(Sunday),6]
# %W - Monday as the first day of the week, week number of the year as a decimal number [00,53]
# %x - preferred local date representation
# %X - preferred local time representation
# %y - year without century as a zero-padded decimal number [00,99]
# %Y - year with century as a decimal number
# %z - UTC offset in the form +HHMM or -HHMM
# %Z - time zone name

current_date = datetime.now()
# the now function returns a datetime object
print('Today is: ' + str(current_date))

# there are functions you can use with datetime objects to manipulate dates
from datetime import datetime, timedelta
today = datetime.now()
print('Today is: ' + str(today))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

# Import the datetime library
import datetime

# Get the current date and time
current_time = datetime.datetime.now()

# Change the time format to 12-hour
current_time_12_hour = current_time.strftime("%I:%M %p")

# Write the date in the desired format
current_date = current_time.strftime("%B, %d, %Y")

# Print the modified date and time
print("Current time in 12-hour format: ", current_time_12_hour)
print("Current date: ", current_date)

# use date functions to control date formatting
from datetime import datetime
current_date = datetime.now()
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

# sometimes you receive the date as a string and need to convert it to a datetime object
from datetime import datetime

birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))

# converting it to a datetime allows you to use the date functions
from datetime import datetime, timedelta
birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))
one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))

# make sure you add exception handling in case the date entered is invalid
from datetime import datetime
birthday = input('When is your birthday (dd/mm/yyyy)?')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))

# btw if you are seeing this and already dont know use cls in the terminal to clear all your stuff if it is cluttering