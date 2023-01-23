import mss
import cv2
import numpy as np
# item_x_coords = (270, 370)
# item_y_coords = (350, 550)280,350,110,220
with mss.mss() as sct:
    
    # Get information of monitor 2
    monitor_number = 1
    mon = sct.monitors[monitor_number]

    # The screen part to capture
    # monitor = {
    #     "top": mon["top"],
    #     "left": mon["left"],
    #     "width": mon["width"],
    #     "height": mon["height"],
    #     "mon": monitor_number,
    # }
    monitor = {
        "top": 350,
        "left": 280,
        "width": 100,
        "height": 200,
        "mon": monitor_number,
    }
    output = "sct-mon{mon}_{top}x{left}_{width}x{height}.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)
    img = np.array(sct.grab(monitor)) # BGR Image
    
    # Display the picture
    cv2.imshow("OpenCV", img)
    cv2.imwrite("correct.png", img)
    cv2.waitKey(0)

    sct_img = sct.grab(monitor)
    img = np.array(sct.grab(monitor)) # BGR Image
    
    # Display the picture
    cv2.imshow("OpenCV", img)
    cv2.imwrite("wrong.png", img)
    cv2.waitKey(0)