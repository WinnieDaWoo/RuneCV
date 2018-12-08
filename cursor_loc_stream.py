import time

import pyautogui
from pynput import keyboard

break_program = False
def on_press(key):
    global break_program
    print('"{0}" key pressed. Ending program'.format(key.char))
    break_program = True
    return False


if __name__ == '__main__':
    print('Press any key to quit.')

    try:
        with keyboard.Listener(on_press=on_press) as listener:
            while break_program == False:
                # Get and print the mouse coordinates.
                x, y = pyautogui.position()
                positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                print(positionStr)
                time.sleep(0.25)
            listener.join()

    except KeyboardInterrupt:
        print('\nDone.')
