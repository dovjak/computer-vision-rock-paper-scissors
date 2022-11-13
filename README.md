# Computer Vision Project: Rock, Paper, Scissors

This project is created to read hand signs of rock, paper and scissors shown on camera. This was done in help with Teachable machine, which has the ability to easily create machine learning models using sample data inputs.

## Milestone 1

Using a Teachable Machine an image project model was creted including 4 classes: Rock, Paper, Scissors and Nothing. Each class was trained with approximately 400 images.The model was downloaded from 'Tensorflow' tab from the Teachable Machine which contains the structure and the parameters of a deep learning model. 

The model created with Teachable Machine will contribute to reading hand signs when either rock, paper or scissors is displayed. The pathway is needed in the model for the hand signs to be read.


## Milestone 2

A virtual environment was created and activated within the VS Code using Terminal. It was set that the project would use Python version 3.8.5 and such libraries installed: opencv-python, tensorflow and ipykernel (within the environment). In addition, a requirements.txt file was created in order if any other user to easily install exact dependencies for the project. After the a file checkthemodel.py was run to see if the model generated and the environment created works as expected. Success.


## Milestone 3

The manual simualtion of the game was written manual_rps.py
The file contais 4 functions. The function get_user_choice() asks the user to put input for the game.
```
def get_user_choice():
    list=['Rock','Paper','Scissors']
    global user_choice
    user_choice=0
    while user_choice not in list:
        user_choice = input("Please enter Rock, Paper or Scissors:").capitalize()
    print(user_choice)
    return user_choice
 ```
 
The following function get_computer_choice() puts a random computer choice for the game. 
```
def get_computer_choice():
    list=['Rock','Paper','Scissors']
    global computer_choice
    computer_choice=random.choice(list)
    print('Computer chose: '+computer_choice)
    return computer_choice
```
The third function get_winner() has all conditions of the game and provides if the user or computer won the game.
```
def get_winner(user_choice,computer_choice):
    global user_wins,computer_wins
    if user_choice=='Nothing':
        print('You lost.')
        computer_wins=computer_wins+1
    elif computer_choice==user_choice:
        print('Tie! Try again.')
    elif user_choice=='Rock':
        if computer_choice=='Paper':
            print('You lost.')
            computer_wins=computer_wins+1
        if computer_choice=='Scissors':
            print('You won.')
            user_wins=user_wins+1
    elif user_choice=='Paper':
        if computer_choice=='Rock':
            print('You won.')
            user_wins=user_wins+1
        if computer_choice=='Scissors':
            print('You lost.')
            computer_wins=computer_wins+1
    elif user_choice=='Scissors':
        if computer_choice=='Paper':
            print('You won.')
            user_wins=user_wins+1
        if computer_choice=='Rock':
            print('You lost.')
            computer_wins=computer_wins+1
```
The final function play() calls functions in order: get_user_choice(), get_computer_choice() and get_winner(). Finally, asks a user if they want to play again. If the answer is yes, the function calls itslef again, if the answer is no, the game is over.
```
def play():
    #get_user_choice()
    get_prediction(prediction)
    cv2.waitKey(1000)
    get_computer_choice()
    cv2.waitKey(1000)
    get_winner(user_choice,computer_choice)
```
Note: the function get_prediction(prediction) was implemented in the later stage but it made sense to add it into the function play() which is saving the sign the user has shown to the camera and the program shows the user what sign has been recognised based on the predictions and the pictures the model has been trained with.

## Milestone 4

In this stage the final file rock_paper_scissors.py was written. Here the game was put all together and a new function get_prediction was added which is used in the main play() function.
```
def get_prediction(prediction):
    global user_choice
    prob1=prediction[0][0]
    prob2=prediction[0][1]
    prob3=prediction[0][2]
    prob4=prediction[0][3]
    #print(prediction)
    list_pred=[prob1,prob2,prob3,prob4]
    position_max_pred=list_pred.index(max(list_pred))
    cv2.waitKey(1000)
    print('3')
    cv2.waitKey(1000)
    print('2')
    cv2.waitKey(1000)
    print('1')
    if position_max_pred==0:
        user_choice='Rock'
        print('You chose: Rock')
    elif position_max_pred==1:
        print('You chose: Paper')
        user_choice='Paper'
    elif position_max_pred==2:
        user_choice='Scissors'
        print('You chose: Scissors')
    elif position_max_pred==3:
        user_choice='Nothing'
        print('You chose: Nothing')
```
The countdown was added with a few seconds delay that the camera captures one image at the time and user has time to think what sign to use in this round. When the game is called, is is repeated until either computer or user gets 3 victories and each win is counted for either computer or user if it is not a tie.

The are a few ways how this game could be improved, such as addidnt a countdown on the camera to improve user experience, but in the future this game will be improved by adding classes instead of having multiple functions to improve readability and functionality of the game. 
