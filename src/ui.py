# Download assets and create an assets folder in your Wordluxe Folder, then place all assets in the assets folder

import customtkinter
import tkinter
from PIL import Image

class WordluxeGame:
    def __init__(self):
        self.game = customtkinter.CTk()
        self.game.geometry("500x500")
        self.game.attributes("-fullscreen", "True")
        self.game.columnconfigure(0, weight=1)
        self.game.rowconfigure(0, weight=1)
        self.game.title("Wordluxe")

        bg_image = customtkinter.CTkImage(Image.open("assets/background1.png"), size=(1620, 1114))
        bg_label = customtkinter.CTkLabel(master=self.game, text="", image=bg_image)
        bg_label.pack()

        wordluxe_image = customtkinter.CTkImage(Image.open("assets/game_logo.png"), size=(480, 60))
        self.wl_label = customtkinter.CTkLabel(master=self.game, text="", image=wordluxe_image)
        self.wl_label.place(relx=0.5, rely=0.30, anchor="center")

        self.play_button = tkinter.Button(master=self.game, text="PLAY", font=("Clear Sans", 20, "bold"), width=19, height=1, borderwidth=1, command=self.play_button_pressed, state="normal", bg="Light Blue")
        self.play_button.place(relx=0.5, rely=0.45, anchor="center")

        self.quit_button = tkinter.Button(master=self.game, text="QUIT", font=("Clear Sans", 20, "bold"), width=19, height=1, borderwidth=1, command=self.quit_button_pressed, state="normal", bg="Light Blue")
        self.quit_button.place(relx=0.5, rely=0.53, anchor="center")

        self.game.iconbitmap("assets/game_icon.ico")

    def play_button_pressed(self):
        self.play_button["state"]= "disabled"
        self.quit_button["state"]= "disabled"

    def quit_button_pressed(self):
        self.game.destroy()

    def run(self):
        self.game.mainloop()

if __name__ == "__main__":
    game_instance = WordluxeGame()
    game_instance.run()
