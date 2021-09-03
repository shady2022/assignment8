import random

option =['rock','paper', 'scissor']
scores= {'user': 0, 'computer':0}

for i in range(10):
    computer_choice = random.choice(option)
    user_choice = input('play the game:')
    
    
if user_choice == 'rock' and computer_choice == 'paper':
    print('computer wins')
    scores['computer'] +=1
    
    
elif user_choice == 'rock' and computer_choice == 'scissor':
    print('you wins')
    scores['user'] +=1
    
    
elif user_choice == 'rock' and computer_choice == 'rock':
    print('equal')
    print(scores)
    
elif user_choice =='paper' and computer_choice == 'paper':
    print('equal')
    print(scores)
    
elif user_choice == 'paper' and computer_choice == 'scissor':
    print('computer wins')
    scores['computer'] +=1
    
    