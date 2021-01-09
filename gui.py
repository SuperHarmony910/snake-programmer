# Credits to Data to Fish: https://datatofish.com/entry-box-tkinter/, RealPython: https://realpython.com/python-gui-tkinter/, https://realpython.com/run-python-scripts, and many Stack Overflow articles, notably: https://stackoverflow.com/questions/45217057/how-to-add-a-placeholder-in-tkinter/45218059
# There are certain commented characters within this program,em here: ^ = Required placement of code, only used when defies code comment organisation.
#TODO More functionality, an epilogue and more goddamn style tbh. Light grey placeholder if possible

from tkinter import *
from tkinter.ttk import *

import tkinter as tk
import tkinter.font as tkFont

# ^
def clear_entry(event, entry):
    entry.delete(0, END)
    entry1.unbind('<Button-1>', click_event)

main = tk.Tk()
# Special setup stuff
main.title("Greetings!")

mainFrame = tk.Frame(main, width = 100, height = 400)
canvas1 = tk.Canvas(main, width = 400, height = 300)
canvas1.pack()

# Font config
mono18 = tkFont.Font(family='Monospace', size=18, weight="bold")
helv16 = tkFont.Font(family='helvetica', size=16, weight="bold")

# Canvas creation
heading = tk.Label(main, text='Greetings!', font=helv16)
canvas1.create_window(200, 25, window=heading)

canvas2 = tk.Canvas(main, width = 400, height = 100)
canvas2.pack()

# Adding to structures
entry1 = tk.Entry(main, width = 32)
placeholder_text = 'Enter your name here!'
entry1.insert(0, placeholder_text)

click_event = entry1.bind("<Button-1>", lambda event: clear_entry(event, entry1))

test = tk.Label(main, text="test")

canvas1.create_window(200, 145, window=entry1)

# Functions start
def forget(input):
    input.forget()

def retrieve(input):
    input.pack(fill = BOTH, expand = True)

def enter(event):
    greeting()
main.bind('<Return>', enter)

def greeting():
    name = entry1.get()
    greet_me = tk.Label(main, text='Hello ' + name + '!', fg='#000080', font=('monospace', 14, 'bold'))
    greet_me.config(font=('monospace', 12, 'bold'))
    canvas1.create_window(200, 260, window=greet_me)
    canvas2.create_window(400, 325, window=test)
    clear_entry(entry1)

# This is to clear the entry box once the name has been submitted
def all():
    greeting()
    clear_entry(entry1)

button1 = tk.Button(text='Greetings!', command=greeting, bg='red', fg='white')
canvas1.create_window(200, 200, window=button1)


main.mainloop()
