import math
from random import randint, uniform
import sys
import time

import subprocess
import pyautogui as pag
import numpy as np
# import cv2

from human import Human

welcome_screen = (640, 400, 160, 40)
world_select = (350, 650, 90, 20)
posible_worlds = (820, 400 + (10 * randint(0,5)), 70, 10)
existing_user = (730, 450, 130, 30)
login_button = (570, 480, 130, 30)
click_to_play = (610, 450, 220, 80)
compass = (965, 160, 20, 20)
scroll_area = (500, 275, 400, 300)
maximize_window = (368, 142, 0, 0)

class LoginBot(Human):
    def openGame(self):
        print('Opening Old School Runescape application')

        subprocess.call(
            ["/usr/bin/open", "-n", "-a", "/Applications/Old School RuneScape.app"]
        )

        timeout = 30*1   # 1 minutes from now
        template = 'triggers/game/welcome_screen.png'
        Human.match_timeout(self, welcome_screen, template, timeout)
        return

    def login(self, username, password):
        print('Selecting world')
        Human.click_within(self, world_select)
        Human.click_within(self, posible_worlds)

        timeout = 10*1   # 1 minutes from now
        template = 'triggers/game/welcome_screen.png'
        Human.match_timeout(self, welcome_screen, template, timeout)

        print('Logging in')
        Human.click_within(self, existing_user)
        pag.typewrite(username)
        Human.random_wait(self, 0.25, 0.50)
        pag.press('tab')
        pag.typewrite(password)
        Human.random_wait(self, 0.25, 0.50)
        Human.click_within(self, login_button)
        Human.random_wait(self, 3, 5)

        timeout = 10*1
        template = 'triggers/game/click_to_play.png'
        Human.match_timeout(self, click_to_play, template, timeout)
        Human.click_within(self, click_to_play)
        Human.random_wait(self, 0.5, 1)

        print('Setting Camera')
        Human.click_within(self, compass)
        Human.move_within(self, scroll_area)
        pag.scroll(-randint(40, 50))
        pag.keyDown('up')
        Human.random_wait(self, 0.75, 1)
        pag.keyUp('up')

        print('Resizing Window')
        Human.click_within(self, maximize_window)   # Fullscreen

        return

if __name__ == '__main__':
    print('Press any key to quit.')

    try:
        start = time.time()
        LoginBot().openGame()
        LoginBot().login(username, password)
        print("Total runtime: {} minutes".format((time.time()-start)/60))


    except KeyboardInterrupt:
        sys.exit()
