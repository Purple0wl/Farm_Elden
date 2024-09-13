import mouse
import keyboard
import time
import pyautogui
import pydirectinput

def farmare():
 keyboard.press('w')
 time.sleep(2.8)
 keyboard.release('w')
 time.sleep(0.1)

 time.sleep(2.8)
 pydirectinput.move(70, -220, relative=True)
 time.sleep(2.6)
 pydirectinput.mouseDown(button='middle')
 time.sleep(0.2)
 pydirectinput.mouseUp(button='middle')
 time.sleep(0.5)

 pydirectinput.mouseDown()
 time.sleep(0.25)
 pydirectinput.mouseUp()
 time.sleep(10)

 keyboard.press('s')
 time.sleep(1.8)
 keyboard.release('s')
 time.sleep(0.3)

 keyboard.press('e')
 time.sleep(0.2)
 keyboard.release('e')
 time.sleep(4)
 

 keyboard.press('q')
 time.sleep(0.2)
 keyboard.release('q')
 



time.sleep(4)

while True:
 farmare()
 time.sleep(0.5)


