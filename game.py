from random import randint

choices = ["rock", "paper", "scissors"]

player_lives = 3
computer_lives = 3
total_lives = 3

player_choice = choices[1]

player_choice = input("Choose rock, paper, or scissors: ")

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

print("Player lives:", player_lives)
print("Computer lives:", computer_lives)