import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt
class WordluxeGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wordluxe")
        self.showFullScreen()

        self.stacked_widget = QStackedWidget(self)
        self.setup_ui()
        self.setCentralWidget(self.stacked_widget)

        with open('src/style.qss', 'r') as f:
            self.stylesheet = f.read()

        QApplication.instance().setStyleSheet(self.stylesheet)

    def setup_ui(self):
        self.setup_main_menu_page()
        self.setup_second_page()

    def setup_main_menu_page(self):
        main_menu_frame = QFrame(self.stacked_widget)
        main_menu_frame.setGeometry(0, 0, self.width(), self.height())
        main_menu_frame.setObjectName("mmframe")

        game_logo = QSvgWidget("assets/game_logo.svg", parent=main_menu_frame)
        game_logo.resize(game_logo.renderer().defaultSize())
        game_logo.move((main_menu_frame.width() - game_logo.width()) // 2, 300)

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
        button_layout.addSpacerItem(QSpacerItem(30, 30))
        button_layout.addWidget(quit_button)
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setContentsMargins(0, int(self.height() * 0.1), 0, 0)
        main_menu_frame.setLayout(button_layout)

        self.stacked_widget.addWidget(main_menu_frame)

    def setup_second_page(self):
        gencat_frame = QFrame(self.stacked_widget)
        gencat_frame.setGeometry(0, 0, self.width(), self.height())
        gencat_frame.setObjectName("gcframe")

        button_names = ["General", "Countries", "Fruits", "Sports", "Animals", "Artists", "Songs"]

        self.create_buttons(button_names, gencat_frame, 250)
        self.stacked_widget.addWidget(gencat_frame)

    def create_buttons(self, names, parent_frame, left_margin):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignVCenter)

        for name in names:
            button = QPushButton(name, parent_frame)
            button.setFixedWidth(240)
            button.setCursor(Qt.PointingHandCursor)
            button.setObjectName("button")
            layout.addWidget(button)
            layout.addSpacing(15)

        layout.setContentsMargins(left_margin, 0, 0, 0)

        parent_frame.setLayout(layout)
        self.setWindowIcon(QIcon("assets/game_icon.ico"))

    def play_button_pressed(self):
        self.stacked_widget.setCurrentIndex(1)

    def quit_button_pressed(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_instance = WordluxeGame()
    game_instance.show()
    sys.exit(app.exec_())
