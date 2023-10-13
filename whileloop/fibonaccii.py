limit=int(input("enter the limit"))
x,y=0,1
count=0
if limit<=0:
    print("please enter a +ve number")
    print(x)
else:
    print("fibonacci sequence")
    while count<limit:
        print(x)
        z=x+y
        x=y
        y=z
        count+=1
