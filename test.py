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



if __name__ == '__main__':
    try:
        time.sleep(2)
        start = time.time()
        # pag.screenshot('triggers/screen.png')
        # print(inventory*2)
        SwordfishBot().is_fishing()

    except KeyboardInterrupt:
        sys.exit()
