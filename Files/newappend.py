#append mode creates the file if it doesnt exist
f=open("messages.txt","a")
f.write("Action Speaks Louder than words")
f.close()

f=open("messages.txt","r")
print(f.read())
