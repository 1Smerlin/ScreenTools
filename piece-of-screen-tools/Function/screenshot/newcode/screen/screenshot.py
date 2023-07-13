import mss

with mss.mss() as sct:
    filename = sct.shot(output="screen.png")
    print(filename)
