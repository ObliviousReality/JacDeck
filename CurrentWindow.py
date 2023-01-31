from ctypes import windll, create_unicode_buffer
import tkinter as tk
import _thread


def loop():
    while True:
        hWnd = windll.user32.GetForegroundWindow()
        length = windll.user32.GetWindowTextLengthW(hWnd)
        buf = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(hWnd, buf, length + 1)
        # print(buf.value)
        lb.config(text=str(buf.value))


window = tk.Tk()

lb = tk.Label(text="hello")
lb.pack()

_thread.start_new_thread(loop, ())
window.mainloop()
print("Hello")
