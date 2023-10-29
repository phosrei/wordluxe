import random
import pycountry
from wordbank import categories
from nltk.corpus import words
from termcolor import colored

dictionary = set(words.words())
currency = 3

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
    powerup_result = ""
    output = ""
    attempt = 1
    msg = ""

    print(f"Coins: {currency}")
    print("Enter 'P' for power-ups")

    while attempt <= max_attempts:
        print(f"Attempt #{attempt}")
        guess = input()

        if guess in ["p", "P"] and max_attempts != 3 and currency > 0:
            powerup_result = get_powerup(word, output, currency)
            continue
        elif guess in ["p", "P"] and currency <= 0:
            print("Unable use power-ups at this time")
            continue
        elif max_attempts == 3:
            print("Unable to use power-ups in extreme mode")
            continue
            
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

        output = (check_guess(guess, word))
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
    print(f"The word is {word}")
    powerup_input = input("Choose a power-up:\n"
    "1. Letter Eraser (-1 coin)\n"
    "2. Invincibility (-2 coins)\n"
    "3. Reveal Vowels (-3 coins)\n").upper()

    if powerup_input not in ["1", "2", "3", "Q"]:
        print('Invalid input')
        get_powerup(output, word)
    elif powerup_input == "Q":
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
        print('You do not have enough coins')

def vowel_powerup(word):
  vowels = 'aeiou'
  vowels_hint = []

  for i in range(len(word)):
    if word[i] in vowels:
      if word[i] not in vowels_hint:
        vowels_hint.append(word[i])

    vowel_string = ", ".join(vowels_hint)
  print(f"The vowel(s) in the word is/are: {vowel_string}")

def eraser_powerup(guess, word):
    eraser = "abcdefghijklmnopqrstvwxyz"
    eraser_list = []

    for i in range(len(eraser)):
        if eraser[i] not in word and eraser[i] not in guess:
                eraser_list.append(eraser[i])

    random_unused_letter = random.choice(list(eraser_list)).upper()
    print(f"{random_unused_letter} is not in the word")

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
    end_input = input("RETRY (R) -- NEW GAME (N) -- QUIT (Q) ").upper()
    if end_input == "R":
        play_game(word, category, max_attempts)
    elif end_input == "N":
        main()
    elif end_input == "Q":
        return
    else:
        print("Invalid input")
        end_options(word, category, max_attempts)

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