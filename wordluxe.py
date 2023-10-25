import random

def main():
    categories = ["general", "countries", "animals", "fruits", "sports", "artists", "songs"]
    difficulty = {
        "easy": ["here", "book", "cake", "rain", "bird", "fire", "fish", "game", "jump", "kind", "loud", "moon", "nest", "open", "park", "quit", "rest", "star", "time", "view"],
        "normal": ["apple", "beach", "chair", "dance", "early", "fence", "glass", "happy", "igloo", "jumbo", "kite", "lemon", "music", "nurse", "ocean", "piano", "quick", "river", "smile", "table"],
        "hard": ["bright", "yellow", "purple", "hidden", "flavor", "dinner", "banana", "turtle", "puzzle", "rabbit", "guitar", "purple", "floral", "market", "window", "summer", "people", "planet", "friend", "invent"],
        "extreme": ["chicken", "musical", "capital", "journey", "freedom", "guitar", "honesty", "victory", "holiday", "history", "hydrate", "illegal", "silence", "justify", "monster", "breathe", "perfect", "nuclear", "quality", "society"]
    }

    user_input = input("Choose category: ")

    while user_input not in categories:
        print("Not in categories")
        user_input = input("Choose category: ")

    user_input = input("Choose difficulty: ")

    while user_input not in difficulty:
        print("Not in difficulties")
        user_input = input("Choose difficulty: ")
    else:
        user_input in difficulty
        random_word = random.choice(difficulty[user_input])

    word_length = len(random_word)
    feedback = ""
    num_guesses = 0
    currency = 0

    while feedback != random_word and num_guesses < 7:

        print(f"Attempt #{str(num_guesses + 1)}")
        guess = input()
        feedback = ""
        num_guesses += 1

        for i in range(word_length):
            if guess[i] in random_word[i]:
                feedback += guess[i] # GREEN BOX
            elif guess[i] in feedback:
                feedback += "X"
            elif guess[i] in random_word:
                feedback += guess[i] # YELLOW BOX
            else:
                feedback += "X" # GRAY BOX
        
        #add coins
        # Fixed bug incrementing only 2 coins when guessed in 2 attempts
        if feedback == random_word:
            if num_guesses <= 2:
                currency += 3 
            elif num_guesses <= 4:
                currency += 2
            else:
                currency += 1
                
        print(feedback.upper())
        
    print("Coins:", currency)
    print("Game over")

main()
