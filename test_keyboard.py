import keyboard
from pyautogui import * 

i = 0
while keyboard.is_pressed('q') == False:
    i+= 1
    sleep(1)
    print(i)