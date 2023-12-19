def brejncancar(ahyesalist):
    
    skincancar = len(ahyesalist)
    
    while skincancar > 1:
    
        chnagestuff = False
    
        for i in range(0, skincancar-1):
    
            if ahyesalist[i] > ahyesalist[i+1]:
    
                ahyesalist[i], ahyesalist[i+1] = ahyesalist[i+1], ahyesalist[i]
    
                chnagestuff = True
    
        skincancar -= 1
    
        print(ahyesalist)
    
        if chnagestuff == False: break
    
    return ahyesalist            
print("This is some sort of sorting program idk man.")# I have no idea what I'm doing
man=[]
markEplier=int(input("Please insert a number of how many numbers thee want to have in thy list: "))
for e in range(markEplier):
    man.append(int(input("Please insert a number: ")))
brejncancar(man)#imma gonna lose my fookin mind. update: lost it