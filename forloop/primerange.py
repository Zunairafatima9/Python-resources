#prime numbers range between 0-100
for i in range(2,101):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        print(i)
