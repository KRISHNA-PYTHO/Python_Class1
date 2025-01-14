print('----Empty Dictinory------')

empty_dict={}
print(empty_dict)

print()

#============================================================

print('-----dicitonary syntax------')

my_dict={'Name':'Roger','Heroic Name':'Captian America','Power':'Shield'}
print(my_dict)

print()

#=============================================================
print('------Dictinory Keys--------')


my_dict={'Name':'Roger','Heroic Name':'Captian America','Power':'Shield'}
numeric_dict={1:'One',2:'Two',3:'Three'}
tuple_dict={('a',1):'value 1',('b',2):'value2'}

print(my_dict)
print(numeric_dict)
print(tuple_dict)

print()

#============================================================

print('------------Dicintonary value----------')

string_values = {'name': 'John', 'age': 25, 'city': 'New York'}

list_values = {'numbers': [1, 2, 3], 'colors': ['red', 'green', 'blue']}

print(string_values)
print(list_values)

print('---- Overwrite Previous Value ---- ')

string_values['name']='Peter' # Represent mutable properties
print(string_values)

print()

#==========================================================================================================

print('----= Accessing Dictionary Values -----')

my_dict = {'Name': 'Roger', 'Heroic Name': 'Captain America', 'Power': 'Sheild'}

print(my_dict['Name'])
print(my_dict['Heroic Name'])
print(my_dict['Power'])   