import mss.tools
import numpy as np

with mss.mss() as sct:

    img = sct.grab(sct.monitors[1])
    np_array = np.array(img)
    print(np_array)
    print("Done")
