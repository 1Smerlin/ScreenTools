import mss
import mss.tools

with mss.mss() as sct:
    screenshot = sct.shot(output="screenshot.png")
