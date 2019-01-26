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
# bank = (680, 455, 20, 15)
# deposit_inventory = (780, 695, 30, 30)
# close_bank = (830, 55, 17, 17)
# chop_position = (980, 470, 10, 20)
# oak_position = (730, 490, 30, 40)
# bank_position = (445, 470, 15, 15)
scroll_area = (500, 275, 400, 300)
level_up = (20, 750, 400, 110)
price_guide = (350, 230, 485, 320)
just_south = (650, 500, 95, 95)


file = open("logs/SwordfishBot.txt", "a")

class SwordfishBot(Human):
    def is_fishing(self):
        # template = 'triggers/game/inventory_previous.png'
        # pag.screenshot('triggers/screen.png')
        # temp = Human.image_match(self, inventory, template, 0.9)
        #
        # original = Image.open('triggers/screen.png')
        # r = inventory
        # cropped = original.crop((r[0]*2, r[1]*2, (r[0]+r[2])*2, (r[1]+r[3])*2))
        # cropped.save('triggers/game/inventory_previous.png')

        pag.screenshot('triggers/screen.png')
        template = 'triggers/swordfishbot/lobster_raw.png'
        moved = not Human.image_match(self, just_south, template, 0.5)

        template = 'triggers/swordfishbot/level_up.png'
        leveled = Human.image_match(self, level_up, template)

        if moved or leveled:
            print("not fishing")
            return False

        print("still fishing")
        return True

    def sort_inventory(self):
        pag.screenshot('triggers/screen.png')
        area = UI
        template = 'triggers/game/buttons/worn_equipment.png'
        loc = Human.locate_object(self, area, template)
        button = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
        Human.click_within(self, button)
        Human.random_wait(self, 0.25, 0.5)

        pag.screenshot('triggers/screen.png')
        area = fullscreen
        template = 'triggers/game/view_guide_prices.png'
        loc = Human.locate_object(self, area, template)
        button = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
        Human.click_within(self, button)

        # pag.screenshot('triggers/screen.png')
        area = price_guide
        template = 'triggers/game/add_all.png'
        timeout = 5
        Human.match_timeout(self, area, template, timeout)
        loc = Human.locate_object(self, area, template)
        button = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
        Human.click_within(self, button)

        area = fullscreen
        template = 'triggers/game/buttons/close.png'
        loc = Human.locate_object(self, area, template)
        button = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
        Human.click_within(self, button)

        pag.screenshot('triggers/screen.png')
        area = UI
        template = 'triggers/game/buttons/inventory.png'
        loc = Human().locate_object(area, template)
        button = (loc[0][0]+area[0], loc[0][1]+area[1], loc[0][2], loc[0][3])
        Human.click_within(self, button)
        Human.random_wait(self, 0.5, 1)

        pag.screenshot('triggers/screen.png')
        return


    def remove_tuna(self):
        pag.screenshot('triggers/screen.png')
        area = inventory
        template = 'triggers/swordfishbot/tuna_raw.png'
        loc = Human.locate_object(self, area, template, 0.9)
        if len(loc)==0:
            print("no tuna in inventory")
            return

        items = []
        for i in loc:
            items.append( (i[0]+area[0], i[1]+area[1], i[2], i[3]) )

        Human.drop_items(self, items)
        Human.random_wait(self, 0.5, 1)
        pag.screenshot('triggers/screen.png')

        return


    # def deposit_bank(self):
    #     pag.screenshot('triggers/screen.png')
    #     if Human.is_inventory_empty(self):
    #         return
    #
    #     print("Depositing")
    #     file.write("{}: Depositing Inventory \n".format(dt.datetime.now()))
    #
    #     # Check if in correct position
    #     timeout = 10*1
    #     template = 'triggers/oakbot/bank_desk.png'
    #     threshold = 0.7
    #     Human.match_timeout(self, bank_desk, template, timeout, threshold)
    #
    #     Human.click_within(self, bank)
    #     Human.random_wait(self, 0.5, 0.75)
    #     Human.click_within(self, deposit_inventory)
    #     Human.random_wait(self, 0.5, 0.75)
    #     Human.click_within(self, close_bank)
    #     Human.random_wait(self, 0.5, 0.75)
    #
    #     return

    def fish_loop(self):
        timeout = time.time() + 60*20   # 10 minutes from now
        pag.screenshot('triggers/screen.png')
        # self.remove_tuna()
        # self.sort_inventory()
        finished = False
        fishing = False
        fishtime = time.time() + 30
        while finished == False: #Human.is_inventory_full(self) == False:
            if time.time() > timeout:
                print("image match timeout after {} seconds".format(600))
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
                menu = []
                while len(menu) == 0:
                    Human.move_within(self, (0, 100, 400, 300))
                    temp = 30
                    template = "triggers/swordfishbot/lobster_raw.png"
                    Human.match_timeout(self, fullscreen, template, temp)
                    s = Human.locate_object(self, fullscreen, template)
                    i = randint(0, len(s)-1)
                    spot = (s[i][0]+5, s[i][1]+5, s[i][2]-10, s[i][3]-10)
                    Human.right_click_within(self, spot)

                    pag.screenshot('triggers/screen.png')
                    template = "triggers/swordfishbot/harpoon_fishing_spot.png"
                    menu = Human.locate_object(self, fullscreen, template)
                Human.click_within(self, menu[0])
                fishing = True
            elif time.time() > fishtime:
                fishing = self.is_fishing()
                fishtime = time.time() + 5
            else:
                Human.idle(self)

            pag.screenshot('triggers/screen.png')

        return

    # def run(self, n=1):




if __name__ == '__main__':
    try:
        # start = time.time()
        # num = randint(20, 25)
        time.sleep(2)
        # SwordfishBot().run(num)
        # print("Total runtime: {} minutes".format((time.time()-start)/60))
        # print("Average looptime: {} minutes".format((time.time()-start)/60/num))
        pag.scroll(-randint(40, 50))
        pag.scroll(10)

        SwordfishBot().fish_loop()
        # SwordfishBot().remove_tuna()
        # SwordfishBot().sort_inventory()

    except KeyboardInterrupt:
        sys.exit()
