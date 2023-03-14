import keyboard
import pyautogui
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Imported modules, now starting main program")
file = open("C:/Users/joNee09a/OneDrive - Tidaholms kommun/Kod XD/Python/PyMacros/macro1.py", "a")

def addclick():
    mouseposx, mouseposy = pyautogui.position()
    file.write("pyautogui.moveto("+str(mouseposx)+", "+str(mouseposy)+")\n")
    file.write("pyautogui.click()\n")
    file.write("time.sleep(0.1)\n")
    logging.info("Saved "+str(mouseposx)+", "+str(mouseposy)+" to file.")

keyboard.add_hotkey("right_shift", addclick)
logging.info("Hotkey added, waiting for 'esc'")

keyboard.wait("esc")
file.close()
