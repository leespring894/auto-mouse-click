#!env python3

from pynput import mouse
from pynput import keyboard
import threading
import time

m = mouse.Controller()

isHalt = False
isEnabled = False

def threadfunc(m : mouse.Controller):
    global isEnabled
    global isHalt
    while not isHalt:
        if isEnabled:
            m.click(mouse.Button.left)
            m.release(mouse.Button.left)
        time.sleep(0.2)

t = threading.Thread(target=threadfunc, args=(m, ))
t.start()


def on_press(key):
    global isEnabled
    if key == keyboard.Key.f2:
        isEnabled = not isEnabled
        print(f"Status changed - {isEnabled}")

def on_release(key):
    if key == keyboard.Key.f12:
        print("End program.")
        return False

print("Starting...")
print("F2  : Toggle auto click mouse.")
print("F12 : Terminate this program.")

# Collect events until releasedab111
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

isHalt = True
t.join()
