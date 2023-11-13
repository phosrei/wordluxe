import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt

class WordluxeGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("assets/game_icon.ico"))
        self.setWindowTitle("Wordluxe")

        self.stacked_widget = QStackedWidget(self)
        self.setup_ui()
        self.setCentralWidget(self.stacked_widget)

        with open('src/style.qss', 'r') as f:
            self.stylesheet = f.read()

        QApplication.instance().setStyleSheet(self.stylesheet)

        self.showFullScreen()

    def setup_ui(self):
        self.setup_main_menu_page()
        self.setup_second_page()

    def setup_main_menu_page(self):
        main_menu_frame = QFrame(self.stacked_widget)
        main_menu_frame.setGeometry(0, 0, self.width(), self.height())
        main_menu_frame.setObjectName("mmframe")

        main_layout = QVBoxLayout(main_menu_frame)
        main_layout.setAlignment(Qt.AlignCenter)

        game_logo = QSvgWidget("assets/game_logo.svg", main_menu_frame)
        game_logo.setFixedSize(game_logo.sizeHint())

        play_button = QPushButton("Play", main_menu_frame, objectName="button")
        play_button.setFixedWidth(240)
        play_button.clicked.connect(self.play_button_pressed)
        play_button.setCursor(Qt.PointingHandCursor)

        quit_button = QPushButton("Quit", main_menu_frame, objectName="quitButton")
        quit_button.setFixedWidth(240)
        quit_button.clicked.connect(self.quit_button_pressed)
        quit_button.setCursor(Qt.PointingHandCursor)

        button_layout = QHBoxLayout()
        button_layout.addWidget(play_button)
        button_layout.addSpacing(30)
        button_layout.addWidget(quit_button)
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setContentsMargins(0, int(self.height() * .3), 0, 0)

        main_layout.addWidget(game_logo)
        main_layout.addLayout(button_layout)

        self.stacked_widget.addWidget(main_menu_frame)

    def setup_second_page(self):
        gen_frame = QFrame(self.stacked_widget)
        gen_frame.setGeometry(0, 0, self.width(), self.height())
        gen_frame.setObjectName("gframe")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        text_label = QLabel("Choose category", gen_frame)
        text_label.setObjectName("cat_text")
        text_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(text_label)
        layout.addSpacing(50)

        cat_buttons = ["General", "Countries", "Fruits", "Sports", "Animals", "Artists", "Songs"]

        self.create_buttons(layout, cat_buttons , gen_frame)
        self.stacked_widget.addWidget(gen_frame)

    def setup_third_page(self):
        gen_frame = QFrame(self.stacked_widget)
        gen_frame.setGeometry(0, 0, self.width(), self.height())
        gen_frame.setObjectName("dframe")

    def create_buttons(self, layout, buttons, parent_frame):
        for button in buttons:
            button = QPushButton(button, parent_frame)
            button.setFixedWidth(260)
            button.setCursor(Qt.PointingHandCursor)
            button.setObjectName("button")
            layout.addWidget(button)
            layout.addSpacing(15)

        parent_frame.setLayout(layout)

    def play_button_pressed(self):
        self.stacked_widget.setCurrentIndex(1)

    def quit_button_pressed(self):
        self.close()
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_instance = WordluxeGame()
    game_instance.show()
    sys.exit(app.exec_())
