#No Duplicate Items
set_a = {"a", "b", "c", "a"}
print(set_a) # {'b', 'a', 'c'}




#Immutable Items: Set items must be immutable.
set_a = {"a", ["c", "a"]}
print(set_a)  # TypeError: unhashable type: 'list'




#Union: Union of two sets is a set containing all elements of both sets. Syntax: set_a | set_b (or) set_a.union(sequence)
set_a = {4, 2, 8}
set_b = {1, 2}
union = set_a | set_b
print(union) # {1, 2, 4, 8}




#Intersection: The intersection of two sets is a set containing common elements of both sets. 
#Syntax: set_a & set_b (or) set_a.intersection(sequence)
set_a = {4, 2, 8}
set_b = {1, 2}
intersection = set_a & set_b
print(intersection) # {2}



#Difference: The difference of two sets is a set containing all the elements in the first set but not the second.
#Syntax: set_a - set_b (or) set_a.difference(sequence)
set_a = {4, 2, 8}
set_b = {1, 2}
diff = set_a - set_b
print(diff) # {8, 4}




#Symmetric Difference: Symmetric difference of two sets is a set containing all elements which are not common to both sets.
#Syntax: set_a ^ set_b (or) set_a.symmetric_difference(sequence)
set_a = {4, 2, 8}
set_b = {1, 2}
symmetric_diff = set_a ^ set_b
print(symmetric_diff) # {8, 1, 4}



