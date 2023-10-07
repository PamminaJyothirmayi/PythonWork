#3-digit Armstrong Number

number = input()
a = int(number[0])**3
b = int(number[1])**3
c = int(number[2])**3

print(a+b+c == int(number))

