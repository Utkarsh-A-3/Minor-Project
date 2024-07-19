#Advanced Widgets
#Creating Menu Bar
from tkinter import *
from tkinter.messagebox import showinfo
root = Tk()
root.title("Notepad")

def new_file():
    pass

def open_file():
    pass

def save_file():
    pass

def quit_app():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def about():
    pass

textarea = Text(root, font = "lucida 13")
file = None
textarea.pack(expand = True, fill = BOTH)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)

filemenu.add_command(label = "New", command = new_file)
filemenu.add_command(label = "Open", command = open_file)
filemenu.add_command(label = "Save", command = save_file)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = quit_app)
menubar.add_cascade(label = "File", menu = filemenu)


root.mainloop()