import mss.tools

with mss.mss() as sct:
    monitor = {
        "top": 150,
        "left": 200,
        "width": 300,
        "height": 200
    }
    img = sct.grab(monitor)
    mss.tools.to_png(img.rgb, img.size, output="screen.png")
    print("Done")
