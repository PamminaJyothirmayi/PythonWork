#Importing from a Module:
from math import factorial
print(factorial(5)) # 120


#Aliasing Imports: 
from math import factorial as fact
print(fact(5)) # 120


#Randint: randint() is a function in random module which returns a random integer in the given interval.
import random
random_integer = random.randint(1, 10)
print(random_integer) # 8


#Choice: choice() is a function in random module which returns a random element from the sequence.

import random
random_ele = random.choice(["A","B","C"])
print(random_ele) # B
