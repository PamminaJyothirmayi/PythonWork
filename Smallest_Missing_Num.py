#  ----- Smallest Missing Number -------
# write a program to print the smallest positive integer missing given number
num = list(map(int,input().split()))
max_num = max(num)

num_list = []
for i in range(1,max_num+2):
    if not(i in num):
        num_list.append(i)
print(num_list[0])        

'''
input  : 3 1 2 5 3 7 7
output : 4


input : 5 5 2 3 1 8 8 4
output : 6
'''
