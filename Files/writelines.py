f=open("file.txt","w")
f.writelines("""hello
there
what's up""")
f.close()

f=open("file.txt","r")
print(f.read())
