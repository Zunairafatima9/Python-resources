#factorial non recursive

n=int(input("enter the number:\n"))
f=1
if n==1 or n==0:
    print(f"factorial of {n} is 1")
elif n<0:
    print("factorial of negative numbers is not possible")
else:
    for i in range(2,n+1):
        f=f*i
    print(f"factorial of {n} is {f}")
