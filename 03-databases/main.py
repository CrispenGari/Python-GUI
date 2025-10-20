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
width, height = 900, 500
top = int(root.winfo_screenheight() / 2 - height / 2)
left = int(root.winfo_screenwidth() / 2 - width / 2)

root.resizable(False, False)
root.title(title)
root.geometry(f"{width}x{height}+{left}+{top}")
root.iconbitmap("icon.ico")

firstNameInput = tk.StringVar()
lastNameInput = tk.StringVar()
studentId = tk.IntVar()
studentIdDelete = tk.IntVar()
firstNameUpdateInput = tk.StringVar()
idUpdate = tk.IntVar()
lastNameUpdateInput = tk.StringVar()



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
        messagebox.showerror(
            "Registering Error",
            "First name and Last Name Must have at least 3 characters.",
        )
    else:
        cur.execute(SQL.REGISTER_STUDENT, [firstName, lastName])
        messagebox.showinfo(
            "Success", f"Student '{firstName} {lastName}' was registered successful!"
        )
        con.commit()
        firstNameInput.set("")
        lastNameInput.set("")
        root.focus()


def listAll():
    res = cur.execute(SQL.ALL_STUDENTS).fetchall()
    listbox.delete(0, tk.END)
    for index, (id, firstName, lastName) in enumerate(res):
        listbox.insert(index + 1, f"{id}. {firstName}, {lastName}")


def quit():
    res = messagebox.askyesnocancel(title, "Are you sure you want to close the app?")
    if res:
        root.destroy()
    else:
        root.focus()


def searchStudent():
    searchListbox.delete(0, tk.END)
    stdId = studentId.get()
    res = cur.execute(SQL.GET_STUDENT_BY_ID, [stdId]).fetchone()
    if res is None:
        messagebox.showinfo("Student Not Found", f"The student with id '{stdId}' was not found.")
    else:
        id, firstName, lastName = res
        searchListbox.insert(1, f"{id}. {firstName}, {lastName}")


def deleteStudent():
    stdId = studentIdDelete.get()
    res = cur.execute(SQL.GET_STUDENT_BY_ID, [stdId]).fetchone()
    if res is None:
        messagebox.showinfo("Student Not Found", f"The student with id '{stdId}' was not found.")
    else:
        cur.execute(SQL.DELETE_STUDENT_BY_ID, [stdId])
        messagebox.showinfo("Student Deleted", f"The student with id '{stdId}' was deleted.")
        con.commit()


def update():
    stdId = idUpdate.get()
    res = cur.execute(SQL.GET_STUDENT_BY_ID, [stdId]).fetchone()
    if res is None:
        messagebox.showinfo("Student Not Found", f"The student with id '{stdId}' was not found.")
    else:
        id, fn, ln = res
        firstName = fn if len(firstNameUpdateInput.get().strip()) == 0 else  firstNameUpdateInput.get().strip()
        lastName =  ln if len(lastNameUpdateInput.get().strip()) == 0 else  lastNameUpdateInput.get().strip()
        if len(firstName.strip()) < 3 or len(lastName.strip()) < 3:
            messagebox.showerror(
                "Updating Error",
                "First name and Last Name Must have at least 3 characters.",
            )
        else:
            cur.execute(SQL.UPDATE_STUDENT_BY_ID, [firstName, lastName, id])
            messagebox.showinfo("Student Updated", f"The student with id '{stdId}' was updated.")
            con.commit()

topFrame = Frame(root, bd=1, padx=10, pady=10)
ttk.Label(topFrame, text="Register", font=("calibre", 15, "normal")).grid(
    row=0, column=0, pady=5, padx=5, sticky="W"
)

ttk.Label(topFrame, text="First Name", font=("calibre", 10, "normal")).grid(
    row=1, column=0, sticky="W"
)
tk.Entry(
    topFrame,
    textvariable=firstNameInput,
    font=("calibre", 10, "normal"),
).grid(row=2, column=0, pady=5)
ttk.Label(topFrame, text="Last Name", font=("calibre", 10, "normal")).grid(
    row=1, column=1, sticky="W"
)
tk.Entry(
    topFrame,
    textvariable=lastNameInput,
    font=("calibre", 10, "normal"),
).grid(row=2, column=1, pady=5, sticky="W")

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


