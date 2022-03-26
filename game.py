from random import randint

choices = ["rock", "paper", "scissors"]
player_lives = 3
computer_lives = 3
total_lives = 3
player_choice = False

def winorlose(status):
    print("You",status,"the game! Would you like to play again?")
    choice = input("Y / N?")

    if choice == "N" or choice == "n":
        print("You chose to quit! Better luck next time!")
        exit()
    elif choice == "Y" or choice == "y":
        global player_lives
        global computer_lives
        global total_lives

        player_lives = total_lives
        computer_lives = total_lives
    else:
        print("Make a valid choice - Y or N")
        choice = input("Y / N?") 

while player_choice is False:
    print("===============/~ Rock, Paper, Scissors Game ~/===============")
    print("  Computer Lives:", computer_lives, "/", total_lives)
    print("  Player Lives:", player_lives, "/", total_lives)
    print("==============================================================")

    print("Choose your weapon - or type quit to exit\n")
    player_choice = choices[1]

    player_choice = input("Choose rock, paper, or scissors: \n ")

    if player_choice == "quit":
        print("You chose to quit")
        exit()

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

    player_choice = False