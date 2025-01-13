print('--------Append Method--------')
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

print()

print('--------extend(iterable) Method--------')
my_list = [1, 2, 3]
my_list1=[4,5,6]
my_list.extend(my_list1)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

print()

print('--------Insert Method--------')
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]

print()

print('--------Remove Method--------')
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2, 4]