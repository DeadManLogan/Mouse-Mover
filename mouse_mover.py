import pyautogui
import time
import random

# your screen's size
width = 1920
height = 1080

# runs for the number of times we want to move our mouse. could work better with while()
for move in range(1, 500):
    x = random.randint(0, width)
    y = random.randint(0, height)

    # moves our mouse to (x, y) position
    pyautogui.moveTo(x, y)

    # we store the localtime of the move
    localtime = time.localtime()
    # we convert the time to a readable format
    result = time.strftime("%I:%M:%S %p", localtime)

    print("Mouse moved at " + str(result) + " (" + str(x) + ", " + str(y) + ")")
    # the number of seconds we wait till next iteration
    time.sleep(60)