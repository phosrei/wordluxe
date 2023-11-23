from nltk.corpus import words
from wordlist import categories
import string

# Dictionary
DICTIONARY = set(words.words())

# Dictionary mapping
WORDLIST_CAT = {
    "general": categories["general"],
    "countries": categories["countries"],
    "animals": categories["animals"],
    "fruits": categories["fruits"],
    "sports": categories["sports"],
    "artists": categories["artists"],
    "songs": categories["songs"]
}

# Keyboard
KEY_WIDTH = 60
KEY_HEIGHT = 80
ENTER_WIDTH = 90
BKSP_WIDTH = 90
KEYBOARD = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
    ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "⌫"]
]

# Colors
LETTER_COLORS = {
    "correct": "#6aaa64",
    "present": "#c9b458",
    "absent": "grey",
}

# Grid and tiles
GAP_SIZE = 10
GRID_FRAME_WIDTH = 500
GRID_FRAME_HEIGHT = 700
BOX_WIDTH = 80
BOX_HEIGHT = 80

# Button names
CATEGORY_BUTTONS = ["General", "Countries", "Fruits", "Sports", "Animals", "Artists", "Songs"]
DIFFICULTY_BUTTONS = ["Easy", "Normal", "Hard", "Extreme"]

# Button dimensions
BUTTON_FIXED_WIDTH = 260
MAIN_BUTTONS_SPACING = 30

# Spacing
BUTTON_SPACING = 15
HEADING_SPACING = 60
ICON_SPACING = 10

# File paths
GAME_ICON_PATH = "assets/game_icon.ico"
GAME_LOGO_PATH = "assets/game_logo.svg"
LETTER_ERASER_PATH = "assets/letter_eraser.svg"
INVINCIBLE_PATH = "assets/invincible.svg"
VOWEL_PATH = "assets/vowel.svg"
STYLE_FILE_PATH = 'style.qss'


# Powerup dimensions
POWERUP_WIDTH = 60
POWERUP_HEIGHT = 60

# Others
VOWELS = 'AEIUO'
ALPHABET = string.ascii_uppercase
EXTREME_DIFFICULTY = "Extreme"
TOP_SPACING = 140
BOTTOM_SPACING = 40
DELAY = 700

# Icons
ICON_WIDTH = 60
ICON_HEIGHT = 60