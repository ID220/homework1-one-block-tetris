from microbit import *
# import utime
from timer import *

# CONSTANTS
UI_REFRESH = 500
INPUT_REFRESH = 100


# update this every 500ms
def updatelogic():
    # your logic here
    pass


# update this every 100ms
def updateInputUI():
    # your logic here
    pass


# main
while True:
    # your logic here

    # these two functions set a callback to be called
    # at respectively 500 and 100 milliseconds
    tick(INPUT_REFRESH, updateInputUI)
    tick(UI_REFRESH, updatelogic)
