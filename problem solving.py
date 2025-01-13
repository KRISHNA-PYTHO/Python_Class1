print('----write a python program that check if a string only contain number if it does print true .else print false----')
def check_if_number(string):
    if string.isdigit():
        print(True)
    else:
        print(False)


input_string = input("Enter a string: ")
check_if_number(input_string)

print('----write  a python program that prints the first  and last three characters of the string  s as a single string------')

def first_and_last_three(s):
    if len(s) < 6:
        print("")  
    else:
        result = s[:3] + s[-3:] 
        print(result)


input_string = input("Enter a string: ")
first_and_last_three(input_string)


print('----write  a python program that print the length of a string s----')

def print_string_length(s):
    print(f"The length of the string is: {len(s)}")


input_string = input("Enter a string: ")
print_string_length(input_string)

print('----write  a python program that prints the character at index i in the string s-----')

def print_character_at_index(s, i):
    if not s: 
        print("empty string")
    elif i < 0 or i >= len(s):  
        print("i is out of range")
    else:
        print(f"The character at index {i} is '{s[i]}'")


s = input("Enter a string: ")
i = int(input("Enter an index: "))
print_character_at_index(s, i)


print('---write  a python program that prints the string s without the characters located at even indices---  ')

def remove_even_indices(s):
    if len(s) <= 1:
        print(s)
    else:
        result = s[1::2]
        print(result)

