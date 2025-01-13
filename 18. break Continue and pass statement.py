#applying break using for loop

for i in range(5):
    if(i==3):
        break
    print(i)

print('---applying break using while loop-----')
#applying break using while loop

i=1
while(True):
    if(i==3):
        break
    print(i)
    i+=1


print('----continue statement start here---')
#applying continue using for loop

for i in range(5):
    if(i==3):
        continue
    print(i)


print('----applying continue using while loop----')
#applying continue using for loop

i=0
while(i<10):
    i+=1
    if(i==3):
        continue
    print(i)

print('----pass statement start here -----')

#applying pass using for loop 
for i in range(10):
    if(i%2==0):
        pass
    else:
        print('odd number is',i)
