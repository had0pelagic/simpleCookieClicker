import pyautogui
from PIL import ImageGrab,ImageOps
import time
from numpy import*
import sys

# coordinates for mouse position 
class Coordinates():
    hitCord = (140,500)

def click():
    pyautogui.click(Coordinates.hitCord)

def main():
    while True:
        cc = input("Start: [y/n]:")
        if cc != 'n':
            amount = input("How many clicks?:")
            for x in range(0,int(amount)):
                click()
                time.sleep(0.0001)
        else: quit()
main()
