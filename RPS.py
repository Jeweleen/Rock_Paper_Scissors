import random


#if(player1Choice == "rock" and player2Choice == "scissors") or \
#    (player1Choice == "paper" and player2Choice == "rock"):
#    print("player 1 wins")
def random_choice():
        choice = ["rock", "paper", "scissors"]
        return random.choice(choice)

while True:

    keepPlaying = input("Do you want to play? Y/N \n")
    if keepPlaying == "n":
        break

    playerChoice = input( "Rock, Paper, Scissors? \n")
    print(f"player1Choice is {playerChoice}")

    RoboChoice = random_choice()
    print(f"RoboChoice is {RoboChoice}")
    if playerChoice == RoboChoice:
        print("It's a Tie!")
    elif(playerChoice == "rock") and (RoboChoice == "scissors") or \
        (playerChoice == "paper") and (RoboChoice == "rock") or\
        (playerChoice == "scissors") and (RoboChoice == "paper"):
        print("Player wins!")
    else:
        print("Robot wins!")


   


