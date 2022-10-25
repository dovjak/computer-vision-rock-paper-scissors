# Computer Vision Project: Rock, Paper, Scissors

This project is created to read hand signs of rock, paper and scissors shown on camera. This was done in help with Teachable machine, which has the ability to easily create machine learning models using sample data inputs.

## Milestone 1

Using a Teachable Machine an image project model was creted including 4 classes: Rock, Paper, Scissors and Nothing. Each class was trained with approximately 400 images.The model was downloaded from 'Tensorflow' tab from the Teachable Machine which contains the structure and the parameters of a deep learning model. 

The model created with Teachable Machine will contribute to reading hand signs when either rock, paper or scissors is displayed. The pathway is needed to the model in order the hand signs to be read.


## Milestone 2

A virtual environment was created and activated within the VS Code using Terminal. It was set that the project would use Python version 3.8.5 and such libraries installed: opencv-python, tensorflow and ipykernel (within the environment). In addition, a requirements.txt file was created in order if any other user to easily install exact dependencies for the project. Afetr thee a file checkthemodel.py was run to see if the model generated and the environment created works as expected. Success.


## Milestone 3

The manual simualtion of the game was written manual_rps.py
The file contais 4 functions. The function get_user_choice() asks the user to put input for the game. The following function get_computer_choice() puts a random computer choice for the game. The third function get_winner() has all conditions of the game and provides if the user or computer won the game. The final function play() calls functions in order: get_user_choice(), get_computer_choice() and get_winner(). Finally, asks a user if they want to play again. If the answer is yes, the function calls itslef again, if the answer is no, the game is over.
