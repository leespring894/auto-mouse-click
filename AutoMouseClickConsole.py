#!env python3

from pynput import mouse
from pynput import keyboard
import threading
import time

from Version import VERSION

m = mouse.Controller()


AUTO_CLICK_BIT = 1
AUTO_MOVE_BIT = 2

g_is_halt = False
g_auto_mouse = 0


def threadfunc(m: mouse.Controller):
    global g_auto_mouse
    global g_is_halt
    move_counter = 0
    while not g_is_halt:
        if g_auto_mouse & AUTO_CLICK_BIT:
            m.click(mouse.Button.left)
            m.release(mouse.Button.left)
        if g_auto_mouse & AUTO_MOVE_BIT:
            move_counter += 1
            if move_counter == 50:
                m.move(1, 1)
            elif 100 < move_counter:
                m.move(-1, -1)
                move_counter = 0
        time.sleep(0.2)


t = threading.Thread(target=threadfunc, args=(m,))
t.start()


def on_press(key):
    global g_auto_mouse
    if key == keyboard.Key.f2:
        g_auto_mouse ^= AUTO_CLICK_BIT
        print(f"Status changed - {g_auto_mouse}")
    elif key == keyboard.Key.f3:
        g_auto_mouse ^= AUTO_MOVE_BIT
        print(f"Status changed - {g_auto_mouse}")


def on_release(key):
    if key == keyboard.Key.f12:
        print("End program.")
        return False # End keyboard event loop


print(f"Auto Mouse Click v{VERSION}")
print("F2  : Toggle auto click mouse.")
print("F3  : Toggle auto move mouse.")
print("F12 : Terminate this program.")


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

g_is_halt = True
t.join()
