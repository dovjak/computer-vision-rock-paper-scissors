# %%
import cv2
from keras.models import load_model
import numpy as np
import time
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
    print('Computer chose: '+computer_choice)
    return computer_choice

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
    

def play():
    #get_user_choice()
    get_prediction(prediction)
    cv2.waitKey(1000)
    get_computer_choice()
    cv2.waitKey(1000)
    get_winner(user_choice,computer_choice)

global user_wins,computer_wins
user_wins=0
computer_wins=0

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    while user_wins<3 and computer_wins<3:
        play()
    if computer_wins>user_wins:
        print('Computer won the game')
    else: print('You won the game')
    break



# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
# %%
