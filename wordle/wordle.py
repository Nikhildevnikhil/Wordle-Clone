import os
import sys
import random
import colorama
from colorama import Fore, Back, Style
import re


list_word = []
word_set = set(())
file = open(os.path.join(sys.path[0], 'sgb-words.txt'), 'r')
for line in file:
        list_word.append(line[:-1])
        word_set.add(line[:-1])

file.close()
random_index = random.randint(0, len(list_word) - 1)
    
word = list_word[random_index]
# word = 'hello'
t = 6

colorama.init(autoreset=True)

def validInput(guess):
    #no special char, numbers, word present in the file
    if re.match("^[a-z]{5}$", guess):
        if guess in word_set:
            return True
        else:
            print(Back.RED + "Word is not in the file!")

    return False

# print(word)

while True:
    if t == 0:
        print('You lost. Better luck next time!')
        print('The word was ', word)
        break
    correctIndex = []
    wrongIndex = []
    print('Total chances left: ', t)
    guess = input('Guess the 5 letter word: ')
    guess = guess.lower()

    if guess == word:
        print(Back.GREEN + word)
        print('You Won!!!')
        break
    elif validInput(guess):
        for i in range(len(guess)):
            if guess[i] in word and guess[i] == word[i]:
                correctIndex.append(i)
            elif guess[i] in word:
                wrongIndex.append(i)

        for i in range(len(guess)):
            if i in correctIndex:
                print(Back.GREEN + guess[i], end='')
            elif i in wrongIndex:
                print(Back.YELLOW + guess[i], end='')
            else:
                print(guess[i], end='')

        print('')
        t = t - 1

    else:
        print(Back.RED + 'Give a valid 5 letter word.')
