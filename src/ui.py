import os
import sys
import json
import random
import pycountry
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt, QTimer, QSize
from config import *

def load_currency():
    with open(CURRENCY_FILE_PATH, 'r') as f:
        return json.load(f)

def save_currency(currency):
    with open(CURRENCY_FILE_PATH, 'w') as f:
        json.dump(currency, f)

currency = load_currency()

class WordluxeGame(QMainWindow):
    # initialize the game
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wordluxe")
        self.setWindowIcon(QIcon(GAME_ICON_PATH))
        self.showFullScreen()

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # set the styling of the window and widgets
        with open(STYLE_FILE_PATH, "r") as f:
            QApplication.instance().setStyleSheet(f.read())

        self.setup_main_menu_page()

    def setup_main_menu_page(self):
        # create the main menu frame
        main_menu_frame = self.create_frame("mmframe")
        main_layout = QVBoxLayout(main_menu_frame)
        main_layout.setAlignment(Qt.AlignCenter)
        # add the game logo to the main menu frame
        game_logo = QSvgWidget(GAME_LOGO_PATH, main_menu_frame)
        game_logo.setFixedSize(game_logo.sizeHint())
        main_layout.addWidget(game_logo)
        main_layout.addSpacing(HEADING_SPACING)
        # add the heading to the main menu frame
        heading = QLabel("The new, and \nimproved wordle!", main_menu_frame)
        heading.setObjectName("heading")
        heading.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(heading)
        main_layout.addSpacing(HEADING_SPACING)
        # adds a button frame for the buttons
        main_buttons_layout = QHBoxLayout()
        main_buttons_layout.setAlignment(Qt.AlignCenter)
        # add buttons, style them, and add to the main menu frame
        for button_text, button_method, button_name in [("Play", self.play_button_pressed, "button"), ("Quit", self.quit_button_pressed, "quitButton")]:
            button = self.create_button(button_text, main_menu_frame, BUTTON_FIXED_WIDTH, button_method, button_name)
            main_buttons_layout.addWidget(button)
            main_buttons_layout.addSpacing(MAIN_BUTTONS_SPACING)

        main_layout.addLayout(main_buttons_layout)

        self.difficulty = ""

        """
        the line of code below adds the main menu frame to the stacked widget.
        The stacked_widget is a container that can hold and manage multiple widgets, 
        but only one widget is visible at a time. 
        """
        self.stacked_widget.addWidget(main_menu_frame)

    def setup_second_page(self):
        self.page_template("cframe", "Choose category", CATEGORY_BUTTONS, self.cat_buttons_pressed)

    def setup_third_page(self):
        self.page_template("dframe", "Choose difficulty", DIFFICULTY_BUTTONS, self.dif_buttons_pressed)

    def page_template(self, frame_name, text, buttons, function):
        # a page template for both the category and difficulty pages
        frame = self.create_frame(frame_name)
        self.stacked_widget.addWidget(frame)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        label = QLabel(text, frame)
        label.setObjectName("heading")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        layout.addSpacing(HEADING_SPACING)

        self.create_buttons(layout, buttons, frame, function)

    def setup_game_page(self):
        self.game_frame = self.create_frame("gframe")
        game_layout = QVBoxLayout(self.game_frame)
        game_layout.setAlignment(Qt.AlignCenter)

        game_layout.addWidget(self.create_grid(), alignment=Qt.AlignCenter)

        if self.difficulty == EXTREME_DIFFICULTY:
            game_layout.addWidget(self.setup_timer(), alignment=Qt.AlignCenter)
        else:
            self.add_powerups(self.game_frame)
        self.add_currency_display(self.game_frame)

        game_layout.addWidget(self.create_keyboard(), alignment=Qt.AlignCenter)

        self.stacked_widget.addWidget(self.game_frame)

    def setup_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_timeout)
        self.timer_label = QLabel(self)
        self.timer_label.setObjectName("timerLabel")

        self.start_timer()

        return self.timer_label
    
    def start_timer(self):
        self.remaining_time = 180
        self.timer.start(1000)
        self.update_timer_label()

    def update_timer_label(self):
        if self.remaining_time == 10:
            self.timer_label.setStyleSheet("QLabel { color: #d03939; }")
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.timer_label.setText(f"{minutes:02d}:{seconds:02d}")

    def timer_timeout(self):
        self.remaining_time -= 1
        self.update_timer_label()

        if self.remaining_time <= 0:
            self.timer.stop()
            self.show_prompt()  


    def create_grid(self):
        self.grid_frame = self.create_frame("gridframe")
        self.grid_layout = QGridLayout()
        self.grid_frame.setLayout(self.grid_layout)

        self.invincible_clicked = False
        self.num_guess = 0
        self.board = []
        self.guess_store = ""
        self.guess = ""

        # create the grid based of the length of the word and max guesses
        for row in range(self.max_guesses):
            row_labels = []
            for col in range(len(self.word)):
                grid_box = self.create_grid_box(self.grid_frame)
                self.grid_layout.addWidget(grid_box, row, col)
                # add the grid box to the row
                row_labels.append(grid_box)
                # add the row to the board
            self.board.append(row_labels)

        # set the size of the grid
        self.grid_frame_width = len(self.word) * (BOX_WIDTH + GAP_SIZE)
        self.grid_frame_height = self.max_guesses * (BOX_HEIGHT + GAP_SIZE)
        self.grid_frame.setFixedSize(self.grid_frame_width, self.grid_frame_height)

        return self.grid_frame

    def create_grid_box(self, parent, text=" "):
        grid_box = QLabel(text, parent)
        grid_box.setAlignment(Qt.AlignCenter)
        grid_box.setObjectName("grid")
        grid_box.setFixedSize(BOX_WIDTH, BOX_HEIGHT)
        return grid_box

    def add_currency_display(self, parent):
        coin_frame = QFrame(parent)
        coin_frame.setObjectName("coinFrame")
        coin_layout = QVBoxLayout(coin_frame)
        coin_layout.setAlignment(Qt.AlignCenter)  # Add alignment to the layout

        currency_logo = QSvgWidget(COIN_PATH)
        currency_logo.setFixedSize(28, 28)
        coin_layout.addWidget(currency_logo)
        coin_layout.addSpacing(4)

        self.currency_value = QLabel(str(currency['value']), coin_frame)
        self.currency_value.setObjectName("currency")
        coin_layout.addWidget(self.currency_value, alignment=Qt.AlignCenter)

        coin_x = self.game_frame.width() // 2 - self.grid_frame.width() // 2 - coin_frame.width() + 20
        coin_y = (self.game_frame.height() - coin_frame.height()) // 3
        coin_frame.move(coin_x, coin_y)

        coin_frame.adjustSize()

        return coin_frame

    def add_powerups(self, parent):
        powerups_frame = QFrame(parent)
        powerups_layout = QVBoxLayout(powerups_frame)
        self.powerup_buttons = {}

        for powerups in [LETTER_ERASER_PATH, INVINCIBLE_PATH, VOWEL_PATH]:

            powerup = QToolButton(powerups_frame,
                cursor=Qt.PointingHandCursor,
                icon=QIcon(powerups),
                objectName="powerupButton",
                iconSize=QSize(ICON_WIDTH, ICON_HEIGHT))

            powerup.clicked.connect(self.on_powerup_clicked)
            powerups_layout.addWidget(powerup)
            powerups_layout.addSpacing(ICON_SPACING)
            self.powerup_buttons[powerups] = powerup

        powerup_x = self.game_frame.width() // 2 + self.grid_frame.width() // 2
        powerup_y = (self.game_frame.height() - powerups_frame.height()) // 4
        powerups_frame.move(powerup_x, powerup_y)
        powerups_frame.adjustSize()

        return powerups_frame
    
    def on_powerup_clicked(self):
        clicked_button = self.sender()
        powerup_actions = {
            self.powerup_buttons[LETTER_ERASER_PATH]: self.check_letter_eraser_powerup,
            self.powerup_buttons[VOWEL_PATH]: self.check_reveal_vowel_powerup,
            self.powerup_buttons[INVINCIBLE_PATH]: self.check_invincible_powerup
        }
        function = powerup_actions.get(clicked_button)
        if function:
            function()

    def check_reveal_vowel_powerup(self):
        if currency['value'] >= 3:
            currency['value'] -= 3
            self.update_currency()
            self.reveal_vowel_powerup()
        else:
            return

    def check_letter_eraser_powerup(self):
        if currency['value'] >= 1:
            currency['value'] -= 1
            self.update_currency()
            self.letter_eraser_powerup()
        else:
            return
        
    def check_invincible_powerup(self):
        if currency['value'] >= 2:
            currency['value'] -= 2
            self.update_currency()
            self.invincible_clicked = True
        else:
            return
        
    def letter_eraser_powerup(self):
        remaining_letters = set(ALPHABET) - set(self.guess_store) - set(self.word)
        if remaining_letters:
            random_char = random.choice(list(remaining_letters))
            self.set_key_color(random_char, "grey")
            self.guess_store += random_char

    def invincible_powerup(self):
        row_labels = []
        for col in range(len(self.word)):
            grid_box = self.create_grid_box(self.grid_frame)
            self.grid_layout.addWidget(grid_box, self.max_guesses, col)
            row_labels.append(grid_box)
        self.board.append(row_labels)
        self.max_guesses += 1
        grid_frame_height = self.max_guesses * (BOX_HEIGHT + GAP_SIZE)
        self.grid_frame.setFixedSize(self.grid_frame_width, grid_frame_height)

    def reveal_vowel_powerup(self):
        remaining_vowels = set(VOWELS) - set(self.guess_store)
        remaining_vowels_in_word = [vowel for vowel in remaining_vowels if vowel in self.word]

        if remaining_vowels_in_word:
            random_char = random.choice(remaining_vowels_in_word)
            self.set_key_color(random_char, "#c9b458")
            self.guess_store += random_char

    def check_guess(self):
        guess = self.guess.lower()
        word = self.word.lower()
        self.guess_store += self.guess

        if self.category.lower() not in ["artists", "countries"]:
            if guess not in DICTIONARY:
                self.highlight_incorrect_guess()
                return
        elif self.category.lower() == "countries":
            if pycountry.countries.get(name=guess) is None:
                self.highlight_incorrect_guess()
                return
        elif self.category.lower() == "artists":
            if guess not in ARTISTSDICT:
                self.highlight_incorrect_guess()
                return
            
        if len(guess) != len(word):
            self.highlight_incorrect_guess()
            return

        word_copy = list(word)
        guess_copy = list(guess)

        for i in range(len(word)):
            if guess[i] == word[i]:
                self.highlight_letter(i, "correct")
                word_copy[word_copy.index(guess[i])] = "-"
                guess_copy[i] = "-"
                self.set_key_color(self.guess[i], "#6aaa64")

        for i in range(len(guess_copy)):
            if guess_copy[i] in word_copy and guess_copy[i] != "-":
                self.highlight_letter(i, "present")
                word_copy[word_copy.index(guess_copy[i])] = "-"
                self.set_key_color(self.guess[i], "#c9b458")
            elif guess_copy[i] != "-":
                self.highlight_letter(i, "absent")
                self.set_key_color(self.guess[i], "grey")

        self.num_guess += 1

        if self.invincible_clicked:
            self.invincible_powerup()
            self.invincible_clicked = False

        if self.num_guess == self.max_guesses:
            self.show_prompt("You failed to guess the word:")
        elif guess == word:
            if self.difficulty != "Easy":
                self.reward_coins()
            
            if self.difficulty != "Easy":
                self.show_prompt("You guessed the word:")
            else:
                self.show_prompt("You guessed the word:\n(No coins are rewarded in Easy mode)")

        self.guess = ""

    def reward_coins(self):
        if  self.difficulty == EXTREME_DIFFICULTY:
            currency['value'] += 10
        elif self.num_guess <= 2:
            currency['value'] += 3
        elif self.num_guess <= 4:
            currency['value'] += 2
        else:
            currency['value'] += 1

        self.update_currency()

    def update_currency(self):
        self.currency_value.setText(str(currency['value']))
        save_currency(currency)

    def show_prompt(self,text="The word is:"):
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(5)

        self.setGraphicsEffect(blur_effect)

        dialog = QDialog()
        dialog.setWindowTitle("ANSWER")
        dialog.setWindowIcon(QIcon(GAME_ICON_PATH))
        dialog.setWindowFlags(Qt.FramelessWindowHint)

        dialog.reject = lambda: None

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        for message, name in [(text, "failPrompt"), (self.word, "answer")]:
            label = QLabel(message)
            label.setObjectName(name)
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)
            layout.addSpacing(10)

        button_layout = QHBoxLayout()
        for button_text, button_method, button_name in [("Try Again", self.try_again, "tgModalButton"), ("Main Menu", self.quit_game, "mmModalButton")]:
            button = self.create_button(button_text, dialog, 130, button_method, button_name)
            button.clicked.connect(dialog.accept)
            button_layout.addWidget(button)

        layout.addLayout(button_layout)
        dialog.setLayout(layout)
        dialog.exec_()

        self.setGraphicsEffect(None)

    def try_again(self):
        self.timer.stop()
        self.stacked_widget.setCurrentWidget(self.game_frame)
        self.stacked_widget.removeWidget(self.game_frame)
        self.get_random_word()
        self.stacked_widget.setCurrentWidget(self.game_frame)      

    def quit_game(self):
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() - 3)
    
    def create_keyboard(self):
        self.keyboard_buttons = {}
        self.keyboard_frame = self.create_frame("keyboardFrame")
        keyboard_layout = QVBoxLayout(self.keyboard_frame)

        for row in KEYBOARD:
            row_layout = QHBoxLayout()
            row_layout.setAlignment(Qt.AlignCenter)

            for key in row:
                button = self.create_key(key)
                row_layout.addWidget(button)
                self.keyboard_buttons[key] = button

            keyboard_layout.addLayout(row_layout)

        return self.keyboard_frame

    def create_key(self, key):
        button = QPushButton(key)
        button.setObjectName("key")
        button.setFixedHeight(KEY_HEIGHT)
        button.setFixedWidth(KEY_WIDTH)

        # add button functionality to backspace and enter keys
        if key == "⌫":
            button.pressed.connect(self.do_backspace)
            button.setFixedWidth(BKSP_WIDTH)
        elif key == "ENTER":
            button.pressed.connect(self.check_guess)
            button.setObjectName("enterButton")
            button.setFixedWidth(ENTER_WIDTH)
        else:
            button.pressed.connect(lambda key=key: self.add_letter(key))

        button.pressed.connect(lambda: self.simulate_key_press(button))

        return button
    
    def simulate_key_press(self, button):
            # make keys appear to be pressed by darkening the color of the key
            current_color = button.palette().button().color().name()
            dark_color = QColor(current_color).darker(125).name()
            button.setStyleSheet(f"background-color: {dark_color}")
            QTimer.singleShot(100, lambda: button.setStyleSheet(f"background-color: {current_color}"))
    
    def set_key_color(self, char, color):
        self.keyboard_buttons[char].setStyleSheet(f"background-color: {color};")

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Escape:
            if self.difficulty == EXTREME_DIFFICULTY:
                self.timer.stop()
            self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() - 1)
            return

        if self.stacked_widget.currentIndex() != 3:
            super().keyPressEvent(event)
            return

        key_func_map = self.key_function_mapping()

        if key in key_func_map:
            func, key_name = key_func_map[key]
            func()
            if key_name is not None: 
                self.simulate_key_press(self.keyboard_buttons[key_name])
        elif event.text().isalpha():
            letter = event.text().upper()
            self.add_letter(letter)
            self.simulate_key_press(self.keyboard_buttons[letter])
        else:
            super().keyPressEvent(event)


    def key_function_mapping(self):
        if self.stacked_widget.currentIndex() == 3:
            return {
                Qt.Key_Return: (self.check_guess, "ENTER"),
                Qt.Key_Backspace: (self.do_backspace, "⌫"),
                Qt.Key_F3: (self.show_prompt, None)
            }

    def play_button_pressed(self):
        if self.stacked_widget.count() < 2:
            self.setup_second_page()
        self.stacked_widget.setCurrentIndex(1) # go to the category page

    def quit_button_pressed(self):
        self.close()

    def cat_buttons_pressed(self):
        self.category = self.sender().text()
        if self.stacked_widget.count() < 3:
            self.setup_third_page()
        self.stacked_widget.setCurrentIndex(2) # go to the difficulty page
            
    def dif_buttons_pressed(self):
        self.difficulty = self.sender().text()
        self.get_grid_row()
        
        if self.stacked_widget.count() > 3:
            self.stacked_widget.removeWidget(self.stacked_widget.widget(3))
        self.get_random_word()
        self.stacked_widget.setCurrentIndex(3) # go to the game page

    def get_random_word(self):
        self.word = random.choice(list(WORDLIST_CAT[self.category.lower()][self.difficulty.lower()])).upper() 
        self.setup_game_page()

    def get_grid_row(self):
        difficulty_levels = {
            "Hard": 4,
            "Extreme": 3
        }
        self.max_guesses = difficulty_levels.get(self.difficulty, 6)

    def add_letter(self, key):
        if len(self.guess) < len(self.word):
            self.board[self.num_guess][len(self.guess)].setText(key)
            self.guess += key

    def do_backspace(self):
        if len(self.guess) > 0:
            self.guess = self.guess[:-1]
            self.board[self.num_guess][len(self.guess)].setText(" ")
    
    def highlight_letter(self, i, type):
        self.board[self.num_guess][i].setStyleSheet(self.set_label_color(LETTER_COLORS[type], "none"))

    def highlight_incorrect_guess(self):
        for i in range(len(self.word)):
            self.board[self.num_guess][i].setStyleSheet(self.set_label_color("#d03939", "none"))
        QTimer.singleShot(DELAY, self.reset_grid)

    def set_label_color(self, color, border):
        return f"QLabel {{font-family: Inter; font-weight: bold; color: black; background-color: {color}; font-size: 48px; border: {border};}}"

    def reset_grid(self):
        for i in range(len(self.word)):
            self.board[self.num_guess][i].setStyleSheet(self.set_label_color("transparent", "2px solid grey"))
            self.do_backspace()
        
    def create_frame(self, object_name):
        frame = QFrame(self.stacked_widget)
        frame.setGeometry(0, 0, self.width(), self.height())
        frame.setObjectName(object_name)
        return frame

    def create_button(self, text, parent, width, function, object_name="button"):
        button = QPushButton(text, parent, objectName=object_name)
        button.setFixedWidth(width)
        button.clicked.connect(function)
        button.setCursor(Qt.PointingHandCursor)
        button.setDefault(True)
        return button

    def create_buttons(self, layout, buttons, parent, function):
        for button_text in buttons:
            button = self.create_button(button_text, parent, BUTTON_FIXED_WIDTH, function)
            if button_text == EXTREME_DIFFICULTY:
                button.setObjectName("extremeButton")
            layout.addWidget(button)
            layout.addSpacing(BUTTON_SPACING)
        parent.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_instance = WordluxeGame()
    game_instance.show()
    sys.exit(app.exec_())
