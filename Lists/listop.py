#slicing in list
'''A slice, or sub-list of Python list elements can be selected from a list
using a colon-separated starting and ending point.

The syntax pattern is myList[START_NUMBER:END_NUMBER].
The slice will include the START_NUMBER index, and
everything until but excluding the END_NUMBER item.'''
L=['a','b','c','d','e','f','g','h']
print(L[2:5])
#add an element at the specific position
L.insert(3,'p')
print(L)
#adds an element at the end
print(L.append('i'))
print(L)
