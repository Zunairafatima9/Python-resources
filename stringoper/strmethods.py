#string methods 
msg="Hello World"
print(msg.lower())#converts the string to lower case
print(msg.upper())#converts the string to upper case
print(msg.swapcase())#swaps the case of given string


msg2="action speaks louder than words"
print(msg2.title())#first character in every word is uppercase
print(msg2.capitalize())#first character of a string to uppercase
print(msg2.split())#splits a string into list
print(msg2.replace("act","ACT"))#replaces old substr with new substr


#slicing
msg3="believe on yourself"
print(msg3[:7]+" in "+msg3[11:])
modified=msg3[:7]+" in "+msg3[11:]
print(modified)
