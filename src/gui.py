# Download assets and create an assets folder in your Wordluxe Folder, then place all assets in the assets folder

import customtkinter
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
        wl_label = customtkinter.CTkLabel(master=self.game, text="", image=wordluxe_image)
        wl_label.place(relx=0.5, rely=0.05, anchor="center")

        self.game.iconbitmap(r"assets\game_icon.ico")

    def run(self):
        self.game.mainloop()

if __name__ == "__main__":
    game_instance = WordluxeGame()
    game_instance.run()
