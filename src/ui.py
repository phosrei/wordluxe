import tkinter as tk
from tkinter import messagebox
import cairosvg
import random
import time
from wordluxe import wordbank_cat
from PIL import ImageTk, Image

game = tk.Tk()
game.attributes("-fullscreen", True)
game.title("Wordluxe")
game.iconbitmap("assets/game_icon.ico")

GREEN = "#6ca965"
YELLOW = "#c8b653"
GRAY = "#787c7f"

category_str = tk.StringVar(value="")
difficulty_str = tk.StringVar(value="")
category = ""
difficulty = ""
current_guess_str = ""
current_guess = []
wordtile_labels = []
letter_count = 0
max_attempts_var = 0
attempts = 1

def play_button_clicked():
    main_menu.place_forget()
    category_menu.place(relx = 0, 
                        rely = 0, 
                        relwidth = 1, 
                        relheight = 1)
    bg_label2.place(x=-400, y=-2)

def category_button_clicked(chosen_category, category_var):
    global category
    category = chosen_category
    global category_str
    category_str.set(category_var)

    category_menu.place_forget()
    difficulty_menu.place(relx = 0, 
                        rely = 0, 
                        relwidth = 1, 
                        relheight = 1)
    bg_label3.place(x=-400, y=-2)

def difficulty_button_clicked(chosen_difficulty, difficulty_var, max_attempts):
    global difficulty
    difficulty = chosen_difficulty
    global difficulty_str
    difficulty_str.set(difficulty_var)

    global word
    word = random.choice(wordbank_cat[category][difficulty])
    update_word_tiles()

    global max_attempts_var
    global attempts

    max_attempts_var = max_attempts

    difficulty_menu.place_forget()
    ingame_menu.place(relx = 0, 
                        rely = 0, 
                        relwidth = 1, 
                        relheight = 1)
    bg_label4.place(x=-400, y=-2)
    starting_tiles_frame.place(relx=0.501,
                           rely=0.353,
                           anchor='center')
    
    if len(word) == 4:
        tiles4_label.grid()
        letter_eraser.place(relx=0.67, 
                        rely=0.125, 
                        anchor="center")
        invincible.place(relx=0.67, 
                  rely=0.235, 
                  anchor="center")
        reveal_vowel.place(relx=0.67, 
                  rely=0.345, 
                  anchor="center")
    elif len(word) == 5:
        tiles5_label.grid()
        letter_eraser.place(relx=0.70, 
                        rely=0.125, 
                        anchor="center")
        invincible.place(relx=0.70, 
                  rely=0.235, 
                  anchor="center")
        reveal_vowel.place(relx=0.70, 
                  rely=0.345, 
                  anchor="center")
    elif len(word) == 6:
        tiles6_label.grid()
        letter_eraser.place(relx=0.73, 
                        rely=0.125, 
                        anchor="center")
        invincible.place(relx=0.73, 
                  rely=0.235, 
                  anchor="center")
        reveal_vowel.place(relx=0.73, 
                  rely=0.345, 
                  anchor="center")
    elif len(word) == 7:
        tiles7_label.grid()
        letter_eraser.place(relx=0.76, 
                        rely=0.125, 
                        anchor="center")
        invincible.place(relx=0.76, 
                  rely=0.235, 
                  anchor="center")
        reveal_vowel.place(relx=0.76, 
                  rely=0.345, 
                  anchor="center")
    
# Main Menu Frame
main_menu = tk.Frame(game)
main_menu.place(relx = 0, 
                rely = 0, 
                relwidth = 1, 
                relheight = 1)

# Wordluxe Background Image
bg_image = ImageTk.PhotoImage(file="assets/background1.png")
bg_label = tk.Label(master = main_menu,
                    image = bg_image,
                    width = 1920,
                    height = 1080)
bg_label.place(x=-400, y=-2)

# Wordluxe Game Logo
svg_data = open("assets/game_logo.svg", "rb").read()
png_data = cairosvg.svg2png(bytestring = svg_data)
photo_image = tk.PhotoImage(data = png_data)

wl_label = tk.Label(master = main_menu,  
                    image = photo_image,
                    width = 740,
                    height = 89)
wl_label.place(relx = 0.5,
               rely = 0.3,
               anchor = "center")

# Wordluxe Main Menu Description
game_desc = tk.Label(master = main_menu,
                    text = "  The all new and \n improved wordle",
                    font = ("Times New Roman", 40),
                    bg = "#26556a",
                    fg = "White")
