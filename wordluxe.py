import random
import wordbank
from nltk.corpus import words
from termcolor import colored

dictionary = set(words.words())
wordbank_cat = {
    "general": wordbank.gen_difficulty,
    "countries": wordbank.countries_difficulty,
    "animals": wordbank.animals_difficulty,
    "fruits": wordbank.fruits_difficulty,
    "sports": wordbank.sports_difficulty,
    "artists": wordbank.artists_difficulty,
    "songs": wordbank.songs_difficulty
}

def main():
    global cat_input
    cat_input = input("Choose category: ")
    global dif_input
    dif_input = input("Choose difficulty: ")

    while cat_input not in wordbank.categories:
        print("Not in categories")
        cat_input = input("Choose category: ")

    while dif_input not in wordbank.gen_difficulty:
        print("Not in difficulties")
        dif_input = input("Choose difficulty: ")

    if cat_input in wordbank.categories:
        word = random.choice(wordbank_cat[cat_input][dif_input])

    if dif_input == "easy":
        easy_mode(word)
    elif dif_input == "normal":
        normal_mode(word)
    elif dif_input == "hard":
        hard_mode(word)
    elif dif_input == "extreme":
        extreme_mode(word)

def check_guess(guess, word):
    length = len(word)
    output = ["-"] * length

    for i in range(length):
        if guess[i] == word[i]:
            output[i] = colored(guess[i], 'green')
            word = word.replace(guess[i], "-", 1)

    for i in range(length):
        if guess[i] in word and output[i] == "-":
            output[i] = colored(guess[i], 'yellow')
        elif guess[i] in output[i]:
            continue
        else:
            output[i] = colored(guess[i], 'dark_grey')

    return ''.join(output)

def easy_mode(word):
    attempts = 0

    while True:
        print(f"Attempt #{attempts + 1}")
        guess = input()

        while guess.lower() not in dictionary:
            if cat_input != "general" and cat_input != "fruits" and cat_input != "animals":
                break
            print(f"'{guess}' is not in the English dictionary.")
            guess = input()
    
        print(check_guess(guess, word))

        if guess == word:
            msg = "You won!"
            break
        attempts += 1
    
    print(msg)
    print("Coins: No coins are rewarded in easy mode.")

def normal_mode(word):
    currency = 0

    for attempt in range(1,6+1):
        print(f"Attempt #{attempt}")
        guess = input()

        while guess.lower() not in dictionary:
            if cat_input != "general" and cat_input != "fruits" and cat_input != "animals":
                break
            print(f"'{guess}' is not in the English dictionary.")
            guess = input()
            
        print(check_guess(guess, word))

        if guess == word:
            msg = "You won!"
            if attempt <= 2:
                currency += 3 
            elif attempt <= 4:
                currency += 2
            else:
                currency += 1
            break
        elif guess != word and attempt == 6:
            msg = "Game over."
            print(f"The word was: {word}")
            break
    
    print(f"Coins: {currency}")
    print(msg)

def hard_mode(word):
    currency = 0

    for attempt in range(1,4+1):
        print(f"Attempt #{attempt}")
        guess = input()

        while guess.lower() not in dictionary:
            if cat_input != "general" and cat_input != "fruits" and cat_input != "animals":
                break
            print(f"'{guess}' is not in the English dictionary.")
            guess = input()

        print(check_guess(guess, word))

        if guess == word:
            msg = "You won!"
            if attempt <= 2:
                currency += 3 
            elif attempt <= 4:
                currency += 2
            else:
                currency += 1
            break
        elif guess != word and attempt == 6:
            msg = "Game over."
            print(f"The word was: {word}")
            break
    
    print(f"Coins: {currency}")
    print(msg)

def extreme_mode(word):
    currency = 0
    
    for attempt in range(1,3+1):
        print(f"Attempt #{attempt}")
        guess = input()

        while guess.lower() not in dictionary:
            if cat_input != "general" and cat_input != "fruits" and cat_input != "animals":
                break
            print(f"'{guess}' is not in the English dictionary.")
            guess = input()

        print(check_guess(guess, word))

        if guess == word:
            msg = "You won!"
            currency += 10
            break
        elif guess != word and attempt == 3:
            msg = "Game over."
            print(f"The word was: {word}")
            break
    
    print(f"Coins: {currency}")
    print(msg)

main()
