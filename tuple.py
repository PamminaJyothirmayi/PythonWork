#Accessing Tuple Elements
tuple_a = (5, "Six", 2, 8.2)
print(tuple_a[1]) # Six


#Tuple Slicing
tuple= ('a','b','c','d','e','f','g','h','i','j')
print(tuple[0:2]) # ('a', 'b')
print(tuple[-1:-3:-2]) # ('j',)
print(tuple[1:7:2]) # ('b', 'd', 'f')


#Membership Check
tuple_a = (1, 2, 3, 4)
is_part = 5 in tuple_a
print(is_part) # False
tuple_a = (1, 2, 3, 4)
is_part = 5 not in tuple_a
print(is_part) # True




#Tuple Packing: () brackets are optional while creating tuples. In Tuple Packing, Values separated by commas will be packed into a tuple.
a = 1, 2, 3
print(type(a))
print(a)
# Output is: <class 'tuple'>
#(1, 2, 3)




#Unpacking: Values of any sequence can be directly assigned to variables. Number of variables in the left should match the length of the sequence.
tuple_a = ('R', 'e', 'd')
(s_1, s_2, s_3) = tuple_a
print(s_1, s_2, s_3) # R e d


