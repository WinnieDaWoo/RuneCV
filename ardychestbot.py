#!/usr/bin/env python

"""


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
chest = (578, 433, 50, 90)
bank_wall = (320, 440, 45, 60)
inventory = (1200, 589, 204, 275)
# inventory_button = (1115, 865, 20, 30)
# bank = (680, 455, 20, 15)
# deposit_inventory = (780, 695, 30, 30)
# close_bank = (830, 55, 17, 17)
steal_position = (1170, 720, 8, 10)
stall_position = (690, 470, 60, 80)
bank_position = (310, 285, 15, 15)
compass = (1235, 55, 20, 20)
scroll_area = (500, 275, 400, 300)
bank = (340, 40, 510, 710)
# level_up = (20, 750, 70, 110)
idle_area = (250, 100, 900, 150)

# file = open("logs/oakbot.txt", "a")

class ArdyChestBot(Human):
    def run(self, sec=3600):
        print('Setting Camera')
        Human.click_within(self, compass)
        Human.move_within(self, scroll_area)
        pag.keyDown('up')
        Human.random_wait(self, 0.75, 1)
        pag.keyUp('up')
        pag.scroll(-randint(40, 50))
        Human.random_wait(self, 0.75, 1)
        pag.scroll(20)

        # file.write("{}: Starting TeaBot \n".format(dt.datetime.now()))
        count = 0
        timeout = time.time() + sec
        while time.time() < timeout:
            start = time.time()
            # file.write("{}: STARTING LOOP #{}\n".format(dt.datetime.now(), count))

            Human.right_click_within(self, chest)
            Human.random_wait(self, 0.25, 0.5)
            pag.screenshot('triggers/screen.png')
            template = "triggers/ardychestbot/search_for_traps.png"
            menu = Human.locate_object(self, fullscreen, template)
            if len(menu) > 0:
                Human.click_within(self, menu[0])
            start_time = time.time()
            Human.random_wait(self, 0.5, 1)
            # self.move_within(idle_area)

            idle_time = randint(5,8)
            while time.time() < start_time + idle_time:
                self.idle()
                self.random_wait(0.05, 0.25)

            pag.screenshot('triggers/screen.png')

            count = count + 1
            print("Loops completed: {}".format(count))
            # file.write("{}: Loops completed: {}\n".format(dt.datetime.now(), count))
            # file.write("{}: Loop time: {} seconds\n".format(dt.datetime.now(), time.time()-start))

        print("End of Ardy Chest Bot")
        # file.write("{}: Oak Bot finished \n\n".format(dt.datetime.now()))

        self.logout()
        return



if __name__ == '__main__':
    try:
        # num = randint(20, 25)
        min = 60 + randint(-10, 10)
        sec = (60 * min) + randint(-60, 60)
        print(sec/60)
        time.sleep(2)
        start = time.time()
        ArdyChestBot().run(sec)
        print("Total runtime: {} minutes".format((time.time()-start)/60))

    except KeyboardInterrupt:
        sys.exit()
