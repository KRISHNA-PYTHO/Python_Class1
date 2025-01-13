n=5
x=n
for _ in range(n):
    if n==5 or n==1:
        for i in range(x):
            print("*",end=' ')
        print()
        n-=1
    else:
        print('* ',' '*(x-2),' *')
        n-=1

print('-----simple method hollow square')
n=5
for i in range(n):
    if i==0  or i==n-1:
        print("* "*n)
    else:
        print('* ',' '*(n-2),' *')


