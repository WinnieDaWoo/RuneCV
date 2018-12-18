# RuneCV

A Collection a Computer Vision Based Runsecape bots

While a majority of bots are designed using injection or reflection frameworks, these botting methods can be easily broken or detected through backend client changes. Instead, these bots use object recognition to identify different objects and their locations, and preform appropriate actions. This is very similar to the way you see a screen, recognize the object model, and decide to preform certain actions.

This method of environment analysis is not a precise as reading the game code itself, but is much more difficult to detect if designed properly. Additionally these concepts can be used in any other game, or real world implementation (such as self driving cars).

These bots are for educational purposes only and I do not endorse botting in RS as it is a violation of Jagex Terms of Service.

## Build

1. install Python 3.5+
2. Install Packages

  ~~~~
  pip install numpy
  pip install opencv-python
  pip install pyautogui
  ~~~~

3. Build and run desired bot

  ~~~~
  python NAMEBOT.py
  ~~~~

  Be sure to read the header at the top of the bot to make sure your camera and character are in the proper postion
