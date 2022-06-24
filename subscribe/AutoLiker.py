import keyboard
import pyautogui
import time


def findAndClick():
    while True:

        x = pyautogui.locateCenterOnScreen("like.png")
        if keyboard.is_pressed('s'):
            break
        print(x)

        if x is not None:
            break
        if keyboard.is_pressed('s'):
            break


    if x is not None:
        pyautogui.click(x)



    # time.sleep(1.5)
    findAndClick()

print("For stop this loop press (S) on keyboard...")
time.sleep(5)
findAndClick()
