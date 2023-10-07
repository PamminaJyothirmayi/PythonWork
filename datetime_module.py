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
