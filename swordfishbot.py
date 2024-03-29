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

# bank_desk = (615, 470, 32, 50)
# bank_wall = (320, 440, 45, 60)
inventory = (1200, 589, 204, 275)
# inventory_button = (1115, 865, 20, 30)
bank = (340, 40, 510, 710)
bank_booth = (670, 400, 50, 30)
# deposit_inventory = (780, 695, 30, 30)
# close_bank = (830, 55, 17, 17)
# chop_position = (980, 470, 10, 20)
# oak_position = (730, 490, 30, 40)
# bank_position = (445, 470, 15, 15)
# level_up = (20, 750, 70, 110)
compass = (1235, 55, 20, 20)
price_guide = (350, 230, 485, 320)
scroll_area = (500, 275, 400, 300)

to_bank = [
    [
        (1387, 157, 1, 1, 6.25),
        (1370, 171, 1, 1, 7.25),
        (1390, 153, 1, 1, 7),
        (1389, 158, 1, 1, 7),
        (1394, 139, 1, 1, 7),
        (1391, 123, 1, 1, 7),
        (1391, 112, 1, 1, 7),
    ]
]

to_dock = [
    [
        (1250, 134, 1, 1, 7.5),
        (1255, 152, 1, 1, 7.5),
        (1249, 116, 1, 1, 7.5),
        (1255, 113, 1, 1, 7.5),
        (1250, 119, 1, 1, 7.5),
        (1291, 63, 1, 1, 7.5),
        (1254, 98, 1, 1, 7.5),
        (160, 150, 120, 120, 5)
    ]
]


file = open("logs/SwordfishBot.txt", "a")

class SwordfishBot(Human):
    def is_fishing(self):
        template = 'triggers/swordfishbot/NOT_fishing.png'
        pag.screenshot('triggers/screen.png')
        temp = Human.image_match(self, fullscreen, template)

        if temp:
            print("not fishing")
            return False

        print("still fishing")
        return True

    def sort_inventory(self):
        pag.screenshot('triggers/screen.png')
        area = UI
        template = 'triggers/game/buttons/worn_equipment.png'
        loc = Human.locate_object(self, area, template)
        temp = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
        button = (temp[0] + 5, temp[1] + 5, temp[2] - 10, temp[3] - 10)
        Human.click_within(self, button)
        Human.random_wait(self, 0.25, 0.5)

        pag.screenshot('triggers/screen.png')
        area = fullscreen
        template = 'triggers/game/view_guide_prices.png'
        loc = Human.locate_object(self, area, template)
        temp = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
        button = (temp[0] + 5, temp[1] + 5, temp[2] - 10, temp[3] - 10)
        Human.click_within(self, button)

        # pag.screenshot('triggers/screen.png')
        area = price_guide
        template = 'triggers/game/add_all.png'
        timeout = 5
        Human.match_timeout(self, area, template, timeout)
        loc = Human.locate_object(self, area, template)
        temp = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
        button = (temp[0] + 5, temp[1] + 5, temp[2] - 10, temp[3] - 10)
        Human.click_within(self, button)

        area = fullscreen
        template = 'triggers/game/buttons/close.png'
        loc = Human.locate_object(self, area, template)
        temp = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
        button = (temp[0] + 5, temp[1] + 5, temp[2] - 10, temp[3] - 10)
        Human.click_within(self, button)

        pag.screenshot('triggers/screen.png')
        area = UI
        template = 'triggers/game/buttons/inventory.png'
        loc = Human().locate_object(area, template)
        temp = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
        button = (temp[0] + 5, temp[1] + 5, temp[2] - 10, temp[3] - 10)
        Human.click_within(self, button)
        Human.random_wait(self, 0.5, 1)

        pag.screenshot('triggers/screen.png')
        return


    def remove_tuna(self):
        template = 'triggers/swordfishbot/tuna_raw.png'
        Human.drop_items(self, template)

        return


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

        Human.click_within(self, bank_booth)
        Human.random_wait(self, 0.5, 0.75)

        area = bank
        template = 'triggers/game/deposit_inventory.png'
        timeout = 5
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

    def fish_loop(self):
        timeout_min = 30
        timeout = time.time() + 60*timeout_min   # 10 minutes from now
        pag.screenshot('triggers/screen.png')
        # self.remove_tuna()
        # self.sort_inventory()
        finished = False
        fishing = False
        fishtime = time.time() + 30
        while finished == False: #Human.is_inventory_full(self) == False:
            if time.time() > timeout:
                print("fish loop timeout after {} seconds".format(timeout_min))
                file.write("{}: Fishing timeout \n".format(dt.datetime.now()))
                sys.exit()

            # template = 'triggers/swordfishbot/level_up.png'
            # if Human.image_match(self, level_up, template):
            #     fishing = False

            if Human.is_inventory_full(self):
                fishing = False
                self.remove_tuna()
                if Human.is_inventory_full(self):
                    self.sort_inventory()
                fishtime = time.time() + 20
                finished = Human.is_inventory_full(self)


            if fishing == False and finished == False:
                menu_harpoon = []
                while len(menu_harpoon) == 0:
                    temp = 30
                    template = "triggers/swordfishbot/lobster_raw.png"
                    Human.match_timeout(self, fullscreen, template, temp)
                    s = Human.locate_object(self, fullscreen, template)
                    i = randint(0, len(s)-1)
                    spot = (s[i][0]+5, s[i][1]+5, s[i][2]-10, s[i][3]-10)
                    Human.right_click_within(self, spot)

                    pag.screenshot('triggers/screen.png')
                    template = "triggers/swordfishbot/harpoon_fishing_spot.png"
                    menu_harpoon = Human().locate_object(fullscreen, template)
                Human.click_within(self, menu_harpoon[0])
                fishing = True
            elif time.time() > fishtime:
                fishing = self.is_fishing()
                fishtime = time.time() + 5
            else:
                Human.idle(self)

            pag.screenshot('triggers/screen.png')

        return

    def run_to_bank(self):
        Human.click_within(self, (170, 140, 80, 80))
        Human.random_wait(self, 3, 3.5)

        for x in to_bank[0]:
            temp = (x[0], x[1], x[2], x[3])
            time = x[4]
            Human.click_within(self, temp)
            Human.random_wait(self, time, time + 0.25)

        return

    def run_to_dock(self):
        for x in to_dock[0]:
            temp = (x[0], x[1], x[2], x[3])
            time = x[4]
            Human.click_within(self, temp)
            Human.random_wait(self, time, time + 0.25)

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
        pag.scroll(10)

        count = 0
        while count < n:
            self.run_to_dock()

            self.fish_loop()

            self.run_to_bank()

            self.deposit_bank()

            count = count + 1




if __name__ == '__main__':
    try:
        start = time.time()
        # num = randint(20, 25)
        num = 1
        time.sleep(2)
        SwordfishBot().run(1)
        runtime = time.time()-start
        print("Total runtime: {} minutes".format(runtime/60))
        print("Average looptime: {} minutes".format(runtime/60/num))
        print("Swordfish/hr: {}".format((28*num)/runtime))


    except KeyboardInterrupt:
        sys.exit()
