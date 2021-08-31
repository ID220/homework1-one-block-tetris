from microbit import *
# import utime
from timer import *

# CONSTANTS
UI_REFRESH = 200
INPUT_REFRESH = 100


# update this every 500ms
def updatelogic():
    if (display.get_pixel(0, 0) == 0):
        display.set_pixel(0, 0, 9)
    else:
        display.set_pixel(0, 0, 0)


# update this every 100ms
def updateInputUI():
    if (display.get_pixel(1, 1) == 0):
        display.set_pixel(1, 1, 9)
    else:
        display.set_pixel(1, 1, 0)


# main
while True:

    # your logic here

    # these two will allow you to have 2 times
    tick(INPUT_REFRESH, updateInputUI)
    tick(UI_REFRESH, updatelogic)
