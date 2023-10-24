def recursive(num):
    if(num==1):
        return 1
    return num*recursive(num-1)

num=int(input("enter the number"))
print(f"product of first{num} terms is",recursive(num))
