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

fullscreen = (0, 0, 1499, 899)
fishing_area = (399, 199, 700, 500)
UI = (950, 850, 450, 50)
inventory = (1199, 589, 204, 275)



if __name__ == '__main__':
    try:
        time.sleep(2)
        start = time.time()
        pag.screenshot('triggers/screen.png')
        area = inventory
        template = 'triggers/swordfishbot/tuna_raw.png'
        loc = Human().locate_object(area, template, 0.9)
        if len(loc)==0:
            print("no tuna in inventory")
            sys.exit()


        for i in loc:
            item = (i[0]+area[0], i[1]+area[1], i[2], i[3])
            print(item)
            Human().shift_click_within(item)

    except KeyboardInterrupt:
        sys.exit()
