#=====list of element that are not in list A=======
print('----list of element that are not in list A-----')
print('---Q1----')
list_a = [1, 2, 3, 4]
list_b = [1,2]

print()

not_available= [i for i in list_a if i not in list_b]
print(not_available)

print('---Q2----')
list_c = [1, 2, 3, 4]
list_d = [1,2,3]

not_available= [i for i in list_c if i not in list_d]
print(not_available)

print()

print('---Q3----')
list_e = [1, 2, 3, 4]
list_f = [1,2,3,4]


not_available= [i for i in list_e if i not in list_f]
print(not_available)

print()

print('---Q4----')
list_g = []
list_h = [1,3]


not_available= [i for i in list_g if i not in list_h]
print(not_available)

print()

#======element that are present in both list=====
print('---element that are present in both list-----')
print('---Q1---')

point_a=[1,2,3]
point_b=[1,2,3]

available= [i for i in point_a if i in point_b]
print(available)

print()

print('---Q2---')

point_c=[4,5,6]
point_d=[1,4,5]

available= [i for i in point_c if i in point_d]
print(available)

print()

print('---Q3---')

point_e=[3,4,5]
point_f=[1,2,3]

available= [i for i in point_e if i in point_f]
print(available)

print()

print('---Q4---')

point_g=[4,5,6]
point_h=[1,2,3]

available= [i for i in point_g if i in point_h]
print(available)

print()

#======Second largest number======

print('----  Second Largest Number -----')

from functools import reduce
numbers = [1,2,3,4]

max_value = reduce(lambda x, y: x if x > y else y, numbers)

print("Maximum Value:", max_value)

print()
