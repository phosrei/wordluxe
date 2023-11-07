import customtkinter as ctk
import tkinter as tk
import io
import cairosvg
from PIL import Image

class WordluxeGame:
    def __init__(self):
        self.game = tk.Tk()
        self.game.attributes("-fullscreen", True)
        self.game.columnconfigure(0, weight=1)
        self.game.rowconfigure(0, weight=1)
        self.game.title("Wordluxe")

        # Convert SVG to a PNG image using cairosvg
        svg_data = open("assets/game_logo.svg", "rb").read()
        png_data = cairosvg.svg2png(bytestring=svg_data)
        photo_image = tk.PhotoImage(data=png_data)

        bg_image = ctk.CTkImage(Image.open("assets/background1.png"), size=(1620, 1114))

        bg_label = ctk.CTkLabel(master=self.game, text="", image=bg_image)
        bg_label.pack()

        self.wl_label = ctk.CTkLabel(master=self.game, text="", image=photo_image)
        self.wl_label.place(relx=0.5, rely=0.30, anchor="center")

        self.play_button = tk.Button(
            master=self.game,
            text="PLAY",
            font=("Clear Sans", 20, "bold"),
            width=19,
            height=1,
            borderwidth=0,
            command=self.play_button_pressed,
            state="normal",
            bg="Light Blue",
        )
        self.play_button.place(relx=0.5, rely=0.45, anchor="center")

        self.quit_button = tk.Button(
            master=self.game,
            text="QUIT",
            font=("Clear Sans", 20, "bold"),
            width=19,
            height=1,
            borderwidth=0,
            command=self.quit_button_pressed,
            state="normal",
            bg="Light Blue",
        )
        self.quit_button.place(relx=0.5, rely=0.53, anchor="center")

        self.game.iconbitmap("assets/game_icon.ico")

    def play_button_pressed(self):
        self.play_button["state"] = "disabled"
        self.quit_button["state"] = "disabled"

    def quit_button_pressed(self):
        self.game.quit()

    def run(self):
        self.game.mainloop()

if __name__ == "__main__":
    game_instance = WordluxeGame()
    game_instance.run()
