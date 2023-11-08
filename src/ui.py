import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt

class GamePage(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-image: url(assets/background1.png);")

        layout = QVBoxLayout()
        label = QLabel("This is the Second Page")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)


class SecondPage(QWidget):
    def __init__(self):
        super().__init__()

class WordluxeGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wordluxe")
        window_width = QApplication.desktop().screenGeometry().width()
        window_height = QApplication.desktop().screenGeometry().height()
        self.setGeometry(0, 0, window_width, window_height)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.stacked_widget = QStackedWidget(self)

        # Main Menu Page
        main_menu_frame = QFrame(self.stacked_widget)
        main_menu_frame.setGeometry(0, 0, window_width, window_height)
        main_menu_frame.setObjectName("mmframe")

        with open('src/style.qss', 'r') as f:
            stylesheet = f.read()
            main_menu_frame.setStyleSheet(stylesheet)

        game_logo = QSvgWidget("assets/game_logo.svg", parent=main_menu_frame)
        game_logo.setFixedSize(game_logo.renderer().defaultSize())
        game_logo.move((main_menu_frame.width() - game_logo.width()) // 2, 50)

        play_button = QPushButton("Play", main_menu_frame, objectName="playButton")
        play_button.setFixedWidth(240)
        play_button.clicked.connect(self.play_button_pressed)
        play_button.setCursor(Qt.PointingHandCursor)

        quit_button = QPushButton("Quit", main_menu_frame, objectName="quitButton")
        quit_button.setFixedWidth(240)
        quit_button.clicked.connect(self.quit_button_pressed)
        quit_button.setCursor(Qt.PointingHandCursor)

        button_layout = QHBoxLayout()
        button_layout.addWidget(play_button)
        button_layout.addSpacerItem(QSpacerItem(30, 30))
        button_layout.addWidget(quit_button)
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setContentsMargins(0, 300, 0, 0)
        main_menu_frame.setLayout(button_layout)

        # Game Page
        game_page = GamePage()
        self.stacked_widget.addWidget(main_menu_frame)
        self.stacked_widget.addWidget(game_page)

        # Second Page
        second_page = SecondPage()
        second_page.setObjectName("secondpage")  # Set an object name for the second page
        self.stacked_widget.addWidget(second_page)

        self.setCentralWidget(self.stacked_widget)

        self.setWindowIcon(QIcon("assets/game_icon.ico"))

    def play_button_pressed(self):
        self.stacked_widget.setCurrentIndex(1)  # Show the second page

    def quit_button_pressed(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_instance = WordluxeGame()
    game_instance.show()
    sys.exit(app.exec_())