game_desc.place(relx=0.5, 
                rely=0.48, 
                anchor="center")

# Play Button
play_image = ImageTk.PhotoImage(file = "assets/play_button.png")
play_button = tk.Button(master = main_menu,
                        image = play_image,
                        borderwidth = 0,
                        state = "normal",
                        bg = "#216061",
                        command = play_button_clicked)
play_button.place(relx = 0.63, 
                  rely = 0.65, 
                  anchor="center")

# How to Play Button
htp_image = ImageTk.PhotoImage(file = "assets/htp_button.png")
htp_button = tk.Button(master = main_menu,
                        image = htp_image,
                        borderwidth = 0,
                        command = "",
                        state = "normal",
                        bg = "#26546a")
htp_button.place(relx = 0.37, 
                 rely = 0.65, 
                 anchor = "center")

# Category Menu Frame
category_menu = tk.Frame(game)

bg_image2 = ImageTk.PhotoImage(file="assets/background1.png")
bg_label2 = tk.Label(master = category_menu,
                    image = bg_image,
                    width = 1920,
                    height = 1080)

# Choose Category
cat_desc = tk.Label(master = category_menu,
                    text = "Choose Category",
                    font = ("Times New Roman", 40),
                    bg = "#2e4377",
                    fg = "White")
cat_desc.place(relx=0.5, 
                rely=0.1, 
                anchor="center")

# General
general_image = ImageTk.PhotoImage(file = "assets/general.png")
general_button = tk.Button(master = category_menu,
                        image = general_image,
                        borderwidth= 0,
                        state = "normal",
                        bg = "#2c4774",
                        command = lambda: category_button_clicked("general", "General"))
general_button.place(relx=0.5, 
                  rely=0.2, 
                  anchor="center")

# Countries
countries_image = ImageTk.PhotoImage(file = "assets/countries.png")
countries_button = tk.Button(master = category_menu,
                        image = countries_image,
                        borderwidth= 0,
                        state = "normal",
                        bg = "#2a4c71",
                        command = lambda: category_button_clicked("countries", "Countries"))
countries_button.place(relx=0.5, 
                  rely=0.3, 
                  anchor="center")

# Animals
animals_image = ImageTk.PhotoImage(file = "assets/animals.png")
animals_button = tk.Button(master = category_menu,
                        image = animals_image,
                        borderwidth= 0,
                        state = "normal",
                        bg = "#28506d",
                        command = lambda: category_button_clicked("animals", "Animals"))
animals_button.place(relx=0.5, 
                  rely=0.4, 
                  anchor="center")

# Fruits
fruits_image = ImageTk.PhotoImage(file = "assets/fruits.png")
fruits_button = tk.Button(master = category_menu,
                        image = fruits_image,
                        borderwidth= 0,
                        state = "normal",
                        bg = "#26556a",
                        command = lambda: category_button_clicked("fruits", "Fruits"))
fruits_button.place(relx=0.5, 
                  rely=0.5, 
                  anchor="center")

# Sports
sports_image = ImageTk.PhotoImage(file = "assets/sports.png")
sports_button = tk.Button(master = category_menu,
                        image = sports_image,
                        borderwidth= 0,
                        state = "normal",
                        bg = "#245967",
                        command = lambda: category_button_clicked("sports", "Sports"))
sports_button.place(relx=0.5, 
                  rely=0.6, 
                  anchor="center")

# Songs
songs_image = ImageTk.PhotoImage(file = "assets/songs.png")
songs_button = tk.Button(master = category_menu,
                        image = songs_image,
                        borderwidth= 0,
                        state = "normal",
                        bg = "#216061",
                        command = lambda: category_button_clicked("songs", "Songs"))
songs_button.place(relx=0.5, 
                  rely=0.7, 
                  anchor="center")

# Artists
artists_image = ImageTk.PhotoImage(file = "assets/artists.png")
artists_button = tk.Button(master = category_menu,
                        image = artists_image,
                        borderwidth= 0,
                        state = "normal",
                        bg = "#216061",
                        command = lambda: category_button_clicked("artists", "Artists"))
artists_button.place(relx=0.5, 
                  rely=0.8, 
                  anchor="center")

# Difficulty Menu Frame
difficulty_menu = tk.Frame(game)

bg_image3 = ImageTk.PhotoImage(file="assets/background1.png")
bg_label3 = tk.Label(master = difficulty_menu,
                    image = bg_image,
                    width = 1920,
                    height = 1080)

