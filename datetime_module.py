
# Representing Date: A date object can be used to represent any valid date (year, month and day).

import datetime
date_object = datetime.date(2023, 12, 17)
print(date_object) # 2023-12-17



# Attributes of Date Object:

from datetime import date
date_object = date(2019, 4, 13)
print(date_object.year) # 2019
print(date_object.month) # 4
print(date_object.day) # 13



#Today’s Date: Class method today() returns a date object with today’s date.

import datetime
date_object = datetime.date.today()
print(date_object) # 2023-01-17

(or)

from datetime import date
date_obj = date.today()
print(date_obj)


#Representing Time: A time object can be used to represent any valid time (hours, minutes and seconds).

from datetime import time
time_object = time(11, 34, 56)
print(time_object) # 11:34:56



#Attributes of Time Object:

from datetime import time
time_object = time(11, 34, 56)
print(time_object.hour) # 11
print(time_object.minute) # 34
print(time_object.second) # 56



#Datetime: The datetime class represents a valid date and time together.

from datetime import datetime
date_time_obj = datetime(2018, 11, 28, 10, 15, 26)
print(date_time_obj.year) # 2018
print(date_time_obj.month) # 11
print(date_time_obj.hour) # 10
print(date_time_obj.minute) # 15


#Timedelta: Timedelta object represents duration.

from datetime import timedelta
delta = timedelta(days=365, hours=4)
print(delta) # 365 days, 4:00:00



#Calculating Time Difference:

import datetime
dt1 = datetime.datetime(2021, 2, 5)
dt2 = datetime.datetime(2022, 1, 1)
duration = dt2 - dt1
print(duration) # 330 days, 0:00:00
print(type(duration)) # <class 'datetime.timedelta'>


#Formatting Datetime: The datetime classes have strftime(format) method to format the datetime into any required format like
#mm/dd/yyyy
#dd-mm-yyyy

from datetime import datetime
now = datetime.now()
formatted_datetime_1 = now.strftime("%d %b %Y %I:%M:%S %p")
print(formatted_datetime_1) # 05 Feb 2021 09:26:50 AM

formatted_datetime_2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print(formatted_datetime_2) # 05/02/2021, 09:26:50



#Parsing Datetime: The class method strptime() creates a datetime object from a given string representing date and time.

from datetime import datetime
date_string = "28 November, 2018"
print(date_string) # 28 November, 2018

date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object) # 2018-11-28 00:00:00












#Home Work 

# --------- Parsing Datetime -----
# Write a program to convert the date given in the string format to a datetime object.
#The date in string format is like "8 Feb 2021."

from datetime import datetime
dates = input()
a = datetime.strptime(dates,"%d %b %Y")
print(a)

'''
input : 2 Jul 2000
output : 2000-07-02 00:00:00

input : 14 Oct 1999
output : 1999-10-14 00:00:00
'''



# --------- Formatting Datetime -----------
#Write a program to convert the date in string format to another string format.

from datetime import datetime
dates = input()
a = datetime.strptime(dates,"%b %d %Y %I:%M%p")
b = datetime.strftime(a,"%d/%m/%Y %H:%M:%S")
print(b)


'''
input : Jul 01 2014 02:43PM
output : 01/07/2014 14:43:00

input : Feb 29 2000 02:43AM
output : 29/02/2000 02:43:00
'''
