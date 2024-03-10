#!env python3

from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import QThread, Slot, Signal
from pynput import mouse
from pynput import keyboard

import sys
import time

from MainDlg import Ui_Dialog
from Version import VERSION

AUTO_CLICK_BIT = 1
AUTO_MOVE_BIT = 2

g_is_halt = False
g_auto_mouse = 0


class BackgroundThread(QThread):
    statusChangeSignal = Signal(int)
    haltSignal = Signal()

    def __init__(self):
        super().__init__()
        self.last_auto_mouse = g_auto_mouse

    def run(self):
        move_counter = 0
        m = mouse.Controller()
        while not g_is_halt:
            if self.last_auto_mouse != g_auto_mouse:
                self.last_auto_mouse = g_auto_mouse
                self.statusChangeSignal.emit(self.last_auto_mouse)

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

        print("Send haltSignal")
        self.haltSignal.emit()


class MainDlg(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(self.windowTitle() + ' - v' + VERSION)

    @Slot(bool)
    def statusChagned(self, auto_mouse):
        if auto_mouse == 0:
            self.ui.labelStatus.setText("<B>Disabled</B>")
        else:
            features = []
            if g_auto_mouse & AUTO_CLICK_BIT:
                features.append("AutoClick")
            if g_auto_mouse & AUTO_MOVE_BIT:
                features.append("AutoMove")
            msg = f'<B><p style="color:blue">{", ".join(features)}</p></B>'
            self.ui.labelStatus.setText(msg)


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
        global g_is_halt
        print("End program.")
        g_is_halt = True
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dlg = MainDlg()

    th = BackgroundThread()
    th.start()

    th.statusChangeSignal.connect(dlg.statusChagned)
    th.haltSignal.connect(dlg.reject)

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    dlg.show()
    # Start the event loop.
    app.exec()

    g_is_halt = True
    th.wait()

    listener.stop()
    listener.join()
