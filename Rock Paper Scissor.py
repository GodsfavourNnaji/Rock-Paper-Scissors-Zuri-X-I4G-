import random

print('Welcome to "Rock Paper Scissor" game by Godsfavour Nnaji \n'
'\n'
'While the player selects his or her own choice,' 
'the computer is set to randomise its own choice from the three! \n'
'A comparism between the choices decides the winner'
'\n'
"The rules of the game are as follows: \n" 
"in Rock vs Paper = Paper wins \n"
"in Rock vs Scissor = Rock wins \n"
"in Paper vs Scissor = scissor wins \n" 
'\n')

user = input('Do you wish to continue? (y/n)\n').lower()

if user == 'y':
    print('let\'s get started!!\n'
    '\n')

    while True:
        print("Enter choice: \n 1 for Rock, \n 2 for Paper, and \n 3 for Scissors \n")
        user_choice = int(input("User turn: "))

        while user_choice > 3 or user_choice < 1:
            user_choice = int(input("please enter valid input(1, 2 0r 3): "))

        if user_choice == 1:
            user_choice_name = 'Rock'
        elif user_choice == 2:
            user_choice_name = 'paper'
        else:
            user_choice_name = 'scissor'
        
        print("user choice is: " + user_choice_name)
        print("\nNow its computer\'s turn.......")

        #computer makes its choice
        choice_list = [1, 2, 3]
        comp_choice = random.choice(choice_list)

        #computer choices are named
        if comp_choice == 1:
                comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'paper'
        else:
            comp_choice_name = 'scissor'

        #choices
        print("Computer choice is: " + comp_choice_name)

        print(user_choice_name + " V/s " + comp_choice_name)


        #winning conditionals (comp_choice vs user_choice)

        #for user to win
        if (user_choice == 1 and comp_choice == 3) or (user_choice == 2 and comp_choice == 1) or (user_choice == 3 and comp_choice == 2):
            result = "Hurray, You win!!!"
        #for computer to win
        elif (comp_choice == 1 and user_choice == 3) or (comp_choice == 2 and user_choice == 1) or (comp_choice == 3 and user_choice == 2) :
            result = "Ohhh, Computer wins"
        #for stalemate
        else:
            result = "It's a Stalemate!!!"

        #result
        print(result)
            
        print("Do you want to play again? (Y/N)")
        ans = input()


        # if user input n or N then condition is True
        if ans == 'n' or ans == 'N':
            break
    #end of while loop
        
    print("\nThanks for playing")

else:
    print('perhaps another time!!!')    

