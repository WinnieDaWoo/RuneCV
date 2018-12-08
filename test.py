import math
from random import randint, uniform
import sys
import time

import subprocess
import pyautogui as pag
from pynput import keyboard
# import numpy as np
# import cv2

# from human import Human as hmn
# from ironbot import IronBot'
from loginbot import LoginBot
from oakbot import OakBot

if __name__ == '__main__':
    try:
        start = time.time()
        num = 12
        time.sleep(2)
        OakBot().oak_loop(num)
        print("Total runtime: {} minutes".format((time.time()-start)/60))
        print("Average looptime: {} minutes".format((time.time()-start)/60/num))

    except KeyboardInterrupt:
        sys.exit()
