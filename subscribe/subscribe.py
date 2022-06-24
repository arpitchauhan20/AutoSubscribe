import keyboard
import pyautogui as pt
import time

time.sleep(0.5)


def chrome():
    chrome = pt.locateCenterOnScreen('chrome.png')
    pt.click(chrome)


def id():
    id = pt.locateCenterOnScreen('id.png')
    pt.click(id)


def yt():
    yt = pt.locateCenterOnScreen('youtube.png')
    pt.click(yt)


def search():
    search = pt.locateCenterOnScreen('search.png', confidence=0.9)
    pt.click(search)


def sub():
    subscribe = pt.locateCenterOnScreen('subscribe.png')
    pt.click(subscribe)


def cut():
    cut = pt.locateCenterOnScreen('cut.png', confidence=0.9)
    pt.click(cut)

n = int(pt.prompt(text='How many chanel you want to enter', title='Arsh Coading...'))

for i in range(n):
    pop = pt.prompt(text='Enter Chanel name', title='Arsh Coading...')
    print(pop)

    time.sleep(2)
    chrome()
    print('Step 1 Done..')

    try:
        if id() is not None:
            id()
            print('Step 2 Done..')
        else:
            pass
    except:
        print("Step 2 is skiped..")

    time.sleep(2)
    yt()
    print('Step 3 Done..')

    time.sleep(2)
    search()
    print('Step 4 Done..')

    time.sleep(1)
    pt.write(pop)
    print('Step 5 Done..')

    time.sleep(1.5)
    pt.press('enter')
    print('Step 6 Done..')

    time.sleep(2)
    sub()
    print('Step 7 Done..')

    time.sleep(2)
    cut()
    print('Step 8 Done..')

    if keyboard.is_pressed('s'):
        break