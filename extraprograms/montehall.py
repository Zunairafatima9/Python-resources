"""
 three doors
 1 prize
 make a choice
 after first choice
 the host will open a door
 again asks the participant for a switch, which entirely depends on participant
 """
import  random
doors=[0]*3
goatdoor=[0]*2
swap=0#no of swap wins
dont_swap=0 #no of sont swap wins
j=0
while(j<10):
    x=random.randint(0,2) #xth door will comprise of prize bmw
    print(x)
    doors[x]="BMW"
    for i in range(0,3):
        if (i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoor.append(i)

    choice=int(input("enter your choice"))
    door_open=random.choice(goatdoor) #oprn a door that comprises of door
    while(door_open==choice): #door opened should not be equal to choice made by the participant
        door_open=random.choice(goatdoor)
    ch=input("do u want to swap? y/n")
    if(ch=='y'):
        if(doors[choice]=="Goat"):
            print("PLAYER WINS")
            swap=swap+1
        else:
            print("player lost")
        
    else:
        if(doors[choice]=="Goat"):
            print("Player lost")
        else:
            print("Player wins")
            dont_swap+=1
    j+=1
print(swap)
print(dont_swap)
