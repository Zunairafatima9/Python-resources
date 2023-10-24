def recursive(L):
    if len(L)==0:
        return 1
    else:
        return L[-1]*recursive(L[:-1])
print(recursive([1,2,3,4,5,6,7,8,9,10]))
