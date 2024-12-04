import pyautogui
import time

while (True):
    try:
        res = pyautogui.locateCenterOnScreen("images/accept.png", confidence=0.9)
        if res:
            pyautogui.moveTo(res)
            pyautogui.click()
            break
        else:
            time.sleep(2)
    except:
        pass
