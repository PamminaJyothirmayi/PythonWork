#Read N Times on N lines
n = int(input())
for i in range(n):
    print(0)

''' 
input : 3
output:
0
0
0
'''



#First N Natural Numbers
num = int(input())
for i in range(1,num+1):
    print(i)



#Average of the N Numbers
n = int(input())
s=0
j = 0
for i in range(1,n+1):
    s = s + i
    j = j + 1
avg = s / j 
print(avg)




#Cubes of N Numbers
n = int(input())
for i in range(1,n+1):
    print(i**3)


'''
input : 4
output : 1 8 27 64
'''



#Print the Character
word = input()     #Morning
for i in word:
    print(i)

'''
M
o
r
n
i
n
g
'''


word = "Python"  
for each_char in word:  
    print(each_char)
'''
P  
y  
t  
h  
o  
n
'''

#Range
for number in range(3):  
    print(number)
'''
0
1
2
'''


for number in range(5, 8):  
    print(number)
'''
5
6
7
'''




#Styled Word
Word = input()        #Python
empty_str =""
for i in range(1,len(Word)):
    empty_str = empty_str + "-"+Word[i]
print(Word[0]+empty_str)    

'''
output : P-y-t-h-o-n
'''



#Factorial
num = int(input())        #4
fact = 1
while n!=0:
    fact=fact*num 
    num = num-1
print(fact)              #24




#Factors of a Number
n = int(input())            #6
for i in range(1,n+1):
    if(n%i == 0):
        print(i)
'''
1
2
3
6
'''

#Factors of a Number - 2
num = int(input())            #15
new_num=""
for i in range(1,num+1):
    if(num%i==0):
        new_num += str(i)+" "
print(new_num)                # 1 3 5 15




#Sum of All Factors
num =int(input())            #12
sum_num =0
for i in range(1,num+1):
    if(num%i == 0):
        sum_num += i
print(sum_num)                #28



#Print Vowels
string = input()
vowels = "aeiou"
for i in string:
    if(i in vowels):
        print(i)
        
'''
input : indian
output : 
i
i
a
'''

#Vowels in a String
string = input()
vowels = "aeiou"
new_str=""
for ch in string:
    if(ch in vowels):
        new_str += ch
print(new_str)

'''
input : container
output : oaie
'''

#Reverse the String
word = input()
new_str =""
for ch in word:
    new_str  = ch+ new_str 
print(new_str) 

'''
input : Hurray! We have won the match.
output : .hctam eht now evah eW !yarruH
'''

#Count of Vowels
string = input()        #developer
vowels = "aeiou"
c=0
for i in string:
    if(i in  vowels):
        c=c+1
print(c)                #4


#Vowels of String-2
string = input()
vowels = "aeiou"
str=""
for i in string:
    if i in vowels:
        str = str + i 
        
if len(str) > 2:
    print("String has more than two vowels")
else:
    print("String doesn't have more than two vowels")

'''
input : Indian
output : String has more than two vowels

input : code
output : String doesn't have more than two vowels
'''



#Multiplication Table
num = int(input())        #3
for i in range(1,11):
    print(num , "x" ,i ,"=",num*i)
    
'''
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
'''




#Greatest Among N Numbers
n = int(input())
s = []
greatest_num=0
for i in range(n):
    m = int(input())
    s.append(m)
print(max(s))  

'''
input : 5
8
11
96
49
25

output: 96
'''

#Smallest Among N Numbers
n = int(input())
smallest = 100
for i in range(n):
    num = int(input())
    if num<smallest:
        smallest=num 
print(smallest)      
'''
input : 5
8
11
96
49
25

output: 8
'''



