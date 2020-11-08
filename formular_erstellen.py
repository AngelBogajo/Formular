# Formular erstellen
#
# Kopfzeile
# Checkboxes
# Radio Buttons
# Option Menu


from tkinter import *

window = Tk()
window.geometry("300x300")

kopfzeile = Label(window, text="FORMULAR-KOPFZEILE")
kopfzeile.config(
    padx=15,
    pady=15,
    fg="white",
    bg="Pink",
    font=("Consolas", 20)
)
kopfzeile.grid(row=0, column=0, sticky=N, columnspan=6)


# Checkboxes

def zeigenBeruflich():

    texto = ""

    if elek.get():
       texto +=" Elektriker "

    if serv.get():
        if elek.get():
            texto +="und Service Techniker"
        else:
            texto += "Service Techniker "

    zeigen.config(text=texto, bg="green", fg="white")


elek = IntVar()
serv = IntVar()

option = Label(window, text="Was machen Sie Berüflich?").grid(row=1, column=0)

Checkbutton(window, text="Elektriker",
            variable=elek,
            onvalue=1,
            offvalue=0,
            command=zeigenBeruflich).grid(row=2, column=0)

Checkbutton(window, text="Service Techniker",
            variable=serv,
            onvalue=1,
            offvalue=0,
            command=zeigenBeruflich).grid(row=3, column=0)

zeigen = Label(window, text="")
zeigen.grid(row=4, column=0)

# Radio Buttons


def choose():
    marked.config(text=option.get())


option = StringVar()
option.set(None)


Label(window, text="Geschlecht:").grid(row=5, column=0)
Radiobutton(window, text="Mannlich", value="Mannlich", variable=option, command=choose).grid(row=6, column=0)
Radiobutton(window, text="Weiblich", value="Weiblich", variable=option, command=choose).grid(row=7, column=0)

marked = Label(window)
marked.grid(row=8)

# Option Menu


def select():
    selected.config(text=optionX.get())


optionX = StringVar()
optionX.set("Option 3")
Label(window, text="choose an option:").grid(row=5, column=1)

selection = OptionMenu(window, optionX, "Option 1", "Option 2", "Option 3")
selection.grid(row=6, column=1)

Button(window, text="See", command=select).grid(row=7, column=1)

selected = Label(window)
selected.grid(row=8, column=1)

window.mainloop()
