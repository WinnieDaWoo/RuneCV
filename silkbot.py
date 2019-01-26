#!/usr/bin/env python

"""
requires RuneLite game client

Loop time: ~2.5 minutes
GP Earnings: ~650 oak logs (~30k/hr @ 45gp/log)
EXP Earnings: ~24,375 woodcutting exp

HOW TO RUN:
    Start at Draynor village bank, northern most booth
    Equip axe
    Close inventory
    Run bot
"""


import math
from random import randint, uniform
import sys
import time
import datetime as dt

from PIL import Image
import subprocess
import pyautogui as pag
import numpy as np
# import cv2

from human import Human


__author__ = "Adam Woo"
__copyright__ = "None"
__credits__ = ["Adam Woo"]
__license__ = "None"
__version__ = "1.0.0"
__maintainer__ = "Adam Woo"
__email__ = "None"
__status__ = "Development"

fullscreen = (0, 0, 1499, 899)
UI = (950, 850, 450, 50)

idle_area = (250, 100, 900, 150)
# bank_desk = (615, 470, 32, 50)
# bank_wall = (320, 440, 45, 60)
inventory = (1200, 589, 204, 275)
# inventory_button = (1115, 865, 20, 30)
bank = (340, 40, 510, 710)
bank_booth = (670, 400, 50, 30)
stall_position = (660, 550, 200, 100)
compass = (1235, 55, 20, 20)
price_guide = (350, 230, 485, 320)
scroll_area = (500, 275, 400, 300)


# file = open("logs/SwordfishBot.txt", "a")

class SilkBot(Human):
    def drop_silk(self):
        template = 'triggers/silkbot/silk.png'
        Human.drop_items(self, template)

        return


    def silk_loop(self, n):
        pag.screenshot('triggers/screen.png')

        for x in range(n):
            self.drop_silk()

            while Human.is_inventory_full(self) == False:
                area = stall_position
                template = 'triggers/silkbot/stall_full.png'
                timeout = 20
                Human.match_timeout(self, area, template, timeout)
                # pag.screenshot('triggers/screen.png')
                loc = Human.locate_object(self, area, template, 0.90)

                if len(loc) > 0:
                    temp = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
                    Human.random_wait(self, 0.5, 1)
                    Human.click_within(self, temp)
                    Human.random_wait(self, 1, 3)
                    self.move_within(idle_area)
                else:
                    Human.idle(self)

                pag.screenshot('triggers/screen.png')

        return

    def run(self, n=1):
        print('Setting Camera')
        Human.click_within(self, compass)
        Human.move_within(self, scroll_area)
        pag.keyDown('up')
        Human.random_wait(self, 0.75, 1)
        pag.keyUp('up')
        pag.scroll(-randint(40, 50))
        Human.random_wait(self, 0.75, 1)
        pag.scroll(15)

        self.silk_loop(n)

        return


if __name__ == '__main__':
    try:
        start = time.time()
        num = randint(5, 10)
        # num = 1
        time.sleep(2)
        SilkBot().run(num)
        runtime = time.time()-start
        print("Total runtime: {} minutes".format(runtime/60))
        print("Average looptime: {} minutes".format(runtime/60/num))
        print("Silk/hr: {}".format((28*num*60*60)/(runtime)))
        print("XP/hr: {}".format((28*num*60*60*24)/(runtime)))


    except KeyboardInterrupt:
        sys.exit()
