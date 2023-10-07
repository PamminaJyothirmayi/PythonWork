#Write a program to mirror the characters of the string in alphabetical order to create a secret message.

"""
a b c d e f g h i j k l m n o p q r s t u v w x y z
z y x w v u t s r q p o n m l k j i h g f e d c b a
"""


dict_word = {}
index=122
for i in range(97,123):
    dict_word[chr(i)] = chr(index)
    index = index-1 
  

string = input().lower()
new_string = ""
for i in string:
    if not(i == " "):
        new_string += dict_word[i]
    else:
        new_string += " "
print(new_string)    


'''
input : python
output : kbgslm

input : Foundations
output : ulfmwzgrlmh

'''






#    ---------Secret Message-2 ----------

#Write a program to print a secret message that replaces characters with numbers 'a' with 1, 'b' with 2, ... 'z' with 26
#where characters are separated by '-'.


dict_word = {}

num_val = 1
for i in range(97,123):
    dict_word[chr(i)] =  int(num_val)
    num_val = num_val + 1

string = input().lower()

result = ""
for char in string:
    if not(char ==" "):
        result += str(dict_word[char])+"-"
    else:
        result += " "        

list_word =[]   
for word in result.split():
    list_word.append(word[:len(word)-1])
print(*list_word)


'''
input : python
output : 16-25-20-8-15-14


input : Foundations
output : 6-15-21-14-4-1-20-9-15-14-19
'''






