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


bank_desk = (615, 470, 32, 50)
bank_wall = (320, 440, 45, 60)
inventory = (1236, 589, 204, 275)
inventory_button = (1115, 865, 20, 30)
bank = (680, 455, 20, 15)
deposit_inventory = (780, 695, 30, 30)
close_bank = (830, 55, 17, 17)
chop_position = (980, 470, 10, 20)
oak_position = (730, 490, 30, 40)
bank_position = (445, 470, 15, 15)
level_up = (20, 750, 70, 110)

file = open("logs/oakbot.txt", "a")

class OakBot(Human):
    def is_tree_cut(self):
        template = 'triggers/oakbot/oak_cut.png'
        # pag.screenshot('triggers/screen.png')
        if(Human.image_match(self, oak_position, template)):
            return True

        return False

    def deposit_bank(self):
        pag.screenshot('triggers/screen.png')
        if Human.is_inventory_empty(self):
            return

        print("Depositing")
        file.write("{}: Depositing Inventory \n".format(dt.datetime.now()))

        # Check if in correct position
        timeout = 10*1
        template = 'triggers/oakbot/bank_desk.png'
        threshold = 0.7
        Human.match_timeout(self, bank_desk, template, timeout, threshold)

        Human.click_within(self, bank)
        Human.random_wait(self, 0.5, 0.75)
        Human.click_within(self, deposit_inventory)
        Human.random_wait(self, 0.5, 0.75)
        Human.click_within(self, close_bank)
        Human.random_wait(self, 0.5, 0.75)

        return

    def oak_loop(self, n=1):
        file.write("{}: Starting OakBot \n".format(dt.datetime.now()))
        Human.click_within(self, inventory_button)
        self.deposit_bank()
        count = 0
        for x in range(n):
            start = time.time()
            file.write("{}: STARTING LOOP #{}\n".format(dt.datetime.now(), count))

            Human.click_within(self, chop_position)
            file.write("{}: Moving to chop position\n".format(dt.datetime.now()))

            # Check if in correct chopping position
            print("Checking chopping position")
            timeout = 20*1
            template = 'triggers/oakbot/bank_wall.png'
            threshold = 0.7
            Human.match_timeout(self, bank_wall, template, timeout, threshold)
            # Human.random_wait(self, 8, 10)

            print("Chopping")
            chopping = False
            timeout = time.time() + 60*10   # 10 minutes from now
            pag.screenshot('triggers/screen.png')
            while Human.is_inventory_full(self) == False:
                if time.time() > timeout:
                    print("image match timeout after {} seconds".format(600))
                    file.write("{}: Chopping timeout \n".format(dt.datetime.now()))
                    sys.exit()

                template = 'triggers/oakbot/level_up.png'
                if Human.image_match(self, level_up, template):
                    chopping = False

                is_cut = self.is_tree_cut()
                if chopping == True and is_cut == True:
                    chopping = False
                    file.write("{}: Tree is cut\n".format(dt.datetime.now()))
                elif chopping == False and is_cut == False:
                    Human.click_within(self, oak_position)
                    chopping = True
                    file.write("{}: Chopping started, now idling\n".format(dt.datetime.now()))
                else:
                    Human.idle(self)

                pag.screenshot('triggers/screen.png')

            print("Inventory full")
            file.write("{}: Inventory full \n".format(dt.datetime.now()))
            Human.click_within(self, bank_position)
            self.deposit_bank()
            count = count + 1
            print("Loops completed: {}".format(count))
            file.write("{}: Loops completed: {}\n".format(dt.datetime.now(), count))
            file.write("{}: Loop time: {} seconds\n".format(dt.datetime.now(), time.time()-start))

        print("End of Oak Bot")
        file.write("{}: Oak Bot finished \n\n".format(dt.datetime.now()))
        return



if __name__ == '__main__':
    try:
        start = time.time()
        num = randint(20, 25)
        time.sleep(2)
        OakBot().oak_loop(num)
        print("Total runtime: {} minutes".format((time.time()-start)/60))
        print("Average looptime: {} minutes".format((time.time()-start)/60/num))

    except KeyboardInterrupt:
        sys.exit()
