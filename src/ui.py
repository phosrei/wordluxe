import customtkinter as ctk
import tkinter as tk
import io
import cairosvg
from PIL import ImageTk, Image

class WordluxeGame:
    def __init__(self):
        self.game = ctk.CTk()
        self.game.attributes("-fullscreen", True)
        self.game.title("Wordluxe")

        global photo_image
        global bg_image
        global play_image

        # Create a frame to group buttons and labels
        self.frame = tk.Frame(self.game)
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Convert SVG to a PNG image using cairosvg
        svg_data = open("assets/game_logo.svg", "rb").read()
        png_data = cairosvg.svg2png(bytestring=svg_data)
        photo_image = tk.PhotoImage(data=png_data)

        bg_image = ctk.CTkImage(Image.open("assets/background1.png"), size=(1620, 1114))

        bg_label = ctk.CTkLabel(master=self.frame, text="", image=bg_image)
        bg_label.pack()

        self.play_image_load = Image.open("assets/play_button.gif")
        play_image = ImageTk.PhotoImage(self.play_image_load)

        self.wl_label = ctk.CTkLabel(master=self.frame, text="", image=photo_image)
        self.wl_label.place(relx=0.5, rely=0.30, anchor="center")

        self.game_desc = ctk.CTkLabel(
            master=self.frame,
            text="  The all new and \n improved wordle",
            font=("Times New Roman", 40),
            bg_color="#26556a"
        )
        self.game_desc.place(relx=0.5, rely=0.48, anchor="center")

        self.play_button = tk.Button(
            master=self.frame,
            image=play_image,
            borderwidth=0,
            command=self.play_button_pressed,
            state="normal",
            bg="#216061",
        )
        self.play_button.place(relx=0.63, rely=0.65, anchor="center")

        self.quit_button = tk.Button(
            master=self.frame,
            image=play_image,
            borderwidth=0,
            command=self.quit_button_pressed,
            state="normal",
            bg="#26546a",
        )
        self.quit_button.place(relx=0.37, rely=0.65, anchor="center")

        self.game.iconbitmap("assets/game_icon.ico")

    def play_button_pressed(self):
        pass
        
    def quit_button_pressed(self):
        self.game.quit()

    def quit_button_pressed(self):
        self.game.quit()

    def run(self):
        self.game.mainloop()

if __name__ == "__main__":
    game_instance = WordluxeGame()
    game_instance.run()
