# ----------------- Perfect_Number ------------------
#A number is considered as a Perfect number if sum of all factors including itself is equal to the number.

     
num = int(input())       #6 --->1 + 2 + 3
sum_num=0
for i in range(1,n):
    if(num%i == 0):
        sum_num += i
    
if(sum_num == num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
