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

# file = open("logs/oakbot.txt", "a")

class TeaBot(Human):
    def is_stall_full(self):
        template = 'triggers/teabot/stall_full.png'
        # pag.screenshot('triggers/screen.png')
        if(Human.image_match(self, stall_position, template)):
            return True

        return False

    def deposit_bank(self):
        pag.screenshot('triggers/screen.png')
        if Human.is_inventory_empty(self):
            return
        #
        # print("Depositing")
        # file.write("{}: Depositing Inventory \n".format(dt.datetime.now()))

        # Check if in correct position
        # timeout = 10*1
        # template = 'triggers/oakbot/bank_desk.png'
        # threshold = 0.7
        # Human.match_timeout(self, bank_booth, template, timeout, threshold)

        # Human.click_within(self, bank_booth)
        # Human.random_wait(self, 0.5, 0.75)

        area = bank
        template = 'triggers/game/deposit_inventory.png'
        timeout = 20
        Human.match_timeout(self, area, template, timeout)
        loc = Human.locate_object(self, area, template)
        temp = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
        button = (temp[0] + 5, temp[1] + 5, temp[2] - 10, temp[3] - 10)
        Human.click_within(self, button)


        area = bank
        template = 'triggers/game/buttons/close.png'
        loc = Human.locate_object(self, area, template)
        temp = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
        button = (temp[0] + 5, temp[1] + 5, temp[2] - 10, temp[3] - 10)
        Human.click_within(self, button)

        pag.screenshot('triggers/screen.png')

        return

    def tea_loop(self, n=1):
        # print('Setting Camera')
        # Human.click_within(self, compass)
        # Human.move_within(self, scroll_area)
        # pag.keyDown('up')
        # Human.random_wait(self, 0.75, 1)
        # pag.keyUp('up')
        # pag.scroll(-randint(40, 50))
        # Human.random_wait(self, 0.75, 1)

        # file.write("{}: Starting TeaBot \n".format(dt.datetime.now()))
        # Human.click_within(self, inventory_button)
        # self.deposit_bank()
        count = 0
        for x in range(n):
            start = time.time()
            # file.write("{}: STARTING LOOP #{}\n".format(dt.datetime.now(), count))

            Human.click_within(self, steal_position)
            Human.random_wait(self, 10, 12)
            # file.write("{}: Moving to tea stall\n".format(dt.datetime.now()))

            # Check if in correct chopping position
            # print("Checking chopping position")
            # timeout = 20*1
            # template = 'triggers/oakbot/bank_wall.png'
            # threshold = 0.7
            # Human.match_timeout(self, bank_wall, template, timeout, threshold)
            # Human.random_wait(self, 8, 10)

            print("stealing")
            t = 60*5
            timeout = time.time() + t   # 10 minutes from now
            pag.screenshot('triggers/screen.png')
            while Human.is_inventory_full(self) == False:
                if time.time() > timeout:
                    print("image match timeout after {} seconds".format(t))
                    # file.write("{}: stealing timeout \n".format(dt.datetime.now()))
                    sys.exit()

                # template = 'triggers/oakbot/level_up.png'
                # if Human.image_match(self, level_up, template):
                #     chopping = False'

                area = stall_position
                template = 'triggers/teabot/stall_full.png'
                # timeout = 10
                # Human.match_timeout(self, area, template, timeout)
                pag.screenshot('triggers/screen.png')
                loc = Human.locate_object(self, area, template, 0.90)

                if len(loc) > 0:
                    temp = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
                    Human.click_within(self, temp)
                    Human.random_wait(self, 0.5, 1)
                else:
                    Human.idle(self)

                pag.screenshot('triggers/screen.png')

            # file.write("{}: Inventory full \n".format(dt.datetime.now()))
            Human.click_within(self, bank_position)
            Human.random_wait(self, 0.5, 1)
            self.deposit_bank()
            count = count + 1
            print("Loops completed: {}".format(count))
            # file.write("{}: Loops completed: {}\n".format(dt.datetime.now(), count))
            # file.write("{}: Loop time: {} seconds\n".format(dt.datetime.now(), time.time()-start))

        print("End of Tea Bot")
        # file.write("{}: Oak Bot finished \n\n".format(dt.datetime.now()))
        return



if __name__ == '__main__':
    try:
        # num = randint(20, 25)
        num = 4
        time.sleep(2)
        start = time.time()
        TeaBot().tea_loop(num)
        print("Total runtime: {} minutes".format((time.time()-start)/60))
        print("Average looptime: {} minutes".format((time.time()-start)/60/num))

    except KeyboardInterrupt:
        sys.exit()
