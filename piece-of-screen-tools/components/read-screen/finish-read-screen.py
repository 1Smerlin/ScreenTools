import mss

with mss.mss() as sct:
    if len(sct.monitors) > 2:
        print("Am PC sind "+str(len(sct.monitors)-1) +
              " bildschirme angeschlossen")
    else:
        print("Am PC ist "+str(len(sct.monitors)-1)+" bildschirm angeschlossen")
    screenNumber = 0
    for key in sct.monitors:
        if screenNumber < 1:
            print("Der Bildschirmbereich ist ", key)
        elif len(sct.monitors) > 2:
            print("Bildschirm."+str(screenNumber)+" hat eine größe von ", key)
        screenNumber += 1
