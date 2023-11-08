import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt

class WordluxeGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wordluxe")
        screen_res = QApplication.desktop().screenGeometry()
        window_width = screen_res.width()
        window_height = screen_res.height()
        self.setGeometry(0, 0, window_width, window_height)
        self.setWindowFlags(Qt.FramelessWindowHint)

        bg_image = QImage("assets/background1.png")
        bg_label = QLabel(self)
        bg_label.setPixmap(QPixmap.fromImage(bg_image))
        bg_label.setGeometry(0, 0, 1920, 1080)
        bg_label.move(0, 0)

        font = QFont("Inter", 20)

        frame = QFrame(self)
        frame.setGeometry(480, 200, 960, 680)

        game_logo = QLabel(frame)
        logo_pixmap = QPixmap("assets/game_logo.svg")
        game_logo.setPixmap(logo_pixmap)

        logo_width = logo_pixmap.width()
        logo_height = logo_pixmap.height()

        center_x = (frame.width() - logo_width) // 2
        center_y = (frame.height() - logo_height) // 2

        game_logo.setGeometry(center_x, 50, logo_width, logo_height)

        button_layout = QHBoxLayout()

        # Play button
        play_button = QPushButton("Play", frame)
        play_button.setFont(font)
        play_button.setFixedWidth(240)
        play_button.clicked.connect(self.play_button_pressed)
        play_button.setCursor(Qt.PointingHandCursor)

        play_button.setStyleSheet("border-radius: 32px;"
            "background-color: #fff;"
            "padding: 20px;" 
            "font-size: 20px"
        )

        # Quit button
        quit_button = QPushButton("Quit", frame)
        quit_button.setFont(font)
        quit_button.setFixedWidth(240)
        quit_button.clicked.connect(self.quit_button_pressed)
        quit_button.setCursor(Qt.PointingHandCursor)

        quit_button.setStyleSheet(
            "border: 2px solid white;"
            "border-radius: 32px;"
            "background-color: transparent;"
            "color: white;"
            "padding: 20px;"
            "font-size: 20px"
        )
        spacer = QSpacerItem(20, 20)

        button_layout.addWidget(play_button)
        button_layout.addItem(spacer)
        button_layout.addWidget(quit_button)

        frame.setLayout(button_layout)

        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setContentsMargins(0, center_y + logo_height + 20, 0, 0)

        self.setWindowIcon(QIcon("assets/game_icon.ico"))

    def play_button_pressed(self):
        pass  # Add code here

    def quit_button_pressed(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_instance = WordluxeGame()
    game_instance.show()
    sys.exit(app.exec_())
