from glob import glob
from random import randint
from secrets import choice

choices = ["rock", "paper", "scissors"]

player_lives = 3
computer_lives = 3
total_lives = 3

# True or False are Boolean data types
# Booleans are equivalent to an ON/OFF switch, 1 or 0

player_choice = False

# Define a win or lose function
def winorlose(status):
    # Version 1 of function
    # print("Inside winorlose function; status is: ", status)
    print("You",status,"the game! Would you like to play again?")
    choice = input("Y / N?")

    if choice == "N" or choice == "n":
        print("You chose to quit! Better luck next time!")
        exit()
    elif choice == "Y" or choice == "y":
        # Reset the player and computer lives
        # Reset player choice to False, so our loop restarts
        global player_lives
        global computer_lives
        global total_lives

        player_lives = total_lives
        computer_lives = total_lives
    else:
        print("Make a valid choice - Y or N")
        # This may generate a bug that we need to fix later
        choice = input("Y / N?") 

# player_choice == False
while player_choice is False:
    print("====================*/ RPS GAME */====================")
    print("  Computer Lives:", computer_lives, "/", total_lives)
    print("  Player Lives:", player_lives, "/", total_lives)
    print("======================================================")

    player_choice = choices[1]

    player_choice = input("Choose rock, paper, or scissors: \n ")

    print("User chose: " + player_choice)

    computer_choice = choices[randint(0, 2)]

    print("Computer chose: " + computer_choice)

    if player_choice == computer_choice:
        print("Draw!")

    elif computer_choice == "rock":
        if player_choice == "scissors":
            print("You lose!")
            player_lives -= 1
        else:
            print("You win!")
            computer_lives -= 1

    elif computer_choice == "paper":
        if player_choice == "scissors":
            print("You win!")
            computer_lives -= 1
        else:
            print("You lose!")
            player_lives -= 1

    elif computer_choice == "scissors":
        if player_choice == "paper":
            print("You lose!")
            player_lives -= 1
        else:
            print("You win!")
            computer_lives -= 1

    if player_lives == 0:
        winorlose("lose")
    
    if computer_lives == 0:
        winorlose("won")

    print("Player lives:", player_lives)
    print("Computer lives:", computer_lives)

# Make the loop keep running, by setting player_choice to False
#unset, so that our loop condition will evaluate to True
    player_choice = False