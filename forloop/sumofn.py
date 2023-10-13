#sum of n numbers
n=int(input("enter the range of sum:\n"))
sum=0
for i in range(1,n+1):
    print(i,end="")
    if i<n:
        print('+',end='')
    sum+=i
print('\nsum of',n,'numbers is:',sum)
