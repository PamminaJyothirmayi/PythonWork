#Creating a Dictionary
dict_a = {
  "name": "Teja",
  "age": 15 
}




#Accessing Items
dict_a = {
  'name': 'Teja',
  'age': 15
}
print(dict_a.get('name')) # Teja
print(dict_a.get('city')) # None



#Membership Check:
dict_a = {
  'name': 'Teja',
  'age': 15
}
result = 'name' in dict_a
print(result) # True




#Adding a Key-Value Pair:

dict_a = {'name': 'Teja','age': 15 }
dict_a['city'] = 'Goa'
print(dict_a) # {'name': 'Teja', 'age': 15, 'city': 'Goa'}





#Modifying an Existing Item

dict_a = {
    'name': 'Teja',
    'age': 15
}
dict_a['age'] = 24
print(dict_a) # {'name': 'Teja', 'age': 24}



#Deleting an Existing Item:
dict_a = {
  'name': 'Teja',
  'age': 15
}
del dict_a['age']
print(dict_a) # {'name': 'Teja'}



