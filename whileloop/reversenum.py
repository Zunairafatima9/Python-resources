#reversing a number
a=int(input("enter the number to reverse:"))
rev=0
while(a>0):
    rem=a%10
    rev=rev*10+rem
    a//=10
print(rev)
