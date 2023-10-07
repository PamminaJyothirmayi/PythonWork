print("Hello World"); #Hello World

print(2+5)        #7

print("2 + 5")   #2+5

print(1 + 1.5)    #2.5

print(5 / 2)    #2.5

print(4 / 2)    #2.0

#Print three Hashes
print("###");    """ ### """

print(2495+789358)  #791853


#Reads a line of input as a string and Take Input From User
username = input()
print(username)




#String Concatenation
a = "Hello" + " " + "World"
print(a)

#output : Hello World




#String Repetition
b = "*" * 10
print(b)

#output : **********




#Star Repetition
s = "Python"
s = ("* " * 3) + s + (" *" * 3)
print(s)

#* * * Python * * *



#Length of String
username = input()
length = len(username)
print(length)


"""
Jyothi
6
"""



#String Indexing
username = "Rani"
first_letter = username[0]
print(first_letter)

#Output:  R




#Print Name and Age
a = input()
b = input()
print(a +" is "+b+" years old")

"""
Output:=
Robert
21
Robert is 21 years old
"""






#String Repetition
a = input()
print((a+" ")*3)

# Output : Apple Apple Apple 







#First & Last Digits
number = input()
first_digit = number[0]
last_digit = number[-1]

print(first_digit)
print(last_digit)

"""
1456
1
6
"""





#Reverse the digits
n = input()
print(n[::-1])

"""
123
321
"""





#Index of Last Character
a = input()
print(len(a)-1)


"""
Python
5
"""

#Half String
a = input()
b = len(a)/2
c = int(b)
print(a[:c])

'''
input : Amazon
output : Ama

input : Bottle
output : Bot
'''

#Half Length of String
a = input()
print(len(a)/2)

"""
Airplane
4.0
"""


#Length Excluding Character 
#print the length of the word excluding the first and last character.
a = input()
print(len(a)-2)

"""
Blockchain
8
"""



#Sum of two numbers
a = int(input())  #4
b = int(input())  #5
sums = a+b
print(sums)      #9




#Calculate the Area of Rectangle
length = int(input())        #3
breadth = int(input())       #4
area=length*breadth
print(area)                  #12




#Perimeter of Rectangle  
length = int(input())            #3
breadth = int(input())           #4
perimeter = 2*(length+breadth)
print(perimeter)                  #14



##Sum of digits
a = input()                      #326
b = len(a)
sums=0
for i in range(b):
    sums = sums+int(a[i])
print(sums)                      #11







#Skip the Fourth Character
s = input()
fisrt = s[:3]
second = s[4:]
print(fisrt+second)

'''
input : Equality
output : Equlity

input : Listen 
output : Lisen
'''
