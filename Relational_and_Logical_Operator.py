#Zero or Positive or Negative
num = int(input())

if(num>0):
    print("Positive")
elif(num<0):
    print("Negative")
else:
    print("Zero")



#Eligible Criteria
maths = int(input())
physics = int(input())
chemistry = int(input())

total_marks =  maths>=70 and physics>=60 and chemistry>=60
total_subject = maths+physics+chemistry >= 180

print(total_marks or total_subject)


#Greatest Among Three Numbers
n1 = int(input())
n2 = int(input())
n3 = int(input())

if(n1>n2 and n1>n3):
    print(n1)
elif(n2>n1 and n2>n3):
    print(n2)
else:
    print(n3)





#Smallest Among Three Numbers
a = int(input())
b = int(input())
c = int(input())
if a<b and a<c:
    print(a)
elif(b<a and b<c):
    print(b)
elif(c<a and c<b):
    print(c)
else:
    print(a)




#Even or Odd Number
num = int(input())
remainder = n % 2
if(remainder==0):
    print("Even")
else:
    print("Odd")
 



#3-digit Armstrong Number
number = input()
a = int(number[0])**3
b = int(number[1])**3
c = int(number[2])**3

print(a+b+c == int(number))

'''
input : 371
output : True

input : 351
output : False
'''



#4-digit Armstrong Number
n = input()                #1634
a = int(n[0])**len(n)
b = int(n[1])**len(n)
c = int(n[2])**len(n)
d = int(n[3])**len(n)

