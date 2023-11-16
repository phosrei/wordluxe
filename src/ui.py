import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt
from config import *
import pycountry
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

        with open(STYLE_FILE_PATH, 'r') as f:
            self.stylesheet = f.read()

        QApplication.instance().setStyleSheet(self.stylesheet)

    def setup_main_menu_page(self):
        main_menu_frame = self.create_frame("mmframe")
        main_layout = QVBoxLayout(main_menu_frame)
        main_layout.setAlignment(Qt.AlignCenter)

        game_logo = QSvgWidget(GAME_LOGO_PATH, main_menu_frame)
        game_logo.setFixedSize(game_logo.sizeHint())

        main_buttons_layout = QHBoxLayout()

        play_button = self.create_button("Play", main_menu_frame, self.play_button_pressed)
        main_buttons_layout.addWidget(play_button)

        main_buttons_layout.addSpacing(MAIN_BUTTONS_SPACING)
        
        quit_button = self.create_button("Quit", main_menu_frame, self.quit_button_pressed, "quitButton")
        main_buttons_layout.addWidget(quit_button)

        main_buttons_layout.setAlignment(Qt.AlignCenter)

        heading = QLabel("The new, and \nimproved wordle!", main_menu_frame)
        heading.setObjectName("heading")
        heading.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(game_logo)
        main_layout.addSpacing(MAIN_LAYOUT_SPACING) 
        main_layout.addWidget(heading)
        main_layout.addSpacing(MAIN_LAYOUT_SPACING)
        main_layout.addLayout(main_buttons_layout)

        self.stacked_widget.addWidget(main_menu_frame)

    def setup_second_page(self):
        self.setup_category_difficulty_page("cframe", "Choose category", CATEGORY_BUTTONS, self.cat_buttons_pressed)

    def setup_third_page(self):
        self.setup_category_difficulty_page("dframe", "Choose difficulty", DIFFICULTY_BUTTONS, self.dif_buttons_pressed)

    def setup_category_difficulty_page(self, frame_name, text, buttons, function):
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

    def setup_game_page(self):
        game_frame = self.create_frame("gframe")

        self.board = []
        self.num_guess = 0
        self.guess = ''

        grid_layout = QGridLayout()
        
        grid_frame = QFrame(game_frame)
        grid_frame_width = len(self.word) * (BOX_WIDTH + GAP_SIZE)
        grid_frame_height = GRID_ROWS * (BOX_HEIGHT + GAP_SIZE)
        grid_frame.setFixedSize(grid_frame_width, grid_frame_height)

        for i in range(GRID_ROWS):
            row_labels = []
            for j in range(len(self.word)):
                grid_label = QLabel(' ')
                grid_label.setAlignment(Qt.AlignCenter)
                grid_label.setObjectName("grid")
                grid_label.setFixedSize(BOX_WIDTH, BOX_HEIGHT)
                row_labels.append(grid_label)
                grid_layout.addWidget(grid_label, i, j)

            self.board.append(row_labels)

        grid_frame.setLayout(grid_layout)
        game_layout = QVBoxLayout(game_frame)
        game_layout.setAlignment(Qt.AlignCenter)
        game_layout.addWidget(grid_frame)

        self.stacked_widget.addWidget(game_frame)
        
    def keyPressEvent(self, event):
        if self.stacked_widget.currentIndex() == 3:
            key_function_mapping = {
                Qt.Key_Escape: self.close,
                Qt.Key_Return: self.validate,
                Qt.Key_Backspace: self.do_backspace,
                Qt.Key_F3: self.show_answer
            }

            if event.key() in key_function_mapping:
                key_function_mapping[event.key()]()
            elif event.text().isalpha():
                self.add_letter(event.text().upper())
            
    def add_letter(self, key):
        if len(self.guess) < len(self.word):
            self.board[self.num_guess][len(self.guess)].setText(key)
            self.guess += key

    def do_backspace(self):
        if len(self.guess) > 0:
            self.guess = self.guess[0:-1]
            self.board[self.num_guess][len(self.guess)].setText(' ')

    def show_answer(self):
        QMessageBox.information(self, 'ANSWER',f'The correct answer is: {self.word}')

    def validate(self):
        guess_lower = self.guess.lower()
        if guess_lower not in DICTIONARY:
            for _ in range(len(self.word)):
                self.do_backspace()
        else:
            self.check_guess()
            
    def check_guess(self):
        word_length = len(self.word)
        guess_length = len(self.guess)
        output = ["-"] * word_length
        word = self.word

        if guess_length == word_length:
            for i in range(word_length):
                if self.guess[i] == word[i]:
                    self.board[self.num_guess][i].setStyleSheet('QLabel {font-family: Inter; font-weight: bold; color: black; background-color: #6aaa64; font-size: 48px}')
                    output[i] = self.guess[i]
                    word = word.replace(self.guess[i], "-", 1)

            for i in range(word_length):
                if self.guess[i] in word and output[i] == "-":
                    self.board[self.num_guess][i].setStyleSheet('QLabel {font-family: Inter; font-weight: bold; color: black; background-color: #c9b458; font-size: 48px}')
                    output[i] = self.guess[i]
                    word = word.replace(self.guess[i], "-", 1)
                elif self.guess[i] in output[i]:
                    continue
                else:
                    self.board[self.num_guess][i].setStyleSheet('QLabel {font-family: Inter; font-weight: bold; color: black; background-color: grey; font-size: 48px}')
                    output[i] = (self.guess[i])
        
            if self.num_guess == 5 or self.word == self.guess:
                self.show_answer()
            else:
                self.num_guess += 1
                self.guess = ''            
        else:
            for _ in range(guess_length):
                self.do_backspace()

    def create_buttons(self, layout, buttons, parent, function):
        for button in buttons:
            button = self.create_button(button, parent, function)
            if button.text() == EXTREME_DIFFICULTY:
                button.setObjectName("extremeButton")
            layout.addWidget(button)
            layout.addSpacing(BUTTON_SPACING)

        parent.setLayout(layout)

    def play_button_pressed(self):
        self.setup_second_page()
        self.stacked_widget.setCurrentIndex(1)

    def cat_buttons_pressed(self):
        global CATEGORY
        CATEGORY = self.sender().text()
        self.setup_third_page()
        self.stacked_widget.setCurrentIndex(2)
        
    def dif_buttons_pressed(self):
        global DIFFICULTY
        DIFFICULTY = self.sender().text()
        self.load_word_bank()
        self.stacked_widget.setCurrentIndex(3)

    def load_word_bank(self):
        if CATEGORY and DIFFICULTY:
            self.word = random.choice(list(WORDLIST_CAT[CATEGORY.lower()][DIFFICULTY.lower()])).upper()
            self.setup_game_page()
            
    def quit_button_pressed(self):
        self.close()

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
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_instance = WordluxeGame()
    game_instance.show()
    sys.exit(app.exec_())