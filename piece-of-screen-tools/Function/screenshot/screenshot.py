import mss
import numpy as np
import cv2

# Screenshot


def screenShot(bildschirm, kordinaten=None):
    with mss.mss() as sct:
        # get information from monitor 1
        monitor_number = bildschirm
        mon = sct.monitors[monitor_number]
        if kordinaten is None:
            monitor = {
                "top": mon["top"],
                "left": mon["left"],
                "width": mon["width"],
                "height": mon["height"],
                "mon": monitor_number,
            }
        else:
            monitor = kordinaten
            monitor["mon"] = monitor_number
    print("top:", monitor["top"])
    print("left:", monitor["left"])
    print("width:", monitor["width"])
    print("height:", monitor["height"])
    print("mon:", monitor["mon"])

    # grab the data
    sct_img = sct.grab(monitor)
    img = np.array(sct_img)

    # let file =open("screenshot.png", "w")
    # file.write(img)
    # file.close()
    # save the picture as PNG file
    cv2.imwrite("screenshot.jpg", img)


screenShot(1)
