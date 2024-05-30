import tkinter
window = tkinter.TK()
# to rename the title of the window
window.title("GUI")
# pack is used to show the object in the window
label = tkinter.label(window, text="Hello world!").pack()

#labels
l1 = label(window, text="somak", font=("Arial Bold", 50))
window.geometry('350x200')
l1.grid(column=0, row=0)

#button
def clicked():
  l1.configure(text="Button was clicked !!")
bt = Button(window, text="Enter", bg="orange", fg="red", command=clicked)
bt.grid(column=1, row=0)

#entry
txt = Entry(window, width=10)
txt.grid(column=1, row=0)

def clicked():
  res = "Welcome to " + txt.get()
  l1.configure(text=res)
bt = Button(window, text="Enter", bg="orange", fg="red", command=clicked)

#combobox
from tkinter.ttk import *
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Text")
combo.current(1)  #set the selected item
combo.grid(column=4, row=0)

#checkbutton
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=0)

#radiobutton
rad1 = Radiobutton(window,text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)

#scrolledtext
from tkinter import scrolledtext
txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.grid(column=0, row=0)

#messagbox
from tkinter import messagebox
messagebox.showinfo("showinfo", "Information")
messagebox.showwarning("showwarning", "Warning")
messagebox.showerror("showerror", "Error")
messagebox.askquestion("askquestion", "Are you sure?")
messagebox.askokcancel("askokcancel", "Want to continue?")
messagebox.askyesno("askyesno", "Find the value?")
messagebox.askretrycancel("askretrycancel", "Try again?")

#spinbox
from tkinter.ttk import *
n = tkinter.StringVar()
spin = Spinbox(window, from_=0, to=10, textvariable=n)
