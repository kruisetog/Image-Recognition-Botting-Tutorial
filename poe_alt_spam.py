#This script locates the image stickman.png in the region we give it and tell you if it can see it

from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con

# while 1:
#     if pyautogui.locateOnScreen('wrong.png', region=(150,175,350,600), grayscale=True, confidence=0.8) != None:
#         print("I can see it")
#         time.sleep(0.5)
#     else:
#         print("I am unable to see it")
#         time.sleep(0.5)
# alts : 95, 250 to 130, 285
# aug: 208, 310 to 242, 338
# regal: 418, 256 to 450, 270
# item: 295, 375 to 360, 512
# "^amber|exalter"
# "^amber|exalter|all skill gem"
def start_check():
    user_input = input("Continue? (y/n)")
    if user_input.upper() == 'Y':
        return True
    else:
        return False
def augmentation_check():
    print("augmentation")
    aug_x_coords = (208, 242)
    aug_y_coords = (310, 338)
    item_x_coords = (295, 360)
    item_y_coords = (375, 512)
    alt_x = random.randrange(aug_x_coords[0], aug_x_coords[1], 2)
    alt_y = random.randrange(aug_y_coords[0], aug_y_coords[1], 2)

    item_x = random.randrange(item_x_coords[0], item_x_coords[1], 2)
    item_y = random.randrange(item_y_coords[0], item_y_coords[1], 2)

    pyautogui.moveTo(alt_x, alt_y, round(random.uniform(0.1,0.2), 4))
    pyautogui.keyDown('shift')
    pyautogui.rightClick()
    pyautogui.moveTo(item_x, item_y, round(random.uniform(0.1,0.2), 4)) 
    pyautogui.leftClick()
    pyautogui.keyUp('shift')
    # if pyautogui.locateOnScreen('correct.png', region=(280,350,110,220), grayscale=True, confidence=0.8) != None:
    #     print("no space for mods, i have found the prefix")

def alteration_spam():
    # alt_x_coords = (95, 130)
    # alt_y_coords = (250, 285)
    # alt_x_coords = (370, 400)
    # alt_y_coords = (650, 680)
    alt_x_coords = (435, 465)
    alt_y_coords = (650, 680)

    item_x_coords = (295, 360)
    item_y_coords = (375, 512)

    alt_x = random.randrange(alt_x_coords[0], alt_x_coords[1], 2)
    alt_y = random.randrange(alt_y_coords[0], alt_y_coords[1], 2)
    item_x = random.randrange(item_x_coords[0], item_x_coords[1], 2)
    item_y = random.randrange(item_y_coords[0], item_y_coords[1], 2)
    print("alteration spam")
    pyautogui.moveTo(alt_x, alt_y, round(random.uniform(0.1,0.2), 4))
    pyautogui.keyDown('shift')
    pyautogui.rightClick()
    pyautogui.moveTo(item_x, item_y, round(random.uniform(0.1,0.2), 4))
    # spam_count = 0
    while pyautogui.locateOnScreen('correct.png', region=(280,350,110,220), grayscale=True, confidence=0.8) == None and keyboard.is_pressed('q') == False:
        pyautogui.leftClick()
        # spam_count += 1
        sleep(round(random.uniform(0.1,0.3), 2))
    print("found")    
    pyautogui.keyUp('shift')

def regal():
    regal_x_coords = (418, 450)
    regal_y_coords = (250, 285)
    item_x_coords = (295, 360)
    item_y_coords = (375, 512)

    regal_x = random.randrange(regal_x_coords[0], regal_x_coords[1], 2)
    regal_y = random.randrange(regal_y_coords[0], regal_y_coords[1], 2)
    item_x = random.randrange(item_x_coords[0], item_x_coords[1], 2)
    item_y = random.randrange(item_y_coords[0], item_y_coords[1], 2)
    print("regal")
    pyautogui.moveTo(regal_x, regal_y, round(random.uniform(0.1,0.2), 4))
    pyautogui.keyDown('shift')
    pyautogui.rightClick()
    pyautogui.moveTo(item_x, item_y, round(random.uniform(0.1,0.2), 4))
    pyautogui.leftClick()
    # sleep(round(random.uniform(0.1,0.3), 2))
    pyautogui.keyUp('shift')

def use_currency(x_pos = (0,0), y_pos = (0,0)):
    item_x_coords = (295, 360)
    item_y_coords = (375, 512)
    item_x = random.randrange(item_x_coords[0], item_x_coords[1], 2)
    item_y = random.randrange(item_y_coords[0], item_y_coords[1], 2)

    curr_x = random.randrange(x_pos[0], x_pos[1], 2)
    curr_y = random.randrange(y_pos[0], y_pos[1], 2)

    pyautogui.moveTo(curr_x, curr_y, round(random.uniform(0.1,0.2), 4))
    pyautogui.keyDown('shift')
    pyautogui.rightClick()
    pyautogui.moveTo(item_x, item_y, round(random.uniform(0.1,0.2), 4))
    pyautogui.leftClick()
    pyautogui.keyUp('shift')

def spam_iteration():
    augmentation_check()
    while keyboard.is_pressed('q') == False:
        if pyautogui.locateOnScreen('correct.png', region=(280,350,110,220), grayscale=True, confidence=0.8) == None:
            alteration_spam()
            
            #Augmentation
            if pyautogui.locateOnScreen('correct.png', region=(280,350,110,220), grayscale=True, confidence=0.8) != None:
                augmentation_check()

                if pyautogui.locateOnScreen('correct.png', region=(280,350,110,220), grayscale=True, confidence=0.8) != None:
                    print("i have found the prefix")
                    break
        time.sleep(0.2)
regal_x_coords = (418, 450)
regal_y_coords = (250, 285)
scour_x_coords = (417, 454)
scour_y_coords = (490, 526)
# transmute: 35, 253 to 72, 286
trans_x_coords = (40, 72)
trans_y_coords = (253, 286)

while start_check() == True:
    pyautogui.moveTo(100, 100, round(random.uniform(0.1,0.2), 4))
    spam_iteration()
    # use_currency(x_pos=regal_x_coords, y_pos= regal_y_coords)
    # scour_input = input("scour? (y/n)")
    # if scour_input.upper() == "Y":
    #     #scour : 417, 490  to 454, 526
    #     print("scour")
    #     use_currency(x_pos= scour_x_coords, y_pos= scour_y_coords)
    #     print("transmute")
    #     use_currency(x_pos= trans_x_coords, y_pos= trans_y_coords)


        


# alts : 95, 250 to 130, 285
# aug: 208, 310 to 242, 338
# item: 295, 375 to 360, 512
# random.randrange(v1,v2,interval)