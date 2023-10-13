#looping through a string
name=input("enter ur name:\n")
for i in name:
    if i=="a":
        break
    print(i)
else:
    print("you have entered",name)
