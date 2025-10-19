from tkinter import Tk, messagebox, Frame
from tkinter import ttk
import tkinter as tk
from commands import SQL
import sqlite3
con = sqlite3.connect("students.db")


cur = con.cursor()

cur.execute(SQL.CREATE_TABLE)

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

firstNameInput = tk.StringVar()
lastNameInput = tk.StringVar()


def clear():
    res = messagebox.askyesno(title, "Are you sure you want to clear the input?")
    if res:
        firstNameInput.set("")
        lastNameInput.set("")
    else:
        root.focus()


def add():
    firstName = firstNameInput.get()
    lastName = lastNameInput.get()
    if len(firstName.strip()) < 3 or len(lastName.strip()) < 3:
        messagebox.showerror("Registering Error",
                             "First name and Last Name Must have at least 3 characters.")
    else:
        cur.execute(SQL.REGISTER_STUDENT, [firstName, lastName])
        messagebox.showinfo("Success", 
                            f"Student '{firstName} {lastName}' was registered successful!")
        firstNameInput.set("")
        lastNameInput.set("")
        root.focus()

def listAll():
    res = cur.execute(SQL.ALL_STUDENTS).fetchall()
    for index, (id, firstName, lastName) in enumerate(res):
        listbox.insert(index +1 , f"{id}. {firstName}, {lastName}")

def quit():
    res = messagebox.askyesnocancel(title, "Are you sure you want to close the app?")
    if res:
        root.destroy()
    else:
        root.focus()

topFrame = Frame(root, bd=1, padx=10, pady=10)
ttk.Label(topFrame, text="Register", font=("calibre", 15, "normal")).grid(
    row=0, column=0, pady=5, padx=5, sticky='W'
)

ttk.Label(topFrame, text="First Name", font=("calibre", 10, "normal")).grid(
    row=1, column=0, sticky='W'
)
tk.Entry(
    topFrame,
    textvariable=firstNameInput,
    font=("calibre", 10, "normal"),
).grid(row=2, column=0, pady=5)
ttk.Label(topFrame, text="Last Name", font=("calibre", 10, "normal")).grid(
    row=1, column=1, sticky='W'
)
tk.Entry(
    topFrame,
    textvariable=lastNameInput,
    font=("calibre", 10, "normal"),
).grid(row=2, column=1, pady=5, sticky='W')

tk.Button(
    topFrame,
    text="Add",
    background="orange",
    command=add,
    width=10,
    fg="white",
    overrelief=tk.FLAT,
    border=0,
).grid(column=2, row=2)
tk.Button(
    topFrame,
    text="Clear",
    bg="red",
    command=clear,
    width=10,
    fg="white",
    overrelief=tk.FLAT,
    border=0,
).grid(column=3, row=2)
topFrame.grid(row=0, column=0)

bottomFrame = Frame(root,
                     bd=1, width=width, padx=10, pady=10)


ttk.Label(bottomFrame, text="All students", font=("calibre", 15, "normal")).grid(
    row=0, column=0, pady=5, padx=5, sticky='W'
)

ttk.Label(bottomFrame, text="First Name", font=("calibre", 10, "normal")).grid(
    row=1, column=0, sticky='W'
)

listbox = tk.Listbox(bottomFrame, 
                    height = 5, 
                  width = 15, 
                  activestyle = 'dotbox', 
                  font = "Helvetica",
)

listbox.grid(row=1, column=0, sticky='W')
tk.Button(
    bottomFrame,
    text="Show All",
    bg="green",
    command=listAll,
    width=10,
    fg="white",
    overrelief=tk.FLAT,
    border=0,
).grid(column=0, row=2)

bottomFrame.grid(
    row=1, column=0,
    sticky='W'
)


root.mainloop()
con.close()