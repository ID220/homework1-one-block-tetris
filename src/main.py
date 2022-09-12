from pyblinkpico import *
import time


#### TICK HELPER ######
prevTime = {}


def tick(ms, callback):
    if (ms not in prevTime):
        prevTime[ms] = 0
    if time.ticks_diff(time.ticks_ms(), prevTime[ms]) > ms:
        callback()
        prevTime[ms] = time.ticks_ms()



#### MAIN ######

# CONSTANTS
INPUT_REFRESH = 100
LOGIC_REFRESH = 500 # start with a slow refresh
# LOGIC_REFRESH = 200 # lower it later when ready


# update this every 500ms
def updateLogic():
    # your logic here
    print('Draw and update your logic')
    pass


# update this every 100ms
def updateInput():
    # your logic and draw here
    print('Read from buttons')
    pass


# main
while True:
    # Your code here

    # these two functions set a callback to be called
    # at respectively 500 and 100 milliseconds
    tick(INPUT_REFRESH, updateInput)
    tick(LOGIC_REFRESH, updateLogic)
