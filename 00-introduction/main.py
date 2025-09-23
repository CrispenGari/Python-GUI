
from tkinter import Tk, messagebox
from tkinter import ttk
root = Tk()

# variables
title = "Calculator"
width, height = 800, 300
top = int(root.winfo_screenheight() / 2 - height / 2) 
left = int(root.winfo_screenwidth() / 2 - width / 2) 

root.resizable(False, False)
root.title(title)
root.geometry(f"{width}x{height}+{left}+{top}")
root.iconbitmap('icon.ico')


def bye(type):
    if type == "info":
        messagebox.showinfo(title, "Good Bye")
    elif type == 'warning':
        messagebox.showwarning(title, "Good Bye")
    elif type == 'error':
        messagebox.showerror(title, "Good Bye")
    else:
        messagebox.showerror(title, "Invalid type")


def quit():
    res = messagebox.askyesnocancel(title, "Are you sure you want to close the app?")
    if res:
        root.destroy()
    else:
        root.focus()
    

root.grid()
ttk.Label(root, text="Hello World!", foreground="red").grid(
    column=0, row=0, )
ttk.Button(root, text="Quit", command=quit).grid(column=1, row=0)
ttk.Button(root, text="Info", command=lambda: bye("info")).grid(column=0, row=1)
ttk.Button(root, text="Error", command=lambda: bye("error")).grid(column=1, row=1)
ttk.Button(root, text="Warning", command=lambda: bye("warning")).grid(column=2, row=1)
ttk.Button(root, text="None", command=lambda: bye("none")).grid(column=3, row=1)

root.mainloop()