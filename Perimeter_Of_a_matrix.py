#Write a python program that reads an M x N matrix and prints "Perimeter of a matrix".
#Perimeter of a matrix is defined as the sum of all the elements on the 4 edges of the matrix.

a = input().split()
m =  int(a[0])
n =  int(a[1])

p=[]
for i in range(m):
    for j in range(n-1):
        if i==0 or i==m-1 or j==0 or j==n-1:
            p.append(a[i][j])
print(p)

a = input().split()
m =  int(a[0])
n =  int(a[1])

matrix=[]#rows
for i in range(m):
    r=input().split()
    nr=[]
    for i in r:
        nr.append(int(i))
    matrix.append(nr)

s=0
for i in range(m):
    for j in range(n):
        if i==0 or i==m-1 or j==0 or j==n-1:
            s += matrix[i][j]
print(s)
