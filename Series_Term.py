#  ------------------ 2 Series ---------------
# Write a program to print the N terms in the given series, each on a new line.

# 2, 22, 222, 2222, .... N terms

'''
Explaination
============

First Term     2
Second Term    22
Third Term     222
Fourth Term    2222
'''

number = int(input())        #6
for i in range(1,number+1):
    print("2"*i)

'''
output: 6
2
22
222
2222
22222
222222

--------

output: 3
2
22
222

'''



#Sum of N Terms in 2 Series
number = int(input())        
sum_num = 0
for i in range(1,number+1):
    sum_num = sum_num + (int("2"*i))
print(sum_num)

'''
input : 3
output : 246

input : 8 
output : 24691356
'''


#Sum of N Terms 1 series      1,11,111,1111,.....,N terms
number = int(input())
sums = 0
for i in range(1,number+1):
    term = "1"
    sums = sums + int(term*i)
print(sums)   

'''
input : 4        (1+11+111+1111)
output : 1234

input : 5 
output : 12345
'''




#Sum of N Terms in X Series      X, XX, XXX, XXXX,....,N terms

X = input()        # 7
N = int(input())   # 4

product = 0
for i in range(1,N+1):
    product = product + int(X*i)
print(product)

'''
input : 7            (7+77+777+7777)
        4
output :8638

input : 6            (6 + 66)
        2
output :72
'''


#Sum of N Terms in X Square Series      (x)^2 + (xx)^2 + (xxx)^2 ... Nterm
x = input()
n = int(input())

sum_num = 0
for i in range(1,n+1):
    sum_num = sum_num + (int(x*i))**2
print(sum_num)

'''
input : 4
        3
output : 199088
'''



#