topRightFrame = Frame(root, bd=1, padx=10, pady=10)
ttk.Label(topRightFrame, text="Search Student", font=("calibre", 15, "normal")).grid(
    row=0, column=0, pady=5, padx=5, sticky="W"
)

ttk.Label(topRightFrame, text="Student ID", font=("calibre", 10, "normal")).grid(
    row=1, column=0, sticky="W"
)
tk.Entry(
    topRightFrame,
    textvariable=studentId,
    font=("calibre", 10, "normal"),
).grid(row=2, column=0, pady=5)
tk.Button(
    topRightFrame,
    text="Search",
    background="orange",
    command=searchStudent,
    width=10,
    fg="white",
    overrelief=tk.FLAT,
    border=0,
).grid(column=2, row=2)
searchListbox = tk.Listbox(
    topRightFrame,
    height=1,
    width=15,
    activestyle="dotbox",
    font="Helvetica",
)
searchListbox.grid(row=3, column=0, sticky="W", rowspan=2)
topRightFrame.grid(row=0, column=1)
bottomFrame = Frame(root, bd=1, width=width, padx=10, pady=10, bg="blue")


ttk.Label(bottomFrame, text="All students", font=("calibre", 15, "normal")).grid(
    row=0, column=0, pady=5, padx=5, sticky="W"
)

ttk.Label(bottomFrame, text="First Name", font=("calibre", 10, "normal")).grid(
    row=1, column=0, sticky="W"
)

listbox = tk.Listbox(
    bottomFrame,
    height=5,
    width=15,
    activestyle="dotbox",
    font="Helvetica",
)

listbox.grid(row=1, column=0, sticky="W")
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
bottomFrame.grid(row=1, column=0, sticky="W")


updateFrame = Frame(root, bd=1, padx=10, pady=10)
ttk.Label(updateFrame, text="Register", font=("calibre", 15, "normal")).grid(
    row=0, column=0, pady=5, padx=5, sticky="W"
)

ttk.Label(updateFrame, text="First Name", font=("calibre", 10, "normal")).grid(
    row=1, column=0, sticky="W"
)
tk.Entry(
    updateFrame,
    textvariable=firstNameUpdateInput,
    font=("calibre", 10, "normal"),
).grid(row=2, column=0, pady=5)
ttk.Label(updateFrame, text="Last Name", font=("calibre", 10, "normal")).grid(
    row=1, column=1, sticky="W"
)
tk.Entry(
    updateFrame,
    textvariable=lastNameUpdateInput,
    font=("calibre", 10, "normal"),
).grid(row=2, column=1, pady=5, sticky="W")

ttk.Label(updateFrame, text="Student Id", font=("calibre", 10, "normal")).grid(
    row=1, column=2, sticky="W"
)
tk.Entry(
    updateFrame,
    textvariable=idUpdate,
    font=("calibre", 10, "normal"),
).grid(row=2, column=2, pady=5, sticky="W")


tk.Button(
    updateFrame,
    text="Update",
    background="orange",
    command=update,
    width=10,
    fg="white",
    overrelief=tk.FLAT,
    border=0,
).grid(column=0, row=3, sticky='W')
updateFrame.grid(row=1, column=1, sticky='W')

deleteStudentFrame = Frame(root, bd=1, padx=10, pady=10)
ttk.Label(deleteStudentFrame, text="Delete Student", font=("calibre", 15, "normal")).grid(
    row=0, column=0, pady=5, padx=5, sticky="W"
)

ttk.Label(deleteStudentFrame, text="Student ID", font=("calibre", 10, "normal")).grid(
    row=1, column=0, sticky="W"
)
tk.Entry(
    deleteStudentFrame,
    textvariable=studentIdDelete,
    font=("calibre", 10, "normal"),
).grid(row=2, column=0, pady=5)
tk.Button(
    deleteStudentFrame,
    text="Delete",
    background="orange",
    command=deleteStudent,
    width=10,
    fg="white",
    overrelief=tk.FLAT,
    border=0,
).grid(column=2, row=2)
deleteStudentFrame.grid(row=3, column=0)



root.mainloop()
con.close()
