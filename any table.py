#while loop
n=int(input('enter any number : '))
j=1
while(j<n+1):
    i=1
    while(i<=10):
        print(j,'*',i,'=',j*i)
        i+=1
    j+=1
    print()

# for

n=int(input('enter any number : '))
for j in range (1,n+1):
    for i in range(1,11):
        print(j,'*',i,'=',j*i)
        print()
