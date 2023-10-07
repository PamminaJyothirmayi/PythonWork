#Zero or Positive or Negative
num = int(input())

if(num>0):
    print("Positive")
elif(num<0):
    print("Negative")
else:
    print("Zero")



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
