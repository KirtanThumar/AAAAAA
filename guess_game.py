import random

def Hidden_number_game():
    hidden_number = random.randrange(1,20)
    print('''
    rules of game:
    1:Hidden number is in between 1 to 20
    2:press x to leave game
    3:press s to see hidden number
    4:press k to start game 
    5:press n to start new game 
    ''')
    User_input= input("enter any key")
    if  User_input == "k":
        while True:
                while True:
                    user_input = input("guess a number between 1 to 20: ")
                    if user_input == "x":
                        print("so sad you finished so early")
                        exit()
                    if user_input == "n":
                        Hidden_number_game()
                    if int(user_input) == hidden_number:
                        print("you guessed it correct")
                        exit()
                    elif int(user_input)>20 or int(user_input)<1:
                        print("enter number between 1 to 20")
                    elif int(user_input)< hidden_number:
                        print("your guess is low")
                        print("try again")
                    else:
                        print("your guess is high")
                        print("try again")
    elif User_input == "x":
        print("so sad you finished so early")
        exit()
    elif User_input == "n":
        Hidden_number_game()

    
    else:
        print("you enterd wrong key")
        input("press any key to continue:")

Hidden_number_game()