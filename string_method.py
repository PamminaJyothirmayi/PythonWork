#Check First Part of a String

s1 = input()
s2 = input()
print(s1.startswith(s2))

'''
input : rainbow
        rain
output : True

input : debug
        bug
output : False
'''






#Eligible Criteria
maths = int(input())
physics = int(input())
chemistry = int(input())

total_marks =  maths>=70 and physics>=60 and chemistry>=60
total_subject = maths+physics+chemistry >= 180

print(total_marks or total_subject)
    
