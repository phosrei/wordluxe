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

# validates if input is a category and in one of the game modes
def validate_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please try again.")

def main():
    cat_input = validate_input("Choose category: ", wordbank.categories)
    dif_input = validate_input("Choose difficulty: ", wordbank.gen_difficulty)

    word = random.choice(wordbank_cat[cat_input][dif_input])

    game_modes = {
    "easy": easy_mode,
    "normal": normal_mode,
    "hard": hard_mode,
    "extreme": extreme_mode
}
    game_modes[dif_input](word, cat_input)

# check guess and assign a color based on certain conditions
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

def easy_mode(word, category):
    attempts = 1

    while True:
        print(f"Attempt #{attempts}")
        guess = input()

        while guess.lower() not in dictionary:
            if category not in ["general", "fruits", "animals"]:
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

def normal_mode(word, category):
    currency = 0
    attempt = 1

    while attempt <= 6:
        print(f"Attempt #{attempt}")
        guess = input()

        while guess.lower() not in dictionary:
            if category not in ["general", "fruits", "animals"]:
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

        attempt += 1

    print(f"Coins: {currency}")
    print(msg)

def hard_mode(word, category):
    currency = 0
    attempt = 1

    while attempt <= 4:
        print(f"Attempt #{attempt}")
        guess = input()

        while guess.lower() not in dictionary:
            if category not in ["general", "fruits", "animals"]:
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
        elif guess != word and attempt == 4:
            msg = "Game over."
            print(f"The word was: {word}")
            break
    
    print(f"Coins: {currency}")
    print(msg)

def extreme_mode(word, category):
    currency = 0
    attempt = 3
    
    while attempt <= 3:
        print(f"Attempt #{attempt}")
        guess = input()

        while guess.lower() not in dictionary:
            if category not in ["general", "fruits", "animals"]:
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
