import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt, QTimer, QSize
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from config import *
import random

class WordluxeGame(QMainWindow):
    # initialize the game
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wordluxe")
        self.setWindowIcon(QIcon(GAME_ICON_PATH))

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)
        self.showFullScreen()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_timeout)

        self.timer_label = QLabel(self)
        self.timer_label.setObjectName("timerLabel")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_timeout)

        self.timer_label = QLabel(self)
        self.timer_label.setObjectName("timerLabel")

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
            button = self.create_button(button_text, main_menu_frame, button_method, button_name)
            main_buttons_layout.addWidget(button)
            main_buttons_layout.addSpacing(MAIN_BUTTONS_SPACING)

        main_layout.addLayout(main_buttons_layout)

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
        # create the game frame
        game_frame = self.create_frame("gframe")
        game_layout = QVBoxLayout(game_frame)
        game_layout.setAlignment(Qt.AlignCenter)
        game_frame.setLayout(game_layout)

        if self.difficulty.lower() == "extreme":
            self.timer_label = QLabel("03:00", game_frame)
            self.timer_label.setObjectName("timerLabel")
            self.timer_label.setFixedSize(200, 100)
            self.timer_label.setAlignment(Qt.AlignCenter)
            self.timer_label.setStyleSheet("QLabel { font-size: 60px; }")

            # set the position of the timer label
            timer_label_x = game_frame.width() // 2 - self.timer_label.width() // 2
            timer_label_y = 150
            self.timer_label.move(timer_label_x, timer_label_y)

        # create the grid and add to the game frame 
        grid_frame = self.create_grid()
        game_layout.addWidget(grid_frame, alignment=Qt.AlignCenter)
        # create an on-screen keyboard
        keyboard_frame = QFrame()
        keyboard_layout = self.create_keyboard_layout()
        keyboard_frame.setLayout(keyboard_layout)
        game_layout.addWidget(keyboard_frame, alignment=Qt.AlignCenter)
        # add powerups to the side of the grid
        if self.difficulty.lower() != "extreme":
            powerups_frame = self.create_powerups_frame(game_frame)
            powerup_x = game_frame.width() // 2 + grid_frame.width() // 2
            powerup_y = (game_frame.height() - powerups_frame.height()) // 3
            powerups_frame.move(powerup_x, powerup_y)

        self.stacked_widget.addWidget(game_frame)

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

    def create_powerups_frame(self, parent):
        powerups_frame = QFrame(parent)
        powerups_layout = QVBoxLayout()
        powerups_frame.setLayout(powerups_layout)
        self.powerup_buttons = {}  # Store the powerup buttons
        for powerups in [LETTER_ERASER_PATH, INVINCIBLE_PATH, VOWEL_PATH]:
            powerup = QToolButton(powerups_frame)
            powerup.setCursor(Qt.PointingHandCursor)
            powerup.setIcon(QIcon(powerups))
            powerup.setObjectName("powerupButton")
            powerup.setIconSize(QSize(ICON_WIDTH, ICON_HEIGHT))
            powerup.clicked.connect(self.on_powerup_clicked)
            powerups_layout.addWidget(powerup)
            powerups_layout.addSpacing(ICON_SPACING)
            self.powerup_buttons[powerups] = powerup  # Add the button to the dictionary
        powerups_frame.adjustSize()

        return powerups_frame
    
    def on_powerup_clicked(self):
        clicked_button = self.sender()
        powerup_actions = {
            LETTER_ERASER_PATH: self.letter_eraser,
            INVINCIBLE_PATH: self.invincible,
            VOWEL_PATH: self.reveal_vowel
        }
        for powerup_path, button in self.powerup_buttons.items():
            if clicked_button is button:
                if powerup_path == INVINCIBLE_PATH:
                    self.invincible_clicked = True
                else:
                    powerup_actions[powerup_path]()

    def letter_eraser(self):
        remaining_letters = set(ALPHABET) - set(self.guess_store) - set(self.word)
        if remaining_letters:
            random_char = random.choice(list(remaining_letters))
            self.set_key_color(random_char, "grey")
            self.guess_store += random_char

    def invincible(self):
        row_labels = []
        for col in range(len(self.word)):
            grid_box = self.create_grid_box(self.grid_frame)
            self.grid_layout.addWidget(grid_box, self.max_guesses, col)
            row_labels.append(grid_box)
        self.board.append(row_labels)
        self.max_guesses += 1
        grid_frame_height = self.max_guesses * (BOX_HEIGHT + GAP_SIZE)
        self.grid_frame.setFixedSize(self.grid_frame_width, grid_frame_height)

    def reveal_vowel(self):
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

        if guess not in DICTIONARY or len(guess) != len(word):
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

        if self.num_guess == (self.max_guesses - 1) or word == guess:
            self.show_answer()
        elif self.invincible_clicked:
            self.invincible_clicked = False
            self.invincible()
        self.num_guess += 1
        self.guess = ""


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
    
    def create_keyboard_layout(self):
        self.keyboard_buttons = {}
        keyboard_layout = QVBoxLayout()

        for row in KEYBOARD:
            row_layout = QHBoxLayout()
            row_layout.setAlignment(Qt.AlignCenter)

            for key in row:
                button = self.create_key(key)
                row_layout.addWidget(button)
                self.keyboard_buttons[key] = button

            keyboard_layout.addLayout(row_layout)

        return keyboard_layout

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
                Qt.Key_F3: (self.show_answer, None)
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

        if self.difficulty == EXTREME_DIFFICULTY:
            self.start_timer()
        
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

    def start_timer(self):
        self.remaining_time = 180  # 3 minutes in seconds
        self.timer.start(1000)  # Timer updates every 1 second
        self.update_timer_label()

    def update_timer_label(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.timer_label.setText(f"{minutes:02d}:{seconds:02d}")

    def timer_timeout(self):
        self.remaining_time -= 1
        self.update_timer_label()

        if self.remaining_time <= 0:
            self.timer.stop()
            self.show_answer()
       
    def reset_game_state(self):
        # initalizes the game state back to the default
        self.board = []
        self.num_guess = 0
        self.guess = ""        

    def add_letter(self, key):
        if len(self.guess) < len(self.word):
            self.board[self.num_guess][len(self.guess)].setText(key)
            self.guess += key

    def do_backspace(self):
        if len(self.guess) > 0:
            self.guess = self.guess[:-1]
            self.board[self.num_guess][len(self.guess)].setText(" ")

    def show_answer(self):
        QMessageBox.information(self, "ANSWER",f"The correct answer is: {self.word}")
    
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

    def create_button(self, text, parent, function, object_name="button"):
        button = QPushButton(text, parent, objectName=object_name)
        button.setFixedWidth(BUTTON_FIXED_WIDTH)
        button.clicked.connect(function)
        button.setCursor(Qt.PointingHandCursor)
        button.setDefault(True)
        return button

    def create_buttons(self, layout, buttons, parent, function):
        for button_text in buttons:
            button = self.create_button(button_text, parent, function)
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
