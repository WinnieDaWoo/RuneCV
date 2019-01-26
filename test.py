import math
from random import randint, uniform
import sys
import time

import subprocess
import pyautogui as pag
from pynput import keyboard
# import numpy as np
# import cv2

from human import Human
# from ironbot import IronBot'
# from loginbot import LoginBot
# from oakbot import OakBot
from swordfishbot import SwordfishBot


fullscreen = (0, 0, 1499, 899)
fishing_area = (399, 199, 700, 500)
UI = (950, 850, 450, 50)
inventory = (1199, 589, 204, 275)
compass = (1235, 55, 20, 20)
scroll_area = (500, 275, 400, 300)



if __name__ == '__main__':
    try:
        time.sleep(2)
        # start = time.time()
        # pag.screenshot('triggers/screen.png')
        # print(inventory*2)
        # SwordfishBot().is_fishing()

        # x = (1250, 134, 1, 1, 8)
        # x = (1255, 152, 1, 1, 8)
        # x = (1249, 116, 1, 1, 8)
        # x = (1255, 113, 1, 1, 8)
        # x = (1250, 119, 1, 1, 8)
        # x = (1291, 63, 1, 1, 8)
        # x = (1254, 98, 1, 1, 8)
        #
        # temp = (x[0], x[1], x[2], x[3])
        # time = x[4]
        # Human().click_within(temp)
        # Human().random_wait(time, time + 0.25)

        Human().logout()



    except KeyboardInterrupt:
        sys.exit()
