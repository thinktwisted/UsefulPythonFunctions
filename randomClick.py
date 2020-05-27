import random
import pyautogui as gui

def randomClick(box):
    '''A function to return random click coordinates from box object from pyautogui'''
    x_click = int(random.uniform(box.left, box.left+box.width))
    y_click = int(random.uniform(box.top, box.top+box.height))
    return (x_click, y_click)
    
# Example Usage
# locates IMAGE, passes the box object to randomClick(), 
# which returns randomly generated coordinates within the box
# then pyautogui moves the mouse to that location
# then it clicks
## gui.moveTo(randomclick(gui.locateOnScreen(IMAGE)))
## gui.click()
