import tkinter as tk
import cairosvg
import time
from PIL import ImageTk, Image

game = tk.Tk()
game.attributes("-fullscreen", True)
game.title("Wordluxe")
game.iconbitmap("assets/game_icon.ico")

def play_button_clicked():
    main_menu.place_forget()
    category_menu.place(relx = 0, 
                        rely = 0, 
                        relwidth = 1, 
                        relheight = 1)
    bg_label2.place(x=-400, y=-2)

def category_button_clicked():
    category_menu.place_forget()
    difficulty_menu.place(relx = 0, 
                        rely = 0, 
                        relwidth = 1, 
                        relheight = 1)
    bg_label3.place(x=-400, y=-2)
    
def difficulty_button_clicked():
    difficulty_menu.place_forget()
    ingame_menu.place(relx = 0, 
                        rely = 0, 
                        relwidth = 1, 
                        relheight = 1)
    bg_label4.place(x=-400, y=-2)

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
                    text = "", 
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
                    bg = "#26556a")
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
htp_button = tk.Button(master = main_menu,
                        image = play_image,
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
                        command = category_button_clicked)
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
                        command = category_button_clicked)
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
                        command = category_button_clicked)
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
                        command = category_button_clicked)
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
                        command = category_button_clicked)
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
                        command = category_button_clicked)
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
                        command = category_button_clicked)
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
                        command = difficulty_button_clicked)
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
                        command = difficulty_button_clicked)
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
                        command = difficulty_button_clicked)
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
                        command = difficulty_button_clicked)
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

game.mainloop()
