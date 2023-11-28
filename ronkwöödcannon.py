import random
print("Welcome to rock paper scissors game!")# WELCOME TO MARIO KART
integer=0
while integer==0:
    ronk=input("Please choose between Rock, Paper and Scissors (case sensitive): ")
    wööd=["Rock","Paper","Scissors"]
    cannon=random.choice(wööd)
    if ronk=="Rock" and cannon=="Paper":
        print("You chose ",ronk,", and computer chose ",cannon,". You lost. Maybe next time!")
        integer=int(input("Do you want to try again? 0 for yes and any other number for no. "))
    elif ronk=="Paper" and cannon=="Scissors":
         print("You chose ",ronk,", and computer chose ",cannon,". You lost. Maybe next time!")
         integer=int(input("Do you want to try again? 0 for yes and any other number for no. "))
    elif ronk=="Scissors" and cannon=="Rock":
        print("You chose ",ronk,", and computer chose ",cannon,". You lost. Maybe next time!")
        integer=int(input("Do you want to try again? 0 for yes and any other number for no. "))
    elif ronk=="Paper" and cannon=="Rock":
        print("You chose ",ronk,", and computer chose ",cannon,". You won. Congratulations!")
        integer=int(input("Do you want to try again? 0 for yes and any other number for no. "))
    elif ronk=="Rock"and cannon=="Scissors":
        print("You chose ",ronk,", and computer chose ",cannon,". You won. Congratulations!")
        integer=int(input("Do you want to try again? 0 for yes and any other number for no. "))
    elif ronk=="Scissors" and cannon=="Paper":
        print("You chose ",ronk,", and computer chose ",cannon,". You won. Congratulations!")
        integer=int(input("Do you want to try again? 0 for yes and any other number for no. "))
    elif ronk==cannon:
        print("You chose ",ronk,", and computer chose ",cannon,". That's a draw. Well, it happens")
        integer=int(input("Do you want to try again? 0 for yes and any other number for no. "))
    else:
        print("Either you forgot that it's case sensitive or you wrote wrong word.")
        integer=int(input("Do you want to try again? 0 for yes and any other number for no. "))