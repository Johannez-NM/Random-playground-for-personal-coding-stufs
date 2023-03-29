import keyboard
import time
import pyautogui
print(' Start')

global count
count = 0

def testdigicode():
    global count

    if count < 10:
        keyboard.write('0')
        keyboard.write(str(count))
    else:
        keyboard.write(str(count))

    keyboard.send('enter')

    time.sleep(0.25)
    keyboard.send('enter')

    time.sleep(0.5)
    pyautogui.click()
    keyboard.send('backspace')
    keyboard.send('backspace')
    
    count += 1

    if count == 100:
        count = 0
        print(' 100')

keyboard.wait('esc')
print('esc stop')


# digikod: 12019070
