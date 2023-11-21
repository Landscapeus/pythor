import random
import time
print("Welcome to fast writing test!")
diffffffffffficulty=int(input("Please insert a number representing the difficulty (from 1 to 5): "))
jeden=["Thee","Thoust","Minos","Bees"]
dwa=["Potato","Sisyphus","Tomato","Chocolate"]
trzy=["Flesh Prison","King Midas","Judge of Hell","Peforator Hive"]
cztery=["Flesh Panopticon","Layer of Violence","Ishallshowtheespeed"]
fünf=["Wyrewolwerowany rewolwerowiec wyrewolwerował wyrewolwerowanego rewolwerowca"]# tak jestem złym człowiekiem jak mogłeś się domyślić
if diffffffffffficulty==1:
    randomizer=random.choice(jeden)
    print("Thy word is: ",randomizer)
    start=time.time()
    beeees=input("Write thy word here: ")
    if beeees==randomizer:
        print("",end='')
        end=time.time()
        print("Thy time is ", end-start," seconds. Nice!")
    else:
        print("Wrong word lad",end='')
elif diffffffffffficulty==2:   
    randomizer=random.choice(dwa)
    print("Thy word is: ",randomizer)
    start=time.time()
    beeees=input("Write thy word here: ")
    if beeees==randomizer:
        print("",end='')
        end=time.time()
        print("Thy time is ", end-start," seconds. Nice!")
    else:
        print("Wrong word lad",end='')
elif diffffffffffficulty==3:
    randomizer=random.choice(trzy)
    print("Thy words are: ",randomizer)
    start=time.time()
    beeees=input("Write thy word here: ")
    if beeees==randomizer:
        print("",end='')
        end=time.time()
        print("Thy time is ", end-start," seconds. Nice!")
    else:
        print("Wrong word lad",end='')
elif diffffffffffficulty==4:
    randomizer=random.choice(cztery)
    print("Thy words are: ",randomizer)
    start=time.time()
    beeees=input("Write thy word here: ")
    if beeees==randomizer:
        print("",end='')
        end=time.time()
        print("Thy time is ", end-start," seconds. Nice!")
    else:
        print("Wrong word lad",end='')
elif diffffffffffficulty==5:
    randomizer=random.choice(fünf)
    print("Good luck: ",randomizer)
    start=time.time()
    beeees=input("Write thy word here: ")
    if beeees==randomizer:
        print("",end='')
        end=time.time()
        print("Thy time is ", end-start," seconds. Nice!")
    else:
        print("Wrong word lad",end='')    
else:
    print("wrong number")