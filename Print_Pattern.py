#Star Repetition
a = input()
b = len(a[1:-1])
print(a[0]+b*"*"+a[-1])

'''
input : qwerty@2020
output : q*********0

input : 9647329032
output : 9********2
'''



# Print Star pattern using for loop
n = int(input())
for i in range(1,4):
    print("* "*n)

'''
input : 4
output :
* * * * 
* * * * 
* * * * 
'''


#Solid Square
n = int(input())        #4
for i in range(n):
    print("* "*n)
    
'''
* * * * 
* * * * 
* * * * 
* * * * 
'''




#Solid Rectangle
row = int(input()) 6
col = int(input()) 2

for i in range(row):
    print("*"*col)

'''
**
**
**
**
**
**
'''




#Solid Right Angled Triangle
n = int(input())            #4
for i in range(1,n+1):
    print("* "*i)

'''
* 
* * 
* * * 
* * * * 
'''


#Inverted Right Angled Triangle
row = int(input())
for i in range(row):
    print("* "*(row-i))
'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''



#Two Right Angled Triangles - 2
n = int(input())        #3
for i in range(1,n+1):
    print("* "*i)
for i in  range(n,0,-1):
    print("* "*i)
'''
*
* *
* * *
* * *
* *
*
'''

#Square with number pattern
n = int(input())            #3
for i in range(1,n+1):
    print(str(i)*n)

'''
1111
2222
3333
'''


#Right Angled Triangle-2
n = int(input())            #4
for i in range(1,n+1):
    a =(str(i)+" ")*i 
    print(a)

'''
1
2 2
3 3 3
4 4 4 4
'''


#Two Right Angled Triangles
n = int(input())            #3
for i in range(2):
    for j in range(1,n+1):
        print(str(j)*j)
        
'''
1
22
333
1
22
333
'''



#Rectangle - 3
m = int(input())
n = int(input())

for i in range(1,m+1):
    a = str(i)+" "
    print(a*n)

'''
1 1 1 1
2 2 2 2
3 3 3 3
'''

#Inverted Right Angled Triangle-2
n = int(input())        #4
for i in range(n,0,-1):
    print((str(i)+" ")*i)

'''
4 4 4 4
3 3 3
2 2
1
'''
