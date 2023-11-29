#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random

def continue_playing():
    command = input('Do you want to continue playing? Yes/No \n').lower()
    response = True
    if command == "yes":
        response = True
    elif command == "no":
        response = False
    else: 
        print("Value not valid \n")
        continue_playing()
    return (response)

def play_game():
    list_decision = ["rock","paper","scissors"]
    user_decision=input('rock, paper, scissors, SHOOT!\n').lower()
    pc_decision=random.choice(list_decision)
    user_won = "False"
    if user_decision == "rock":
        if pc_decision == "paper":
            user_won = "False"
            print ("Paper wraps rock!")
        elif pc_decision == "scissors":
            user_won = "True"
            print ("Rock destroys scissors!")
        elif pc_decision == "rock":
            user_won = "Tie"
            print ("Rock collides with rock!")

    elif user_decision == "paper":
        if pc_decision == "paper":
            user_won = "Tie"
            print ("Paper collides with paper!")
        elif pc_decision == "scissors":
            user_won = "False"
            print ("Scissors cut paper!")
        elif pc_decision == "rock":
            user_won = "True"
            print ("Paper wraps rock!")    

    elif user_decision == "scissors":
        if pc_decision == "paper":
            user_won = "True"
            print ("Scissors cut paper!")
        elif pc_decision == "scissors":
            user_won = "Tie"
            print ("Scissors collide with scissors!")
        elif pc_decision == "rock":
            user_won = "False"
            print ("Rock destroys scissors!") 
    else:
        print("Option not valid \nEnter your choice again\n")
        play_game()
    return user_won
    


def main():
    print('Hi! Welcome to Rock, Paper, Scissors')
    input('Press Enter to play')

    keep_playing = True
    score= 0
    while keep_playing:
        result = play_game()
        if result == "True":
            score+=1
            print("You win!")
        elif result == "False":
            print ("You Lose!")
        else:
            ("You are tied!")
        keep_playing = continue_playing()
        if keep_playing == False:
            print("Your score was " + str(score) + "\n")
            input('Thanks for playing!')
            break

if __name__ == "__main__":
    main()
