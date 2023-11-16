from nltk.corpus import words
from wordlist import categories

DICTIONARY = set(words.words())
CATEGORY = None
DIFFICULTY = None

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

# Grid and tiles
GAP_SIZE = 10
GRID_ROWS = 6
GRID_COLUMNS = 5
GRID_FRAME_WIDTH = 500
GRID_FRAME_HEIGHT = 700
BOX_WIDTH = 80
BOX_HEIGHT = 80

# Button names
CATEGORY_BUTTONS = ["General", "Countries", "Fruits", "Sports", "Animals", "Artists", "Songs"]
DIFFICULTY_BUTTONS = ["Easy", "Normal", "Hard", "Extreme"]

# Button dimensions
BUTTON_FIXED_WIDTH = 260
WIDTH = 240
MAIN_BUTTONS_SPACING = 30

# Spacing
BUTTON_SPACING = 15
MAIN_LAYOUT_SPACING = 60
CAT_DIF_LAYOUT_SPACING = 30
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
INDEX_THREE = 3