'''HANGMAN GAME'''

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
'''

lives = len(stages) - 1
print(logo)
w_list = ["adwerd","baboon","camel","mario"]
rnd = random.choice(w_list)
print(rnd)
display = []


print(lives)
for _ in rnd:
    display.append("_")
# gs = input("Guess a word: ").lower()
# print(display)

'''
    DISPLAY LOGIC
'''
# for i in range(len(rnd)):
#     letter = rnd[i]
#     # print(i)
#     if letter == gs:
#         display[i] = letter


# print(display)

# hang_man = ["O","/","|","\\","/","\\"]
stg = 0
eog = False
while not eog:
    gs = input("Guess a letter: ")
    for i in range(len(rnd)):
        letter = rnd[i]
        if letter == gs:
            display[i] = letter

    print(lives)
    print(display)

    if gs not in display:
        lives -= 1
        if lives == 0:
            eog == True
            print("You Lose!")
            print(stages[0])
            break

    if "_" not in display:
        eog = True
        print("You Win!!")
    print(stages[lives])