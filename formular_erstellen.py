from tkinter import *

window = Tk()
window.geometry("700x300")

kopfzeile = Label(window, text="FORMULAR-KOPFZEILE")
kopfzeile.config(
    padx=15,
    pady=15,
    fg="white",
    bg="Pink",
    font=("Consolas", 20)
)
kopfzeile.pack(fill=X, expand=YES, side=TOP, anchor=N)
window.mainloop()