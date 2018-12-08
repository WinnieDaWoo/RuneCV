import math
from random import randint, uniform
import sys
import time

import subprocess
import pyautogui as pag
import numpy as np
import cv2

# from human import Human

class IronBot(Human):
    """
    start in bank

    for number of runs:
        if inventory empty and proper equipment:
            walk to mine{
                running or walking?
                avoid scorpions
            }

            while(last inventory slot not full)
                mine ore

            walk to bank

            deposit all

        else:
            logout

            kill bot
    """

    # [path][step][axis]
    mine_to_bank = [
        [(1, 2), (3, 4)],
        [(11, 12), (13, 14)],
        [(21, 22), (23, 24)],
    ]

    # [path][step][axis]
    bank_to_mine = [
        [(1, 2), (3, 4)],
        [(11, 12), (13, 14)],
        [(21, 22), (23, 24)],
    ]

    def iron_loop(self, rock_locations, triggers, mininglap):
        order = ['rock1', 'rock2', 'rock3']
        trigger_order = ['rock1iron', 'rock1noiron', 'rock2iron', 'rock2noiron', 'rock3iron', 'rock3noiron']

        for i in range(len(order)):
            # Checks for full inventory.
            if not self.image_match((2352, 682, 63, 55), 'triggers/bankslot.png'):
                return True

            # Checks for scorpions and moves to the location of rock #3.
            if i == 2:
                self.random_coordinate(rock_locations['movetorock3'])
                self.check_for_scorpion((rock_locations['movetorock3'][0], rock_locations['movetorock3'][1],
                                         rock_locations['movetorock3'][2] + 250, rock_locations['movetorock3'][3] + 250))
                pag.click()

            self.random_coordinate(rock_locations[order[i]])
            self.wait_for_trigger(triggers[trigger_order[(i*2)]])  # wait for iron
            pag.click()
            self.wait_for_trigger(triggers[trigger_order[(i*2)+1]])  # wait for success
            self.random_wait(0.05, 0.1)

        # Resets location for the beginning of the next loop.
        self.random_coordinate(rock_locations['reset'])
        self.check_for_scorpion((rock_locations['reset'][0], rock_locations['reset'][1],
                                 rock_locations['reset'][2] + 250, rock_locations['reset'][3] + 250))
        pag.click()
        self.wait_for_trigger((1700, 50, 150, 150, 'triggers/reset_check.png'))  # check to make sure made it to right location

        return
