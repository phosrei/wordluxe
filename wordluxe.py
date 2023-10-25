import random
import time 
from nltk.corpus import words
from termcolor import colored
from wordbank import categories, difficulty

dictionary = set(words.words())

cat_input = input("Choose category: ")
dif_input = input("Choose difficulty: ")

while cat_input not in categories:
    print("Not in categories")
    cat_input = input("Choose category: ")

while dif_input not in difficulty:
    print("Not in difficulties")
    dif_input = input("Choose difficulty: ")

random_word = random.choice(difficulty[dif_input])
word_length = len(random_word)
msg = ""

def easy_mode():
    attempts = 0
    while True:
        print(f"Attempt #{attempts + 1}")
        guess = input()
        feedback = ""
        while guess.lower() not in dictionary:
            print(f"'{guess}' is not in the English dictionary.")
            guess = input()

        # TODO: Append letter in a list instead to improve performance and remove checking redundancy
        for i in range(word_length):
            if guess[i] in random_word[i]:
                feedback += colored(guess[i], 'green')
            elif guess[i] in feedback:
                feedback += colored(guess[i], 'dark_grey')
            elif guess[i] in random_word:
                feedback += colored(guess[i], 'yellow')
            else:
                feedback += colored(guess[i], 'dark_grey')
        
        print(feedback)
        #add coins
        if guess == random_word:
            msg = "You won!"
            break
        attempts += 1
    
    print("Coins: No coins are rewarded in easy mode.")
    print(msg)

def normal_mode():
    for attempt in range(1,6+1):
        print(f"Attempt #{attempt}")
        guess = input()
        feedback = ""
        currency = 0
        while guess.lower() not in dictionary:
            print(f"'{guess}' is not in the English dictionary.")
            guess = input()

       
            msg = "Game over."
            print(f"The word was: {random_word}")
            break
    
    print(f"Coins: {currency}")
    print(msg)

def hard_mode():
    for attempt in range(1,4+1):
        print(f"Attempt #{attempt}")
        guess = input()
        feedback = ""
        currency = 0
        while guess.lower() not in dictionary:
            print(f"'{guess}' is not in the English dictionary.")
            guess = input()

        # TODO: Append letter in a list instead to improve performance and remove checking redundancy
        for i in range(word_length):
            if guess[i] in random_word[i]:
                feedback += colored(guess[i], 'green')
            elif guess[i] in feedback:
                feedback += colored(guess[i], 'dark_grey')
            elif guess[i] in random_word:
                feedback += colored(guess[i], 'yellow')
            else:
                feedback += colored(guess[i], 'dark_grey')
        
        print(feedback)
        #add coins
        if guess == random_word:
            msg = "You won!"
            currency += 5
            break
        elif guess != random_word and attempt == 6:
            msg = "Game over."
            print(f"The word was: {random_word}")
            break
    
    print(f"Coins: {currency}")
    print(msg)

def extreme_mode():
    for attempt in range(1,3+1):
        print(f"Attempt #{attempt}")
        guess = input()
        feedback = ""
        currency = 0
        while guess.lower() not in dictionary:
            print(f"'{guess}' is not in the English dictionary.")
            guess = input()

        # TODO: Append letter in a list instead to improve performance and remove checking redundancy
        for i in range(word_length):
            if guess[i] in random_word[i]:
                feedback += colored(guess[i], 'green')
            elif guess[i] in feedback:
                feedback += colored(guess[i], 'dark_grey')
            elif guess[i] in random_word:
                feedback += colored(guess[i], 'yellow')
            else:
                feedback += colored(guess[i], 'dark_grey')
        
        print(feedback)
        #add coins
        if guess == random_word:
            msg = "You won!"
            currency += 10
            break
        elif guess != random_word and attempt == 3:
            msg = "Game over."
            print(f"The word was: {random_word}")
            break
    
    print(f"Coins: {currency}")
    print(msg)

if dif_input == "easy":
    easy_mode()
elif dif_input == "normal":
    normal_mode()
elif dif_input == "hard":
    hard_mode()
elif dif_input == "extreme":
    extreme_mode()
