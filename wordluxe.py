import random
from nltk.corpus import words
from termcolor import colored
from wordbank import categories, difficulty

dictionary = set(words.words())

cat_input = input("Choose category: ")

while cat_input not in categories:
    print("Not in categories")
    cat_input = input("Choose category: ")

dif_input = input("Choose difficulty: ")

while dif_input not in difficulty:
    print("Not in difficulties")
    dif_input = input("Choose difficulty: ")

random_word = random.choice(difficulty[dif_input])
word_length = len(random_word)
currency = 0
msg = ""

for attempt in range(1,7):
    print(f"Attempt #{attempt}")
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
        if attempt <= 2:
            currency += 3 
        elif attempt <= 4:
            currency += 2
        else:
            currency += 1
        break
    elif guess != random_word and attempt == 5:
        msg = "Game over."
        print(f"The word was: {random_word}")
        break
    
print(f"Coins: {currency}")
print(msg)
