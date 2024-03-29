import math
from random import randint, uniform
import sys
import time

from PIL import Image
import subprocess
import pyautogui as pag
import numpy as np
import cv2

inventory = (1200, 589, 204, 275)
inventory_button = (1115, 865, 20, 30)
last_slot = (1349, 820, 40, 30)
fullscreen = (0, 0, 1499, 899)
idle_area = (250, 100, 900, 150)
logout1 = (1380, 50, 15, 15)
logout2 = (1235, 810, 135, 30)




class Human(object):
    """Class encapulates all bots in order to make them look as human as possible"""
    def random_wait(self, min=0.25, max=0.50):
        """Waits a random number of seconds between two numbers (0.25 and 0.50 default) to mimic human reaction time"""
        return time.sleep(uniform(min, max))

    def travel_time(self, x2, y2):
        """Calculates cursor travel time in seconds per 240-270 pixels, based on a variable rate of movement"""
        rate = uniform(0.09, 0.15)
        x1, y1 = pag.position()
        distance = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))

        return max(uniform(.08, .12), rate * (distance/randint(250, 270)))

    def move_within(self, location):
        """Moves cursor to random locaction still above the object to be clicked"""
        x = randint(location[0], location[0]+location[2])
        y = randint(location[1], location[1]+location[3])
        time = self.travel_time(x, y)

        return pag.moveTo(x, y, time)

    def click_within(self, location):
        """Moves cursor to random locaction still above the object and clicks"""
        self.move_within(location)
        self.random_wait(0.05, 0.25)
        pag.click()
        self.random_wait(0.05, 0.25)
        # self.move_within((0, 0, 1439, 899))

        return

    def drop_items(self, template):
        pag.screenshot('triggers/screen.png')
        area = inventory
        loc = Human.locate_object(self, area, template, 0.9)
        if len(loc)==0:
            print("no tuna in inventory")
            return

        items = []
        for i in loc:
            items.append( (i[0]+area[0], i[1]+area[1], i[2], i[3]) )

        pag.keyDown('shift')
        self.random_wait(0.05, 0.25)
        for i in items:
            self.move_within(i)
            self.random_wait(0.05, 0.25)
            pag.click()
        pag.keyUp('shift')
        self.random_wait(0.05, 0.25)
        # self.move_within((0, 0, 1439, 899))
        Human.random_wait(self, 0.5, 1)
        pag.screenshot('triggers/screen.png')

        return

    def right_click_within(self, location):
        """Moves cursor to random locaction still above the object and clicks"""
        self.move_within(location)
        self.random_wait(0.05, 0.5)
        pag.click(button='right')
        self.random_wait(0.05, 0.25)
        # self.move_within((0, 0, 1439, 899))

        return

    # def keyboardtype(self, string):
    #     while
    #     randint(location[0], location[0]+location[2])
    #     return

    def image_match(self, r, img, threshold = 0.80):
        if r != fullscreen:
            original = Image.open('triggers/screen.png')
            temp = (r[0]*2, r[1]*2, (r[0]+r[2])*2, (r[1]+r[3])*2)
            cropped = original.crop(temp)
            cropped.save('triggers/temp.png')
            screen = cv2.imread('triggers/temp.png')
        else:
            screen = cv2.imread('triggers/screen.png')

        template = cv2.imread(img)

        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        # threshold = .70
        loc = np.where(res >= threshold)
        if len(loc[0]) > 0:
            return True

        return False

    def locate_object(self, r, img, threshold = 0.80):
        if r != fullscreen:
            original = Image.open('triggers/screen.png')
            temp = (r[0]*2, r[1]*2, (r[0]+r[2])*2, (r[1]+r[3])*2)
            cropped = original.crop(temp)
            cropped.save('triggers/temp.png')
            screen = cv2.imread('triggers/temp.png')
        else:
            screen = cv2.imread('triggers/screen.png')

        template = cv2.imread(img)
        h, w, channels = template.shape
        temp = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(temp >= threshold)
        res = []
        for pt in zip(*loc[::-1]):
            # cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)
            res.append((pt[0]/2, pt[1]/2, w/2, h/2))

        # cv2.imshow('Detected',screen)
        # cv2.waitKey(2)
        return res


    def match_timeout(self, r, img, seconds, threshold = 0.80):
        next = False;
        timeout = time.time() + seconds
        while  next == False:
            pag.screenshot('triggers/screen.png')
            if time.time() > timeout:
                print("image match timeout after {} seconds".format(seconds))
                sys.exit()
            next = self.image_match(r, img, threshold)
        # self.random_wait(0.25, 0.5)
        return

    def idle(self):
        option = randint(0, 999)
        if option < 900:
            return time.sleep(0.1)
        elif option < 980:
            self.move_within(idle_area)
        else:
            self.move_within(idle_area)
            pag.click(button='right')

    def is_inventory_empty(self):
        # self.click_within(inventory_button)
        print("is inventory empty")
        trigger = 'triggers/game/inventory_empty.png'
        threshold = 0.90
        if self.image_match(inventory, trigger, threshold):
            return True

        return False

    def is_inventory_full(self):
        # self.click_within(inventory_button)
        trigger = 'triggers/game/last_slot_empty.png'
        threshold = 0.80
        if self.image_match(last_slot, trigger, threshold):
            print("inventory is not full")
            return False

        print("inventory is full")
        return True

    def logout(self):
        self.click_within(logout1)
        self.random_wait(0.25, 0.5)
        self.click_within(logout2)

        return
