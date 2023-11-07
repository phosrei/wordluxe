from string import ascii_lowercase
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
        user_input = input(prompt).strip().lower()  # Apply both suggestions
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please try again.")

def calculate_reward(attempt, max_attempts):
    if max_attempts == 3:
        return 10
    elif max_attempts == 4:
        return 5
    elif attempt <= 2:
        return 3
    elif attempt <= 4:
        return 2
    else:
        return 1

def play_game(word, category, max_attempts):
    global currency
    powerup_result = ""
    output = ""
    attempt = 1
    msg = ""

    print(f"Coins: {currency}")
    print("Enter 'P' for power-ups")

    while attempt <= max_attempts:
        print(f"Attempt #{attempt}")
        guess = input()

        if guess.lower() == "p":
            if max_attempts == 3:
                print("Power-ups are disabled in extreme mode")
            else:
                powerup_result = get_powerup(word, output, currency)
            continue

        if category not in ["songs", "artists", "sports", "countries"]:
            if guess.lower() not in dictionary:
                print(f"'{guess}' is not a word.")
                continue
        elif category == "countries":
            if pycountry.countries.get(name=guess) is None:
                print(f"'{guess}' is not a valid country.")
                continue

        if len(guess) != len(word):
            print(f"Guess should be {len(word)} letters.")
            continue

        output = check_guess(guess, word)
        print(output)

        if powerup_result == "2":
            powerup_result = ""
            continue

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

    end_options(word, category, max_attempts)

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

def get_powerup(word, output, currency):
    print("Choose a power-up:")
    print("1. Letter Eraser (-1 coin)")
    print("2. Invincibility (-2 coins)")
    print("3. Reveal Vowels (-3 coins)")

    powerup_input = input().upper()

    if powerup_input in ["Q", "1", "2", "3"]:
        if powerup_input == "Q":
            return
        elif powerup_input == "1" and currency >= 1:
            currency -= 1
            eraser_powerup(output, word)
        elif powerup_input == "2" and currency >= 2:
            currency -= 2
            return "2"
        elif powerup_input == "3" and currency >= 3:
            currency -= 3
            vowel_powerup(word)
        else:
            print("Not enough coins")
    else:
        print("Invalid input")
    return

def vowel_powerup(word):
    vowels = 'aeiou'
    vowels_hint = []

    for char in word:
        if char in vowels and char not in vowels_hint:
            vowels_hint.append(char)

    vowel_string = ", ".join(vowels_hint)
    print(f"The vowel(s) in the word is/are: {vowel_string.upper()}")

def eraser_powerup(guess, word):
    alphabet = ascii_lowercase
    eraser_list = []

    for letter in alphabet:
        if letter not in word and letter not in guess:
                eraser_list.append(letter)

    random_unused_letter = random.choice(eraser_list).upper()
    print(f"{random_unused_letter.upper()} is not in the word")

def easy_mode(word, category):
    play_game(word, category, max_attempts = float("inf"))
    print("Coins: No coins are rewarded in easy mode")

def normal_mode(word, category):
    play_game(word, category, max_attempts = 6)

def hard_mode(word, category):
    play_game(word, category, max_attempts = 4)

def extreme_mode(word, category):
    play_game(word, category, max_attempts = 3)

def end_options(word, category, max_attempts):
    while True:
        end_input = input("RETRY (R) -- NEW GAME (N) -- QUIT (Q) ").upper()
        
        if end_input == "R":
            play_game(word, category, max_attempts)
        elif end_input == "N":
            main()
        elif end_input == "Q":
            return
        else:
            print("Invalid input")

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
