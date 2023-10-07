""" Two Words Combination """
#Print all the unique combinations of two words in lexicographical order.

def combination_word(words):
    words = sorted(words) #['cricket', 'plays', 'raju']
    items = list(range(len(words))) #[0, 1, 2]
    #c1 = [[i] for i in items]
    c1 = []     #[[0], [1], [2]]
    for i in items:
        c1.append([i])
    
    c2 = []    #[[0, 1], [0, 2], [1, 2]]
    for c in c1:
        for i in items:
            if i > c[0]:
                c2.append(c + [i])
  
    w_c1 = [] #[('cricket', 'plays'), ('cricket', 'raju'), ('plays', 'raju')]
    for c in c2:
        w_c2 = []  #['cricket', 'plays'] ['cricket', 'raju'] ['plays', 'raju']
        for index in c:
            w_c2.append(words[index])
        w_c1.append(tuple(w_c2))

    return sorted(set(w_c1))
    
    
    
string = input().split() #['raju', 'plays', 'cricket']
result = combination_word(string) #[('cricket', 'plays'), ('cricket', 'raju'), ('plays', 'raju')]


for c in result:
    print(' '.join(c))


"""
raju plays cricket

cricket plays
cricket raju
plays raju
"""










""" Three Words Combination """ 
#Print all the unique combinations of three words in lexicographical order.

def combination_word(words):
    words = sorted(words) #['cricket', 'plays', 'raju']
    items = list(range(len(words))) #[0, 1, 2]

    #c1 = [[i] for i in items]
    c1 = []     #[[0], [1], [2]]
    for i in items:
        c1.append([i])
    
    c2 = []    #[[0, 1], [0, 2], [1, 2]]
    for c in c1:
        for i in items:
            if i > c[-1]:
                c2.append(c + [i])
    
    c3 = []    #[[0, 1], [0, 2], [1, 2]]
    for c in c2:
        for i in items:
            if i > c[-1]:
                c3.append(c + [i])            
  
    w_c1 = [] #[('cricket', 'plays'), ('cricket', 'raju'), ('plays', 'raju')]
    for c in c3:
        w_c2 = []  #['cricket', 'plays'] ['cricket', 'raju'] ['plays', 'raju']
        for index in c:
            w_c2.append(words[index])
        w_c1.append(tuple(w_c2))
    return sorted(set(w_c1))
    
    
    
string = input().split() #['raju', 'plays', 'cricket']
result = combination_word(string) #[('cricket', 'plays'), ('cricket', 'raju'), ('plays', 'raju')]
#result.sort()

for c in result:
    print(' '.join(c))



"""
apple is a fruit

a apple fruit
a apple is
a fruit is
apple fruit is
"""







""" N Words Combination """ 

def combination_word(words,n):
    words = sorted(words) #['cricket', 'plays', 'raju']
    items = list(range(len(words))) #[0, 1, 2]

    old_combination = [[]]
  
    for i in range(n):
        new_combination = []
        for c in old_combination:
            for j in items:
                if(c and j > c[-1]) or len(c) == 0:
                    new_combination.append(c+[j])
            old_combination = new_combination       
    
    w_c1 = [] #[('cricket', 'plays'), ('cricket', 'raju'), ('plays', 'raju')]
    for c in new_combination:
        w_c2 = []  #['cricket', 'plays'] ['cricket', 'raju'] ['plays', 'raju']
        for index in c:
            w_c2.append(words[index])
        w_c1.append(tuple(w_c2))
    return sorted(set(w_c1))
    
    
    
string = input().split() #['raju', 'plays', 'cricket']
n = int(input())
result = combination_word(string,n) #[('cricket', 'plays'), ('cricket', 'raju'), ('plays', 'raju')]

for c in result:
    print(' '.join(c))


"""
output1:=
apple is a fruit
3

a apple fruit
a apple is
a fruit is
apple fruit is



output2:=
raju plays cricket
2

cricket plays
cricket raju
plays raju
"""