# Choose Difficulty
dif_desc = tk.Label(master = difficulty_menu,
                    text = "Choose Difficulty",
                    font = ("Times New Roman", 40),
                    bg = "#2e4377",
                    fg = "White")
dif_desc.place(relx=0.5, 
                rely=0.1, 
                anchor="center")

# Easy Button
easy_image = ImageTk.PhotoImage(file = "assets/easy.png")
easy_button = tk.Button(master = difficulty_menu,
                        image = easy_image,
                        borderwidth= 0,
                        state = "normal",
                        bg = "#2c4774",
                        command = lambda: difficulty_button_clicked("easy", "Easy", max_attempts=6))
easy_button.place(relx=0.5, 
                  rely=0.2, 
                  anchor="center")

# Normal Button
normal_image = ImageTk.PhotoImage(file = "assets/normal.png")
normal_button = tk.Button(master = difficulty_menu,
                        image = normal_image,
                        borderwidth= 0,
                        state = "normal",
                        bg = "#2a4c71",
                        command = lambda: difficulty_button_clicked("normal", "Normal", max_attempts=6))
normal_button.place(relx=0.5, 
                  rely=0.3, 
                  anchor="center")

# Hard Button
hard_image = ImageTk.PhotoImage(file = "assets/hard.png")
hard_button = tk.Button(master = difficulty_menu,
                        image = hard_image,
                        borderwidth= 0,
                        state = "normal",
                        bg = "#28506d",
                        command = lambda: difficulty_button_clicked("hard", "Hard", max_attempts=4))
hard_button.place(relx=0.5, 
                  rely=0.4, 
                  anchor="center")

# Extreme Button
extreme_image = ImageTk.PhotoImage(file = "assets/extreme.png")
extreme_button = tk.Button(master = difficulty_menu,
                        image = extreme_image,
                        borderwidth= 0,
                        state = "normal",
                        bg = "#26556a",
                        command = lambda: difficulty_button_clicked("extreme", "Extreme", max_attempts=3))
extreme_button.place(relx=0.5, 
                  rely=0.5, 
                  anchor="center")

# In-game Menu
ingame_menu = tk.Frame(game)

bg_image4 = ImageTk.PhotoImage(file="assets/background1.png")
bg_label4 = tk.Label(master = ingame_menu,
                    image = bg_image,
                    width = 1920,
                    height = 1080)

catt_desc = tk.Label(master = ingame_menu,
                    textvariable = category_str,
                    font = ("Franklin Gothic Medium", 20, "bold"),
                    bg = "#303d7b",
                    fg = "White")
catt_desc.place(relx=0.5, 
                rely=0.02, 
                anchor="center")

diff_desc = tk.Label(master = ingame_menu,
                    textvariable = difficulty_str,
                    font = ("Franklin Gothic Medium", 20, "bold"),
                    bg = "#303d7b",
                    fg = "White")
diff_desc.place(relx=0.5, 
                rely=0.055, 
                anchor="center")

# Power-up icons
letter_eraser_image = ImageTk.PhotoImage(file = "assets/letter_eraser.png", width=75, height=75)
letter_eraser = tk.Button(master = ingame_menu,
                        image = letter_eraser_image,
                        borderwidth = 0,
                        state = "normal",
                        bg = "#2c4774",
                        command = "")

invincible_image = ImageTk.PhotoImage(file = "assets/invincible.png")
invincible = tk.Button(master = ingame_menu,
                        image = invincible_image,
                        borderwidth = 0,
                        state = "normal",
                        bg = "#2a4c71",
                        command = "")

vowel_image = ImageTk.PhotoImage(file = "assets/vowel.png")
reveal_vowel = tk.Button(master = ingame_menu,
                        image = vowel_image,
                        borderwidth = 0,
                        state = "normal",
                        bg = "#28506d",
                        command = "")

lettervar = tk.StringVar()
guess_input = tk.Entry(textvariable=lettervar, master=ingame_menu, font=("Helvetica", 20), justify="center")
guess_input.place(relx=0.5,rely=0.675,width=200,height=70,anchor="center")

keyboard_layout = [
    'QWERTYUIOP',
    'ASDFGHJKL',
    '⌫ZXCVBNM↵'
]

# Create and place the keyboard buttons
keyboard_frame = tk.Frame(ingame_menu, background="#216061")
keyboard_frame.place(relx=0.5, rely=0.84, anchor="center")

