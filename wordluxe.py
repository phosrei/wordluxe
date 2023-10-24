import random

# TODO: Re-evaluate
easy_words = ["APPLE", "LEMON", "MELON", "PEACH", "GUAVA", "GRAPE"]
normal_words = ["CLOUD", "BEACH", "MAPLE", "GREED", "SMILE"]
hard_words = ["ABYSS", "PRISM", "RAVEN", "CHAOS", "CYNIC"]
extreme_words = ["QUIRK", "XENON", "VIXEN", "OZONE", "EXALT"]
categories = ['GENERAL', 'COUNTRIES', 'ANIMALS', 'FRUITS', 'SPORTS', 'ARTISTS', 'SONGS']
diff_list = {1:easy_words,2:normal_words,3:hard_words,4:extreme_words}

user_input = input("choose category: ").upper()

if user_input in categories:
	print(user_input, "is chosen")
else:
	print('Not in the categories.')

feedback = ""
tries = 1
currency = 0

user_input = int(input("Choose difficulty: "))
if user_input in diff_list:
    random_word = random.choice(diff_list[user_input])
else:
    print("Not available.")

word_length = len(random_word)
feedback = ""
tries = 1
currency = 0

while feedback != random_word and tries < 7:
    print("Attempt #", tries)
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
    
    #add coins
    # TODO: Fix incrementing only 2 coins when guessed in 2 attempts
    if feedback == random_word:
        if tries <= 2:
            currency += 3 
        elif tries <= 4:
            currency += 2
        else:
            currency += 1
            
    print(feedback)
    
print("Coins:", currency)
print("Game over")
