import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt, QTimer
from config import *
import random

class WordluxeGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(GAME_ICON_PATH))
        self.setWindowTitle("Wordluxe")

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)
        self.showFullScreen()
        self.setup_main_menu_page()

        with open(STYLE_FILE_PATH, "r") as f:
            QApplication.instance().setStyleSheet(f.read())

    def setup_main_menu_page(self):
        main_menu_frame = self.create_frame("mmframe")
        main_layout = QVBoxLayout(main_menu_frame)
        main_layout.setAlignment(Qt.AlignCenter)

        game_logo = QSvgWidget(GAME_LOGO_PATH, main_menu_frame)
        game_logo.setFixedSize(game_logo.sizeHint())
        main_layout.addWidget(game_logo)
        main_layout.addSpacing(MAIN_LAYOUT_SPACING)

        heading = QLabel("The new, and \nimproved wordle!", main_menu_frame)
        heading.setObjectName("heading")
        heading.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(heading)
        main_layout.addSpacing(MAIN_LAYOUT_SPACING)

        main_buttons_layout = QHBoxLayout()
        main_buttons_layout.setAlignment(Qt.AlignCenter)

        for button_text, button_method, button_name in [("Play", self.play_button_pressed, "button"), ("Quit", self.quit_button_pressed, "quitButton")]:
            button = self.create_button(button_text, main_menu_frame, button_method, button_name)
            main_buttons_layout.addWidget(button)
            main_buttons_layout.addSpacing(MAIN_BUTTONS_SPACING)

        main_layout.addLayout(main_buttons_layout)

        self.stacked_widget.addWidget(main_menu_frame)

    def setup_second_page(self):
        self.page_template("cframe", "Choose category", CATEGORY_BUTTONS, self.cat_buttons_pressed)

    def setup_third_page(self):
        self.page_template("dframe", "Choose difficulty", DIFFICULTY_BUTTONS, self.dif_buttons_pressed)

    def setup_game_page(self):
        game_frame = self.create_frame("gframe")
        game_frame.setFixedSize(self.width(), self.height())

        self.board = []
        self.num_guess = 0
        self.guess = ""

        grid_layout = QGridLayout()
        powerups_layout = QVBoxLayout()
        powerups_layout.setAlignment(Qt.AlignTop)

        powerups_frame = QFrame(game_frame)

        for powerups in [LETTER_ERASER_PATH, INVINCIBLE_PATH, VOWEL_PATH]:
            powerup = QSvgWidget(powerups, powerups_frame)
            powerup.setFixedSize(powerup.sizeHint())
            powerups_layout.addWidget(powerup)
            powerups_layout.addSpacing(10)

        powerups_frame.setLayout(powerups_layout)

        grid_frame = QFrame(game_frame)
        grid_frame_width = len(self.word) * (BOX_WIDTH + GAP_SIZE)
        grid_frame_height = self.max_guesses * (BOX_HEIGHT + GAP_SIZE)
        grid_frame.setFixedSize(grid_frame_width, grid_frame_height)

        for i in range(self.max_guesses):
            row_labels = []
            for j in range(len(self.word)):
                grid_label = QLabel(" ")
                grid_label.setAlignment(Qt.AlignCenter)
                grid_label.setObjectName("grid")
                grid_label.setFixedSize(BOX_WIDTH, BOX_HEIGHT)
                row_labels.append(grid_label)
                grid_layout.addWidget(grid_label, i, j)

            self.board.append(row_labels)

        grid_frame.setLayout(grid_layout)

        game_layout = QHBoxLayout(game_frame)
        game_layout.setAlignment(Qt.AlignCenter)
        game_layout.addWidget(grid_frame)
        game_layout.addWidget(powerups_frame)

        game_layout.setAlignment(powerups_frame, Qt.AlignTop)

        game_frame.setLayout(game_layout)

        self.stacked_widget.addWidget(game_frame)

    def page_template(self, frame_name, text, buttons, function):
        frame = self.create_frame(frame_name)
        self.stacked_widget.addWidget(frame)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        label = QLabel(text, frame)
        label.setObjectName("cat_text")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        layout.addSpacing(CAT_DIF_LAYOUT_SPACING)

        self.create_buttons(layout, buttons, frame, function)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex() - 1)
        elif self.stacked_widget.currentIndex() == 3:
            key_function_mapping = {    
                Qt.Key_Return: self.check_guess,
                Qt.Key_Backspace: self.do_backspace,
                Qt.Key_F3: self.show_answer
            }

            if event.key() in key_function_mapping:
                key_function_mapping[event.key()]()
            elif event.text().isalpha():
                self.add_letter(event.text().upper())

    def play_button_pressed(self):
        if self.stacked_widget.count() < 2:
            self.setup_second_page()
        self.stacked_widget.setCurrentIndex(1)

    def quit_button_pressed(self):
        self.close()

    def cat_buttons_pressed(self):
        self.category = self.sender().text()
        if self.stacked_widget.count() < 3:
            self.setup_third_page()
        self.stacked_widget.setCurrentIndex(2)
            
    def dif_buttons_pressed(self):
        self.difficulty = self.sender().text()
        self.get_grid_row()
        if self.stacked_widget.count() > 3:
            self.stacked_widget.removeWidget(self.stacked_widget.widget(3))
        self.get_random_word()
        self.stacked_widget.setCurrentIndex(3)

    def get_grid_row(self):
        difficulty_levels = {
            "Hard": 5,
            "Extreme": 4
        }
        self.max_guesses = difficulty_levels.get(self.difficulty, 6)
       
    def reset_game_state(self):
        self.board = []
        self.num_guess = 0
        self.guess = ""
            
    def add_letter(self, key):
        if len(self.guess) < len(self.word):
            self.board[self.num_guess][len(self.guess)].setText(key)
            self.guess += key

    def do_backspace(self):
        if len(self.guess) > 0:
            self.guess = self.guess[0:-1]
            self.board[self.num_guess][len(self.guess)].setText(" ")

    def show_answer(self):
        QMessageBox.information(self, "ANSWER",f"The correct answer is: {self.word}")
    
    def check_guess(self):
        guess = self.guess.lower()
        word = self.word.lower()

        if guess not in DICTIONARY or len(guess) != len(word):
            self.highlight_incorrect_guess()
            return

        for i in range(len(word)):
            if guess[i] == word[i]:
                self.highlight_letter(i, "correct")
                word = word.replace(guess[i], "-", 1)
                guess = guess.replace(guess[i], "-", 1)
            elif guess[i] in word:
                self.highlight_letter(i, "present")
                word = word.replace(guess[i], "-", 1)
                guess = guess.replace(guess[i], "-", 1)
            else:
                self.highlight_letter(i, "absent")

        if self.num_guess == (self.max_guesses - 1) or word == guess:
            self.show_answer()
        else:
            self.num_guess += 1
            self.guess = ""

    def highlight_letter(self, i, type):
        self.board[self.num_guess][i].setStyleSheet(self.set_label_color(LETTER_COLORS[type], "none"))

    def highlight_incorrect_guess(self):
        for i in range(len(self.word)):
            self.board[self.num_guess][i].setStyleSheet(self.set_label_color("#d03939", "none"))
        QTimer.singleShot(700, self.reset_grid)

    def reset_grid(self):
        for i in range(len(self.word)):
            self.board[self.num_guess][i].setStyleSheet(self.set_label_color("transparent", "2px solid grey"))
            self.do_backspace()
            
    def set_label_color(self, color, border):
        return f"QLabel {{font-family: Inter; font-weight: bold; color: black; background-color: {color}; font-size: 48px; border: {border};}}"

    def get_random_word(self):
        self.word = random.choice(list(WORDLIST_CAT[self.category.lower()][self.difficulty.lower()])).upper() 
        self.setup_game_page()

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
        return button

    def create_buttons(self, layout, buttons, parent, function):
        for button_text in buttons:
            button = self.create_button(button_text, parent, function)
            if button_text == EXTREME_DIFFICULTY:
                button.setObjectName("extremeButton")
            layout.addWidget(button)
            layout.addSpacing(BUTTON_SPACING)
        parent.setLayout(layout)

        parent.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_instance = WordluxeGame()
    game_instance.show()
    sys.exit(app.exec_())