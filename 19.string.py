x ='This is a string'
y ="This is another string"

print(x+y)
print(x,y)

print()

print('------length of a string------ ')

#Length of A  String
my_string ="Hello, World!"
length =len(my_string)
print(length)

print()

print('------slicing of string-----')

#slicing of string
print(my_string[1:12:2])
print(my_string[1:12])

print()

print('----Accessing string using for loop-----')

#Accessing string using for loop
x='avengers'
for i in x:
    print (i)

print()

print('------2nd method------')

for i in 'avengers':
    print(i)

print()

print('-----3rd method-----')

x='avengers'
y=len(x)
for i in range(y):
    print(x[i])

print()

print('---th method----')

x='avengers'
for i in range(len(x)):
    print(x[i])

print()

print('-----Repetition operator *------')

print('avengers'*5)