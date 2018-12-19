# test

import math
from random import randint, uniform
import sys
import time

from PIL import Image
import subprocess
import pyautogui as pag
import numpy as np
import mss
import mss.tools
import pyscreenshot
import cv2


# [path][step][axis]
mine_to_bank = [
    [(1, 2), (3, 4)],
    [(11, 12), (13, 14)],
    [(21, 22), (23, 24)],
]


region=(930,455,190,260)

inventory = (1200, 589, 204, 275)
last_slot = (1349, 820, 40, 30)
welcome_screen = (640, 400, 160, 40)
click_to_play = (610, 450, 220, 80)
bank_desk = (615, 470, 32, 50)
oak_position = (720, 490, 70, 50)
level_up = (20, 750, 70, 110)
bank_wall = (320, 440, 45, 60)


if __name__ == '__main__':
    x = last_slot[0]*2
    y = last_slot[1]*2
    w = last_slot[2]*2
    h = last_slot[3]*2

    print(pag.size())
    time.sleep(2)
    pag.screenshot('triggers/game/last_slot_empty.png')

    original = Image.open('triggers/game/last_slot_empty.png')
    cropped_example = original.crop((x, y, x+w, y+h))
    cropped_example.save('triggers/game/last_slot_empty.png')
