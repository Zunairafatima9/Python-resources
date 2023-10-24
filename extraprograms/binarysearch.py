def Binary(L,find,start,end):
    mid=int((start+end)/2)
    if(start==end):
        if(L[end]==find):
            return end
        else:
            return -100
    if(L[mid]==find):
        return mid
    elif(find>L[mid]):
        return Binary(L,find,mid+1,end)
    else:
        return Binary(L,find,start,mid-1)

L=[10,20,30,40,50,60]
find=50
print(Binary(L,find,0,len(L)-1))
