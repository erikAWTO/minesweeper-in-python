SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

MIN_ROWS = 2
MIN_COLUMNS = 2
MIN_MINES = 2
MAX_ROWS = 12
MAX_COLUMNS = 12
MAX_MINES = 64

# Define variables for the default values of the input fields
DEFAULT_ROWS = 8
DEFAULT_COLUMNS = 8
DEFAULT_MINES = 10

@staticmethod
def screen_width_prcnt(percentage):
    return int(SCREEN_WIDTH * percentage / 100)

@staticmethod
def screen_height_prcnt(percentage):
    return int(SCREEN_HEIGHT * percentage / 100)