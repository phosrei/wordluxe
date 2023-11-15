import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt
from constants import *
import random

class WordluxeGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(GAME_ICON_PATH))
        self.setWindowTitle("Wordluxe")

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)
        self.showFullScreen()
        self.setup_ui()

        with open(STYLE_FILE_PATH, 'r') as f:
            self.stylesheet = f.read()

        QApplication.instance().setStyleSheet(self.stylesheet)

    def setup_ui(self):
        self.setup_main_menu_page()
        self.setup_second_page()
        self.setup_third_page()
        self.setup_game_page()

    def setup_main_menu_page(self):
        main_menu_frame = QFrame(self.stacked_widget)
        main_menu_frame.setGeometry(0, 0, self.width(), self.height())
        main_menu_frame.setObjectName("mmframe")

        main_layout = QVBoxLayout(main_menu_frame)
        main_layout.setAlignment(Qt.AlignCenter)

        game_logo = QSvgWidget(GAME_LOGO_PATH, main_menu_frame)
        game_logo.setFixedSize(game_logo.sizeHint())

        main_buttons_layout = QHBoxLayout()

        play_button = QPushButton("Play", main_menu_frame, objectName="button")
        play_button.setFixedWidth(BUTTON_FIXED_WIDTH)
        play_button.clicked.connect(self.play_button_pressed)
        play_button.setCursor(Qt.PointingHandCursor)
        main_buttons_layout.addWidget(play_button)

        main_buttons_layout.addSpacing(MAIN_BUTTONS_SPACING)
        
        quit_button = QPushButton("Quit", main_menu_frame, objectName="quitButton")
        quit_button.setFixedWidth(BUTTON_FIXED_WIDTH)
        quit_button.clicked.connect(self.quit_button_pressed)
        quit_button.setCursor(Qt.PointingHandCursor)
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
        cat_frame = QFrame(self.stacked_widget)
        self.stacked_widget.addWidget(cat_frame)
        cat_frame.setGeometry(0, 0, self.width(), self.height())
        cat_frame.setObjectName("cframe")

        cat_layout = QVBoxLayout()
        cat_layout.setAlignment(Qt.AlignCenter)

        cat_text = QLabel("Choose category", cat_frame)
        cat_text.setObjectName("cat_text")
        cat_text.setAlignment(Qt.AlignCenter)
        cat_layout.addWidget(cat_text)
        cat_layout.addSpacing(CAT_DIF_LAYOUT_SPACING)

        self.create_buttons(cat_layout, CATEGORY_BUTTONS, cat_frame, self.cat_buttons_pressed)

    def setup_third_page(self):
        dif_frame = QFrame(self.stacked_widget)
        self.stacked_widget.addWidget(dif_frame)
        dif_frame.setGeometry(0, 0, self.width(), self.height())
        dif_frame.setObjectName("dframe")

        dif_layout = QVBoxLayout()
        dif_layout.setAlignment(Qt.AlignCenter)

        dif_text = QLabel("Choose difficulty", dif_frame)
        dif_text.setObjectName("cat_text")
        dif_text.setAlignment(Qt.AlignCenter)
        dif_layout.addWidget(dif_text)
        dif_layout.addSpacing(CAT_DIF_LAYOUT_SPACING)

        self.create_buttons(dif_layout, DIFFICULTY_BUTTONS, dif_frame, self.dif_buttons_pressed)

    def setup_game_page(self):
        game_frame = QFrame(self.stacked_widget)
        self.stacked_widget.addWidget(game_frame)
        game_frame.setGeometry(0, 0, self.width(), self.height())
        game_frame.setObjectName("gframe")

        self.board = []
        self.num_guess = 0
        self.guess = ''

        grid_layout = QGridLayout()
        
        grid_frame = QFrame(game_frame)
        grid_frame.setFixedSize(GRID_FRAME_WIDTH, GRID_FRAME_HEIGHT)

        for i in range(GRID_ROWS):
            row_labels = []
            for j in range(GRID_COLUMNS):
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
        
    def keyPressEvent(self, event):
        print("Key pressed:", event.key())

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
        if len(self.guess) < 5:
            self.board[self.num_guess][len(self.guess)].setText(key)
            self.guess += key

    def do_backspace(self):
        if len(self.guess) > 0:
            self.guess = self.guess[0:-1]
            self.board[self.num_guess][len(self.guess)].setText(' ')

    def show_answer(self):
        QMessageBox.information(self, 'Answer', self.word)

    def validate(self):
        guess_lower = self.guess.lower()
        if guess_lower not in DICTIONARY:
            for _ in range(5):
                self.do_backspace()
        else:
            self.check_guess()
    def check_guess(self):
        length = len(self.word)
        output = ["-"] * length
        word = self.word

        for i in range(length):
            if self.guess[i] == word[i]:
                self.board[self.num_guess][i].setStyleSheet('QLabel {font-family: Inter; font-weight: bold; color: black; background-color: #6aaa64; font-size: 48px}')
                output[i] = self.guess[i]
                word = word.replace(self.guess[i], "-", 1)

        for i in range(length):
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

    def load_word(self, fname):
        with open(fname, 'r') as f:
            self.words = list(map(str.strip, f.read().split('\n')))

    def create_buttons(self, layout, buttons, parent, function):
        for button in buttons:
            button = QPushButton(button, parent)
            button.setFixedWidth(BUTTON_FIXED_WIDTH)
            button.setCursor(Qt.PointingHandCursor)
            button.clicked.connect(lambda _, text=button: function(text))

            if button.text() == EXTREME_DIFFICULTY:
                button.setObjectName("extremeButton")
            else:
                button.setObjectName("button")
            layout.addWidget(button)
            layout.addSpacing(BUTTON_SPACING)

        parent.setLayout(layout)

    def play_button_pressed(self):
        self.stacked_widget.setCurrentIndex(1)

    def cat_buttons_pressed(self, category):
        self.stacked_widget.setCurrentIndex(2)
        global CATEGORY
        CATEGORY = category.text()
        self.load_word_bank()
        
    def dif_buttons_pressed(self, difficulty):
        self.stacked_widget.setCurrentIndex(3)
        global DIFFICULTY
        DIFFICULTY = difficulty.text()
        self.load_word_bank()

    def load_word_bank(self):
        if CATEGORY and DIFFICULTY:
            self.words = WORDBANK_CAT[CATEGORY.lower()][DIFFICULTY.lower()]
            self.word = random.choice(list(self.words)).upper()
            
    def quit_button_pressed(self):
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_instance = WordluxeGame()
    game_instance.show()
    sys.exit(app.exec_())
