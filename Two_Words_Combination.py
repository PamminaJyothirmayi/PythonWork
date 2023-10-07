#print all the unique combinations of two words in lexicographical order.

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


