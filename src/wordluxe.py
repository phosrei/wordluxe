import random
import pycountry
from wordbank import categories
from nltk.corpus import words
from termcolor import colored


dictionary = set(words.words())
currency = 0

wordbank_cat = {
    "general": categories.get("general"),
    "countries": categories.get("countries"),
    "animals": categories.get("animals"),
    "fruits": categories.get("fruits"),
    "sports": categories.get("sports"),
    "artists": categories.get("artists"),
    "songs": categories.get("songs")
}


def validate_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please try again.")

def calculate_reward(attempt, max_attempts):
    if max_attempts == 3:
        return 10
    elif max_attempts == 4:
        return 5
    if attempt <= 2:
        return 3
    elif attempt <= 4:
        return 2
    else:
        return 1

def play_game(word, category, max_attempts):
    global currency
    attempt = 1
    msg = ""

    while attempt <= max_attempts:
        print(f"Attempt #{attempt}")
        guess = input()

        if category not in ["songs", "artists", "sports", "countries"]:
            if guess.lower() not in dictionary:
                print(f"'{guess}' is not a word.")
                continue
        elif category == "countries":
            if pycountry.countries.get(name=guess) == None:
                print(f"'{guess}' is not a valid country.")

        if len(guess) != len(word):
            print(f"Guess should be {len(word)} letters.")
            continue

        print(check_guess(guess, word))

        if guess == word:
            msg = "You won!"
            currency += calculate_reward(attempt, max_attempts)
            break
        elif attempt == max_attempts:
            msg = "Game over."
            print(f"The word was: {word}")
            break
        
        attempt += 1

    if max_attempts != float("inf"):
        print(f"Coins: {currency}")
    print(msg)

def check_guess(guess, word):
    length = len(word)
    output = ["X"] * length 

    for i in range(length):
        if guess[i] == word[i]:
            output[i] = colored(guess[i], 'green')
            word = word.replace(guess[i], "X", 1)

    for i in range(length):
        if guess[i] in word and output[i] == "X":
            output[i] = colored(guess[i], 'yellow')
            word = word.replace(guess[i], "X", 1)
        elif guess[i] in output[i]:
            continue
        else:
            output[i] = colored(guess[i], 'dark_grey')

    return ''.join(output)

def easy_mode(word, category):
    play_game(word, category, max_attempts = float("inf"))
    print("Coins: No coins are rewarded in easy mode")

def normal_mode(word, category):
    play_game(word, category, max_attempts = 6)

def hard_mode(word, category):
    play_game(word, category, max_attempts = 4)

def extreme_mode(word, category):
    play_game(word, category, max_attempts = 3)

def main():
    cat_input = validate_input("Choose category: ", categories)
    dif_input = validate_input("Choose difficulty: ", categories.get("general"))

    word = random.choice(wordbank_cat[cat_input][dif_input])

    game_modes = {
        "easy": easy_mode,
        "normal": normal_mode,
        "hard": hard_mode,
        "extreme": extreme_mode
    }
    game_modes[dif_input](word, cat_input)

main()
