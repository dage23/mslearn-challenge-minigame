#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
def continue_playing():
    command = input('Do you want to continue playing? Yes/No \n')
    response = True
    if command == "Yes" or command == "yes":
        response = True
    elif command == "No" or command == "no":
        response = False
    else: 
        print("Value not valid \n")
        continue_playing()
    return (response)


def main():
    print('Hi! Welcome to Rock, Paper, Scissors')
    input('Press Enter to play')

    play = True
    list_decision = ["rock","paper","scissors"]
    score= 0
    while play:
        user_decision=input('rock, paper, scissors, SHOOT!\n')


        score+=1
        play = continue_playing()
        if play == False:
            print("Your score was " + str(score) + "\n")
            input('Thanks for playing!')
            break

if __name__ == "__main__":
    main()
