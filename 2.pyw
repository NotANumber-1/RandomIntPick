import tkinter as tk
import tkinter.messagebox as mb
import random, os

root = tk.Tk()
root.title("Random - Ready")
root.iconbitmap("app.ico")
root.geometry("300x0")
def resettitle():
    root.title("Random - Ready")
def pick(_=None):
    filename = os.path.splitext(os.path.basename(__file__))[0]
    num = random.randint(1,int(filename))
    root.title("Random - Result: " + str(num))
    root.after(1500, resettitle)
root.bind("<Return>", pick)
root.mainloop()
