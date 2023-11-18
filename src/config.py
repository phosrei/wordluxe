from nltk.corpus import words
from wordlist import categories

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
KEYBOARD = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
    ["Z", "X", "C", "V", "B", "N", "M"]
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

# Others
EXTREME_DIFFICULTY = "Extreme"
DELAY = 700

# Powerup dimensions
POWERUP_WIDTH = 70
POWERUP_HEIGHT = 70