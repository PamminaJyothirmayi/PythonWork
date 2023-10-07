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
