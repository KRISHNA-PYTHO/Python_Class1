text="Hello how"
for x in text:
    print(x)

print('----nested for loop-----')
#Nested for loop
print('----printing Inner Loop and Outer Loop----')

for i in range(3):
    print('outer loop')
    for j in range(1,4):
        print('inner loop')
    print('another loop started')

print('-----printing table using for loop------')

x=11
for i in range(1,11):

    print(x,"*",i,'=',x*i)

print('----printing table using nested for loop-----')

for i in range(1,3):
    for j in range(1,11):
        result =i*j
        print(i,'*',j,'=',result)
    print()

x=11
for i in range(1,11):
    print(x,'*',i,'=',i*x)