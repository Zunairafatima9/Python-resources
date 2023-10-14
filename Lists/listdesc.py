#random module returns a random int between the given range
import random
#creates an empty list
L=[]
#append method is used to add an element at the end of the list
for i in range(10):
    L.append(random.randint(0,10))
#sort method sorts the list ascending by default
L.sort()
#reverses the elements in the list
L.reverse()
print(L)