if a+b+c+d == int(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

#output : Armstrong Number






#Years, Weeks & Days
# N = 1329 , The value can be 1329  = 3 years + 33 weeks + 3days
number = int(input())

year = number//365
print(year)

week_nums = number%365
weeks = week_nums//7
print(weeks)

day_nums = week_nums%7
print(day_nums)

'''
input: 1329
output : 3
         33
         3
'''



#Print Divisible by 5

number = 5
is_divisible_by_10 = (number % 10 == 0)
is_divisible_by_5 = (number % 5 == 0)
if is_divisible_by_10:
    print("Divisible by 10")
elif is_divisible_by_5:
    print("Divisible by 5")
else:
   print("Not Divisible by 10 or 5")

#output : Divisible by 5





#Name of the polygon
n = int(input())
if(n<3):
    print("Not Polygon")
elif(n==3):
    print("Triangle")
elif(n==4):
    print("Quadrilateral")
elif(n==5):
    print("Pentagon")
else:
    print("Big Polygon")





#Profit or Loss
cp =int(input())
sp = int(input())

if sp==cp:
    print("No Profit - No Loss")
elif sp>cp:
    print("Profit")
else: 
    print("Loss")




#Get Season
#Write a program to find season for the given month number.
num  = int(input())
if(num==1 or num==11 or num==12):
    print("Winter")
elif(num==2 or num==3):
    print("Spring")
elif(num==4 or num==5 or num==6):
    print("Summer")
elif(num==7 or num==8):
    print("Rainy")
else:
    print("Autumn")



#Weather condition
T=float(input())
if(T<0):
    print("Freezing weather")
elif(0 <= T < 10):   
    print("Very Cold weather")
elif(10 <= T < 20):
    print("Cold weather")
elif(20 <= T < 30):
    print("Normal")
elif(30 <= T < 40):
    print("Hot")
else:
    print("Very Hot")




#Leap Year
year = int(input())
print(yyear%4==0 and year%100!= 0)

'''
input : 2016
output : True

input : 1800
output : False
'''



#Relation between two numbers 
a = int(input())
b = int(input())

if(a==b):
    print("A == B")
elif(a>b):
    print("A > B")
else:
    print("A < B")


#Day Name
#Write a program that reads a day number and prints the corresponding day name.
n = int(input())
if n==1:
    print("Monday")
elif(n==2):
    print("Tuesday")
elif(n==3):
    print("Wednesday")
elif(n==4):
    print("Thursday")
elif(n==5):
    print("Friday")
elif(n==6):
    print("Saturday")
else:
    print("Sunday")



#Name of Month
#Given the number of the month, write a program to print the name of the month.

month = int(input())
if(month==1):
    print("January")
elif(month==2):
    print("February")
elif(month==3):
    print("March")
elif(month==4):
    print("April")
elif(month==5):
    print("May")
elif(month==6):
    print("June")
elif(month==7):
    print("July")
elif(month==8):
    print("August")
elif(month==9):
    print("September")
elif(month==10):
    print("October")
elif(month==11):
    print("November")
elif(month==12):
    print("December")
else:
    print("Invalid Month Number")

'''
input : 4
output : April 


input : 13
output : Invalid Month Number
'''


#Simple Calculator
c = input()
f = int(input())
s = int(input())

if(c == "+"):
    print(f+s)
elif(c == "-"):
    print(f-s)
elif(c == "*"):
    print(f*s)
elif(c == "/"):
    print(f/s)
else:
    print(f%s)

'''
*
2
5

output : 10
'''

#Denomination-2
#Write a program that reads an amount A and prints the minimum number of 100,50,10 and 1 rupees notes required for the given amount.
n = int(input())
a = (n//100)
x = n%100 

b = x//50
y = x%50 

c = y//10
z = y%10 

d = z//1
print("100:"+str(a))
print("50:"+str(b))
print("10:"+str(c))
print("1:"+str(d))


'''
input :    893
output :   100:8
           50:1
           10:4
           1:3
'''
#---------------------------------------------

m = int(input())

is_divisible_by_500 = m//500 
print("500:",is_divisible_by_500 , end=" ")

x = m%500 
is_divisible_by_50 = x//50 
print("50:",is_divisible_by_50 ,end =" ")

y = x%50
is_divisible_by_10 = y//10 
print("10:",is_divisible_by_10 , end=" ")

z = y%10 
reminder_value = z 
print("1:",reminder_value)

'''
input : 1543
output : 500: 3 50: 0 10: 4 1: 3
'''

#-----------------------------------------

n = int(input()) #370

hundred_notes = n//100 #3
print("100 Notes:",hundred_notes)

x = n%100  #70

fifty_notes = x//50 #1
print("50 Notes:",fifty_notes)

y = x%50 #20

twenty_notes = y//20 #1
print("20 Notes:",twenty_notes)

z = y%20 #0 

ten_notes = z//10 #0 
print("10 Notes:",ten_notes)

'''
input : 370
output : 100 Notes: 3
         50 Notes: 1
         20 Notes: 1
         10 Notes: 0
'''

#---------------------------


amount = int(input())

a_1000 = amount//1000

x = amount%1000 
a_500 = x//500 

y = x%500 
a_100 = y//100 

z = y%100 
a_50 = z//50

p = z%50 
a_20 = p//20 

q = p%20 
a_5 = q//5 

r = q%5 
a_1 = r  

print("1000:" + str(a_1000))
print("500:" + str(a_500))
print("100:" + str(a_100))
print("50:" + str(a_50))
print("20:" + str(a_20))
print("5:" + str(a_5))
print("1:"+ str(a_1))

'''
input: 8593

output:=
1000:8
500:1
100:0
50:1
20:2
5:0
1:3
'''










# Day Name-2 Hard level
# Given the weekday of the first day of the month, determine the day of the week of the week of the given date in that month.

day  = input()
number = int(input())
name_of_day = 0

if day == "Monday":
    name_of_day = 1 
elif day == "Tuesday":
    name_of_day = 2
elif day == "Wednesday":
    name_of_day = 3
elif day == "Thursday":
    name_of_day = 4
elif day == "Friday":
    name_of_day = 5
elif day == "Saturday":
    name_of_day = 6
else:
    name_of_day = 0
 
number_of_day= name_of_day        
odd_days = number_of_day+(number-1)
reminder = odd_days%7 # it will be 4

if reminder==1:
    print("Monday")
elif reminder==2:
    print("Tuesday")
elif reminder==3:
    print("Wednesday")
elif reminder==4:
    print("Thursday")
elif reminder==5:
    print("Friday")
elif reminder==6:
    print("Saturday")
elif reminder==0:
    print("Sunday")


'''
input:  Monday
        16

output : Tuesday
'''






#Days Conversion

n = int(input())
y = int(n/365)
w = int((n%365)/7)
d = (n - ((y*365)+(w*7)))
print(str(y) +" years " + str(w) +" weeks "+ str(d) +" days")

'''
input : 1329
output : 3 years 33 weeks 3 days


input : 960
output : 2 years 32 weeks 6 days
'''



#Traingles

a = int(input())
b = int(input())
c = int(input())

if(a==b==c):
    print("Equilateral")
elif(a==b or a==c or b==c):
    print("Isosceles")
else:
    print("Scalene")

'''
input : 4
        4
        4
output : Equilateral


input : 4
        4
        3
output : Isosceles
'''