for row, key_row in enumerate(keyboard_layout, 1):
    for col, char in enumerate(key_row):
        if row == 2:
            column_span = 2
        elif row == 3:
            column_span = 2
        else:
            column_span = 1

        button = tk.Button(keyboard_frame, text=char, borderwidth=0.5, bg="#2a4c71", fg="Steel Blue", font=("Arial", 30, "bold"), width=2, height=1, command=lambda c=char: show_letter_in_guess(c))
        button.grid(row=row, column=col, padx=2, pady=2, columnspan=column_span)

def show_letter_in_guess(char):
    global attempts
    current_text = lettervar.get()

    if guess_input["state"] == "normal":
        if char == "⌫":
            new_text = current_text[:-1]
            lettervar.set(new_text)
        elif char == "↵":
            check_guess()
        else:
            char = char.lower()
            lettervar.set(current_text + char)

starting_tiles_frame = tk.Frame(ingame_menu)

tiles_4 = ImageTk.PhotoImage(file = "assets/tiles_4.png")
tiles_5 = ImageTk.PhotoImage(file = "assets/tiles_5.png")
tiles_6 = ImageTk.PhotoImage(file = "assets/tiles_6.png")
tiles_7 = ImageTk.PhotoImage(file = "assets/tiles_7.png")

tiles4_label = tk.Label(master = starting_tiles_frame, 
                        image=tiles_4,
                        border=0,
                        width=334,
                        height=503)

tiles5_label = tk.Label(master = starting_tiles_frame, 
                        image=tiles_5,
                        border=0,
                        width=422,
                        height=505)

tiles6_label = tk.Label(master = starting_tiles_frame, 
                        image=tiles_6,
                        border=0,
                        width=507,
                        height=339)

tiles7_label = tk.Label(master = starting_tiles_frame, 
                        image=tiles_7,
                        border=0,
                        width=591,
                        height=254)

def place_word_tile(i, letter, attempts):
    global wordtile_labels

    wordtile_label = tk.Label(
        master=starting_tiles_frame,
        text=letter.upper(),
        font=("Helvetica", 30, "bold"),
        borderwidth=0,
        border=0,
        width=2,
        height=1,
        bg="Steel Blue"
    )
    
    wordtile_labels.append(wordtile_labels)

    if len(word) == 4:
        wordtile_label.place(relx=0.05, x=i * 84.28, rely=-0.134, y=(attempts - 1) * 84.4)
    elif len(word) == 5:
        wordtile_label.place(relx=0.04, x=i * 84.4, rely=-0.132, y=(attempts - 1) * 84.5)
    elif len(word) == 6:
        wordtile_label.place(relx=0.031, x=i * 84.4, rely=-0.190, y=(attempts - 1) * 84.5)
    elif len(word) == 7:
        wordtile_label.place(relx=0.027, x=i * 84.4, rely=-0.26, y=(attempts - 1) * 84.5)

    if letter == word[i]:
        wordtile_label.config(fg=GREEN)
    elif letter in word and not letter == word[i]:
        wordtile_label.config(fg=YELLOW)
    elif letter not in word:
        wordtile_label.config(fg="seashell4")

def place_word_tiles_one_by_one(i, guess, attempts):
    if i < len(guess):
        place_word_tile(i, guess[i], attempts)
        game.after(250, place_word_tiles_one_by_one, i + 1, guess, attempts)

def check_guess():
    global word
    global attempts
    global wordtile_labels

    guess = guess_input.get()
    attempts += 1

    if attempts <= max_attempts_var:
        if len(guess) == len(word):
            if guess == word:
                place_word_tiles_one_by_one(0, guess, attempts)
                ingame_menu.after(1000, lambda: messagebox.showinfo("You win!", f"The word was '{word}'."))
                guess_input.delete(0, tk.END)
                guess_input.config(state="readonly")
            else:
                place_word_tiles_one_by_one(0, guess, attempts)
                guess_input.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Guess must be the same length as the word.")
            attempts -= 1
    else:
        place_word_tiles_one_by_one(0, guess, attempts)
        ingame_menu.after(1000, lambda: messagebox.showerror("You Lose!", f"The word was '{word}'."))
        guess_input.delete(0, tk.END)
        guess_input.config(state="readonly")

def update_word_tiles():
    for widget in ingame_menu.winfo_children():
        if isinstance(widget, tk.Label) and widget.winfo_name() == "word_tile":
            widget.destroy()

game.mainloop()
