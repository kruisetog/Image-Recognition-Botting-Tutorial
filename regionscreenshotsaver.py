#This script saves the image of the region 660,350,600,400 as savedimage.png in the path "C:\Users\Antec\Desktop\Tutorial\savedimage.png"

import pyautogui
item_x_coords = (270, 370)
item_y_coords = (350, 550)
im1 = pyautogui.screenshot(region=(270, 786,100,100))
im1.save(r"./savedimage.png")
