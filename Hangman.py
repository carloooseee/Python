#Hangman Game by Juan Carlos S. Laran
import random
def hangman(x):
    if x == 5:
        print(''' 
           _______
           |/   
           |   
           |   
           |    
           |   
           |
           |_____''')
    elif x == 4:
        print(''' 
           _______
           |/    |
           |   
           |   
           |    
           |   
           |
           |_____''')
    elif value == 3:
        print(''' 
           _______
           |/    |
           |    (_)
           |   
           |    
           |   
           |
           |_____''')
    elif value == 2:
        print(''' 
           _______
           |/    |
           |    (_)
           |    /|\\
           |    
           |   
           |
           |_____''')
    elif x == 1:
        print(''' 
           _______
           |/    |
           |    (_)
           |    /|\\
           |     |
           |   
           |
           |_____''')
    elif x == 0:
        print('')
        print('Bro is dead, now live with the guilt that you\'ve killed a person! HAHAHHAHAHA!')
        print(''' 
            _______
            |/    |
            |    (_)
            |    /|\\
            |     |
            |    / \\
            |
            |_____''')

#Initialized Values
value = 5
words = ['phone', 'laptop', 'charger', 'protien', 'python', 'pen']
randomword = random.choice(words)

#Start of Program
print('''
===========================================
||   HANGMAN GAME by JUAN CARLOS LARAN   ||
||   12/8/2023                           ||
||   First year of Computer Science      ||
===========================================
''')
hangman(value)
print('')
if randomword == 'phone':
    print('Clue! A portable communication device typically used for making calls and accessing various applications.')
elif randomword == 'laptop':
    print('Clue! A portable computer with a keyboard and screen, suitable for use on the go.')
elif randomword == 'charger':
    print('Clue! A device used to replenish the energy of electronic devices, typically by supplying electrical power.')
elif randomword == 'protein':
    print('Clue! A vital macronutrient essential for the growth and repair of tissues in living organisms.')
elif randomword == 'python':
    print('Clue! A high-level programming language known for its readability and versatility in various applications.')
elif randomword == 'pen':
    print('Clue! A tool used for writing or drawing, typically used in an office environment to write hard copies')
else:
    print(randomword)
#User Input and Output Results
for i in range(1, value+1):
    print('')
    guess = input('Guess the Word: ').lower()
    if guess in randomword:
        print('You win!')
        break
    elif guess not in randomword:
        print('')
        print('--------------------')
        print('')
        print('Try entering again.')
        value -= 1
        hangman(value)
