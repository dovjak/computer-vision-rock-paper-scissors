# %%
import random

def get_user_choice():
    list=['Rock','Paper','Scissors']
    global user_choice
    user_choice=0
    while user_choice not in list:
        user_choice = input("Please enter Rock, Paper or Scissors:").capitalize()
    print(user_choice)
    return user_choice

def get_computer_choice():
    list=['Rock','Paper','Scissors']
    global computer_choice
    computer_choice=random.choice(list)
    print(computer_choice)
    return computer_choice

def get_winner(user_choice,computer_choice):
    if computer_choice==user_choice:
        print('Tie! Try again.')
    elif user_choice=='Rock':
        if computer_choice=='Paper':
            print('You lost.')
        if computer_choice=='Scissors':
            print('You won.')
    elif user_choice=='Paper':
        if computer_choice=='Rock':
            print('You won.')
        if computer_choice=='Scissors':
            print('You lost.')
    elif user_choice=='Scissors':
        if computer_choice=='Paper':
            print('You won.')
        if computer_choice=='Rock':
            print('You lost.')

def play():
    get_user_choice()
    get_computer_choice()
    get_winner(user_choice,computer_choice)
    options=['Yes','No']
    play_again=0
    while play_again not in options:
        play_again=input('Do you want to play again? Yes/No').capitalize()
        if play_again=='Yes':
            play()
        elif play_again=='No':
            print('Thank you for playing!')




#get_user_choice()
#get_computer_choice()
#get_winner(get_user_choice(),get_computer_choice())
play()



# %%
