#========program value is empty or not empty============
print('-----program value is empty or not empty-----')
def check_list_empty(input_list):
    if not input_list:
        print("empty")
    else:
        print("not empty")


my_list = []
check_list_empty(my_list)

print()

my_list = [4]
check_list_empty(my_list)

print()

my_list = [4,5,6,7],
check_list_empty(my_list)

print()
#=========count number of element greater than 3=====================
print('-----count number of element greater than 3-----')

def count_elements_greater_than_three(input_list):
    count = sum(1 for element in input_list if element > 3)
    return count

my_list = [1,-1,0,2,2,3]
result = count_elements_greater_than_three(my_list)
print(f"Number of elements greater than 3: {result}")

print()

my_list = [1,2,3,4]
result = count_elements_greater_than_three(my_list)
print(f"Number of elements greater than 3: {result}")

print()

my_list = [7,8,9,10]
result = count_elements_greater_than_three(my_list)
print(f"Number of elements greater than 3: {result}")

print()

my_list = []
result = count_elements_greater_than_three(my_list)
print(f"Number of elements greater than 3: {result}")

print()
#=======multiply all the items in a list by the value of the variable====
print('-----multiply all the items in a list by the value of the variable-----')

def multiply_list_by_variable(input_list,factor):
    return [element * factor for element in input_list]


my_list = [3,4,5,6]
factor = int(input("enter your number is factor: "))  
result = multiply_list_by_variable(my_list, factor)
print(f"Original list: {my_list}")
print(result)

print()

my_list = ['a','b','c']
factor = int(input("enter your number is factor: "))  
result = multiply_list_by_variable(my_list, factor)
print(f"Original list: {my_list}")
print(result)