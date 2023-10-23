import random

words = ["APPLE", "LEMON", "MELON", "PEACH", "GUAVA", "GRAPE"]
random_word = random.choice(words)
word_length = 5
feedback = ""
tries = 0

while feedback != random_word and tries < 6:
    guess = input().upper()
    feedback = ""
    tries += 1
    for i in range(word_length):
        if guess[i] in random_word[i]:
            feedback += guess[i]
        elif guess[i] in random_word:
            feedback += guess[i].lower() # lowercase means correct letter but in wrong position
        else:
            feedback += "X" # cross indicates wrong letter
    print(feedback)