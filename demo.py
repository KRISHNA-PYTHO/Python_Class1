#function with while
def print_multiplication_table(x):
 n =x
 j =1
 while(j<n+1):
     i=1
     while(i<=10):
         print(j,'*',i,'=',j*i)
         i+=1
     j+=1
     print()

print_multiplication_table(3)


#function with for
def for_multiplication_table(y):
 n =y
 for j in range (1,n+1):
    for i in range(1,11):
        print(j,'*',i,'=',j*i)
    print()
    
for_multiplication_table(5)


x='string'
for char in x:
   x= char + x
   
print(x)
