#append mode- will append at the end of the file
f=open("quote.txt","a")
#writes the content
f.write(" be positive")
#closes the file after writing
f.close()
#opens file in readmode
f=open("quote.txt","r")

print(f.read())
