from tkinter import Tk, messagebox, Frame
from tkinter import ttk
import tkinter as tk

root = Tk()

# variables
title = "Calculator"
width, height = 800, 300
top = int(root.winfo_screenheight() / 2 - height / 2)
left = int(root.winfo_screenwidth() / 2 - width / 2)

root.resizable(False, False)
root.title(title)
root.geometry(f"{width}x{height}+{left}+{top}")
root.iconbitmap("icon.ico")

screenVar = tk.StringVar()


def clear():
    res = messagebox.askyesno(title, "Are you sure you want to clear the input?")
    if res:
        screenVar.set("")
    else:
        root.focus()


def history():
    value = screenVar.get()
    print(value)


def quit():
    res = messagebox.askyesnocancel(title, "Are you sure you want to close the app?")
    if res:
        root.destroy()
    else:
        root.focus()


def getValue(val):
    print(val)
    pass


topFrame = Frame(root, bg="blue", bd=1, padx=10, pady=10)

screenInput = tk.Entry(
    topFrame,
    textvariable=screenVar,
    font=("calibre", 20, "normal"),
    bg="seagreen",
    border=4,
    justify="right",
    width=25,
)
screenInput.grid(row=0, column=0, pady=5, padx=5, rowspan=2)
tk.Button(
    topFrame,
    text="History",
    background="orange",
    command=history,
    width=10,
    font=("calibre", 10, "bold"),
    fg="white",
    overrelief=tk.FLAT,
    border=0,
).grid(column=1, row=0)
tk.Button(
    topFrame,
    text="Clear",
    bg="red",
    command=clear,
    width=10,
    font=("calibre", 10, "bold"),
    fg="white",
    overrelief=tk.FLAT,
    border=0,
).grid(column=1, row=1)
topFrame.grid(row=0, column=0)


# -------------- Buttom frame
btns = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    ["±", 0, ","],
]

bottomFrame = Frame(root, bg="orange", bd=1, width=width, padx=10, pady=10)
for rowindx, row in enumerate(btns):
    for colindx, btn in enumerate(row):
        tk.Button(
            bottomFrame,
            text=str(btn),
            width=3,
            command=lambda: getValue(str(btn)),
            font=("calibre", 15, "bold"),
        ).grid(column=colindx, row=rowindx)
bottomFrame.grid(row=1, column=0, sticky="w")


# ttk.Label(root, text="Hello World!", foreground="red").grid(
#     column=0, row=0, )
# ttk.Button(root, text="Quit", command=quit).grid(column=1, row=0)
# ttk.Button(root, text="Info", command=lambda: bye("info")).grid(column=0, row=1)
# ttk.Button(root, text="Error", command=lambda: bye("error")).grid(column=1, row=1)
# ttk.Button(root, text="Warning", command=lambda: bye("warning")).grid(column=2, row=1)
# ttk.Button(root, text="None", command=lambda: bye("none")).grid(column=3, row=1)
root.mainloop()
