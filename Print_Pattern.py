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



# Print Star pattern

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

#Print + pattern
n = int(input())
for i in range(1,4):
    print("+ "*n)

'''
input : 4

output:
+ + + +
+ + + +
+ + + +
'''
