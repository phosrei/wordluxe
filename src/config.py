from nltk.corpus import words
from wordbank import categories

DICTIONARY = set(words.words())
CATEGORY = None
DIFFICULTY = None

# Wordbank categories
WORDBANK_CAT = {
    "general": categories["general"],
    "countries": categories["countries"],
    "animals": categories["animals"],
    "fruits": categories["fruits"],
    "sports": categories["sports"],
    "artists": categories["artists"],
    "songs": categories["songs"]
}

# Grid and tiles
GRID_ROWS = 6
GRID_COLUMNS = 5
GRID_FRAME_WIDTH = 500
GRID_FRAME_HEIGHT = 700
BOX_WIDTH = 80
BOX_HEIGHT = 80

# Button names
CATEGORY_BUTTONS = ["General", "Countries", "Fruits", "Sports", "Animals", "Artists", "Songs"]
DIFFICULTY_BUTTONS = ["Easy", "Normal", "Hard", "Extreme"]

# Button dimensions and spacing
BUTTON_FIXED_WIDTH = 260
BUTTON_SPACING = 15
WIDTH = 240
MAIN_BUTTONS_SPACING = 30

# Layout spacing
MAIN_LAYOUT_SPACING = 60
CAT_DIF_LAYOUT_SPACING = 30

# File paths
GAME_ICON_PATH = "assets/game_icon.ico"
GAME_LOGO_PATH = "assets/game_logo.svg"
STYLE_FILE_PATH = 'style.qss'

# Others
EXTREME_DIFFICULTY = "Extreme"
SETUP_PAGES = ["setup_main_menu_page", "setup_second_page", "setup_third_page", "setup_game_page"]