# Armstrong Number
# 153, 370, 371, 407, 1634, 8208, 9474, 54748

num = input()    #153
sum_num = 0
for i in num:
    sum_num += (int(i) ** len(num))
    
if(sum_num == int(num)):
    print("Armstrong Number")    
else:
    print("Not an Armstrong Number")

#Armstrong Number
