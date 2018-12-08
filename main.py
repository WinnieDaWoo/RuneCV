import math
from random import randint, uniform
import sys
import time

import subprocess
import pyautogui as pag
from pynput import keyboard
# import numpy as np
# import cv2

# from human import Human as hmn
# from ironbot import IronBot'
from loginbot import LoginBot
from oakbot import OakBot


break_program = False
def on_press(key):
    global break_program
    print('"{0}" key pressed. Ending program'.format(key.char))
    break_program = True
    return False


lgn = LoginBot()
# username = "runthistest@protonmail.com"
# password = "I66enLpASoRA"

username = "getallto99@protonmail.com"
password = "light111"


if __name__ == '__main__':
    print('Press any key to quit.')

    try:
        start = time.time()
        lgn.openGame()
        lgn.login(username, password)
        print("Total runtime: {} minutes".format((time.time()-start)/60))


    except KeyboardInterrupt:
        sys.exit()
