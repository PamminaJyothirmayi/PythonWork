#     ---------- Weekends ---------

#Given two dates D1 and D2, write a program to count the number of Saturdays and Sundays
#from D1 and D2. The date in string format is like "8 Feb 2021"

import datetime

date1 = input()
date2 = input()

first_date = datetime.datetime.strptime(date1,"%d %b %Y")
last_date = datetime.datetime.strptime(date2,"%d %b %Y")

day = datetime.timedelta(days=1)
saturday = 0 
sunday = 0 

while first_date <= last_date:
    if first_date.isoweekday() == 6:
        saturday += 1
    elif first_date.isoweekday() == 7:
        sunday += 1
    first_date += day   
    
print("Saturday:",saturday)        
print("Sunday:",sunday)



'''
input:  25 Jan 2021
        14 Feb 2021


output: Saturday: 3
        Sunday: 3

'''
