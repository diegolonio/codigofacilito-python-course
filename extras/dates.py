'''In order to work with dates using Python we are going to use 
the datetime library. This time we are going to list some examples
that can help you to better understand the library'''

'''To get the current date we have to
import the necessary dependencies'''
from datetime import date
from datetime import datetime

# Current day
today = date.today()

# Current date
now = datetime.now()

print(today)
print(now)

'''Attributes
Once we get the current date we can get the day, month, year,
hours, minutes and seconds from it'''

#Date
print("The current day is {}".format(today.day))
print("The current month is {}".format(today.month))
print("The current year is {}".format(today.year))

#Datetime
print("The current day is {}".format(now.day))
print("The current month is {}".format(now.month))
print("The current year is {}".format(now.year))

print("The current hour is {}".format(now.hour))
print("The current minute is {}".format(now.minute))
print("The current second is {}".format(now.second))

'''New date
If we want we can work with a particular date'''

new_date = datetime(2019, 2, 28, 10, 15, 00, 00000)

'''The arguments will be: Year, Month, Day, Hour, Minutes,
Seconds, Milliseconds'''

'''Operations
Sometimes we will have the needed to perfom some operations
with dates, it could be because we want to add days, subtract
years or just want to make comparisons. With Python we will be
able to perfom all of this operations without problems'''

from datetime import datetime
from datetime import timedelta

# Add two days to the current date
now = datetime.now()
new_date = now + timedelta(days=2)
print(new_date)

# Comparison
if now < new_date:
    print("The current date is less than the new date")

'''Date formats
Although dates in Python already have a human readable format,
sometimes we will need to be more explicit to do not fall in
ambiguities, so we will use strftme method'''

now = datetime.now()
format = now.strftime('Day :%d, Month: %m, Year: %Y, Hour: %H, Minutes: %M, Seconds: %S')
print(format)

''' %d Day
    %m Month
    %Y Year
    %H Hour
    %M Minutes
    %S Seconds
I like to define a function which allows me to display
a more human readable date format'''

from datetime import datetime

def current_date_format(date):
    months = ("January", "February", "March", "April", "May",
    	"June", "July", "August", "September", "October", "November", "December")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} {}, {}".format(month, day, year)

    return messsage

now = datetime.now()
print(current_date_format(now))